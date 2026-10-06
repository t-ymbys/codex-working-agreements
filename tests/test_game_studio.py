from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = (
    ROOT
    / ".agents"
    / "skills"
    / "game-studio-orchestrator"
    / "scripts"
    / "validate_game_studio.py"
)
SPEC = importlib.util.spec_from_file_location("validate_game_studio", VALIDATOR_PATH)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class GameStudioTest(unittest.TestCase):
    def test_suite_and_templates_validate(self):
        validator.validate_repository(ROOT)

    def test_end_to_end_fixtures_validate_without_invented_playtests(self):
        fixture_root = ROOT / "tests" / "fixtures" / "game-studio"
        for scenario in ("existing-concept", "zero-to-concept"):
            studio = fixture_root / scenario / ".game-studio"
            validator.validate_project(studio)
            state = yaml.safe_load((studio / "studio-state.yaml").read_text(encoding="utf-8"))
            hypothesis = yaml.safe_load((studio / "fun-hypotheses.yaml").read_text(encoding="utf-8"))
            self.assertEqual("hold", state["gate"]["decision"])
            self.assertTrue(state["next_decision"])
            self.assertTrue(all(item["evidence_level"] in {"E0", "E1"} for item in hypothesis["hypotheses"]))

    def test_invalid_evidence_level_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            artifact = root / "fun-hypotheses.yaml"
            artifact.write_text(
                """schema_version: game-studio/v0.4
hypotheses:
  - id: bad
    mechanism: action
    expected_behavior: behavior
    desired_experience: experience
    observable_signal: signal
    failure_signal: failure
    evidence_level: E9
    confidence: high
    status: active
    provenance: test
""",
                encoding="utf-8",
            )
            with self.assertRaises(validator.ValidationError):
                validator.validate_project(root)

    def test_progressive_disclosure_and_local_release_boundary(self):
        orchestrator = (ROOT / ".agents" / "skills" / "game-studio-orchestrator" / "SKILL.md").read_text(encoding="utf-8")
        implementation = (ROOT / ".agents" / "skills" / "game-implementation" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Do not load the full", orchestrator)
        self.assertIn("local-first-app-development", implementation)
        self.assertIn("Do not deploy", implementation)


if __name__ == "__main__":
    unittest.main()
