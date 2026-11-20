# Configuration

## Layering

Keep these layers distinct:

1. portable baseline in `config/default/config.toml`;
2. portable profile examples in `config/profiles/`;
3. private machine-local `~/.codex/config.toml`;
4. named runtime profile files beside the base config;
5. trusted project-local `.codex/config.toml`;
6. managed or system requirements;
7. command-line overrides.

The installer copies named Agent OS profiles but does not merge or overwrite the private base config. Plugin enablement, MCP commands, environment mappings, project trust, model availability, desktop preferences, and credentials remain machine-local.

## Stable Baseline

The portable baseline uses:

```toml
approval_policy = "on-request"
sandbox_mode = "workspace-write"
```

Command network remains off in the ordinary workspace-write profile. This supports routine repository work without defaulting to unrestricted filesystem or network access.

These templates use the established sandbox settings. Codex also supports beta
permission profiles selected by `default_permissions` (for example,
`:workspace` or `:read-only`) and custom rules under `[permissions]`.
A named CLI configuration profile can supply sandbox settings itself. When
migrating, review every loaded layer: an explicit `sandbox_mode` or
`--sandbox` normally selects the older settings. Managed
`allowed_permission_profiles` takes precedence. Follow the
[permission profile guide](https://learn.chatgpt.com/docs/permissions)
when migrating the base config and its overrides together.

## Named Profiles

- `agent-os-restricted`: read-only, on-request, web search disabled.
- `agent-os-research`: workspace-write, on-request, live web search and sandboxed command network enabled.
- `agent-os-deep-review`: workspace-write, on-request, higher reasoning effort, command network left off.

Select a profile with `codex --profile agent-os-research`. Current Codex profile files are separate `~/.codex/<name>.config.toml` files. Legacy `[profiles.<name>]` tables and the top-level `profile` selector are not used.

Profiles do not compose. Use a one-off flag or config override when a deep review also needs research networking, rather than multiplying profiles for every combination.

## Network Policy

Web search, sandboxed command network, MCP connections, apps/connectors, browser access, and approved full-sandbox execution are separate surfaces. Enabling one does not imply that all are enabled.

The research profile intentionally enables both live web search and command network. Use it only when primary literature, source repositories, documentation, DOI services, or package registries are decision-relevant. Keep routine local edits on the baseline.

## MCP and Plugins

MCP settings remain in private config or a plugin package only when live capability is required. For new servers, prefer explicit `enabled_tools` and per-server or per-tool approval modes. Do not put research methodology into MCP configuration.

Plugin enablement and marketplace state are preserved as machine-local runtime configuration. Agent OS installation does not add, remove, enable, or disable plugins.

## Schema Verification

Run `scripts/validate` to load each portable template as an isolated base config
with `codex app-server --strict-config --print-startup-config`. This checks
syntax and recognized settings. Run `scripts/doctor` to check the selected
runtime home's base config and file parity. Use `--include-codex-runtime` for
the built-in runtime diagnostics. Effective permissions also depend on profile
selection and managed requirements.

Official references:

- [Config basics](https://learn.chatgpt.com/docs/config-file/config-basic)
- [Configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference)
- [Advanced configuration](https://learn.chatgpt.com/docs/config-file/config-advanced)
- [Agent approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security)
- [MCP](https://learn.chatgpt.com/docs/extend/mcp)
