# Computational and Numerical Research

Use this reference for symbolic computation, numerical mathematics, simulations, computational experiments, and implementation-dependent scientific claims.

## Experiment Contract

Before a substantial computation, define:

- the question and competing hypotheses;
- independent and dependent quantities;
- parameter domain and sampling plan;
- baseline or analytically solvable cases;
- precision, tolerance, seed, and stopping criteria;
- expected artifacts or failure modes;
- the output that would discriminate the hypotheses.

Start with the cheapest informative computation. Do not run a large sweep merely because compute is available.

## Symbolic Computation

Preserve exact arithmetic when appropriate. Record assumptions, coefficient fields, variable and monomial order, localization or saturation, eliminated variables, and interpretation of components when they affect the claim.

Check denominators, singular loci, extraneous solutions, generic versus exceptional components, and transformations performed by the system.

A computer-algebra output is evidence, not a proof, until the logical link from the computation to the claim is explained.

## Numerical Computation

Assess as relevant:

- convergence and conditioning;
- precision and solver tolerance;
- initialization and branch selection;
- sensitivity to parameters, seeds, and discretization;
- stability across implementations or algorithms;
- agreement with known or exactly solvable cases.

Distinguish numerical instability, visualization artifacts, and implementation behavior from mathematical structure. A plot is not a theorem.

## Implementation Integrity

Inspect whether the code actually implements the stated object and protocol. Look for stale outputs, unit or indexing mistakes, leakage between phases, serialization changes, platform differences, and silent fallback behavior.

Preserve the chain:

`mathematical object → code → parameters → environment → execution → output → interpretation`

Keep source versioned, separate generated outputs from source, and record nondeterminism when exact reproduction is impossible.

## Output

Report the executed configuration, actual outputs inspected, sensitivity or benchmark checks, implementation risks, reproducibility status, and which conclusions are numerical observations rather than established results.
