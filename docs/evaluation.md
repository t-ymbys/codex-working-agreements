# Evaluation

## Comparison

- **A:** initial public release `027320c`, large global policy and monolithic workflows.
- **B:** checkpoint `d3019ee`, reduced global policy and routed Research Skill.
- **C:** current Agent OS, explicit source/runtime separation, execution-policy templates, installer, doctor, and Skill-only plugin boundary.

Use isolated checkouts and runtime homes. Hold model capability, reasoning level, tools, task input, repository state, and limits constant. Randomize configuration order and use multiple runs for any stochastic performance claim.

## Golden Task Set

1. trivial local code edit that should not activate Research;
2. multi-file refactor with user changes already present;
3. bounded bug diagnosis with repeated-failure stopping;
4. mathematical proof or derivation verification;
5. literature investigation requiring primary sources;
6. interrupted-session recovery using Git and HANDOFF;
7. correct Skill and reference routing;
8. destructive or external action that must stop for approval;
9. offline task that should not use network;
10. research task that requires network;
11. source install, drift detection, and rollback;
12. Skill-only plugin package construction.

Define acceptance criteria, required evidence, forbidden actions, and expected routing before each run.

## Measures

- task completion, correctness, and acceptance-criteria satisfaction;
- unsupported claims and hallucinated repository facts;
- irrelevant exploration, files read, tokens, tool calls, and retry count;
- user intervention and permission escalation frequency;
- Skill activation, wrong activation, and reference-routing accuracy;
- validation coverage and recovery success;
- accidental destructive action and network usage;
- runtime configuration drift and installation reproducibility.

Use deterministic checks for explicit criteria and owner labels for research quality. Calibrate any LLM judge against owner labels and keep it blind to configuration identity where practical.

## Current Results

The repository-level regression suite covers static structure, current config-schema acceptance, Skill routing, package identity, isolated install idempotence, drift refusal, backup restoration, and runtime hash comparison. These checks establish software integrity, not superior agent behavior.

Behavioral superiority of C remains `NOT VERIFIED` until the golden tasks are run repeatedly. Adopt C operationally only if it reduces persistent or irrelevant context without a material loss in task success, research verification, safety, or recovery.
