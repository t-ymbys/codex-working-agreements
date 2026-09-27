# Evaluation Proposal

## Question

Does progressive disclosure reduce persistent and irrelevant context while preserving or improving task success, research rigor, recovery, and auditability?

## Configurations

- **A — original:** commit `027320c` with a large global `AGENTS.md` and monolithic Research Skill.
- **B — intermediate:** commit `84e2c5c` with the previous global file and partially routed Research Skill.
- **C — refactored:** this architecture with minimal global instructions and routed references.

Run each configuration in an isolated checkout with the same model capability, reasoning level, tools, task input, repository state, and time or cost limits. Randomize configuration order. Use at least five runs for important stochastic comparisons; increase runs when observed variance could change the decision.

## Task Set

Include representative tasks:

1. a small code change that should not activate research;
2. recovery of interrupted repository work;
3. a bounded literature review and novelty claim;
4. a mathematical claim requiring proof audit and counterexample search;
5. a computational or empirical result requiring reproduction and threat analysis;
6. a manuscript verification and independent critical review;
7. an operational incident that should be captured locally but not promoted globally;
8. a repeated high-value lesson that should route to a deterministic check or narrow Skill reference.

Define acceptance criteria, required evidence, forbidden actions, and expected Skill/reference routing before running the tasks. Keep task graders blind to configuration where practical.

## Measures

### Outcome and safety

- task success and acceptance-criteria satisfaction;
- unsupported research claims and hallucinated repository facts;
- preservation of user changes and authorization boundaries;
- recovery success after interruption;
- user intervention required.

### Rigor

- validation coverage for central claims;
- primary-source and citation verification;
- counterexample and competing-hypothesis coverage;
- separation of correctness, novelty, significance, and publication readiness;
- reproducibility of reported results.

### Context and efficiency

- input and output tokens;
- files and Skill references read;
- irrelevant exploration and repeated low-information calls;
- tool calls and debug retry count;
- context compaction frequency;
- time and cost, reported by capability tier.

### Routing

- Skill activation precision and recall;
- reference-routing correctness;
- knowledge stored at the narrowest sufficient scope;
- duplicates created across instructions, Skills, handoffs, and documentation;
- deterministic checks used where appropriate.

## Evidence Collection

Collect machine-readable traces where available, repository diffs, validation outputs, source lists, and final artifacts. Use deterministic scoring for explicit acceptance criteria and owner-labeled review for research quality. Calibrate any LLM judge against a sample of owner labels and keep the judge isolated from configuration identity.

## Decision Rule

Adopt C only if it materially lowers persistent or irrelevant context without a meaningful loss in task success, central-claim verification, literature accuracy, recovery, or safety. Investigate failures by task class rather than averaging away a severe regression.

Static validation of this repository establishes structural integrity, not behavioral superiority. That claim remains `NOT VERIFIED` until the multi-run evaluation is executed.
