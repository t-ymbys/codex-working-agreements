---
name: game-iteration
description: Turn game evidence into bottleneck-first controlled mutations, pairwise comparisons, ablations, and kill-or-promote decisions. Use after evaluation or when progress has become polishing without stronger play; not to add features reflexively.
---

# Game Iteration

## Trigger

Use when evidence must change the design, variants must compete, or the project
needs a kill, hold, de-scope, or promotion decision.

## Inputs

Use raw observations, evaluation claims, experiment history, creator feedback,
project ambition, current maturity matrix, and the version being changed.

## Workflow

1. Identify the single current bottleneck to the intended experience; distinguish
   root cause from symptom.
2. Generate a small tournament of materially different responses when the choice
   is consequential. Use controlled mutations such as add, remove, merge, invert,
   constrain, amplify, hide, reveal, delay, accelerate, randomize, make
   deterministic, make persistent, or make reversible.
3. Include an ablation or subtraction candidate. Reject content brute force when
   the loop itself is weak.
4. Compare variants pairwise on the question that matters, including creator
   preference and player behavior where available.
5. Record the decision, evidence, rejected alternatives, reversal condition, and
   next test. Preserve useful failures in the design graveyard.
6. Apply `kill` early when the core hypothesis fails; treat that as successful
   learning, not incomplete production.

## Outputs

Update the experiment log, decision log, maturity bottleneck, and graveyard as
needed. Use [mutation-and-promotion.md](references/mutation-and-promotion.md) for
mutation controls and promotion checks.

## Stop Conditions

Stop when one bounded mutation is ready for implementation or a justified gate
decision is recorded. Do not call a change an improvement until the relevant
evidence has been collected.
