# Artifact Contracts

## General Rules

- Store project state under `.game-studio/` unless the project already has a
  clearer canonical location.
- Copy only needed templates from `assets/studio-template/`; never create every
  artifact as ceremony.
- Use stable ASCII identifiers. Free-text values may use the creator's language.
- Preserve raw observations separately from interpretation.
- Use ISO 8601 dates and repository-relative artifact paths where possible.
- Append experiments and decisions; do not silently rewrite failed history.
- Unknown information is `null`, `unknown`, or an explicit open question, not an
  invented value.

## Required Enumerations

- ambition: `experiment`, `prototype`, `small_game`, `release_candidate`,
  `signature_candidate`
- prototype rung: `D0`, `P0`, `P1`, `P2`, `VS`, `A0`, `RC`
- evidence level: `E0`, `E1`, `E2`, `E3`, `E4`, `E5`, `E6`
- confidence: `low`, `medium`, `high`
- gate: `advance`, `hold`, `mutate`, `kill`, `de_scope`
- status: `active`, `supported`, `weakened`, `rejected`, `unknown`

## Artifact Ownership

| Artifact | Primary owner | Update condition |
|---|---|---|
| `studio-state.yaml` | orchestrator | stage, gate, owner, or next decision changes |
| `creator-taste.yaml` | creative director | creator confirms, rejects, or contextualizes a taste hypothesis |
| `creator-conviction.yaml` | creative director | conviction changes or new evidence arrives |
| `fun-hypotheses.yaml` | concept design | mechanism, behavior, experience, or signals change |
| `reference-ledger.yaml` | reference originality | a reference materially affects design reasoning |
| `experiment-log.yaml` | prototype strategy and iteration | experiment is proposed, run, or decided |
| `v1-maturity.yaml` | orchestrator and iteration | current bottleneck or maturity evidence changes |
| `decision-log.yaml` | decision owner | consequential choice is made or reversed |
| `evaluations/*` | evaluation | a frozen version is evaluated |
| `design-graveyard/*` | iteration | a rejected path contains reusable learning |

## Evidence Discipline

`E0` concept speculation; `E1` analytical reasoning; `E2` runnable prototype;
`E3` creator playtest; `E4` internal human playtest; `E5` target-player
playtest; `E6` behavioral telemetry.

Every evaluative claim needs level, confidence, rationale, provenance, and the
version it concerns. Higher levels do not automatically dominate lower levels;
they answer different questions and may be confounded.

## Validation

Run:

```sh
python3 .agents/skills/game-studio-orchestrator/scripts/validate_game_studio.py \
  .game-studio
```

The validator checks structure and enumerations. It does not validate creative
quality, factual claims, playtest integrity, or promotion readiness.
