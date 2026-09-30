# Risk Report

Snapshot date: 2026-09-30. No trust, MCP, plugin, credential, or unrelated runtime setting was changed during the audit.

## Findings

| Area | Status | Evidence | Recommended treatment |
|---|---|---|---|
| Git | Low risk | Canonical repository was clean at `d3019ee`; source and live AGENTS/Skills matched | Preserve `d3019ee` as the pre-refactor checkpoint |
| Config schema | Low risk | Current Codex accepted the live file with `--strict-config`; no retired `approval_policy = "untrusted"`, nested `[profiles.*]`, or top-level profile selector was found | Continue strict validation after upgrades |
| Effective sandbox | Acceptable | Built-in doctor reported restricted filesystem and restricted network with `OnRequest` approvals | Keep least-privilege default; do not adopt full access as baseline |
| Policy explicitness | Moderate | Base config does not explicitly declare approval, sandbox, or network keys; current effective values come from runtime defaults or managed layers | Provide explicit portable examples, but do not overwrite the private base config automatically |
| Project trust | Moderate | Ten trusted project entries exist; one covers the Desktop subtree rather than a repository | Review manually and narrow to repository roots if compatible with actual workflows; no automatic mutation |
| Network | Acceptable with profile discipline | Default effective command network is restricted; research may require external retrieval | Keep default off and enable explicitly through the research profile or a one-off override |
| MCP | Moderate | One machine-local stdio MCP server is configured; additional capabilities are app/plugin supplied | Preserve settings, keep secrets out of source, and use per-server/per-tool approvals when adding new servers |
| Plugins | Low risk for this migration | Nine enabled plugins and several managed marketplaces are present | Preserve them; do not copy cache or enable/disable plugins as part of Agent OS installation |
| Credentials and private state | High if leaked | Authentication, session, memory, SQLite, environment mapping, and local paths exist under `~/.codex` | Exclude wholesale; scan distributable source and packages deterministically |
| Runtime drift | Moderate before installer | Runtime was maintained by manual scoped `rsync` and had no version manifest | Install with hashes, version manifest, backups, and doctor comparison |
| Disk capacity | Moderate operational risk | Built-in doctor reported roughly 2.7 GiB free, below its 5 GiB warning threshold | Free space separately; avoid copying caches or building large artifacts |
| Thread inventory | Low-to-moderate operational risk | Built-in doctor reported missing rollout DB rows and duplicate thread inventory entries while databases were healthy | Preserve state; investigate with Codex support or a separate maintenance task rather than mutating databases here |
| Hooks | No present need | No Agent OS hook is required for install, validation, or packaging | Do not add an execution surface without a concrete benefit |

## Approval Design

The stable baseline uses `on-request`: safe work inside the sandbox proceeds, while boundary crossings can be reviewed. Granular approvals are current but are not selected as the portable default because a false category disables that escalation instead of merely hiding prompts, and the correct split is machine/workflow-specific.

Destructive operations, external publication, access changes, and full sandbox bypass remain explicit human decisions. Noninteractive automation should use a separately reviewed profile and should never inherit an unrestricted interactive configuration by accident.

## Permission-Profile Decision

Current Codex supports beta permission profiles, but they do not compose with legacy `sandbox_mode` configuration. This release keeps the mature `read-only` and `workspace-write` sandbox profiles and documents permission profiles as a future migration candidate rather than mixing both systems.

## Remaining Human Decision

Whether to narrow the broad Desktop trust entry depends on which project-local configurations are intentionally used beneath it. The safe recommendation is repository-level trust, but changing it without that usage decision could disable valid project configuration.
