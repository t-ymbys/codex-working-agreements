# Reproducibility, Research Artifacts, and Publication

Use this reference for research project organization, provenance, manuscript claims, publication assessment, and completion review.

## 1. Reproducibility

A research result should preserve enough information to reconstruct the path:

`input/data → code/procedure → configuration → execution → output → figure/table → manuscript claim`

Where applicable, preserve:

- source data or data provenance;
- preprocessing;
- code;
- environment;
- software versions;
- parameters;
- seeds;
- command or notebook entry point;
- generated figures and tables;
- mapping from outputs to manuscript claims.

Do not treat an artifact as authoritative if its provenance is unknown.

## 2. Research Artifact Provenance

For important outputs, determine:

- who or what generated it;
- from which input;
- using which code;
- with which parameters;
- under which software environment;
- whether it has been regenerated successfully;
- whether it has been independently checked.

Examples include:

- figures;
- tables;
- symbolic results;
- numerical datasets;
- simulation outputs;
- benchmark reports;
- manuscript equations.

When replacing a historical tool or implementation, preserve enough of the old artifact to compare results.

## 3. Project Structure

Adapt to the project, but a research repository may use:

- `manuscript/` for papers and supplementary text;
- `src/` for reusable source code;
- `experiments/` for experiment entry points;
- `data/` for data or data manifests;
- `results/` for generated outputs;
- `literature/` for notes or bibliographic material;
- `docs/` for durable research documentation;
- `HANDOFF.md` for current multi-session state when needed.

Do not create directories merely to satisfy a template.

Use existing project conventions when they are coherent.

## 4. Git Scope

Prefer:

`one logical research project = one Git repository`

A project may include its manuscript, computational code, experiments, figures, and supporting documentation.

Do not use branches to represent unrelated research topics.

Use branches only when isolation within the same research project is useful, such as:

- alternative theoretical formulations;
- reviewer revisions;
- risky refactors;
- parallel implementations;
- competing computational strategies.

For ordinary sequential personal research, a single main branch is sufficient.

## 5. Research Planning

For substantial research, define:

- research question;
- nearest prior work;
- candidate contribution;
- minimal falsification test;
- pilot calculation or experiment;
- evidence required for a strong conclusion;
- foreseeable failure modes;
- publication target only after contribution strength is understood.

Prefer staged investment:

1. cheap conceptual checks;
2. targeted literature;
3. pilot calculation;
4. full analysis;
5. manuscript expansion.

Do not front-load expensive implementation when a cheaper check could invalidate the premise.

## 6. Research Failure Is Valid

Valid outcomes include:

- novelty claim invalidated;
- theorem false as stated;
- method fails against a baseline;
- effect disappears under robustness checks;
- data cannot identify the proposed causal effect;
- numerical phenomenon is an artifact;
- project is not publication-worthy in current form.

Do not disguise negative outcomes as success.

A useful research report explains why the original hypothesis failed and what remains informative.

## 7. Manuscript Claims

Every important manuscript claim should match the actual evidence.

Avoid language stronger than justified.

Distinguish:

- proved;
- derived under assumptions;
- numerically observed;
- empirically supported;
- consistent with;
- suggestive;
- hypothesized;
- conjectured.

Do not write definitive novelty language until the literature review supports it.

Do not cite a source for a claim the source does not actually support.

## 8. Publication Assessment

Assess publication viability along separate dimensions:

- correctness;
- novelty;
- significance;
- evidence strength;
- clarity;
- reproducibility;
- fit to venue;
- completeness.

A technically correct result may still be too incremental.

A novel result may still be too weakly validated.

For venue recommendations, distinguish:

- realistic;
- ambitious;
- fallback.

Do not optimize for venue prestige before establishing the research contribution.

## 9. Reviewer-Style Audit

Before a major submission milestone, ask:

- What is the central claim?
- What is the strongest prior-art objection?
- What assumption is easiest to attack?
- What result would a reviewer request to reproduce?
- What baseline is missing?
- Is the theorem stronger than the proof?
- Is the empirical claim stronger than the identification?
- Is the computational evidence robust?
- Is the contribution meaningful beyond new terminology?
- Can a reader reproduce the central result?

## 10. Final Research Validation

Before treating a milestone as complete, check as applicable:

- internal mathematical consistency;
- notation consistency;
- assumptions;
- symbolic verification;
- numerical reproduction;
- empirical uncertainty;
- code reproducibility;
- literature verification;
- citation accuracy;
- novelty claims;
- alternative explanations;
- counterexamples;
- boundary cases;
- reviewer-level objections.

A polished manuscript is not equivalent to a validated research result.

## 11. Reporting Status

At a milestone, summarize:

- established results;
- evidence obtained;
- unverified claims;
- failed hypotheses;
- limitations;
- remaining work;
- current publication assessment.

Prefer a precise incomplete status over an unjustified declaration of completion.
