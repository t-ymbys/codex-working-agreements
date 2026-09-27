# Empirical and Statistical Research

Use this reference for experiments, observational studies, causal inference, prediction, benchmarks, and privacy-sensitive data.

## Data and Observation Process

Treat the data-generating and observation process as part of the research object. Identify as relevant:

- target population and sampling process;
- inclusion, exclusion, censoring, and missingness;
- measurement and aggregation;
- temporal structure and dependence;
- intervention, exposure, or assignment mechanism;
- target variable, estimand, or prediction objective.

A dataset is not a neutral representation of reality.

## Claim Type

Separate descriptive, predictive, and causal claims.

For causal claims, state the treatment, outcome, estimand, identification assumptions, adjustment set or design, plausible violations, and sensitivity analysis. Do not use causal language when the design supports only association.

For predictive claims, distinguish training, validation, sealed test, temporal generalization, and domain generalization. Specify the validation design before using the result to support a claim.

## Threats to Validity

Check the threats that can change the conclusion, including selection, confounding, measurement error, missingness, dependence, leakage, benchmark contamination, multiple testing, model-selection bias, post-treatment conditioning, distribution shift, and external validity.

Do not enumerate threats mechanically; connect each material threat to a diagnostic, sensitivity analysis, limitation, or stop condition.

## Baselines, Uncertainty, and Robustness

Compare against the simplest credible baseline, established methods, and competing explanations. Determine whether gains arise from genuine signal, extra information, tuning effort, sample differences, leakage, or evaluation artifacts.

Report uncertainty appropriate to the claim, such as intervals, calibration, coverage, posterior uncertainty, bootstrap variation, or sensitivity to assumptions. Point estimates and significance thresholds alone are insufficient when uncertainty changes the decision.

Vary only the choices that probe material fragility, such as preprocessing, sample definition, model class, time window, seed, missing-data assumptions, outlier treatment, or metric.

## Sensitive Data

Treat confidential records, PII, PHI, credentials, and similarly sensitive fields as protected by default.

Process them only when the workflow explicitly authorizes it and the environment and privacy requirements are verified. Prefer aggregation, redaction, pseudonymization, anonymization, synthetic data, or minimization when scientifically sufficient.

Do not reproduce sensitive values in prompts, traces, logs, debugging output, or generated artifacts. Removing names alone is not necessarily anonymization; combinations of timestamps, location, rare attributes, free text, demographics, and external linkage may re-identify records.

If the work cannot proceed without violating the applicable boundary, stop that part and report the constraint.

## Reproducible Analysis

Preserve dataset provenance and version, inclusion logic, preprocessing, features, splits, seeds, model configuration, evaluation code, and generated tables or figures. Keep raw data immutable where practical and separate source, intermediate, and derived data.

## Output

Report the claim type, target population, design, estimand or prediction target, material validity threats, baselines, uncertainty, robustness, privacy boundary, reproducibility status, and limitations. Ensure the causal or predictive language matches the evidence.
