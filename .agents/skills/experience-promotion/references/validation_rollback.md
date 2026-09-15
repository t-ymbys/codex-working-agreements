# Validation and Rollback

Read this reference before applying a durable change. A proposal is not deployment authorization.

## Validation Questions

- Does the change address the observed failure or improve the verified success path?
- Is the causal explanation sufficiently supported for the proposed scope?
- Which alternative explanations remain viable?
- Could valid workflows be unnecessarily blocked or slowed?
- Does the change conflict with existing policy, Skills, procedures, or user preferences?
- Would deterministic enforcement be more reliable and appropriate than a prompt rule?
- Is the proposed change testable and reversible?
- Could it become stale when tools, models, resources, or environments change?
- Is human review required by impact or authorization boundaries?

Validation strength should increase in this order:

`lesson < procedure < Skill modification < global policy < deterministic guardrail < parameter adaptation`

## Deployment Record

For a material durable change, record:

- evidence and confidence;
- exact target and scope;
- expected benefit and possible collateral effects;
- validation performed and unresolved uncertainty;
- reviewer or authorization when required;
- monitoring signal;
- rollback trigger and rollback method;
- deployment and review dates.

## Monitoring and Rollback

Use bounded monitoring. Do not repeatedly scan unrelated work for confirmation.

Rollback, narrow, or supersede a change when it blocks valid workflows, fails to mitigate the problem, conflicts with stronger policy, rests on a disproven explanation, or becomes stale. Prefer reversible edits and preserve enough provenance to explain why the change was introduced and later withdrawn.

Do not deploy destructive automation, broad restrictions, global-policy changes, security/privacy boundary changes, hard guardrails, or parameter adaptation without the required human review.

