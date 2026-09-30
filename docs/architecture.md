# Architecture

## System Boundary

This repository treats Codex configuration as a small Agent Operating System rather than a prompt collection.

```text
Codex Runtime
|
|-- Cognitive Control Plane
|   |-- global/AGENTS.md
|   |-- repository AGENTS.md files
|   |-- .agents/skills/*
|   |-- routed references and templates
|   `-- Experience Promotion
|
|-- Execution Control Plane
|   |-- machine-local config.toml
|   |-- portable config templates and profiles
|   |-- sandbox and approvals
|   |-- network and MCP policy
|   `-- project trust
|
|-- Durable State
|   |-- Git history
|   |-- HANDOFF.md
|   `-- project artifacts and reports
|
|-- Deterministic Control
|   |-- scripts/validate
|   |-- scripts/doctor
|   |-- scripts/install and scripts/uninstall
|   `-- plugin package validation
|
`-- Distribution
    |-- portable Skill-only plugin manifest
    `-- generated exact copies of canonical Skills
```

## Cognitive Control Plane

The global policy contains only durable cross-project invariants. The repository root `AGENTS.md` is intentionally different: it governs development of this source repository. Project-specific facts remain in the nearest project `AGENTS.md`.

Skill descriptions provide cheap discovery. `SKILL.md` contains activation, routing, core invariants, and completion conditions. Detailed procedures are loaded from references only when they can affect the current decision. The Research Skill keeps correctness verification distinct from novelty, significance, and defensibility review.

Experience Promotion changes canonical source only through a scoped, evidence-based proposal. It may add, merge, compress, demote, archive, replace, or delete guidance. It does not write directly to live global instructions as an unversioned self-modification loop.

## Execution Control Plane

`config.toml`, sandboxing, approvals, permission profiles, network policy, MCP tool approvals, plugin enablement, and project trust define enforceable capabilities. Research methodology does not belong in this layer, and filesystem or network boundaries must not depend only on natural-language reminders.

The repository supplies validated portable examples, not a public copy of the machine's live config. The live config may contain project paths, installed plugin state, MCP commands, environment mappings, and credential-adjacent settings.

## Persistent and Lazy Context

Always-loaded context should have high decision value for nearly every task. Conditional procedures remain behind Skill routing. Raw search results, logs, and historical state are not prompt context; they become artifacts only when audit or reconstruction value justifies retention.

The governing principle is:

`minimal persistent context + progressive disclosure + durable external state + explicit validation`

## Source, Runtime, and Generated Output

- **Canonical source:** this Git repository.
- **Installed runtime:** `~/.codex/AGENTS.md`, selected profile files, and `~/.agents/skills/*`.
- **Machine-local private layer:** `~/.codex/config.toml`, credentials, local MCP settings, plugin state, trust entries, memories, sessions, databases, and caches.
- **Generated output:** install manifest, backups, and plugin staging under `dist/`.

The stable workflow is:

`edit source -> validate -> inspect diff -> checkpoint -> install -> doctor -> runtime verification`

## Git and HANDOFF

Git stores historical and recoverable state. `HANDOFF.md` stores the current resumable semantic state: objective, established results, live claims, objections, remaining validation, next actions, and checkpoint. A handoff is not a transcript.

## Plugin Boundary

The distributable plugin contains generalized Skills and their references, scripts, and assets. It excludes global personal policy, config profiles, trust entries, MCP settings, credentials, installer state, and private artifacts.

The first package is Skill-only. It declares no MCP, app, hook, or hosted dependency. MCP should be added only when authenticated live data or controlled external action becomes a demonstrated requirement. A Skill defines workflow; MCP supplies live capability.
