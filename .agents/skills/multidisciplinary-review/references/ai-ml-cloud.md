# AI, ML, Data, and Cloud Engineering Lens

Use this lens to evaluate the full production system rather than model quality
in isolation.

## Data and Learning Problem

- Define the user outcome, prediction or generation task, target population,
  data-generating process, labels or feedback, and decision boundary.
- Check representativeness, leakage, contamination, missingness, drift,
  privacy, licensing, and retention.
- Separate training, development, evaluation, and sealed test usage.

## Model and Evaluation

- Compare against simple, strong, and operationally realistic baselines.
- Measure task quality, calibration or uncertainty where relevant, robustness,
  harmful failure modes, and human-review requirements.
- For generative systems, test the complete prompt, retrieval, tool, policy,
  post-processing, and user workflow rather than the base model alone.
- Define offline and online metrics and state where they may diverge.

## Production and Cloud Architecture

- Evaluate latency, throughput, concurrency, availability, durability,
  observability, incident response, rollback, and disaster recovery.
- Model unit economics: inference, storage, data movement, retrieval, logging,
  evaluation, support, and peak capacity.
- Review identity, authorization, secrets, tenant isolation, data residency,
  supply-chain risk, and auditability.
- Identify vendor-specific dependencies, portable interfaces, fallback modes,
  and migration cost without assuming that multi-cloud is automatically useful.

## Delivery

- Distinguish prototype, pilot, production, and regulated-system requirements.
- Prefer staged rollout, shadow evaluation, canaries, bounded retries, and
  explicit rollback criteria where risk warrants them.
- Record model, prompt, data, code, configuration, and evaluation provenance.

## Output

Report the end-to-end architecture, evaluation gaps, reliability and security
risks, cost drivers, deployment gate, and next validation step.
