#!/usr/bin/env python3
"""Validate, install, diagnose, uninstall, and package the Codex Agent OS."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"
GLOBAL_AGENTS = ROOT / "global" / "AGENTS.md"
VERSION_FILE = ROOT / "VERSION"
PLUGIN_SOURCE = ROOT / "plugin"
INSTALL_MANIFEST = "agent-os-install.json"
BACKUP_DIR = "agent-os-backups"
OLD_REFERENCE_NAMES = {
    "empirical_data.md", "literature_novelty.md", "recovery_escalation.md",
    "reproducibility_publication.md", "theoretical_computational.md",
    "promotion_policy.md", "self_model.md", "significance_assessment.md",
    "validation_rollback.md",
}
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FRONTMATTER_RE = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)
SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:[-+][0-9A-Za-z.-]+)?$")
SENSITIVE_PATTERNS = {
    "absolute macOS home path": re.compile(r"/" + r"Users/[^/\s)`>]+"),
    "GitHub token": re.compile(r"\bgh[oprsu]_[A-Za-z0-9]{20,}\b"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "private key": re.compile(r"BEGIN [A-Z ]*PRIVATE KEY"),
    "password assignment": re.compile(r"(?i)\bpassword\s*=\s*[^<\s][^\s]*"),
}


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.ok: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def pass_(self, message: str) -> None:
        self.ok.append(message)

    def print(self) -> None:
        for message in self.ok:
            print(f"PASS: {message}")
        for message in self.warnings:
            print(f"WARN: {message}")
        for message in self.errors:
            print(f"FAIL: {message}")
        print(f"summary: {len(self.ok)} pass, {len(self.warnings)} warn, {len(self.errors)} fail")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def digest_path(path: Path) -> str:
    if path.is_file():
        return sha256_file(path)
    if not path.is_dir():
        raise FileNotFoundError(path)
    digest = hashlib.sha256()
    for item in sorted(path.rglob("*")):
        if item.is_symlink():
            raise ValueError(f"symlink not allowed in managed artifact: {item}")
        if item.is_file():
            rel = item.relative_to(path).as_posix().encode()
            digest.update(len(rel).to_bytes(4, "big"))
            digest.update(rel)
            digest.update(bytes.fromhex(sha256_file(item)))
    return digest.hexdigest()


def load_json(path: Path, report: Report, label: str) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        report.error(f"{label} is not readable JSON: {error}")
        return None
    if not isinstance(value, dict):
        report.error(f"{label} must contain a JSON object")
        return None
    return value


def frontmatter_field(frontmatter: str, name: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(name)}:\s*(.+?)\s*$", frontmatter)
    return match.group(1).strip() if match else None


def text_files() -> Iterable[Path]:
    allowed = {".md", ".toml", ".json", ".py", ".sh", ""}
    excluded = {".git", "dist", "__pycache__"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in excluded for part in path.parts):
            continue
        if path.suffix in allowed or path.name in {"VERSION", "install", "uninstall", "doctor", "validate", "package-plugin"}:
            yield path


def validate_skill(skill_file: Path, report: Report) -> None:
    rel = skill_file.relative_to(ROOT)
    text = skill_file.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        report.error(f"missing or malformed Skill frontmatter: {rel}")
        return
    name = frontmatter_field(match.group("body"), "name")
    description = frontmatter_field(match.group("body"), "description")
    if name != skill_file.parent.name:
        report.error(f"Skill name mismatch in {rel}: {name!r}")
    if not description:
        report.error(f"missing Skill description: {rel}")
    routed = {Path(target.split("#", 1)[0]).name for target in LINK_RE.findall(text)}
    for reference in sorted((skill_file.parent / "references").glob("*.md")):
        if reference.name not in routed:
            report.error(f"unrouted reference from {rel}: {reference.name}")


def validate_config_with_codex(path: Path, report: Report) -> None:
    codex = shutil.which("codex")
    if codex is None:
        report.warn(f"Codex unavailable; schema not checked for {path.relative_to(ROOT)}")
        return
    with tempfile.TemporaryDirectory(prefix="agent-os-config-") as temp:
        home = Path(temp)
        shutil.copy2(path, home / "config.toml")
        env = os.environ.copy()
        env["CODEX_HOME"] = str(home)
        result = subprocess.run(
            [codex, "--strict-config", "--version"], env=env, text=True,
            capture_output=True, timeout=30,
        )
    if result.returncode:
        detail = (result.stderr or result.stdout).strip().splitlines()[-1:]
        report.error(f"unsupported config in {path.relative_to(ROOT)}: {' '.join(detail)}")
    else:
        report.pass_(f"current Codex accepts {path.relative_to(ROOT)}")


def validate_manifests(report: Report) -> None:
    version = VERSION_FILE.read_text(encoding="utf-8").strip() if VERSION_FILE.is_file() else ""
    if not SEMVER_RE.fullmatch(version):
        report.error("VERSION must contain semantic versioning")
    portable = load_json(PLUGIN_SOURCE / "plugin.json", report, "portable plugin manifest")
    compat = load_json(PLUGIN_SOURCE / ".codex-plugin" / "plugin.json", report, "Codex compatibility manifest")
    for label, manifest in (("portable", portable), ("compatibility", compat)):
        if manifest is None:
            continue
        if manifest.get("name") != "codex-agent-os-skills":
            report.error(f"{label} plugin name is inconsistent")
        if manifest.get("version") != version:
            report.error(f"{label} plugin version does not match VERSION")
        for forbidden in ("mcpServers", "apps", "hooks"):
            if forbidden in manifest:
                report.error(f"Skill-only {label} manifest must not declare {forbidden}")
    if portable is not None and portable.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        report.error("portable plugin manifest uses an unexpected schema")


def validate_source() -> Report:
    report = Report()
    required = (
        ROOT / "AGENTS.md", GLOBAL_AGENTS, VERSION_FILE, ROOT / "README.md", ROOT / "README.ja.md",
        ROOT / "docs" / "architecture.md", ROOT / "docs" / "configuration.md",
        ROOT / "docs" / "installation.md", ROOT / "docs" / "security.md",
        ROOT / "docs" / "development.md", ROOT / "docs" / "migration.md",
        ROOT / "docs" / "evaluation.md", ROOT / "docs" / "inventory.md",
        ROOT / "docs" / "risk-report.md", ROOT / "templates" / "project-AGENTS.md",
    )
    for path in required:
        if not path.is_file():
            report.error(f"missing required source file: {path.relative_to(ROOT)}")
    if GLOBAL_AGENTS.is_file():
        size = GLOBAL_AGENTS.stat().st_size
        if size > 8192:
            report.warn(f"global/AGENTS.md exceeds the 8 KiB soft target: {size} bytes")
        else:
            report.pass_(f"global/AGENTS.md is within the soft target: {size} bytes")
    skill_files = sorted(SKILLS.glob("*/SKILL.md"))
    if not skill_files:
        report.error("no canonical Skills found")
    names: set[str] = set()
    for skill_file in skill_files:
        validate_skill(skill_file, report)
        name = skill_file.parent.name
        if name in names:
            report.error(f"duplicate Skill name: {name}")
        names.add(name)
    if skill_files:
        report.pass_(f"found {len(skill_files)} canonical Skills")
    markdown = [path for path in text_files() if path.suffix == ".md"]
    for path in markdown:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        for target in LINK_RE.findall(text):
            raw = target.split("#", 1)[0]
            if not raw or "://" in raw or raw.startswith("mailto:"):
                continue
            if not (path.parent / raw).resolve().exists():
                report.error(f"broken link in {rel}: {target}")
    for path in text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        rel = path.relative_to(ROOT)
        for label, pattern in SENSITIVE_PATTERNS.items():
            if pattern.search(text):
                report.error(f"possible {label} in distributable source: {rel}")
        if any(part in OLD_REFERENCE_NAMES for part in path.parts):
            report.error(f"deprecated reference remains: {rel}")
    for path in ROOT.rglob("*"):
        if path.is_symlink() and not path.exists():
            report.error(f"broken symlink: {path.relative_to(ROOT)}")
    validate_manifests(report)
    for config in sorted((ROOT / "config").rglob("*.toml")):
        validate_config_with_codex(config, report)
    if not report.errors:
        report.pass_(f"checked {len(markdown)} Markdown files")
    return report


def managed_artifacts(codex_home: Path, agents_home: Path) -> list[dict[str, Any]]:
    artifacts: list[dict[str, Any]] = [
        {"kind": "file", "source": GLOBAL_AGENTS, "destination": codex_home / "AGENTS.md"},
    ]
    for profile in sorted((ROOT / "config" / "profiles").glob("*.config.toml")):
        artifacts.append({"kind": "file", "source": profile, "destination": codex_home / profile.name})
    for skill_file in sorted(SKILLS.glob("*/SKILL.md")):
        source = skill_file.parent
        artifacts.append({"kind": "directory", "source": source, "destination": agents_home / "skills" / source.name})
    return artifacts


def remove_path(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)


def copy_artifact(source: Path, destination: Path, kind: str) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if kind == "file":
        with tempfile.NamedTemporaryFile(dir=destination.parent, delete=False) as handle:
            temp = Path(handle.name)
        shutil.copy2(source, temp)
        os.replace(temp, destination)
    else:
        temp = Path(tempfile.mkdtemp(prefix=f".{destination.name}.", dir=destination.parent))
        shutil.rmtree(temp)
        shutil.copytree(source, temp)
        if destination.exists():
            previous = Path(tempfile.mkdtemp(prefix=f".{destination.name}.previous.", dir=destination.parent))
            shutil.rmtree(previous)
            os.replace(destination, previous)
            try:
                os.replace(temp, destination)
            except BaseException:
                os.replace(previous, destination)
                raise
            shutil.rmtree(previous)
        else:
            os.replace(temp, destination)


def git_revision() -> str | None:
    result = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True, capture_output=True)
    return result.stdout.strip() if result.returncode == 0 else None


def source_label(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def install(codex_home: Path, agents_home: Path, dry_run: bool) -> int:
    report = validate_source()
    if report.errors:
        report.print()
        return 1
    manifest_path = codex_home / INSTALL_MANIFEST
    previous: dict[str, Any] = {}
    if manifest_path.is_file():
        try:
            previous = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            print(f"refusing install: unreadable existing manifest {manifest_path}")
            return 1
    previous_by_dest = {item["destination"]: item for item in previous.get("artifacts", []) if isinstance(item, dict) and "destination" in item}
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup_root = codex_home / BACKUP_DIR / timestamp
    records: list[dict[str, Any]] = []
    for index, item in enumerate(managed_artifacts(codex_home, agents_home)):
        source: Path = item["source"]
        destination: Path = item["destination"]
        expected = digest_path(source)
        old = previous_by_dest.get(str(destination), {})
        backup: Path | None = Path(old["backup"]) if old.get("backup") else None
        if destination.exists() or destination.is_symlink():
            try:
                current = digest_path(destination)
            except (ValueError, FileNotFoundError) as error:
                print(f"refusing install: unsafe destination {destination}: {error}")
                return 1
            if current == expected:
                print(f"up-to-date: {destination}")
                records.append({"kind": item["kind"], "source": source_label(source), "destination": str(destination), "sha256": expected, "backup": str(backup) if backup else None})
                continue
            if old:
                if current != old.get("sha256"):
                    print(f"refusing install: managed destination drifted: {destination}")
                    return 1
                print(f"update: {destination}")
            else:
                backup = backup_root / f"{index:02d}-{destination.name}"
                print(f"backup: {destination} -> {backup}")
                if not dry_run:
                    backup.parent.mkdir(parents=True, exist_ok=True)
                    if backup.exists():
                        print(f"refusing install: backup target already exists: {backup}")
                        return 1
                    shutil.move(str(destination), str(backup))
        print(f"install: {source_label(source)} -> {destination}")
        if not dry_run:
            copy_artifact(source, destination, item["kind"])
        records.append({"kind": item["kind"], "source": source_label(source), "destination": str(destination), "sha256": expected, "backup": str(backup) if backup else None})
    if dry_run:
        print("dry-run: no files changed")
        return 0
    codex_home.mkdir(parents=True, exist_ok=True)
    manifest = {
        "schema_version": 1,
        "agent_os_version": VERSION_FILE.read_text(encoding="utf-8").strip(),
        "source_revision": git_revision(),
        "installed_at": datetime.now(timezone.utc).isoformat(),
        "artifacts": records,
    }
    temp_manifest = manifest_path.with_suffix(".tmp")
    temp_manifest.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    os.replace(temp_manifest, manifest_path)
    print(f"installed manifest: {manifest_path}")
    return 0


def uninstall(codex_home: Path) -> int:
    manifest_path = codex_home / INSTALL_MANIFEST
    if not manifest_path.is_file():
        print(f"nothing to uninstall: {manifest_path} is absent")
        return 0
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"refusing uninstall: unreadable manifest: {error}")
        return 1
    artifacts = manifest.get("artifacts", [])
    for item in artifacts:
        destination = Path(item["destination"])
        if not destination.exists():
            print(f"refusing uninstall: managed destination missing: {destination}")
            return 1
        if digest_path(destination) != item["sha256"]:
            print(f"refusing uninstall: managed destination drifted: {destination}")
            return 1
    for item in reversed(artifacts):
        destination = Path(item["destination"])
        backup = Path(item["backup"]) if item.get("backup") else None
        remove_path(destination)
        if backup is not None and backup.exists():
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(backup), str(destination))
            print(f"restored: {destination}")
        else:
            print(f"removed: {destination}")
    manifest_path.unlink()
    print(f"removed manifest: {manifest_path}")
    return 0


def build_plugin(destination: Path, force: bool = False) -> Path:
    if destination.exists():
        if not force:
            raise FileExistsError(f"package destination exists: {destination}")
        remove_path(destination)
    destination.mkdir(parents=True)
    shutil.copy2(PLUGIN_SOURCE / "plugin.json", destination / "plugin.json")
    shutil.copytree(PLUGIN_SOURCE / ".codex-plugin", destination / ".codex-plugin")
    skill_root = destination / "skills"
    skill_root.mkdir()
    for skill_file in sorted(SKILLS.glob("*/SKILL.md")):
        shutil.copytree(skill_file.parent, skill_root / skill_file.parent.name)
    return destination


def validate_package(package: Path) -> Report:
    report = Report()
    portable = load_json(package / "plugin.json", report, "packaged portable manifest")
    compat = load_json(package / ".codex-plugin" / "plugin.json", report, "packaged compatibility manifest")
    if portable and portable.get("version") != VERSION_FILE.read_text(encoding="utf-8").strip():
        report.error("packaged portable version mismatch")
    if compat and compat.get("skills") != "./skills/":
        report.error("compatibility manifest must declare ./skills/")
    packaged = sorted((package / "skills").glob("*/SKILL.md"))
    canonical = sorted(SKILLS.glob("*/SKILL.md"))
    if [p.parent.name for p in packaged] != [p.parent.name for p in canonical]:
        report.error("packaged Skill set differs from canonical Skill set")
    for source in canonical:
        target = package / "skills" / source.parent.name
        if digest_path(source.parent) != digest_path(target):
            report.error(f"packaged Skill drift: {source.parent.name}")
    if not report.errors:
        report.pass_(f"Skill-only package contains {len(packaged)} exact Skill copies")
    return report


def config_risk_summary(config: Path, report: Report) -> None:
    if not config.is_file():
        report.warn(f"runtime config absent: {config}")
        return
    text = config.read_text(encoding="utf-8")
    deprecated = {
        'approval_policy = "untrusted"': r"(?m)^\s*approval_policy\s*=\s*['\"]untrusted['\"]",
        "legacy nested profiles": r"(?m)^\s*\[profiles\.",
        "legacy top-level profile selector": r"(?m)^\s*profile\s*=",
    }
    for label, pattern in deprecated.items():
        if re.search(pattern, text):
            report.error(f"runtime config uses {label}")
    for key in ("approval_policy", "sandbox_mode", "web_search", "default_permissions"):
        match = re.search(rf"(?m)^\s*{key}\s*=\s*([^#\n]+)", text)
        report.pass_(f"runtime {key}: {match.group(1).strip() if match else '<implicit/default>'}")
    project_paths = re.findall(r'(?m)^\[projects\."([^"]+)"\]', text)
    home = Path.home()
    broad = [path for path in map(Path, project_paths) if path in {home, home / "Desktop", home / "Documents"}]
    if broad:
        report.warn(f"runtime config trusts {len(broad)} broad home subtree(s); review without automatic mutation")
    report.pass_(f"runtime config contains {len(project_paths)} project trust entries")


def doctor(codex_home: Path, agents_home: Path, include_runtime: bool) -> int:
    report = validate_source()
    manifest_path = codex_home / INSTALL_MANIFEST
    if not manifest_path.is_file():
        report.warn(f"install manifest absent: {manifest_path}")
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            for item in manifest.get("artifacts", []):
                destination = Path(item["destination"])
                if not destination.exists():
                    report.error(f"installed artifact missing: {destination}")
                elif digest_path(destination) != item["sha256"]:
                    report.error(f"installed artifact drift: {destination}")
            current_version = VERSION_FILE.read_text(encoding="utf-8").strip()
            if manifest.get("agent_os_version") != current_version:
                report.warn(f"runtime version {manifest.get('agent_os_version')} differs from source {current_version}")
            else:
                report.pass_(f"runtime manifest matches source version {current_version}")
        except (OSError, json.JSONDecodeError, KeyError, ValueError) as error:
            report.error(f"invalid install manifest: {error}")
    for item in managed_artifacts(codex_home, agents_home):
        destination: Path = item["destination"]
        if destination.exists() and digest_path(item["source"]) == digest_path(destination):
            report.pass_(f"runtime matches source: {destination}")
        elif destination.exists():
            report.warn(f"runtime differs from source: {destination}")
        else:
            report.warn(f"runtime artifact absent: {destination}")
    for root in (codex_home, agents_home):
        if root.exists():
            for link in root.rglob("*"):
                if link.is_symlink() and not link.exists():
                    report.error(f"broken runtime symlink: {link}")
    for old in OLD_REFERENCE_NAMES:
        for match in (agents_home / "skills").glob(f"*/references/{old}"):
            report.error(f"deprecated runtime reference remains: {match}")
    config = codex_home / "config.toml"
    config_risk_summary(config, report)
    codex = shutil.which("codex")
    if codex:
        strict = subprocess.run([codex, "--strict-config", "--version"], text=True, capture_output=True, timeout=30)
        if strict.returncode:
            report.error("current Codex rejects runtime config under --strict-config")
        else:
            report.pass_("current Codex accepts runtime config under --strict-config")
        if include_runtime:
            result = subprocess.run([codex, "doctor", "--json"], text=True, capture_output=True, timeout=60)
            try:
                payload = json.loads(result.stdout)
                checks = payload.get("checks", {})
                sandbox = checks.get("sandbox.helpers", {})
                if sandbox:
                    report.pass_(f"effective sandbox: {sandbox.get('summary', '<unknown>')}")
                for check_id in ("system.disk", "state.rollout_db_parity", "mcp.config", "desktop.security.enforcement"):
                    check = checks.get(check_id)
                    if check and check.get("status") not in {"ok", "not_applicable"}:
                        report.warn(f"Codex doctor {check_id}: {check.get('summary')}")
            except (json.JSONDecodeError, AttributeError):
                report.warn("unable to parse built-in Codex doctor JSON")
    else:
        report.warn("Codex executable unavailable; runtime schema and effective sandbox not checked")
    with tempfile.TemporaryDirectory(prefix="agent-os-plugin-") as temp:
        package = build_plugin(Path(temp) / "codex-agent-os-skills")
        package_report = validate_package(package)
        report.errors.extend(package_report.errors)
        report.warnings.extend(package_report.warnings)
        report.ok.extend(package_report.ok)
    report.print()
    return 1 if report.errors else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate", "install", "uninstall", "doctor", "package"))
    parser.add_argument("--codex-home", type=Path, default=Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")))
    parser.add_argument("--agents-home", type=Path, default=Path(os.environ.get("AGENTS_HOME", Path.home() / ".agents")))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--include-codex-runtime", action="store_true")
    parser.add_argument("--output", type=Path, default=ROOT / "dist" / "codex-agent-os-skills")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.command == "validate":
        report = validate_source()
        with tempfile.TemporaryDirectory(prefix="agent-os-plugin-") as temp:
            package = build_plugin(Path(temp) / "codex-agent-os-skills")
            package_report = validate_package(package)
            report.errors.extend(package_report.errors)
            report.warnings.extend(package_report.warnings)
            report.ok.extend(package_report.ok)
        report.print()
        return 1 if report.errors else 0
    if args.command == "install":
        return install(args.codex_home.expanduser(), args.agents_home.expanduser(), args.dry_run)
    if args.command == "uninstall":
        return uninstall(args.codex_home.expanduser())
    if args.command == "doctor":
        return doctor(args.codex_home.expanduser(), args.agents_home.expanduser(), args.include_codex_runtime)
    if args.command == "package":
        package = build_plugin(args.output.resolve(), args.force)
        report = validate_package(package)
        report.print()
        if not report.errors:
            print(f"package ready: {package}")
        return 1 if report.errors else 0
    raise AssertionError(args.command)


if __name__ == "__main__":
    sys.exit(main())
