#!/usr/bin/env python3
"""Validate Game Studio v0.4 Skill sources or project artifacts.

This is a structural validator. It does not evaluate game quality or evidence
truthfulness.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError as error:  # pragma: no cover - environment diagnostic
    raise SystemExit("PyYAML is required to validate Game Studio YAML") from error


SKILLS = {
    "game-studio-orchestrator",
    "game-creative-director",
    "game-reference-originality",
    "game-concept-design",
    "game-systems-design",
    "game-prototype-strategy",
    "game-evaluation",
    "game-iteration",
    "game-implementation",
}
AMBITIONS = {
    "experiment",
    "prototype",
    "small_game",
    "release_candidate",
    "signature_candidate",
}
RUNGS = {"D0", "P0", "P1", "P2", "VS", "A0", "RC"}
EVIDENCE = {f"E{number}" for number in range(7)}
CONFIDENCE = {"low", "medium", "high"}
GATES = {"advance", "hold", "mutate", "kill", "de_scope"}
STATUSES = {"active", "supported", "weakened", "rejected", "unknown"}
YAML_FILES = {
    "studio-state.yaml",
    "creator-taste.yaml",
    "creator-conviction.yaml",
    "fun-hypotheses.yaml",
    "reference-ledger.yaml",
    "experiment-log.yaml",
    "v1-maturity.yaml",
    "decision-log.yaml",
}


class ValidationError(Exception):
    pass


def load_yaml(path: Path) -> dict:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        raise ValidationError(f"{path}: invalid YAML: {error}") from error
    if not isinstance(data, dict):
        raise ValidationError(f"{path}: top-level YAML must be a mapping")
    if data.get("schema_version") != "game-studio/v0.4":
        raise ValidationError(f"{path}: schema_version must be game-studio/v0.4")
    return data


def require_enum(path: Path, label: str, value: object, allowed: set[str]) -> None:
    if value not in allowed:
        options = ", ".join(sorted(allowed))
        raise ValidationError(f"{path}: {label}={value!r}; expected one of {options}")


def validate_claim(path: Path, claim: dict) -> None:
    require_enum(path, "claim.evidence_level", claim.get("evidence_level"), EVIDENCE)
    require_enum(path, "claim.confidence", claim.get("confidence"), CONFIDENCE)
    for key in ("rationale", "provenance"):
        if not claim.get(key):
            raise ValidationError(f"{path}: claim requires {key}")


def validate_artifact(path: Path) -> None:
    data = load_yaml(path)
    name = path.name
    if name == "studio-state.yaml":
        require_enum(path, "ambition", data.get("ambition"), AMBITIONS)
        require_enum(path, "prototype_rung", data.get("prototype_rung"), RUNGS)
        gate = data.get("gate") or {}
        require_enum(path, "gate.decision", gate.get("decision"), GATES)
    elif name == "creator-conviction.yaml":
        for field in (
            "concept_conviction",
            "prototype_conviction",
            "system_conviction",
            "aesthetic_conviction",
            "signature_conviction",
        ):
            require_enum(path, f"{field}.status", (data.get(field) or {}).get("status"), STATUSES)
        if data.get("player_validation_is_separate") is not True:
            raise ValidationError(f"{path}: player_validation_is_separate must be true")
    elif name == "fun-hypotheses.yaml":
        for item in data.get("hypotheses", []):
            require_enum(path, "hypothesis.evidence_level", item.get("evidence_level"), EVIDENCE)
            require_enum(path, "hypothesis.confidence", item.get("confidence"), CONFIDENCE)
            require_enum(path, "hypothesis.status", item.get("status"), STATUSES)
            for key in ("mechanism", "expected_behavior", "desired_experience", "observable_signal", "failure_signal"):
                if not item.get(key):
                    raise ValidationError(f"{path}: hypothesis requires {key}")
    elif name == "experiment-log.yaml":
        for item in data.get("experiments", []):
            require_enum(path, "experiment.prototype_rung", item.get("prototype_rung"), RUNGS)
            require_enum(path, "experiment.evidence_level", item.get("evidence_level"), EVIDENCE)
            if item.get("decision") is not None:
                require_enum(path, "experiment.decision", item.get("decision"), GATES)
    elif name == "evaluation-template.yaml" or path.parent.name == "evaluations":
        if data.get("recommendation") is not None:
            require_enum(path, "recommendation", data.get("recommendation"), GATES)
        for claim in data.get("claims", []):
            validate_claim(path, claim)


def validate_project(root: Path) -> None:
    found = False
    for path in sorted(root.rglob("*.yaml")):
        if path.name in YAML_FILES or path.parent.name == "evaluations":
            validate_artifact(path)
            found = True
    if not found:
        raise ValidationError(f"{root}: no Game Studio YAML artifacts found")


def validate_repository(root: Path) -> None:
    skills_root = root / ".agents" / "skills"
    missing = sorted(name for name in SKILLS if not (skills_root / name / "SKILL.md").is_file())
    if missing:
        raise ValidationError(f"missing Game Studio Skills: {', '.join(missing)}")
    for skill in sorted(SKILLS):
        text = (skills_root / skill / "SKILL.md").read_text(encoding="utf-8")
        if "[TODO" in text:
            raise ValidationError(f"{skill}: unresolved scaffold TODO")
    template = skills_root / "game-studio-orchestrator" / "assets" / "studio-template"
    missing_templates = sorted(name for name in YAML_FILES if not (template / name).is_file())
    if missing_templates:
        raise ValidationError(f"missing templates: {', '.join(missing_templates)}")
    validate_project(template)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.path).resolve()
    try:
        if (root / ".agents" / "skills").is_dir():
            validate_repository(root)
        else:
            validate_project(root)
    except ValidationError as error:
        print(f"FAIL: {error}")
        return 1
    print(f"PASS: Game Studio structure is valid at {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
