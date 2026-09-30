# Migration

## Baseline

The pre-Agent-OS source is preserved at commit `d3019ee5f4bb8236d0b23c292f82ef52b4cc35ec`. Existing live AGENTS and all four personal Skills matched that source before migration.

## Artifact Mapping

| Original location | Original role | New canonical location | Runtime location | Action | Reason |
|---|---|---|---|---|---|
| Root `AGENTS.md` | Global runtime policy and repository instruction | `global/AGENTS.md` | `~/.codex/AGENTS.md` | Moved | Separates personal global policy from repository-local development guidance |
| None | Repository development instruction | Root `AGENTS.md` | Repository context only | Added | Gives the source repository its own narrow rules |
| `.agents/skills/*` | Canonical and repository-discovered Skills | Same | `~/.agents/skills/*` | Retained | Native repo discovery avoids a duplicate `skills/` source tree |
| Research HANDOFF asset | Current semantic-state template | Same | Copied with Research Skill | Retained | Keeps the template with its consuming workflow |
| None | Portable execution baseline | `config/default/config.toml` | Manual merge only | Added | Live base config is private and must not be overwritten wholesale |
| None | Restricted, research, and deep-review profiles | `config/profiles/*` | `~/.codex/*.config.toml` | Added | Current profile syntax uses separate files and enables task-dependent permissions |
| Live `~/.codex/config.toml` | Machine execution, plugin, MCP, desktop, and trust state | No public copy | Same | Preserved | Contains machine-specific and credential-adjacent values |
| Manual `rsync` deployment | Source-to-runtime copy | `scripts/install` and manifest | Runtime copies plus backups | Replaced | Adds idempotence, provenance, drift detection, and reversibility |
| Repository validator | Static repository checks | `scripts/agent_os.py validate` | Not installed | Expanded | Adds current config and plugin boundary checks |
| None | Agent OS health audit | `scripts/doctor` | Reads live runtime | Added | Makes source/runtime drift and execution policy observable |
| None | Portable Plugin source | `plugin/` | Generated under `dist/` or another target | Added | Enables Skill-only packaging without duplicating canonical Skills |
| Uppercase architecture/migration/eval docs | Earlier focused refactor records | Lowercase Agent OS documentation | Source only | Merged and expanded | Avoids parallel canonical documents |
| Runtime caches, sessions, memories, databases, auth, plugin snapshots | Private/generated state | None | Unchanged | Excluded | Not portable source |

## Config Syntax Decisions

- Retired `approval_policy = "untrusted"` is neither present nor introduced.
- Legacy `[profiles.<name>]` and top-level `profile` selectors are not used. Profiles are separate files selected with `--profile`.
- Stable `sandbox_mode` is used instead of mixing it with beta permission-profile configuration.
- Granular approvals are documented but not imposed as a universal portable policy.
- No existing MCP, plugin, marketplace, desktop, memory, or trust setting is regenerated.

## Rollback

Git can restore source to `d3019ee`. The installer records preexisting runtime artifacts as timestamped backups, and the uninstaller restores them only when installed outputs still match their recorded hashes.
