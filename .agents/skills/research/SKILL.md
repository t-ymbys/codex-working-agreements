---
name: research
description: >
  Rigorous academic and scientific research workflow for literature review,
  novelty assessment, theoretical or mathematical work, computational and
  empirical studies, replication, research planning, manuscript preparation,
  publication assessment, and interrupted research recovery. Use when a task
  requires scientific claim validation, prior-work analysis, theorem or model
  scrutiny, empirical inference, reproducibility, or publication-quality research.
---

# Research

## Objective

The objective is not to validate the initial idea.

The objective is to determine, as accurately as the available evidence allows:

1. what is already known;
2. what is actually being claimed;
3. whether the claim is correct;
4. whether the claim is new;
5. what evidence would distinguish it from alternatives;
6. what remains uncertain;
7. what work would make the result scientifically stronger or publishable.

Treat research failure, null results, invalidated novelty claims, and negative findings as valid outcomes.

---

## Core Epistemic Discipline

Maintain explicit distinctions among relevant epistemic states.

Use labels when useful:

- `FACT` — directly verified factual information;
- `ESTABLISHED RESULT` — result supported by reliable existing literature;
- `DERIVED RESULT` — result derived during the current work;
- `PREVIOUS UNPUBLISHED RESULT` — prior unpublished result supplied by the researcher;
- `NUMERICAL OBSERVATION` — computational or empirical observation not analytically established;
- `HYPOTHESIS` — empirically or conceptually motivated proposition;
- `CONJECTURE` — mathematically formulated but unproved claim;
- `RESEARCH QUESTION` — unresolved question;
- `SPECULATION` — plausible but weakly supported interpretation;
- `NOT VERIFIED` — claim whose source or correctness has not been verified.

Do not silently promote one category into another.

In particular, do not confuse:

- mathematical possibility with proof;
- internal consistency with physical validity;
- numerical agreement with theorem;
- correlation with causation;
- structural analogy with theoretical identity;
- novelty of wording with novelty of substance;
- absence of discovered prior art with proof of novelty.

---

## Research Question Before Method

Before developing a sophisticated method, identify the actual research question.

Clarify, when relevant:

- object of study;
- target claim;
- scope;
- assumptions;
- observables or measurable quantities;
- comparison class;
- success criteria;
- failure or falsification criteria.

Prefer questions for which competing answers can be distinguished by mathematics, computation, data, or experiment.

---

## External Verification

Literature-sensitive claims require external retrieval.

Do not treat internal model knowledge as verified evidence for:

- novelty;
- priority;
- attribution;
- publication status;
- current state of the literature;
- exact bibliographic metadata;
- claims about what a paper proved or demonstrated.

Use available scholarly search, web search, arXiv or comparable repositories, publisher or journal sources, bibliographic databases, DOI metadata, official archives, or other primary sources.

Internal model knowledge may generate search terms, terminology variants, candidate authors, or candidate references, but those are leads to verify, not evidence.

If retrieval is unavailable, prohibited, incomplete, or fails:

- do not invent papers, authors, titles, dates, identifiers, quotations, or results;
- mark affected claims `NOT VERIFIED`;
- state the retrieval limitation;
- weaken or defer novelty and attribution conclusions.

Never fabricate references.

For literature review, prior-art search, and novelty assessment, read:

`references/literature_novelty.md`

---

## Adversarial Validation

For every central claim, actively consider:

- strongest objection;
- alternative explanation;
- counterexample;
- hidden assumption;
- degenerate or boundary case;
- known theorem that may subsume the result;
- simpler explanation;
- identification failure;
- measurement artifact;
- numerical artifact;
- implementation artifact.

Do not omit evidence because it weakens the preferred interpretation.

Prefer discriminating tests over demonstrations compatible with every competing explanation.

---

## Mathematical, Theoretical, and Computational Work

For substantial mathematical or theoretical work:

- make definitions and assumptions explicit;
- distinguish necessary from sufficient conditions;
- inspect exceptional sets and boundary cases;
- separate exact statements from approximations;
- audit proof dependencies;
- preserve symbolic and numerical provenance;
- do not promote computation or dimension counting into proof.

