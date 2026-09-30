# Environment Inventory

Snapshot date: 2026-09-30. Paths use `~` intentionally; private values were not copied into this repository.

## Artifact Inventory

| Artifact | Purpose | State and class | Source of truth | Git-managed | Distribution | Notes |
|---|---|---|---|---|---|---|
| `~/Desktop/git/codex-working-agreements` | Portable Agent OS source | `ACTIVE`, `SOURCE` | This repository | Yes | Sanitized source | Clean at pre-refactor checkpoint `d3019ee` |
| `~/.codex/AGENTS.md` | Live global cognitive policy | `ACTIVE`, `RUNTIME`, installed copy | `global/AGENTS.md` after migration | No | No direct copy | Matched the prior canonical source before refactor |
| `~/.agents/skills/{research,experience-promotion,multidisciplinary-review,local-first-app-development}` | Live personal Skills | `ACTIVE`, `RUNTIME`, installed copies | `.agents/skills/*` | No | Via Skill-only package | All four matched prior canonical source before refactor |
| `~/.agents/skills/.system` and `~/.codex/skills/.system` | Bundled system Skills | `ACTIVE`, `RUNTIME`, managed | Codex installation | No | No | Do not vendor or overwrite |
| `~/.codex/config.toml` | Live execution and desktop configuration | `ACTIVE`, `RUNTIME`, `PRIVATE`, machine-specific | Machine-local file | No | Never wholesale | Mode `0600`; parses under current strict config |
| `~/.codex/*.config.toml` | Named profile layers | Absent at audit start | Canonical profile templates after migration | No | Templates only | Current syntax uses separate profile files |
| `~/.codex/auth.json` | ChatGPT authentication | `ACTIVE`, `PRIVATE`, credential state | Runtime/keychain | No | Never | Excluded from all scans and packages |
| `~/.codex/sessions`, databases, logs, queue, memories | Conversation and application state | `ACTIVE`, `GENERATED`, `PRIVATE` | Runtime | No | Never | Not suitable for Git source |
| `~/.codex/cache`, `.tmp`, plugin caches | Downloaded/generated dependencies | `ACTIVE`, `GENERATED` | Runtime and marketplaces | No | Never | More than one thousand cached plugin files were present |
| `~/.codex/config.toml` plugin tables | Nine enabled packaged capabilities | `ACTIVE`, `RUNTIME`, machine-specific | Runtime config and marketplaces | No | No | Preserved unchanged |
| User-configured MCP entry | Local Node REPL capability | `ACTIVE`, `RUNTIME`, machine-specific | Runtime config | No | No | Command and environment mappings remain private |
| Built-in or surface-injected MCP capabilities | Desktop and computer-use integrations | `ACTIVE` or surface-dependent, `GENERATED` | Codex app/plugin runtime | No | No | Not canonical Agent OS source |
| Project trust entries | Enable project config and local rules | `ACTIVE`, `PRIVATE`, machine-specific | Runtime config | No | Never | Ten entries; one covers a broad Desktop subtree |
| Research HANDOFF template | Resumable scientific state | `ACTIVE`, `SOURCE` | Research Skill asset | Yes | Yes | Canonical template remains with the Skill |
| Current working project local `AGENTS.md`, `HANDOFF.md`, `.codex/config.toml` | Project overrides | None found in the inspected project boundary | Project repositories | Project-dependent | No global distribution | Do not invent project rules |

## Classification Decisions

- Runtime databases, authentication, caches, marketplace snapshots, session files, generated media, memories, and local plugin state are not migration candidates.
- Live `config.toml` is not copied into public source. Only generalized execution-policy examples are canonicalized.
- Source/runtime duplication for installed AGENTS and Skills is intentional and checked by hashes and the install manifest.
- Bundled system Skills and plugin caches are dependencies, not repository assets.
- Unknown runtime files remain untouched.
