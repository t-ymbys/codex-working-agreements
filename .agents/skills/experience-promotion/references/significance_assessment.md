# Significance Assessment

Use this reference only when an event's significance is unclear or material. Prefer qualitative judgments over a falsely precise score.

## Assessment Axes

- **Severity:** How serious was the actual or plausible impact?
- **Generalizability:** Does the lesson extend beyond the immediate case?
- **Expected reuse:** How likely is it to affect future decisions?
- **Confidence:** How strongly do the evidence and explanation support the lesson?
- **Transferability:** Does it apply across projects, environments, tools, or models?
- **Human salience:** Did the user explicitly identify the outcome or constraint as important?
- **Mitigation value:** Would a change materially reduce cost, risk, or repeated effort?
- **Reversibility:** How easily can the proposed intervention be undone?

Frequency is evidence about recurrence, not a substitute for importance. A rare privacy near-miss may matter more than a frequent harmless warning.

## Evidence Discipline

Keep these fields distinct:

- **Observation:** What directly happened.
- **Candidate explanation:** A plausible causal account.
- **Alternative explanations:** Other accounts compatible with the observation.
- **Confidence:** Low, medium, or high, with a brief reason when material.

`Human says this matters` is a strong operational signal. It does not verify a causal explanation.

## Decision Guide

Retain as transient context when impact and reuse are low. Capture an episode when the event is important but not yet generalizable. Consider a reusable lesson when the abstraction has plausible reuse and adequate evidence. Require progressively stronger evidence as scope, blast radius, or irreversibility increases.

Do not infer an absolute rule from one event. For example:

- **Observation:** Three concurrent high-cost research tasks rapidly exhausted the available usage budget.
- **Candidate explanation:** Concurrent tasks may share a finite usage budget and accelerate depletion.
- **Alternatives:** Large contexts, tool-heavy work, reset timing, or model-specific costs.
- **Confidence:** Medium until resource accounting is verified.

The provisional lesson may justify considering concurrency budgets, checkpoints, cheaper secondary models, or serial execution under tight limits. It does not establish `maximum concurrency = 1`.

