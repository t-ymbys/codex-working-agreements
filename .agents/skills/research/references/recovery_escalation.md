# Research Recovery, Handoff, and Model Escalation

Use this reference when research resumes after interruption, when project state is uncertain, or before high-cost reasoning or major multi-file work.

## 1. Recovery Takes Priority

After an interruption, do not immediately continue substantive editing.

Possible interruption causes include:

- credit exhaustion;
- context loss;
- model switch;
- tool failure;
- user interruption;
- process failure;
- partial file writes;
- unfinished multi-file edits.

First reconstruct the current state.

Never assume the interrupted operation either completed successfully or made no changes.

## 2. Recovery Phase

Perform the applicable subset in this order.

### A. Identify project boundary

Determine the logical project root.

If a parent directory contains independent research projects, do not automatically treat the parent as a single repository.

Prefer:

`one logical research project = one Git repository`

### B. Read applicable instructions

Read:

- global instructions already loaded;
- the nearest applicable project `AGENTS.md`, if any;
- this research Skill;
- existing `HANDOFF.md`, if present.

Do not invent missing instructions.

### C. Inspect filesystem state

Inspect:

- directory structure;
- relevant recently modified files;
- manuscripts;
- source code;
- generated outputs;
- logs or TODOs where useful.

Do not start large new edits during this phase.

### D. Inspect Git state

If Git exists, inspect:

- repository root;
- current branch;
- `git status`;
- relevant diffs;
- recent commits;
- untracked files.

Preserve pre-existing user work.

If Git does not exist and the work is substantial, multi-file, or multi-session, prefer initializing Git at the logical project root after checking `.gitignore` requirements.

### E. Classify current work

Classify relevant items as:

- completed;
- in progress;
- not started;
- unvalidated;
- uncertain.

For research claims, also distinguish:

- established result;
- computational evidence;
- literature-supported claim;
- interpretation;
- hypothesis or conjecture;
- unverified statement.

### F. Determine what actually ran

Separate evidence of completed execution from generated plans or prose.

Determine which of the following were actually performed:

- calculations;
- tests;
- literature searches;
- builds;
- scripts;
- figure generation;
- numerical experiments.

Do not infer successful execution merely because an output file exists.

## 3. First Git Baseline After Unversioned Interruption

If the project was not previously versioned and now contains partial agent changes, the first commit is not a pristine historical baseline.

After checking for secrets, private data, large generated files, caches, and other exclusions, use an explicit recovery checkpoint such as:

`checkpoint: recovered working state after interrupted agent session`

Do not call it:

- `initial clean state`;
- `original state`;
- `pristine baseline`.

The commit records the earliest recoverable state currently available.

## 4. HANDOFF.md

Use project-local `HANDOFF.md` for substantial multi-session work when it materially improves recovery.

Do not use it as a chronological diary.

Keep it current and concise.

Recommended structure:

```markdown
# HANDOFF

## Objective

## Current Status

## Completed

## In Progress

## Open Questions

## Current Claims

## Unverified Claims

## Validation Performed

## Validation Remaining

## Next Actions

## Last Checkpoint
```

Update it when the semantic project state changes materially.

Git stores historical state.

`HANDOFF.md` stores current semantic state.

## 5. Recovery Completion

Before resuming substantive research, be able to state:

- repository root;
- current branch;
- working tree status;
- completed work;
- incomplete work;
- uncertain work;
- validation already performed;
- validation still needed;
- immediate next action.

Create a checkpoint when appropriate.

Then resume only the remaining work.

Do not blindly rerun the original task from the beginning.

## 6. Model and Compute Escalation

Use the least expensive model and reasoning level that can reliably perform the current subtask.

Use routine-capability models for:

- recovery inspection;
- Git and handoff maintenance;
- ordinary manuscript edits;
- ordinary implementation;
- routine symbolic or numerical setup;
- formatting and cleanup;
- standard validation.

Escalate to a stronger model only when the unresolved issue materially benefits from deeper reasoning, such as:

- difficult proof validation;
- subtle theorem assumptions;
- deep counterexample search;
- novelty assessment with ambiguous prior art;
- competing theoretical formulations;
- high-impact conceptual review;
- important issues unresolved after competent lower-cost attempts.

Model names change over time. Treat current product names as examples, not permanent policy.

If the environment currently offers a capable standard model and a more expensive frontier model, use the standard model for recovery and routine research, and reserve the expensive model for the high-leverage questions above.

Do not assume an agent can switch models automatically. If a switch requires user action, preserve state and clearly identify the question that merits escalation.

## 7. Before High-Cost Reasoning

Before an expensive review or reasoning phase:

1. save completed work;
2. create a coherent Git checkpoint when appropriate;
3. update `HANDOFF.md` if used;
4. isolate the exact unresolved question;
5. minimize irrelevant context;
6. identify expected output, such as:
   - proof audit;
   - counterexample search;
   - novelty review;
   - architectural decision;
   - referee-style critique.

Do not spend frontier-model budget on mechanical filesystem work.

## 8. After High-Cost Review

Do not automatically accept all suggestions.

Classify important outputs as:

- accepted;
- rejected;
- requires verification;
- optional;
- unresolved.

Use ordinary execution tools or models to implement accepted changes where practical.

Validate the resulting state.

Checkpoint the coherent post-review state.

## 9. Branch Use

Do not use branches to separate unrelated research projects.

Branches are optional isolation mechanisms within one project.

Use a branch when it has a concrete benefit, for example:

- alternative formulation;
- risky refactor;
- reviewer revision;
- parallel implementation;
- experimental approach.

For ordinary sequential work on a personal research project, staying on the main branch is acceptable.

## 10. Recovery Stopping Criterion

Recovery is complete when the project state is sufficiently understood to continue without likely overwriting, duplicating, or contradicting prior work.

Do not continue forensic investigation once:

- the relevant project state is known;
- important uncertainty is documented;
- the project is recoverable;
- the next action is clear.

The objective is safe continuation, not perfect reconstruction of every historical action.
