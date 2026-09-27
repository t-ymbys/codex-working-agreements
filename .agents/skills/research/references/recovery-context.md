# Recovery, Context, and Escalation

Use this workflow when research is interrupted, state is uncertain, context is large, or a high-cost capability may be warranted.

## Recover Before Resuming

Reconstruct the current state from the smallest authoritative surface:

1. identify the project boundary and applicable instructions;
2. inspect Git status, recent checkpoints, and relevant diffs;
3. read `HANDOFF.md` when present;
4. inspect the named artifacts and validation outputs;
5. distinguish completed, in-progress, unverified, and obsolete work;
6. resume from the first unresolved decision rather than rerunning the project blindly.

`HANDOFF.md` is current semantic state. Git is historical and recoverable state. Generated reports preserve detailed evidence. Conversation history is not the canonical store for any of them.

## Context Management

Treat the context window as working memory for the current decision, not as a knowledge archive.

- Load only references and repository surfaces that can affect the present step.
- Summarize large exploration into claims, evidence, decisions, and unresolved questions.
- Keep raw searches and logs in artifacts when retention matters.
- Avoid rereading unchanged material without a decision-relevant reason.
- Before compaction or interruption, externalize the semantic state and checkpoint coherent work.

## Capability Routing

Use capability levels rather than durable model-name taxonomies:

1. routine execution for mechanical edits and standard checks;
2. standard reasoning for ordinary analysis and implementation;
3. advanced reasoning for difficult mathematical, statistical, or architectural judgment;
4. highest-cost review for unresolved central claims, independent adversarial review, or high-stakes publication decisions.

Preferred sequence:

`routine or standard work -> targeted escalation -> validation -> checkpoint`

Escalate a specific unresolved question, not the entire project. Preserve completed work and the evidence motivating escalation first.

## Subagents and Independence

Use a subagent only when permitted and when context isolation, independent judgment, or parallel read-heavy exploration has material value. Good candidates include a large literature landscape, independent adversarial review, broad repository discovery, or competing implementation paths.

Do not delegate trivial inspection, formatting, one-command validation, or a short formula check merely to create roles. Return a compressed result containing evidence, decision impact, and uncertainty rather than the raw search process.

## Checkpoints

Create recoverable checkpoints at semantic milestones and before risky, expensive, or interruptible work. Do not checkpoint noise merely on a timer. Record the latest meaningful baseline in the handoff when future recovery depends on it.
