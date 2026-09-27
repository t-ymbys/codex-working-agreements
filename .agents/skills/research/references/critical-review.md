# Critical Review

Use this workflow to answer: `Even if the claim is correct, is it meaningful, novel, well-scoped, and defensible?`

Correctness belongs to [verification.md](verification.md). Prior-art retrieval belongs to [literature.md](literature.md). Load those references only when the review requires them.

## Review Frame

Identify:

- the strongest version of the claimed contribution;
- the intended comparison class and audience;
- the decision at stake, such as further research, manuscript revision, submission, or rejection;
- the evidence that would materially change that decision.

## Adversarial Questions

### Assumptions and scope

- Which assumptions are explicit, hidden, unrealistic, or doing most of the work?
- Does the conclusion hold only in a narrow regime that the presentation obscures?
- Are definitions, estimands, populations, or comparison classes shifting?

### Competing explanations

- Can a simpler mechanism, artifact, leakage path, selection effect, or implementation choice explain the result?
- What observation would distinguish the preferred explanation from its strongest competitor?
- Have negative controls, ablations, counterexamples, or boundary cases been considered where relevant?

### Novelty and relation to prior work

- What is the closest prior work at the level of mechanism and claim, not just keywords?
- Is the contribution a new result, synthesis, implementation, interpretation, benchmark, or application?
- Would the novelty claim survive narrower and more accurate wording?

### Significance and generality

- Does the result change understanding, capability, practice, or a consequential decision?
- Is the gain large enough to matter relative to uncertainty and cost?
- Which parts generalize, and which are local to the studied assumptions or data?

### Defensibility

- What would a technically informed skeptical reviewer object to first?
- Which claim is least supported by the current evidence?
- Are limitations, negative results, and alternative interpretations visible rather than buried?
- Does the title, abstract, or conclusion outrun the verified contribution?

## Output

Separate:

- verified strengths;
- major objections;
- minor objections;
- competing interpretations;
- novelty and significance assessment;
- required changes before the next decision;
- residual disagreement or uncertainty.

Do not convert an absence found in a bounded search into proof of novelty or nonexistence.
