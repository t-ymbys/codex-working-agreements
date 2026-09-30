# Codex Agent Operating System

[日本語](README.ja.md)

A small, versioned, testable, installable, and auditable operating layer for Codex.

It separates:

- **Cognitive control:** global and project AGENTS, progressively disclosed Skills, research epistemics, HANDOFF, and Experience Promotion.
- **Execution control:** portable approval, sandbox, network, and reasoning profiles while preserving private machine configuration.
- **Durable state:** Git, HANDOFF, and reconstructable project artifacts.
- **Deterministic control:** validation, installation, doctor, rollback, and plugin packaging.
- **Distribution:** a generated Skill-only portable plugin with no MCP, hooks, credentials, or personal configuration.

The design principle is:

> minimal persistent context + progressive disclosure + least privilege + durable external state + explicit validation

## Layout

```text
.
├── AGENTS.md                    # repository-local development rules
├── global/AGENTS.md             # canonical global runtime policy
├── .agents/skills/              # canonical, repo-discoverable Skills
├── config/
│   ├── default/config.toml      # portable baseline example
│   └── profiles/                # installable named profiles
├── templates/project-AGENTS.md
├── plugin/                      # Skill-only package manifests
├── scripts/                     # validate, install, doctor, uninstall, package
├── docs/
└── VERSION
```

Canonical Skills remain under `.agents/skills` because that is the repository-native discovery location. Plugin packaging copies them exactly into the standard plugin `skills/` directory; there is no second editable Skill tree.

## Quick Start

Review the source and then run:

```sh
scripts/validate
scripts/install --dry-run
scripts/install
scripts/doctor --include-codex-runtime
```

The installer manages only global AGENTS, the four repository Skills, and named Agent OS profile files. It backs up changed destinations and writes a hash manifest. It does **not** replace the private base `~/.codex/config.toml`, credentials, MCP settings, plugin state, project trust, memories, sessions, or caches.

Build a distributable Skill-only plugin with:

```sh
scripts/package-plugin
```

Generated packages go under ignored `dist/` by default.

## Included Skills

- **Research:** routed literature, mathematical, computational, empirical, verification, critical-review, publication, reproducibility, and recovery workflows.
- **Experience Promotion:** evidence-based classification, deduplication, compression, narrow routing, maintenance, demotion, archive, and deletion.
- **Multidisciplinary Review:** selective cross-domain review for consequential decisions.
- **Local-First App Development:** local development and validation without implicit publication.

## Documentation

- [Architecture](docs/architecture.md)
- [Environment inventory](docs/inventory.md)
- [Risk report](docs/risk-report.md)
- [Configuration](docs/configuration.md)
- [Installation and rollback](docs/installation.md)
- [Security](docs/security.md)
- [Development](docs/development.md)
- [Migration mapping](docs/migration.md)
- [Evaluation](docs/evaluation.md)

## Evidence Boundary

Static validation and isolated deployment tests establish structural integrity and reproducibility. They do not prove that the new architecture improves agent behavior. Behavioral superiority remains `NOT VERIFIED` until the multi-run golden-task evaluation is completed.

This is a personal, sanitized configuration project, not an official OpenAI project. Current official Codex documentation should be rechecked before changing config schemas or publishing a plugin.

## License

[MIT](LICENSE)
