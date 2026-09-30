# Development

## Workflow

1. Inspect applicable instructions, Git status, source/runtime mapping, and current schema.
2. Make the smallest coherent canonical-source change.
3. Run `scripts/validate`.
4. Test installer, doctor, uninstaller, or package behavior in isolated temporary homes when changed.
5. Inspect the complete diff and create a semantic checkpoint.
6. Run `scripts/install --dry-run`, then install only after the source commit is recoverable.
7. Run doctor and compare runtime hashes.

## Commands

```sh
scripts/validate
scripts/doctor
scripts/package-plugin --output /tmp/codex-agent-os-skills
```

The compatibility entry point `python3 scripts/validate_repository.py` remains available.

## Deterministic Boundaries

Validation checks required source files, Skill frontmatter and routing, local Markdown links, sensitive patterns, deprecated references, current Codex config schema, global policy size, plugin manifests, exact package Skill contents, install idempotence, restoration, and drift refusal.

Installation checks source validity, uses scoped backups, installs exact copies, and records hashes. Doctor checks source, runtime drift, config deprecations, broad trust, stale Skill paths, broken symlinks, and package construction.

## Versioning

Update `VERSION` and both plugin manifests together for a release. Use semantic Git commits. Keep stable source on `main`; create another branch only when isolation has a concrete benefit.

Generated `dist/` packages, install manifests, backups, and runtime state are not committed.
