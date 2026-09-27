# Migration Report

## Baseline

The migration started from clean commit `84e2c5c4ee871506a7be1d1ae4fdfa0a4720320d`. This commit is the recoverable pre-refactor checkpoint; the prior design remains available in Git history.

## Classification

| Classification | Content | Destination or action |
|---|---|---|
| `KEEP_GLOBAL` | User-work protection, authorization boundaries, epistemic discipline, progressive exploration, bounded execution, stopping, validation, privacy, local-first release, recoverability principles | Compressed in `AGENTS.md` |
| `MOVE_PROJECT` | Repository commands, local architecture, validation details, directory-specific rules | Guidance for project-local `AGENTS.md`; no invented rules added here |
| `MOVE_SKILL_ROOT` | Research and experience activation, routing, minimum workflow, completion gates | Thin Skill roots |
| `MOVE_SKILL_REFERENCE` | Literature, mathematical, computational, empirical, verification, critical-review, publication, recovery, promotion, and storage procedures | Routed supporting references |
| `MOVE_DETERMINISTIC` | Frontmatter, links, required files, sensitive patterns, persistent size signal | `scripts/validate_repository.py` |
| `MOVE_HANDOFF` | Current claims, conjectures, objections, calculations, validation, changed files, next action, checkpoint | Research handoff template |
| `MERGE` | Overlapping research and experience references | Eight research references and three experience references |
| `ARCHIVE` | Superseded instruction text with possible historical value | Git history |
| `DELETE_REDUNDANT` | Repeated research mandates and generic engineering taxonomies | Removed from active global context |
| `DELETE_OBSOLETE` | Append-only promotion semantics and model-specific scaffolding | Replaced by scoped routing and capability-based escalation |

## Retained

- protection of user work and explicit authorization boundaries;
- observed, verified, inferred, assumed, hypothesized, and unresolved distinctions;
- literature verification, competing hypotheses, counterexamples, reproducibility, and reviewer-level challenge;
- recoverable checkpoints and state reconstruction;
- local-first release boundaries;
- proportional validation and explicit stopping conditions.

## Moved or Rewritten

- Generic architecture, schema, dependency, logging, and testing tutorials were removed from persistent global instructions. Their decision-relevant invariant—validate proportionally and prefer deterministic enforcement—remains.
- Research detail moved from a broad root and five mixed references to a router and eight decision-specific references. Verification and critical review are now separate.
- Recovery, context isolation, capability routing, and subagent selection moved to the research recovery reference.
- Experience Promotion now routes knowledge to the narrowest valid scope and supports merge, compression, demotion, archive, and deletion.
- `HANDOFF.template.md` now represents current semantic state rather than a generic activity list.

## Canonical Locations

- Cross-project invariant: `AGENTS.md`
- Repository-specific rule: nearest project `AGENTS.md`
- Task workflow: Skill root and selected references
- Current research state: `HANDOFF.md`
- History and recoverability: Git
- Repeatable check: script, test, schema, lint, CI, or hook
- Detailed evidence: generated report or artifact

The migration intentionally avoids copying full rules into this report. Git preserves the old text; the active files are authoritative for current behavior.
