---
name: research
description: Conduct rigorous academic and scientific research, including literature and novelty review, theorem or model scrutiny, empirical inference, reproducibility, manuscript work, and interrupted-project recovery. Use when claims require external evidence, scientific validation, or publication-quality analysis.
---

# Research

## Objective

Determine as accurately as the available evidence allows:

- what is already known;
- what is being claimed;
- whether the claim is correct and new;
- what evidence distinguishes it from alternatives;
- what remains uncertain;
- what next work is justified.

Do not optimize for validating the initial idea. Null results, counterexamples, non-novel findings, and failed hypotheses are valid outcomes.

## Epistemic Discipline

Keep relevant states distinct. Use labels when they improve clarity:

- `FACT` — directly verified factual information;
- `ESTABLISHED RESULT` — supported by reliable existing literature;
- `DERIVED RESULT` — derived in the current work;
- `PREVIOUS UNPUBLISHED RESULT` — prior unpublished result supplied by the researcher;
- `NUMERICAL OBSERVATION` — computed or observed but not analytically established;
- `HYPOTHESIS` — empirically or conceptually motivated proposition;
- `CONJECTURE` — mathematically formulated but unproved claim;
- `RESEARCH QUESTION` — unresolved question;
- `SPECULATION` — plausible but weakly supported interpretation;
- `NOT VERIFIED` — source or correctness not verified.

Do not silently promote one state into another. In particular, do not confuse numerical agreement with proof, correlation with causation, structural analogy with identity, or failure to find prior art with proof of novelty.

Literature-sensitive claims require external retrieval. Model memory may suggest queries or candidate references but is not evidence. If retrieval is unavailable or incomplete, mark affected claims `NOT VERIFIED`, state the limitation, and weaken or defer novelty and attribution conclusions. Never fabricate references or metadata.

## Start with the Research Question

Before choosing a sophisticated method, identify as applicable:

- object of study and target claim;
- scope, assumptions, and comparison class;
- observables, estimand, or measurable outcome;
- success criteria;
- failure, falsification, or stop criteria.

Prefer a question for which competing answers can be distinguished by mathematics, computation, data, or experiment.

If the task resumes after interruption or the project state is uncertain, read [references/recovery_escalation.md](references/recovery_escalation.md) before substantive work. Reconstruct the project boundary, Git state, artifacts, claims, and validation already performed; do not blindly restart.

## Reference Routing

Read only the references needed for the current task:

- Read [references/literature_novelty.md](references/literature_novelty.md) for literature review, prior-art search, novelty, priority, attribution, or current-frontier claims.
- Read [references/theoretical_computational.md](references/theoretical_computational.md) for theorem development, proof audit, mathematical modeling, symbolic computation, numerical mathematics, or theory-heavy work.
- Read [references/empirical_data.md](references/empirical_data.md) for experiments, observational data, causal inference, prediction, benchmarks, statistical uncertainty, or sensitive datasets.
- Read [references/reproducibility_publication.md](references/reproducibility_publication.md) for provenance, project organization, manuscript claims, publication assessment, or milestone review.
- Read [references/recovery_escalation.md](references/recovery_escalation.md) for interrupted work, uncertain state, handoff, or preparation for high-cost reasoning.

Do not bulk-load all references.

## Core Workflow

Adapt the depth to the research phase and stakes.

1. **Recover state when needed.** Establish what exists, what ran, what changed, and what remains unvalidated.
2. **Formalize the question.** State the claim, assumptions, comparison class, and discriminating evidence.
3. **Establish the evidence boundary.** Retrieve literature or source material, inspect provenance, and separate supplied claims from verified results.
4. **Challenge the central claim.** Seek the strongest objection, alternative explanation, counterexample, hidden assumption, boundary case, simpler mechanism, and identification or implementation failure.
5. **Run the cheapest discriminating check.** Prefer a minimal calculation, pilot, baseline, ablation, or experiment before full-scale work.
6. **Validate the result.** Confirm that calculations actually ran, evidence supports the wording, uncertainty is represented, and artifacts can be reconstructed to the level the claim requires.
7. **Decide the next phase.** Continue, revise, merge, stop, or escalate based on information gained rather than attachment to the initial hypothesis.

A useful progression is landscape, gap, formalization, pilot, full study, and publication. Do not perform expensive downstream work before cheaper checks establish viability, and do not remain in planning when calculation or experiment is the next discriminating action.

## Search and Investigation Bounds

Before open-ended investigation:

1. define the question and minimum evidence needed;
2. set a reasonable depth or effort budget;
3. diversify queries or methods rather than repeating near-identical attempts;
4. stop when the budget is reached, sources become redundant, or information gain materially diminishes;
5. record residual uncertainty and the next method needed to resolve it.

Distinguish `not found within the performed search`, `no known example after substantial review`, and `proved not to exist`.

## Reproducibility and Claim Strength

For results that matter beyond the current session, preserve the relevant chain:

`input/data → code/procedure → configuration → execution → output → figure/table → manuscript claim`

A polished artifact is not a validated result. Match wording to evidence: distinguish proved, derived under assumptions, numerically observed, empirically supported, consistent with, suggestive, hypothesized, and conjectured.

## Human Review Boundary

Explicitly flag decisions requiring human judgment, especially central novelty claims, unresolved theorem assumptions, ambiguous causal interpretations, privacy-sensitive data handling, venue choice, high-stakes conclusions, and destructive or irreversible project changes.

## Completion Gate

Before declaring a substantial milestone complete, determine which of the following apply and report their status:

- research question and assumptions are explicit;
- relevant literature was externally checked;
- novelty and attribution are appropriately qualified;
- central claims received adversarial scrutiny;
- analytical, computational, and empirical claims have suitable validation;
- uncertainty, limitations, and negative findings are recorded;
- artifacts are reproducible enough for the intended use;
- manuscript language matches the evidence;
- unresolved issues and next actions are explicit.

Stop when the requested research decision or artifact is supported to the required standard and further work would not materially change it. Do not continue merely to make the process appear more comprehensive.
