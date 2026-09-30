# Agent OS Repository Instructions

## Scope

This repository is the canonical source for the portable parts of the Codex Agent Operating System. Installed files under `~/.codex` and `~/.agents` are runtime copies, not editing targets.

## Source Boundaries

- Global runtime policy is sourced from `global/AGENTS.md`.
- Repository-discoverable Skill sources live under `.agents/skills/`.
- Portable execution-policy examples live under `config/`; never copy a private runtime `config.toml` into this repository.
- Runtime state, credentials, sessions, caches, memories, plugin caches, local MCP settings, and project trust entries are not distributable source.
- The Skill-only plugin package is generated from canonical Skill sources; do not maintain duplicate Skill bodies under `plugin/`.

## Change Workflow

Before material changes, inspect Git status and the relevant source/runtime mapping. Preserve unrelated work and use semantic checkpoints.

Run:

```sh
scripts/validate
```

before committing. For installation changes, test with isolated `--codex-home` and `--agents-home` directories before touching the live runtime. Use `scripts/install --dry-run` before a live install and `scripts/doctor` afterward.

## Public-Safety Boundary

Do not commit credentials, authentication files, private paths, project trust entries, local MCP environment values, unpublished research, session history, or machine-generated runtime state. Use relative paths, environment variables, and sanitized examples.

Do not add MCP servers, hooks, hosted services, or marketplace installation merely to make the package look complete. The distributable package remains Skill-only until a live capability has a demonstrated requirement.
