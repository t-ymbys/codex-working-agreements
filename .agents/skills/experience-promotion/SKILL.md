---
name: experience-promotion
description: Capture and govern durable operational lessons from important failures, explicit user feedback, new constraints, or reusable techniques. Skip routine successes, trivial edits, one-off noise, and ordinary post-task reflection.
---

# Experience Promotion

## Objective

Turn selected operational experience into the minimum durable intervention that meaningfully improves future work without materially slowing ordinary tasks.

Conceptual lifecycle:

`experience -> assess -> abstract -> classify -> propose -> validate -> deploy -> monitor -> rollback if needed`

This lifecycle is conceptual, not a checklist to run after every task.

## Core Invariants

- `Primary Task > Meta-Learning`.
- `frequency != importance`; consider severity, reuse, transferability, human salience, and mitigation value.
- Separate observation, candidate explanation, alternative explanations, and confidence.
- Preserve uncertainty; one event rarely justifies an absolute rule.
- Choose the lowest layer that preserves the useful value. Promotion is not status.
- Keep procedure in this Skill and mutable records in the learning store.
- Respect existing authorization boundaries. Proposing a change does not authorize deploying it.
- Never create recursive or unbounded self-improvement loops.

## Activation Router

### Stage 0: Fast Path

For ordinary successful tasks, trivial formatting, typo fixes, disposable one-offs, insignificant transient errors, and repetitive low-value noise: do no learning work and do not read the learning store.

### Stage 1: Cheap Trigger Check

Only consider this Skill when an event may yield a durable lesson, including:

- an unexpected or repeated failure;
- resource exhaustion, context loss, or recovery failure;
- a privacy or security near-miss;
- important explicit user feedback;
- a newly discovered system constraint;
- a costly operational mistake or a defect in an existing Skill or policy;
- a technique with clear reuse value across tasks or projects.

Make this decision from the current event. Do not load references or scan history merely to decide whether a trigger exists.

### Stage 2: Minimal Capture

For a meaningful event, capture at most one concise record using [assets/experience.template.md](assets/experience.template.md). Record observation, context, outcome, human feedback, candidate explanation, alternatives, and confidence. Do not perform deep promotion analysis unless Stage 3 applies.

If capture would materially interrupt the primary task, defer it. `capture now, consolidate later` is a preference, not permission to write outside the task's authorized scope.

### Stage 3: Deep Promotion Analysis

Proceed only for high severity, recurrence, high cross-project relevance, high human salience, clear reuse value, an actual durable-change proposal, or an explicit self-improvement request.

1. Assess significance only as deeply as needed.
2. Abstract the lesson without erasing contrary evidence.
3. Check likely duplicates with targeted retrieval.
4. Select the lowest sufficient promotion layer.
5. Propose a change; validate before deployment.
6. Require human review for high-impact changes.
7. Monitor deployed changes and roll back if evidence weakens.

When several candidates exist, consolidate them as a batch: identify duplicates, shared causes, merge targets, retained episodes, rejected candidates, and archive candidates.

## Promotion Layers

- `L0` Transient Context
- `L1` Episodic Experience
- `L2` Reusable Lesson
- `L3` Self-Model
- `L4` Operational Procedure
- `L5` Skill Candidate
- `L6` Global Policy Candidate
- `L7` Deterministic Guardrail Candidate
- `L8` Parameter Adaptation Candidate

Higher layers have broader scope, blast radius, validation cost, and often lower reversibility; require stronger evidence accordingly.

## Reference Routing

Read only the reference needed for the current decision:

- Read [references/significance_assessment.md](references/significance_assessment.md) only when significance is unclear or material.
- Read [references/promotion_policy.md](references/promotion_policy.md) only when durable promotion or batch consolidation is being considered.
- Read [references/self_model.md](references/self_model.md) only when operational capability or constraint knowledge may change.
- Read [references/validation_rollback.md](references/validation_rollback.md) only before applying a durable change.

Do not load all references by default.

## Mutable Learning Store

When an authorized workflow needs durable state, use `${CODEX_HOME:-$HOME/.codex}/learning/` as an environment-specific convention, not as part of the Agent Skills standard:

```text
INDEX.md
SELF_MODEL.md
ISSUES.md
experiences/
candidates/lessons/
candidates/skills/
candidates/policies/
candidates/guardrails/
archive/
```

Create only the files and directories currently needed. Keep `INDEX.md` compact: active issues, important current lessons, known constraints, promotion candidates, and topic/tag pointers. Use tags, filenames, the index, and targeted text search; never scan the full store during ordinary work. Start `SELF_MODEL.md` and `ISSUES.md` from the corresponding assets when needed.

Before adding knowledge, search only the relevant portions of existing policy, Skills, references, Self-Model, issues, candidates, and index. Prefer updating or consolidating an existing concept over creating a duplicate.

## Runtime Budget

Operational learning must not materially dominate the primary task. Default limits:

- no deep analysis during ordinary tasks;
- at most one lightweight capture per meaningful incident;
- no recursive self-analysis;
- no full learning-store scan;
- no policy promotion without explicit justification;
- defer consolidation when it would materially interrupt the primary task.

## Stopping Condition

Stop when any needed observation is captured, significance is sufficiently assessed, the lowest sufficient layer is selected, uncertainty is preserved, unnecessary immediate promotion is deferred, and the primary task can resume. Do not optimize for perfect self-analysis.
