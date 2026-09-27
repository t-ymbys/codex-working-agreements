# Literature Review and Novelty

Use this reference for literature surveys, prior-art searches, novelty, priority, attribution, and current-frontier claims.

## Evidence Boundary

External retrieval is required for claims about prior work, bibliographic metadata, publication status, priority, novelty, what a source proved, and the current literature.

Prefer primary or authoritative sources. Model memory may propose terminology, authors, or candidate papers but does not verify them. If retrieval is incomplete, mark the affected conclusion `NOT VERIFIED` and state the search boundary.

Never invent titles, authors, dates, identifiers, quotations, or results.

## Search Design

Before searching, define:

- the claim or question;
- the closest expected research areas;
- the minimum evidence needed;
- a reasonable query and source budget;
- the condition for expanding or stopping.

Search at several semantic levels when the claim matters:

- direct terminology and exact technical phrases;
- synonyms, older vocabulary, notation variants, and adjacent disciplines;
- structural or mathematical equivalents expressed under different names;
- references and citing works around the closest sources;
- competing methods that solve the same problem differently.

Diversify queries rather than repeating lexical variants with little new information.

## Source Use

Prefer approximately:

1. original papers containing the relevant result;
2. peer-reviewed papers;
3. authoritative monographs or textbooks;
4. official repositories, standards, datasets, or institutional records;
5. preprints, clearly identified as such;
6. high-quality secondary literature;
7. informal commentary only when necessary.

Verify important metadata. Distinguish preprint, revision, presentation, and publication dates when priority depends on them.

For each central source, record only what the decision needs, such as its claim, assumptions, method, evidence, limitations, relevance, and overlap with the current contribution.

## Novelty Analysis

Do not assume a gap before reviewing the literature. If the closest prior art removes the proposed gap, revise the research question.

For substantial work, use a claim-level matrix:

| Claim | Closest prior work | Overlap | Remaining difference | Evidence | Status |
|---|---|---|---|---|---|

Evaluate novelty at the level actually claimed: theorem, mechanism, method, representation, algorithm, experiment, dataset, benchmark, prediction, or explanation.

Correctness and novelty are independent. A result may be correct but known, new but incorrect, partially known, incremental, or both new and significant. Evidence for one dimension does not establish another.

## Search Stopping Condition

Stop when the predefined depth is reached, additional sources are materially redundant, ordinary search cannot resolve the remaining uncertainty, or a mathematical, computational, empirical, or expert-review step has higher expected value.

Do not interpret failure to find prior art as proof that none exists.

## Output

Report:

- what was searched and within what bounds;
- the strongest and closest prior art;
- conceptual families or competing approaches;
- overlap and remaining difference at claim level;
- confidence and unverified areas;
- whether deeper search or expert review is warranted.

Prefer `No direct precedent was found within the performed search` over an absolute absence claim unless the stronger conclusion is proved.
