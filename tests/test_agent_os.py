from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import agent_os  # noqa: E402


class AgentOSTest(unittest.TestCase):
    def quiet(self, function, *args):
        with contextlib.redirect_stdout(io.StringIO()):
            return function(*args)

    def test_source_and_package_validate(self):
        report = agent_os.validate_source()
        self.assertEqual([], report.errors)
        with tempfile.TemporaryDirectory() as temp:
            package = agent_os.build_plugin(Path(temp) / "plugin")
            package_report = agent_os.validate_package(package)
            self.assertEqual([], package_report.errors)

    def test_install_is_idempotent_and_restores_preexisting_files(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            codex_home = base / "codex"
            agents_home = base / "agents"
            codex_home.mkdir()
            prior_skill = agents_home / "skills" / "research"
            prior_skill.mkdir(parents=True)
            (codex_home / "AGENTS.md").write_text("prior global\n", encoding="utf-8")
            (prior_skill / "SKILL.md").write_text("prior research\n", encoding="utf-8")

            self.assertEqual(0, self.quiet(agent_os.install, codex_home, agents_home, False))
            self.assertEqual(0, self.quiet(agent_os.install, codex_home, agents_home, False))
            self.assertTrue((codex_home / agent_os.INSTALL_MANIFEST).is_file())
            self.assertEqual(agent_os.digest_path(agent_os.GLOBAL_AGENTS), agent_os.digest_path(codex_home / "AGENTS.md"))

            self.assertEqual(0, self.quiet(agent_os.uninstall, codex_home))
            self.assertEqual("prior global\n", (codex_home / "AGENTS.md").read_text(encoding="utf-8"))
            self.assertEqual("prior research\n", (prior_skill / "SKILL.md").read_text(encoding="utf-8"))

    def test_drift_blocks_uninstall(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            codex_home = base / "codex"
            agents_home = base / "agents"
            self.assertEqual(0, self.quiet(agent_os.install, codex_home, agents_home, False))
            with (codex_home / "AGENTS.md").open("a", encoding="utf-8") as handle:
                handle.write("runtime drift\n")
            self.assertEqual(1, self.quiet(agent_os.uninstall, codex_home))

    def test_managed_update_preserves_original_backup(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            codex_home = base / "codex"
            agents_home = base / "agents"
            source = base / "global.md"
            codex_home.mkdir()
            (codex_home / "AGENTS.md").write_text("original\n", encoding="utf-8")
            source.write_text("version one\n", encoding="utf-8")
            original_source = agent_os.GLOBAL_AGENTS
            try:
                agent_os.GLOBAL_AGENTS = source
                self.assertEqual(0, self.quiet(agent_os.install, codex_home, agents_home, False))
                source.write_text("version two\n", encoding="utf-8")
                self.assertEqual(0, self.quiet(agent_os.install, codex_home, agents_home, False))
                self.assertEqual("version two\n", (codex_home / "AGENTS.md").read_text(encoding="utf-8"))
                self.assertEqual(0, self.quiet(agent_os.uninstall, codex_home))
                self.assertEqual("original\n", (codex_home / "AGENTS.md").read_text(encoding="utf-8"))
            finally:
                agent_os.GLOBAL_AGENTS = original_source


if __name__ == "__main__":
    unittest.main()
