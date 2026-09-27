---
name: experience-promotion
description: Classify, validate, deduplicate, compress, route, and retire durable operational lessons from important failures, explicit user feedback, new constraints, or reusable techniques. Skip routine success, trivial edits, and one-off noise.
---

# Experience Promotion

## Objective

Improve future work with the smallest durable intervention justified by evidence.

The lifecycle is:

`experience -> classify -> validate -> deduplicate -> compress -> route to the narrowest sufficient scope -> monitor -> merge, demote, archive, or delete when warranted`

Promotion is not synonymous with adding text to global instructions.

## Activation

Consider this Skill only for an important failure or near-miss, repeated costly friction, explicit user correction, newly verified constraint, reusable technique, stale durable instruction, or explicit request to improve the operating system.

Skip routine successes, disposable tasks, harmless transient errors, ordinary formatting, and isolated noise. One event may justify an episode; it rarely justifies a global rule.

Do not let learning work materially interrupt the primary task. Capture at most one concise event with [experience.template.md](assets/experience.template.md) when deferral would lose important evidence.

## Minimum Decision Process

1. Separate the observation, candidate explanation, alternatives, confidence, and user feedback.
2. Assess significance, generality, stability, expected reuse, and evidence.
3. Search only likely canonical locations for overlap or contradiction.
4. Compress the lesson to the shortest statement that preserves its decision value.
5. Choose the narrowest sufficient destination.
6. Prefer deterministic enforcement when a machine can check the condition reliably.
7. Validate the proposed intervention in proportion to scope and blast radius.
8. Define how the intervention can be reviewed, narrowed, superseded, or removed.

## Routing

Read only the reference that controls the present decision:

- Use [significance-policy.md](references/significance-policy.md) when deciding whether the evidence warrants durable treatment.
- Use [storage-routing.md](references/storage-routing.md) when choosing among global or project instructions, Skill content, current state, deterministic mechanisms, documentation, archive, or discard.
- Use [promotion-policy.md](references/promotion-policy.md) before deploying, consolidating, demoting, archiving, or deleting durable guidance.

Do not load all references or scan a learning store merely because the Skill activated.

## Core Rules

- `Primary Task > Meta-Learning`.
- Frequency is not importance; severity, reuse, human salience, and mitigation value also matter.
- Preserve uncertainty and contrary evidence.
- Update or merge a canonical concept instead of duplicating it across files.
- Broader scope, lower reversibility, or stronger enforcement requires stronger evidence and review.
- Proposing a change does not authorize deploying it.
- Do not create recursive or unbounded self-improvement loops.
- Re-evaluate whether old scaffolding is still needed as models, tools, and environments change.

## Mutable Records

When an authorized workflow needs durable episodes or candidates, use `${CODEX_HOME:-$HOME/.codex}/learning/` as a local convention. Create only the needed paths and use targeted retrieval rather than full-store scans. Assets in this Skill provide optional record templates.

Keep mutable operational facts dated and scoped. They are not timeless identity claims and should be corrected or retired when stale.

## Completion

Stop when the event is classified, the evidence and uncertainty are preserved, any intervention is routed to one canonical location, validation and rollback are proportionate, and no further meta-work would materially improve a future decision.
