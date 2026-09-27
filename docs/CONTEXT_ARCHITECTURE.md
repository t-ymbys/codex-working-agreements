# Context Architecture

## Design Principle

`minimal persistent context + progressive disclosure + durable external state + explicit validation`

The context window is working memory for the current decision. It is not the canonical store for general knowledge, project history, or raw exploration.

## Placement Model

Classify durable information by scope, lifetime, activation condition, authority, loading cost, omission cost, and verifiability before deciding where it belongs.

| Layer | Scope and lifetime | Activation and authority | Validation |
|---|---|---|---|
| Global `AGENTS.md` | Stable cross-project invariants | Always active; subordinate to system, developer, and explicit user instructions | Review for conflicts, necessity, and persistent-token value |
| Project or directory `AGENTS.md` | Repository- or subtree-specific rules | Active only in its scope; closer files refine broader files | Test commands and conventions against the repository |
| Skill root | Reusable task family | Loaded when description matches; routes the task | Validate activation and routing |
| Skill reference | Specialist procedure | Loaded only when its named decision arises | Validate links and representative workflows |
| `HANDOFF.md` | Current semantic project state | Read for recovery or continuation | Keep claims, validation, blockers, and next actions current |
| Git | Historical and recoverable state | Inspect when resuming, comparing, or rolling back | Commits, diffs, and reproducible checkpoints |
| Script, test, schema, lint, CI, or hook | Mechanically checkable invariant | Runs at the relevant boundary | Deterministic pass or fail |
| Report or archive | Evidence and superseded material | Read only for audit, reproduction, or historical analysis | Provenance and reconstruction checks |

Use the narrowest sufficient canonical location. Link to canonical knowledge instead of copying it across instructions, Skills, handoffs, and documentation.

## Global and Project Instructions

Global instructions contain only durable cross-project behavior whose omission would repeatedly cause material harm. Generic software-engineering knowledge, task procedures, research manuals, and discoverable repository facts do not belong there.

Project instructions should state repository-specific boundaries, commands, conventions, and validation. Directory-local files may refine them for a subtree. They should not restate global rules or hold temporary status.

A useful project `AGENTS.md` contains only the applicable subset of:

- its scope and repository boundary;
- authoritative build, test, format, and validation commands;
- local architecture or interface constraints that are not cheaply discoverable;
- data, release, or external-side-effect boundaries specific to the project;
- pointers to canonical project procedures or specifications.

Current progress belongs in `HANDOFF.md`; command output belongs in reports or logs; generic engineering advice belongs nowhere in the project instructions unless the repository has a specific nonstandard requirement.

## Progressive Disclosure

A Skill root defines activation, core invariants, routing, minimum discipline, and completion conditions. Detailed procedures live in references selected for a concrete decision. An invocation that routinely reads every reference indicates poor routing or excessive fragmentation.

Temporary exploration should be compressed into claims, evidence, decisions, and unresolved questions. Preserve large raw outputs as artifacts only when they have audit or reproduction value.

## State and Recovery

`HANDOFF.md` records the current semantic state; Git records history. A handoff is not a transcript. It should enable a future worker to resume from the first unresolved decision without replaying the entire task.

Create checkpoints at semantic milestones and before risky, expensive, or interruptible work. Reconstruct state from instructions, Git, handoff, named artifacts, and validation before rerunning or editing interrupted work.

## Validation and Enforcement

Writing a file is not completion. Apply the cheapest reliable validation that can establish the requested acceptance criteria. Correctness verification and critical review are separate: the former tests whether a claim is true; the latter tests whether a correct claim is meaningful and defensible.

Move reliably checkable constraints into deterministic mechanisms. Keep prose for intent, judgment, activation, and exceptions that code cannot safely decide.

## Cost, Tools, and Independence

Optimize information value, not the raw number of tool calls. Avoid repeated low-information actions, but do not omit primary sources, counterexample search, or verification to save tokens.

Use capability-based routing: routine execution, standard reasoning, advanced judgment, and highest-cost review. Escalate an isolated high-value uncertainty, validate the result, and checkpoint the decision.

Use subagents only when permitted and when independence, parallelism, or context isolation materially improves the result. Their output should return compressed evidence and decision impact, not an undigested search trace.
