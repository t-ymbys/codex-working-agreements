---
name: research
description: Conduct rigorous academic or scientific research with verified literature, explicit claim status, adversarial validation, and reproducible evidence. Use for novelty review, theorem or model scrutiny, empirical inference, manuscript or publication assessment, and interrupted research recovery.
---

# Research

## Objective

Determine what is known, what is claimed, whether the claim is correct and new, what evidence distinguishes it from alternatives, and what work is justified next.

Do not optimize for validating the initial idea. Null results, counterexamples, non-novel findings, and failed hypotheses are valid outcomes.

## Core Discipline

- State the research question, scope, assumptions, comparison class, success criteria, and falsification or stop condition before investing in a sophisticated method.
- Distinguish `VERIFIED`, `DERIVED`, `NUMERICAL OBSERVATION`, `HYPOTHESIS`, `CONJECTURE`, `SPECULATION`, and `NOT VERIFIED` when the distinction affects the decision.
- Treat model memory as a source of search hypotheses, not evidence. Literature-sensitive claims require external retrieval.
- Evaluate correctness, novelty, significance, and publication readiness separately.
- Seek competing hypotheses, counterexamples, hidden assumptions, boundary cases, simpler explanations, and artifacts.
- Preserve the provenance needed to reconstruct important claims.
- Never fabricate references, metadata, execution, or validation.

## Route Before Reading

Classify the task, then read only the references that can change the result.

| Task type | Read |
|---|---|
| Literature review or prior-art search | [literature.md](references/literature.md) |
| Novelty assessment | [literature.md](references/literature.md); add [critical-review.md](references/critical-review.md) when significance or defensibility matters |
| Mathematical or theoretical research | [mathematical-research.md](references/mathematical-research.md); add [verification.md](references/verification.md) for a correctness claim |
| Computational or numerical research | [computational-research.md](references/computational-research.md); add [verification.md](references/verification.md) for central results |
| Empirical or statistical research | [empirical-research.md](references/empirical-research.md); add [verification.md](references/verification.md) for central results |
| Claim, proof, citation, implementation, or reproduction check | [verification.md](references/verification.md) plus the one relevant domain reference |
| Independent or reviewer-style challenge | [critical-review.md](references/critical-review.md); add [literature.md](references/literature.md) only for prior-art or novelty questions |
| Manuscript revision or publication assessment | [publication-reproducibility.md](references/publication-reproducibility.md); add domain, literature, verification, or critical-review references only as required by the claims |
| Interrupted work, uncertain state, handoff, context isolation, or high-cost escalation | Read [recovery-context.md](references/recovery-context.md) first |

Do not read every reference by default. A task spanning several modes may load several references, but each must have a concrete decision role.

## Minimum Workflow

1. Recover current state first when the task is interrupted or uncertain.
2. Identify the research phase: landscape, gap, formalization, pilot, full study, manuscript, or publication review.
3. Define the central claim and the evidence that would discriminate it from the strongest alternative.
4. Retrieve or inspect the minimum authoritative evidence needed for the current decision.
5. Run the cheapest discriminating calculation, experiment, audit, or reproduction.
6. Separate verification from critical review:
   - verification asks whether the claim is correct;
   - critical review asks whether a correct claim is meaningful, novel, well-scoped, and defensible.
7. Report established results, evidence obtained, negative findings, unverified claims, limitations, and the next decision.

## Search and Tool Discipline

Before open-ended investigation, define the target question, minimum evidence, effort bound, and stopping condition. Diversify queries or methods rather than repeating low-information calls.

Do not omit primary-source checks, counterexample searches, or validation merely to reduce tool use. Stop when sources become redundant, the effort bound is reached, or another method is more likely to resolve the uncertainty.

Distinguish `not found within this search`, `no known example after substantial review`, and `proved not to exist`.

## Escalation and Independence

Use the least costly capability that can reliably perform the current step. Escalate only an isolated high-value uncertainty such as a difficult proof, ambiguous novelty claim, adversarial review, or unresolved conceptual conflict.

Use a subagent only when permitted and when independent judgment, parallel exploration, or isolation of a large noisy search materially improves the result. Do not spawn one for a small formula check, trivial file inspection, one-command validation, or routine formatting.

## Completion Gate

Before declaring a substantial milestone complete, determine which checks apply:

- question, scope, and assumptions are explicit;
- relevant literature and attribution were externally checked;
- central claims received domain-appropriate verification;
- competing explanations and reviewer-level objections were considered;
- negative results and residual uncertainty are recorded;
- artifacts are reproducible enough for the intended claim;
- manuscript wording matches the evidence;
- remaining work and human decisions are explicit.

Stop when the requested research decision or artifact is supported to the required standard and further work would not materially change it.
