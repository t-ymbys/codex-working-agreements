# Security and Privacy

## Least Privilege

Use `workspace-write` with on-request approvals for normal version-controlled work and `read-only` for inspection. Do not make `danger-full-access` or approval bypass a persistent default.

Network access is task-dependent. The ordinary baseline keeps command network restricted; the research profile enables it explicitly. MCP, apps, browser access, web search, and sandbox command networking have separate permission surfaces.

## Public Distribution Boundary

Never distribute:

- authentication files, API keys, tokens, passwords, private keys, or credential helpers;
- runtime `config.toml` copied wholesale;
- project trust paths, private home paths, machine IDs, or internal URLs;
- MCP environment values or private server configuration;
- sessions, memories, databases, logs, caches, plugin snapshots, or generated runtime state;
- private repositories, unpublished sensitive research, client information, or personal records.

The validator scans source and generated packages for obvious secrets and personal absolute paths. This is defense in depth, not proof that every sensitive fact has been removed; review diffs before publication.

## Project Trust

Trust activates project-local `.codex` configuration, hooks, and rules. Prefer repository-level trust to broad home subtrees. The doctor reports broad trust entries but does not modify them because narrowing trust can disable intentional project configuration.

## Hooks and MCP

Hooks execute code and therefore expand the attack surface. This release includes none. MCP is likewise excluded from the distributable plugin because the current Skills need workflow instructions, not authenticated live services.

If either is added later:

- define the live capability it provides;
- restrict tools and approvals;
- keep credentials in approved runtime stores;
- validate input and output boundaries;
- document installation, removal, and failure behavior;
- add it only to the narrowest package that needs it.

## Self-Modification

Operational learning follows:

`experience -> proposal -> classification -> canonical source diff -> validation -> eval when material -> checkpoint -> install`

Runtime files are not silently rewritten as the durable source of truth.
