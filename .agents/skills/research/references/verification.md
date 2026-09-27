# Verification

Use this workflow to answer: `Is the claim actually correct?`

Verification is distinct from critical review. It does not by itself establish novelty, significance, good scope, or publication value.

## Define the Verification Target

State the exact claim, assumptions, inputs, expected output, tolerance, and failure condition. Split compound claims when different evidence is required.

Classify the target as one or more of:

- proof or derivation;
- implementation or algorithm;
- symbolic transformation;
- numerical result;
- empirical estimate;
- citation or attribution;
- internal manuscript consistency;
- reproducibility of an artifact.

## Verification Modes

### Proof and derivation

- Check definitions, quantifiers, domains, boundary cases, and use of prior results.
- Inspect each nontrivial inference; do not accept an argument from plausibility or examples alone.
- Search for minimal counterexamples and degenerate cases.
- Distinguish a verified theorem from a derivation conditional on unverified premises.

### Implementation and computation

- Establish an oracle: trusted implementation, exact case, invariant, independent formulation, or analytically known limit.
- Check data flow, indexing, units, precision, seeds, stopping rules, and failure paths relevant to the claim.
- Prefer paired comparisons against the oracle over visual similarity.
- Re-run representative and adversarial cases; record the environment and exact command when reconstruction matters.

### Symbolic and numerical results

- Use symbolic checks where identities should hold exactly.
- Use numerical checks across representative, boundary, and ill-conditioned cases.
- State tolerance and precision explicitly; separate numerical agreement from proof.

### Citations

- Open the source rather than relying on memory or snippets.
- Confirm that the cited source supports the precise claim and that metadata identifies the intended work.
- Label indirect or secondary support as such.

### Reproduction

- Recover the declared inputs, code or procedure, configuration, environment, and expected outputs.
- Run the narrowest reproduction that tests the central claim.
- Record discrepancies and do not silently substitute different inputs or settings.

## Independence

Independent verification is valuable when the claim is consequential or the original derivation may anchor the review. Use a separate method, oracle, reviewer, or permitted subagent only when the independence benefit justifies the added cost.

## Result Status

Report one of:

- `VERIFIED`: the specified checks passed for the stated scope;
- `PARTIALLY VERIFIED`: only named components or cases passed;
- `NOT VERIFIED`: required evidence was unavailable or not run;
- `CONTRADICTED`: evidence conflicts with the claim;
- `INCONCLUSIVE`: checks do not discriminate between live alternatives.

Include the target, evidence, commands or sources, coverage, failures, and remaining uncertainty. Never generalize beyond the verified scope.
