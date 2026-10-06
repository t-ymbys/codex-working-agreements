# Systems Heuristics

## Core Loop Audit

Trace the player's action, immediate feedback, state change, next decision,
consequence, and learning. A reward delivered without a changed future decision
is weak systemic feedback.

## Depth Audit

Use this as a qualitative lens, not a score:

`depth ~= interaction density x decision consequences x strategic horizon x mastery potential`

Ask:

- Do rules interact or merely accumulate?
- Can the same state support meaningfully different strategies?
- Are consequences legible soon enough to learn and delayed enough to plan?
- Does mastery reveal new understanding rather than only execution speed?
- Can a rule be removed without reducing meaningful play?
- Is difficulty produced by richer decisions or inflated statistics?

## Variant Construction

Hold all but one major variable stable when possible. Useful mutations include
add, remove, merge, invert, constrain, amplify, hide, reveal, delay, accelerate,
randomize, make deterministic, make persistent, and make reversible.

## Failure Diagnosis

- repetition without changed understanding: vary relationships, not content;
- choices with similar consequences: widen tradeoffs or remove false choices;
- rewards driving otherwise empty play: repair the loop before progression;
- randomness standing in for depth: expose controllable responses and planning;
- tutorial compensating for unreadable rules: improve feedback and affordances;
- feature inflation: run ablation and identify the smallest expressive ruleset.
