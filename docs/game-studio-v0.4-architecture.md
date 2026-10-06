# Game Studio Skill Suite v0.4 Architecture Proposal

## Status and Evidence Boundary

This document is the implementation baseline for the first Game Studio build.
It translates the supplied specification into Skill boundaries, artifacts, and
validation criteria. It is a design proposal, not evidence that the workflow
produces better games. Behavioral superiority remains `NOT VERIFIED` until the
end-to-end comparisons are run with real creators and playtest evidence.

## Objective

Optimize the workflow for discovering and refining games worth finishing:

`intent -> reflection -> research -> design -> alternatives -> conviction -> prototype -> play -> evidence -> critique -> mutation -> comparison -> refinement -> production`

The system must preserve creator authority, keep game work local unless release
is explicitly authorized, and distinguish playable software from demonstrated
fun, originality, memorability, or market value.

## Existing-System Review

- Canonical repository Skills live in `.agents/skills/`; installation and plugin
  packaging discover Skill directories dynamically.
- `research` owns scholarly evidence retrieval, novelty checking, verification,
  and reproducibility. Game-specific lineage analysis may invoke it but must not
  duplicate its literature protocol.
- `local-first-app-development` owns deployment and distribution authorization.
  Game implementation must invoke it for build, preview, release, or cleanup
  boundaries instead of restating the policy.
- `multidisciplinary-review` remains optional for explicitly requested or
  consequential cross-domain reviews.
- `experience-promotion` governs durable operating-system lessons, not ordinary
  game experiment logs.

## Skill-Boundary Decision

Phase 1 keeps nine independently discoverable Skills because each has a distinct
activation surface, input contract, and stopping condition:

| Skill | Owns | Does not own |
|---|---|---|
| `game-studio-orchestrator` | routing, project state, gates, artifact integrity | specialist design judgments |
| `game-creative-director` | intent, taste, conviction, identity forks | selecting implementation details |
| `game-reference-originality` | lineage, anti-reference, transformation, derivative risk | broad market sizing or legal clearance |
| `game-concept-design` | player fantasy, thesis, pillars, engagement and memory reasons | detailed mechanics or production architecture |
| `game-systems-design` | loops, decisions, depth, mastery, parameterized system alternatives | code implementation |
| `game-prototype-strategy` | empirical question, prototype rung, experiment design | judging subjective results |
| `game-evaluation` | independent evidence plan, playtest observation, critical review | mutating the design under evaluation |
| `game-iteration` | bottleneck choice, controlled mutation, comparison, kill/promote | declaring unsupported quality gains |
| `game-implementation` | reversible local prototype/production implementation | creative authority or release authorization |

Phase 2 areas remain references or project-owned work until use demonstrates a
need for separate Skills. Do not create placeholder Skills for market, world,
level, visual, audio, or technical design in this phase.

## Progressive-Disclosure Design

- Each `SKILL.md` contains only trigger, inputs, workflow, outputs, routed
  references, and stop conditions.
- The orchestrator owns shared stage and artifact contracts.
- Detailed schemas are reusable assets copied into a game project's
  `.game-studio/` directory only when needed.
- Specialist references contain only domain-specific heuristics that materially
  change decisions; they do not repeat the master specification.
- A request loads only the orchestrator plus the smallest specialist set needed
  for the current uncertainty.

## Project Artifact Model

Default project state lives under `.game-studio/` so generated artifacts remain
separate from Skill source:

```text
.game-studio/
|-- studio-state.yaml
|-- creator-taste.yaml
|-- creator-conviction.yaml
|-- fun-hypotheses.yaml
|-- reference-ledger.yaml
|-- experiment-log.yaml
|-- v1-maturity.yaml
|-- decision-log.yaml
|-- evaluations/
`-- design-graveyard/
```

Create only artifacts needed by the current project and stage. Preserve failed
experiments when their learning value exceeds their maintenance cost.

## State and Gates

Project ambition is one of `experiment`, `prototype`, `small_game`,
`release_candidate`, or `signature_candidate`. Prototype rung is one of `D0`,
`P0`, `P1`, `P2`, `VS`, `A0`, or `RC`.

Promotion requires evidence proportional to ambition:

- Production promotion: core-fun evidence, creator conviction, and design
  coherence.
- Signature promotion: distinct identity, strongest moments, reference
  differentiation, creator pride, and external player evidence.
- No AI-generated score may substitute for creator choice or player behavior.
- The orchestrator may recommend `advance`, `hold`, `mutate`, `kill`, or
  `de-scope`; consequential creative forks remain human decisions.

## Evidence Contract

Use evidence levels `E0` through `E6` from concept speculation to behavioral
telemetry. Every evaluative claim records evidence level, confidence, rationale,
and provenance. Human-dominant qualities such as fun, feel, fear, humor, wonder,
beauty, emotional resonance, and memorability cannot be promoted beyond the
human evidence actually collected.

## Phase 1 Acceptance Criteria

1. All nine Skills pass the bundled structural validator.
2. Shared artifact templates parse as YAML and use only documented enumerations.
3. Repository validation, unit tests, and plugin packaging pass.
4. A deterministic suite check detects missing Skills, broken artifact schemas,
   unresolved scaffold text, and forbidden unsupported quality claims.
5. One existing-concept fixture and one zero-to-concept fixture exercise routing,
   artifacts, evidence labeling, and gate decisions without claiming human
   playtest results.
6. Regression checks confirm that the suite does not require every specialist,
   full research, feature inflation, or implementation before a discriminating
   prototype question exists.

## Stop Conditions

Stop Phase 1 when the acceptance criteria pass and remaining uncertainty is
behavioral rather than structural. Do not install into the live runtime,
publish, push, deploy, or claim improved game quality without separate explicit
authorization and evidence.
