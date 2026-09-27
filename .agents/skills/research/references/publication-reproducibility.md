# Publication and Reproducibility

Use this workflow for manuscript revision, publication assessment, and artifact preparation.

## Evidence Chain

Every consequential manuscript claim should be traceable through:

`claim -> source or result -> inputs -> method/code -> configuration -> output -> validation`

The required depth depends on the claim and venue. Preserve enough provenance for another qualified person to reconstruct the result without relying on conversation history.

## Reproducibility Package

Where applicable, record:

- source data and immutable identifiers or checksums;
- preprocessing and inclusion or exclusion rules;
- code version and exact commands;
- environment, dependencies, seeds, hardware-sensitive settings, and numerical precision;
- generated tables, figures, and intermediate artifacts;
- expected outputs, tolerances, and known nondeterminism;
- licenses, privacy constraints, and unavailable inputs.

Prefer scripts, manifests, tests, and build rules over prose reminders for repeatable steps.

## Manuscript Consistency

- Match the abstract, claims, figures, tables, methods, limitations, and conclusion to the same evidence boundary.
- Check terminology, notation, sample counts, metrics, units, and reported uncertainty across the manuscript.
- Distinguish exploratory from confirmatory analysis and observation from causal interpretation.
- Cite primary sources for literature-sensitive claims and verify the cited passages.
- Preserve negative or null results when they constrain the conclusion.

## Publication Assessment

Evaluate separately:

- correctness and verification coverage;
- novelty relative to the closest prior work;
- significance for the intended audience;
- methodological and reporting completeness;
- reproducibility and artifact availability;
- ethical, privacy, authorship, licensing, and disclosure constraints;
- fit with the target venue and likely reviewer objections.

Use calibrated outcomes such as `READY`, `READY AFTER NAMED CHANGES`, `HOLD`, or `NO-GO`, with evidence and conditions. Do not equate a clean build or completed draft with scientific readiness.

## Durable State

Keep current claims, objections, performed validation, remaining work, and the last checkpoint in `HANDOFF.md` when the project uses one. Keep historical changes in Git and generated evidence in reproducible reports or artifacts rather than expanding the handoff into a transcript.
