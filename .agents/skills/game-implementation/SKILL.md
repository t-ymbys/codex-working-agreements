---
name: game-implementation
description: Implement local game prototypes and production increments for explicit experiment questions using reversible architecture, test scenes, observability, and proportional validation. Use when the design decision and acceptance criteria are ready; not to decide creative direction or authorize release.
---

# Game Implementation

## Trigger

Use after the prototype question, controlled variables, and acceptance criteria
are explicit. Also use for bounded production increments with established design
evidence. Invoke `local-first-app-development` for its local preview, release,
and cleanup boundary.

## Inputs

Inspect applicable instructions, repository status, existing user changes,
architecture, experiment brief, target platform, validation commands, and the
exact source or build being tested.

## Workflow

1. Preserve unrelated work and implement the smallest coherent change that
   answers the experiment question.
2. Isolate disposable prototypes from production code. Prefer parameters,
   seams, and test scenes for movement, timing, camera, difficulty, behavior,
   resources, spawn rules, and progression when they are likely to change.
3. Add enough debug UI, logs, or telemetry to observe the tested state without
   silently collecting or transmitting user data.
4. Avoid premature architecture and premature polish. Build polish only when it
   is the variable under test or supported by promotion evidence.
5. Validate syntax, tests, build, representative local play path, and served
   source identity as appropriate. Automated success proves mechanics and
   regressions, not fun or emotional quality.
6. Inspect the resulting diff and report exact validation plus residual risk.

## Outputs

Produce a runnable local increment, test evidence, observability notes, and a
version or build identifier linked from the experiment log. Use
[reversible-game-engineering.md](references/reversible-game-engineering.md) for
prototype isolation and validation guidance.

## Stop Conditions

Stop when the bounded acceptance criteria pass or the experiment is blocked by
a design decision. Do not deploy, host, upload, distribute, or release without
explicit authorization through a named channel.
