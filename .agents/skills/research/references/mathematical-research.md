# Mathematical and Theoretical Research

Use this reference for theorem development, proof audit, formal models, and theory-heavy claims. Use [verification.md](verification.md) when the result must be certified rather than merely developed.

## Formalize the Claim

Identify as applicable:

- definitions, domain, and codomain;
- assumptions and regularity conditions;
- genericity, exceptional sets, and boundary conditions;
- local, global, generic, and almost-everywhere scope;
- exact versus approximate status;
- necessary versus sufficient conditions;
- dependencies on earlier lemmas or external theorems.

Do not let prose carry assumptions that belong in the formal statement.

## Develop or Audit the Argument

For each central implication:

1. state the claim precisely;
2. identify dependencies;
3. isolate lemmas;
4. determine whether the implication is one-way or reversible;
5. test simple, degenerate, singular, and boundary cases;
6. search for counterexamples;
7. check compatibility with known results;
8. mark any heuristic or unresolved step.

Treat previous unpublished work, including the researcher's own, with the same logical scrutiny as external work.

Classify the result when useful as:

- rigorous as stated;
- correct under added assumptions;
- repairable with additional lemmas;
- heuristic;
- numerically supported only;
- requiring reformulation;
- unresolved.

## Structural Reasoning

Dimension counting, symmetry, analogy, or representation similarity can guide discovery but do not prove the claim without the missing conditions.

Distinguish relations such as equivariance, conjugacy, semiconjugacy, embedding, isomorphism, and equivalence. Do not upgrade one relation into another because the structures look similar.

## Adversarial Checks

Seek:

- hidden coordinate, gauge, or normalization dependence;
- reducible or non-generic cases;
- failure under limiting operations;
- alternative definitions that change the result;
- a simpler theorem that subsumes the claim;
- known results that trivialize or contradict it.

Do not hide a proof gap by strengthening the prose.

## Output

State the exact surviving claim, assumptions, proof status, dependencies, counterexamples considered, unresolved steps, and the next discriminating lemma or calculation.
