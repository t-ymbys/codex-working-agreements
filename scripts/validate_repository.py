#!/usr/bin/env python3
"""Validate the published instruction and Skill repository using stdlib only."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"
REQUIRED = (
    ROOT / "AGENTS.md",
    ROOT / "README.md",
    ROOT / "README.ja.md",
    ROOT / "docs" / "CONTEXT_ARCHITECTURE.md",
    ROOT / "docs" / "MIGRATION_REPORT.md",
    ROOT / "docs" / "EVAL_PROPOSAL.md",
)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FRONTMATTER_RE = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)
SENSITIVE_PATTERNS = {
    "absolute user path": re.compile(r"/Users/[^/\s)`>]+"),
    "GitHub token": re.compile(r"\bgh[oprsu]_[A-Za-z0-9]{20,}\b"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "private key": re.compile(r"BEGIN [A-Z ]*PRIVATE KEY"),
}


def field(frontmatter: str, name: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(name)}:\s*(.+?)\s*$", frontmatter)
    return match.group(1).strip() if match else None


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for path in REQUIRED:
        if not path.is_file():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")

    agents = ROOT / "AGENTS.md"
    if agents.is_file() and agents.stat().st_size > 8192:
        warnings.append(f"AGENTS.md exceeds the 8 KiB soft target: {agents.stat().st_size} bytes")

    names: dict[str, Path] = {}
    roots = sorted(SKILLS.glob("*/SKILL.md"))
    if not roots:
        errors.append("no Skills found")

    for skill_file in roots:
        text = skill_file.read_text(encoding="utf-8")
        match = FRONTMATTER_RE.match(text)
        rel = skill_file.relative_to(ROOT)
        if not match:
            errors.append(f"missing or malformed frontmatter: {rel}")
            continue
        name = field(match.group("body"), "name")
        description = field(match.group("body"), "description")
        if name != skill_file.parent.name:
            errors.append(f"frontmatter name mismatch in {rel}: {name!r}")
        if not description:
            errors.append(f"missing frontmatter description: {rel}")
        if name in names:
            errors.append(f"duplicate Skill name {name!r}: {names[name]} and {rel}")
        elif name:
            names[name] = rel

        referenced = {Path(target.split("#", 1)[0]).name for target in LINK_RE.findall(text)}
        for reference in sorted((skill_file.parent / "references").glob("*.md")):
            if reference.name not in referenced:
                errors.append(f"unrouted reference from {rel}: {reference.name}")

    markdown_files = sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        for target in LINK_RE.findall(text):
            raw = target.split("#", 1)[0]
            if not raw or "://" in raw or raw.startswith("mailto:"):
                continue
            if not (path.parent / raw).resolve().exists():
                errors.append(f"broken link in {rel}: {target}")
        for label, pattern in SENSITIVE_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"possible {label} in {rel}")

    if errors:
        for message in errors:
            print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARNING: {message}")
    print(f"checked {len(roots)} Skills and {len(markdown_files)} Markdown files")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
