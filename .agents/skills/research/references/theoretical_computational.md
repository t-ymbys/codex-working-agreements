# Theoretical, Mathematical, and Computational Research

Use this reference for theorem development, proof auditing, mathematical modeling, symbolic computation, numerical mathematics, and theory-heavy research.

## 1. Formalize the Claim

For each important mathematical claim, identify:

- definitions;
- domain and codomain;
- assumptions;
- regularity conditions;
- genericity assumptions;
- exceptional sets;
- boundary conditions;
- exact versus approximate status;
- necessary versus sufficient conditions.

Do not rely on prose to carry assumptions that belong in the formal statement.

## 2. Theorem Audit

For proposed or inherited theorems, inspect:

- exact statement;
- definitions used;
- logical dependencies;
- proof structure;
- hidden assumptions;
- exceptional cases;
- necessity versus sufficiency;
- compatibility with known results;
- plausible counterexamples.

For previous work, including the researcher's own work, do not assume the original theorem statement is complete.

Classify the result when useful as:

- rigorous as stated;
- essentially correct but missing assumptions;
- repairable with additional lemmas;
- heuristic;
- numerically supported;
- requiring substantial reformulation;
- uncertain.

Treat previous user work with the same scrutiny as external work.

## 3. Proof Development

When constructing a proof:

1. state the claim precisely;
2. identify dependencies;
3. isolate lemmas;
4. check whether each implication is reversible or one-way;
5. inspect degenerate and boundary cases;
6. test against simple examples;
7. search for counterexamples where feasible;
8. distinguish local, generic, almost-everywhere, and global claims;
9. record any step that remains heuristic.

Do not hide a proof gap by strengthening prose.

## 4. Dimensional and Structural Arguments

Dimension counting, symmetry arguments, analogy, and representation-theoretic similarity can be informative but do not by themselves establish a theorem unless the missing conditions are proved.

Distinguish:

- structural analogy;
- equivariance;
- conjugacy;
- semiconjugacy;
- embedding;
- isomorphism;
- equivalence of categories or representations.

Do not upgrade one relation into another merely because the structures look similar.

## 5. Symbolic Computation

Treat symbolic computation as evidence whose assumptions and algebraic transformations matter.

Where relevant:

- preserve exact arithmetic;
- record assumptions;
- check denominator and singular loci;
- identify generic versus exceptional components;
- detect extraneous solutions;
- verify factorization or elimination independently where practical;
- record software and version when reproducibility matters.

For Gröbner-basis or elimination calculations, record:

- polynomial ring and coefficient field;
- variable order;
- monomial order;
- saturation or localization assumptions;
- eliminated variables;
- interpretation of components.

Do not present a CAS output as a proof without explaining why the computation implies the claimed result.

## 6. Numerical Computation

For numerical results, consider:

- convergence;
- precision;
- initialization;
- solver tolerance;
- parameter sensitivity;
- conditioning;
- numerical stability;
- reproducibility across implementations;
- analytically solvable or benchmark cases.

Distinguish numerical instability from actual mathematical or dynamical structure.

A plot is evidence, not proof.

## 7. Computational Experiment Design

Before large computation, identify:

- question being tested;
- independent and dependent variables;
- parameter range;
- baseline;
- expected failure modes;
- stopping criteria;
- output needed to discriminate competing hypotheses.

Start with the cheapest informative experiment.

Do not run large sweeps merely because compute is available.

## 8. Adversarial Checks

For a central theoretical result, actively seek:

- counterexamples;
- singular cases;
- reducible or degenerate cases;
- hidden dependence on coordinates or gauge;
- non-generic behavior;
- failure under limiting procedures;
- alternative definitions that change the conclusion;
- known theorems that trivialize or contradict the result.

For a computational result, seek:

- implementation artifacts;
- precision artifacts;
- branch or root-selection artifacts;
- sampling artifacts;
- solver dependence;
- visualization artifacts.

## 9. Reproducible Computation

Preserve the chain:

`mathematical object → code → parameters → environment → execution → output → interpretation`

Where practical:

- keep source code versioned;
- separate generated outputs from source;
- record important parameters;
- use deterministic seeds where appropriate;
- record non-deterministic behavior;
- make figure generation reproducible.

## 10. Completion Criteria

Do not treat a theoretical or computational milestone as complete until the relevant subset of the following is true:

- statement is precise;
- assumptions are explicit;
- proof dependencies are understood;
- counterexamples were considered;
- symbolic calculations were actually executed;
- numerical calculations were actually executed;
- outputs were inspected;
- results are reproducible enough for the intended claim;
- manuscript wording matches the strength of the evidence;
- unresolved gaps are explicitly documented.
