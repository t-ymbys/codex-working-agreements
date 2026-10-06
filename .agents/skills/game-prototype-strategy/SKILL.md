---
name: game-prototype-strategy
description: Choose the cheapest game prototype or experiment that removes the most important uncertainty, with controlled variables, observables, and kill criteria. Use when design uncertainty has become empirical; not to build a broad v0 by default.
---

# Game Prototype Strategy

## Trigger

Use when reasoning alone cannot resolve the next design decision. A prototype is
an experiment, not a miniature commitment to production.

## Inputs

Use the highest-priority uncertainty, candidate alternatives, fun hypothesis,
available evidence, creator constraints, and current prototype rung.

## Workflow

1. Write one primary question and the decision it will inform.
2. Choose the lowest sufficient rung: `D0`, `P0`, `P1`, `P2`, `VS`, `A0`, or
   `RC`. Split movement, combat, economy, world, or other questions when a single
   build would confound them.
3. Define hypothesis, change, controlled variables, observations, failure signal,
   kill criterion, effort bound, and next action for each possible outcome.
4. Prefer test scenes and reversible parameters. Delay polish unless feel,
   readability, visual identity, or audio identity is the variable under test.
5. Use variants and pairwise comparison for subjective questions; avoid absolute
   scores without evidence.
6. Prevent `fast_v0_slow_v1`: state what is disposable, reusable, or prohibited
   from hardening into production architecture.

## Outputs

Append an `experiment-log.yaml` entry and a prototype brief. Use
[prototype-ladder.md](references/prototype-ladder.md) for rung selection,
experiment design, and promotion boundaries.

## Stop Conditions

Stop planning when the experiment is small enough to run and its result can
change a decision. Do not prototype when no outcome would affect the plan.
