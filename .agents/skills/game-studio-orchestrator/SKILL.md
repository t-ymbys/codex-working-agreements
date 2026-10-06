---
name: game-studio-orchestrator
description: Route creator-centered game work through the smallest useful Game Studio workflow, maintain evidence-aware project state, and apply prototype, production, or signature gates. Use for starting, resuming, coordinating, or promoting a game project; not for isolated implementation edits that need no studio decision.
---

# Game Studio Orchestrator

## Trigger

Use when a game project needs stage recovery, workflow routing, artifact setup,
or a decision to advance, hold, mutate, kill, or de-scope. Do not load the full
suite for a narrow task.

## Inputs

Recover the creator's request, current project files, applicable instructions,
Git state when present, existing `.game-studio/` artifacts, ambition level,
prototype rung, and unresolved decision. Treat missing state as unknown rather
than inventing it.

## Workflow

1. Identify the next decision and the cheapest evidence that could change it.
2. Route only the needed specialist Skills using
   [routing-and-gates.md](references/routing-and-gates.md).
3. Create or update only the artifacts required by that decision. Use
   [artifact-contracts.md](references/artifact-contracts.md) and the templates in
   `assets/studio-template/`; preserve provenance and uncertainty.
4. Keep creator authority over identity, major concept, signature direction,
   scope, and conviction. Make small reversible technical choices autonomously.
5. Apply a gate proportional to ambition. Never equate runnable, tested, or
   polished with fun, original, memorable, or ready for release.
6. Record a concise state transition and next discriminating action.

Default sequence for a new game is:

`creative direction -> taste and intent -> reference originality -> concept -> systems -> prototype strategy -> implementation -> creator playtest -> independent evaluation -> iteration`

Skip steps that cannot affect the current decision. When uncertainty becomes
empirical, stop analysis and prototype.

## Outputs

- an updated `.game-studio/studio-state.yaml` or equivalent project state;
- routed specialist outputs with evidence levels and provenance;
- one explicit gate decision: `advance`, `hold`, `mutate`, `kill`, or
  `de_scope`;
- the smallest next experiment, decision, or user choice.

## References

- Read [routing-and-gates.md](references/routing-and-gates.md) for stage routing,
  promotion criteria, ambition levels, and anti-pattern guards.
- Read [artifact-contracts.md](references/artifact-contracts.md) before creating
  or materially changing Studio artifacts.
- Run `scripts/validate_game_studio.py` after copying or editing the templates.

## Stop Conditions

Stop when the next decision, evidence boundary, owner, and action are explicit.
Do not continue generating documents after they cease to reduce uncertainty.
Do not install, publish, deploy, or release without separate authorization.
