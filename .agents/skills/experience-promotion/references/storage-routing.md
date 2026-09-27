# Storage Routing

Route each durable item to the narrowest sufficient canonical location.

| Destination | Use for | Do not use for |
|---|---|---|
| Global `AGENTS.md` | Stable cross-project invariants that must affect almost every task | Generic knowledge, project procedures, temporary constraints |
| Project or directory `AGENTS.md` | Repository-specific commands, conventions, boundaries, and validation | Cross-project manuals or current task status |
| Skill root | Activation, routing, core invariants, minimum workflow | Detailed specialist procedures |
| Skill reference | Specialist procedure loaded only for a matching task | Rules every invocation must know |
| `HANDOFF.md` | Current semantic state, claims, blockers, validation, next actions | Historical transcript or generic policy |
| Git | Historical and recoverable state | Current semantic summary |
| Test, linter, schema, CI, hook, or script | Reliably machine-checkable constraints | Nuanced judgment that the mechanism cannot encode safely |
| Documentation or report | Explanations, evidence, generated findings, and user-facing procedures | Agent control rules that must activate automatically |
| Archive | Superseded evidence worth retaining | Active guidance |
| Discard | Noise, duplicates, unstable workarounds, and obsolete scaffolding with no archival value | Evidence needed for audit or recovery |

## Canonicality

Keep one authoritative expression of a concept. Other files may link to it, but should not restate the full rule. Before adding anything, search only the likely canonical locations and update, merge, or supersede existing content where possible.

Prefer deterministic enforcement for formatting, schemas, reproducibility, dependency constraints, forbidden artifacts, and regressions when the rule can be encoded reliably. Keep the intent in prose only when it helps users understand the mechanism.

## Mutable Operational Knowledge

Environment facts, current capabilities, unresolved issues, and candidate lessons may live in a dated local learning store such as `${CODEX_HOME:-$HOME/.codex}/learning/`. Use [SELF_MODEL.template.md](../assets/SELF_MODEL.template.md) for scoped capability facts and [ISSUES.template.md](../assets/ISSUES.template.md) for unresolved issues.

These records are mutable evidence, not global instruction. Load them only when relevant, label provenance and verification date, and retire stale claims.