For detailed theorem auditing, symbolic computation, numerical validation, and theoretical workflows, read:

`references/theoretical_computational.md`

---

## Empirical and Statistical Work

For substantial empirical work:

- model the data-generating and observation process;
- distinguish prediction from causal identification;
- inspect selection, confounding, measurement error, missingness, dependence, leakage, and external validity;
- report uncertainty at a level appropriate to the claim;
- use baselines and competing explanations;
- protect confidential and personal data.

For detailed empirical, privacy, robustness, and data-analysis procedures, read:

`references/empirical_data.md`

---

## Reproducibility, Artifacts, and Publication

Research artifacts should preserve the chain:

`input/data → code/procedure → configuration → execution → output → figure/table → manuscript claim`

A polished artifact is not equivalent to a validated result.

For reproducibility, artifact provenance, manuscript claims, publication assessment, and completion criteria, read:

`references/reproducibility_publication.md`

---

## Phase Discipline

Use the lightest research phase sufficient for the current objective.

A useful default progression is:

1. landscape;
2. research gap;
3. formalization;
4. pilot validation;
5. full study;
6. publication.

Do not perform expensive full-scale work before cheaper checks have established that the research question, gap, and method remain viable.

Conversely, do not stay indefinitely in literature review or planning when the next uncertainty is best resolved by calculation or experiment.

---

## Search and Investigation Bounds

All searches and investigations must have stopping criteria.

Before a potentially open-ended search:

1. define the question;
2. choose a reasonable depth or effort budget;
3. diversify queries or methods instead of repeating near-identical attempts;
4. stop when the budget is reached or information gain materially diminishes;
5. record residual uncertainty.

Distinguish:

- `not found within the performed search`;
- `no known example after substantial review`;
- `proved not to exist`.

Do not turn bounded failure to find evidence into an absolute claim.

---

## Human Review Flags

Explicitly flag matters that should receive human judgment, especially:

- central novelty claims;
- theorem statements with unresolved assumptions;
- interpretation of ambiguous empirical evidence;
- important causal claims;
- privacy-sensitive data handling;
- publication venue choice;
- high-stakes conclusions;
- destructive or irreversible project changes.

Do not hide unresolved uncertainty behind polished prose.

---

## Interrupted or Long-Running Research

If a task resumes after:

- credit exhaustion;
- context loss;
- model switch;
- failed execution;
- user interruption;
- partially completed edits;

do not immediately continue substantive research.

First read:

`references/recovery_escalation.md`

and perform the applicable recovery procedure.

For substantial multi-session research, maintain project-local durable state such as `HANDOFF.md` when useful.

Do not create a handoff file for trivial or disposable tasks.

---

## Model and Compute Use

Use the least expensive model and reasoning effort that can reliably perform the current subtask.

Use routine models for:

- file inspection;
- ordinary implementation;
- manuscript editing;
- standard calculations;
- formatting;
- documentation;
- deterministic cleanup.

Escalate only when the unresolved issue materially benefits from stronger reasoning, such as:

- difficult proof validation;
- deep counterexample search;
- subtle novelty assessment;
- competing theoretical formulations;
- high-impact conceptual review;
- important issues that remain unresolved after competent lower-cost attempts.

Treat model names as environment-specific implementation details rather than permanent research policy.

Before expensive reasoning, preserve project state and isolate the exact question.

---

## Completion Gate

Do not declare a substantial research milestone complete merely because text, code, figures, or calculations exist.

Before completion, determine which of the following apply:

- research question is explicit;
- relevant literature was externally checked;
- novelty claims are appropriately qualified;
- assumptions are explicit;
- central claims have adversarial scrutiny;
- analytical claims have proof or appropriate qualification;
- computational results were actually executed and checked;
- empirical claims have appropriate validation and uncertainty;
- artifacts are reproducible enough for the intended use;
- manuscript claims match the evidence;
- unresolved issues are documented.

Report what is complete, what is validated, and what remains unresolved.
