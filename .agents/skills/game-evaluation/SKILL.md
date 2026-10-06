---
name: game-evaluation
description: Independently evaluate a game concept or build with evidence-calibrated playtests, selected quality dimensions, behavioral observations, and adversarial critique. Use after a testable artifact exists or at major gates; not to praise the design or mutate it during evaluation.
---

# Game Evaluation

## Trigger

Use for creator playtest capture, internal or target-player tests, pairwise
comparison, milestone criticism, or promotion evidence. Separate the evaluator's
context from the design rationale when practical.

## Inputs

Use a frozen build or concept version, the question being tested, selected
dimensions, participant type, protocol, prior evidence, and known confounds.
Do not infer human reactions from automated play.

## Workflow

1. Select only dimensions material to the current decision.
2. Record evidence level `E0` through `E6`, confidence, rationale, provenance,
   version, and limitations for every judgment.
3. Observe repeated actions, hesitation, experimentation, voluntary replay,
   quitting, unused mechanics, unexpected strategies, and unprompted discussion.
4. Save creator playtest separately from target-player results. Analyze
   disagreement rather than selecting a mechanical winner.
5. Use automation for regression, coverage, reachability, economy simulation,
   edge cases, crashes, and strategy search, not human-dominant experience claims.
6. At important milestones ask why the game is mediocre, why it would be
   remembered among competent alternatives, what survives the shelf test, and
   what might matter in ten years.
7. Report observations before interpretations and interpretations before
   recommendations. Do not change the evaluated build during the pass.

## Outputs

Write a versioned evaluation under `.game-studio/evaluations/` and update
evidence links without overwriting raw observations. Use
[evidence-and-playtests.md](references/evidence-and-playtests.md) for level and
dimension definitions.

## Stop Conditions

Stop when the question has enough evidence for a decision, the effort bound is
reached, or a different test is more discriminating. Mark human-dominant claims
`NOT VERIFIED` when no human evidence exists.
