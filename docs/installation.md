# Installation

## Stable Copy Install

The supported stable workflow copies validated canonical source into runtime locations and writes a versioned hash manifest.

```sh
scripts/validate
scripts/install --dry-run
scripts/install
scripts/doctor --include-codex-runtime
```

By default this manages:

- `global/AGENTS.md` -> `~/.codex/AGENTS.md`;
- `.agents/skills/*` -> `~/.agents/skills/*`;
- `config/profiles/*.config.toml` -> `~/.codex/*.config.toml`.

It does not overwrite `~/.codex/config.toml`, credentials, MCP settings, plugin state, trust entries, memories, sessions, or caches.

## Safety Properties

- **Idempotent:** identical destinations are reported as up to date.
- **Deterministic:** installed artifacts are exact source copies with SHA-256 digests.
- **Recoverable:** differing destinations are moved into a timestamped backup before replacement.
- **Scoped:** unrelated Skills and configuration are untouched.
- **Observable:** `agent-os-install.json` records version, source revision, destinations, hashes, and backups.
- **Drift-aware:** doctor and uninstall refuse to treat modified installed files as unchanged managed output.

## Isolated Testing

Test changes without touching live runtime:

```sh
scripts/install \
  --codex-home /tmp/agent-os-test/codex \
  --agents-home /tmp/agent-os-test/agents

scripts/doctor \
  --codex-home /tmp/agent-os-test/codex \
  --agents-home /tmp/agent-os-test/agents
```

## Uninstall

`scripts/uninstall` reads the install manifest, verifies that managed outputs have not drifted, removes exact managed copies, and restores recorded backups. It refuses to proceed if a managed destination was edited after installation.

## Development Mode

Symlink-based installation is intentionally not automated in this release. It makes broken in-progress source immediately affect normal runtime and interacts poorly with protected `.agents` and `.codex` paths. Developers can use isolated homes or explicit local copies instead. A symlink mode should be added only if a real iteration workflow justifies the risk.
