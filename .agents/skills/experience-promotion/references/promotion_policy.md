# Promotion Policy

Use this reference only when a durable promotion or batch consolidation is actually being considered.

## Layer Semantics

### L0: Transient Context

Current-task information with no durable storage requirement.

### L1: Episodic Experience

A concrete event record that preserves what happened without claiming generality.

### L2: Reusable Lesson

An evidence-qualified abstraction likely to inform multiple future tasks.

### L3: Self-Model

Current operational knowledge about the agent: capabilities, unavailable capabilities, tools, model restrictions, resource constraints, known failure modes, human-required actions, and environment assumptions.

### L4: Operational Procedure

A repeatable workflow or checklist with a defined purpose and stopping condition.

### L5: Skill Candidate

A multi-step capability with plausible reuse across projects. Prefer improving a relevant existing Skill when possible.

### L6: Global Policy Candidate

A broad cross-project rule. Require strong evidence, conflict review, and human review before material global-policy modification.

### L7: Deterministic Guardrail Candidate

A constraint better enforced by code or system controls than prompting, such as hooks, CI, permissions, schemas, secret scanners, concurrency controllers, sandboxes, or automated validation.

### L8: Parameter Adaptation Candidate

Fine-tuning or another parameter-level change. Treat this as the highest-cost, least-reversible option and never recommend or perform it casually.

## Selection Rule

Choose the lowest layer that preserves the useful value. A higher layer is not a reward and should not be a target. Increasing scope, blast radius, validation cost, or irreversibility requires stronger evidence and review.

Before creating a new lesson or rule, perform only targeted duplicate checks using relevant tags, filenames, `INDEX.md`, active issues, candidates, the Self-Model, related Skills, and applicable policy. Prefer update, merge, supersession, or rejection over conflicting duplication.

## Separate Capture from Consolidation

An incident normally ends after minimal capture and return to the primary task. Consolidate at task or session completion, after several candidates accumulate, on explicit request, after a high-severity event, or when a durable policy change is under consideration.

For a batch, ask:

- Do records share a root cause?
- Are any duplicates or contradictory?
- Can they update an existing lesson?
- Is a procedure or Skill justified?
- Should each item remain an episode, be archived, or be rejected?

Record rejected and superseded candidates when that history prevents repeated reconsideration.

## Human Review Boundary

Require human review before:

- material modification of global `AGENTS.md`;
- privacy or security boundary changes;
- destructive automation;
- broad workflow restrictions;
- shared organizational policy changes;
- parameter-level adaptation.

Default governance is: observe automatically, propose automatically when authorized, validate before promotion, and require human review when impact is high. Never deploy hard guardrails or parameter adaptation automatically.

If a small global trigger is proposed, keep it narrowly scoped:

> Consider the experience-promotion Skill only when a task produces a potentially durable operational lesson, repeated failure, important user feedback, newly discovered system constraint, or reusable technique. Do not invoke it for ordinary successful tasks or trivial events.

