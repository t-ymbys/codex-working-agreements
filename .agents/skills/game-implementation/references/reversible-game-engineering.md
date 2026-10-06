# Reversible Game Engineering

## Prototype Isolation

Keep a disposable prototype, test scene, or adapter separate from production
architecture when its rules are still volatile. Record what may be reused and
what must not become a dependency. Do not prematurely migrate all prototype code
into production modules.

## Parameterization

Parameterize only likely experiment variables: movement, timing, camera,
difficulty, enemy behavior, resources, spawn rules, progression, and similar
high-change values. Avoid building a general framework without demonstrated need.

## Test Scenes and Observability

Use focused scenes such as movement, combat, economy, boss, puzzle, late-game,
visual, or audio tests. Expose enough internal state to explain results through
debug UI, deterministic seeds, logs, counters, or local telemetry. Remove or
protect debug facilities before release review.

## Validation Ladder

Select proportionally:

1. syntax, type, or static checks;
2. unit tests for rules and state transitions;
3. deterministic simulation for economy, reachability, or strategy bounds;
4. build and startup checks;
5. representative local interaction path and saved-state compatibility;
6. served source, URL, title, and console verification for browser games;
7. human playtest for experiential claims.

State exactly which checks ran. Passing steps 1 through 6 does not prove fun,
fear, humor, wonder, beauty, resonance, or memorability.
