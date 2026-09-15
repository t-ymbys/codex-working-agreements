# Empirical, Statistical, and Data Research

Use this reference for empirical studies, observational data, experiments, causal inference, prediction, benchmark evaluation, and privacy-sensitive datasets.

## 1. Data-Generating Process

Treat the data-generating and observation process as part of the research object.

Before modeling, identify where relevant:

- target population;
- sampling process;
- inclusion and exclusion rules;
- observation mechanism;
- measurement process;
- intervention or exposure assignment;
- censoring;
- missingness;
- aggregation;
- temporal structure.

A dataset is not a neutral representation of reality.

## 2. Bias and Validity

Explicitly consider:

- selection bias;
- confounding;
- survivorship bias;
- measurement error;
- missingness;
- target leakage;
- train/test contamination;
- benchmark contamination;
- dependence;
- model-selection bias;
- multiple testing;
- temporal leakage;
- post-treatment conditioning;
- distribution shift;
- external validity.

Do not infer causality from predictive association.

## 3. Causal Claims

For causal claims, identify:

- estimand;
- treatment or intervention;
- outcome;
- identification assumptions;
- adjustment set;
- identification strategy;
- plausible violations;
- alternative explanations.

Where relevant, consider:

- randomization;
- natural experiments;
- difference-in-differences;
- instrumental variables;
- regression discontinuity;
- matching or weighting;
- causal graphs;
- sensitivity analysis.

Do not use causal terminology when the design only supports association.

## 4. Predictive Claims

For predictive research, distinguish:

- training performance;
- validation performance;
- test performance;
- temporal or domain generalization.

Specify the validation design.

Use baselines.

Check whether performance gains are scientifically or operationally meaningful, not merely statistically detectable.

## 5. Statistical Uncertainty

Report uncertainty appropriate to the research question.

Consider:

- confidence or credible intervals;
- bootstrap uncertainty;
- posterior uncertainty;
- calibration;
- coverage;
- multiple-comparison adjustment;
- sensitivity to modeling assumptions.

Do not rely only on point estimates or significance thresholds.

## 6. Baselines and Competing Explanations

Compare against appropriate:

- naive baselines;
- standard methods;
- current strong methods;
- simpler explanations;
- ablations.

A sophisticated method should justify its complexity.

When a new method improves a metric, determine whether the improvement reflects:

- genuine signal;
- leakage;
- additional information unavailable to the baseline;
- tuning effort;
- sample-selection differences;
- evaluation artifacts.

## 7. Robustness

Where appropriate, vary:

- preprocessing;
- model class;
- hyperparameters;
- sample definition;
- time windows;
- random seeds;
- missing-data assumptions;
- outlier treatment;
- evaluation metric.

A result that depends on a narrow arbitrary choice should be described accordingly.

## 8. Confidential, Personal, and Sensitive Data

Treat confidential data and personally identifiable or health-related information as protected by default.

Do not load, paste, transmit, summarize into model context, or emit into logs raw confidential information, PII, PHI, credentials, secrets, or similarly sensitive records unless:

1. the workflow explicitly authorizes such processing; and
2. the processing environment and applicable privacy requirements have been verified.

Before using a potentially sensitive dataset:

1. determine whether sensitive fields are present;
2. determine whether record-level sensitive data is actually necessary;
3. prefer aggregation, redaction, pseudonymization, anonymization, synthetic data, or minimization when scientifically sufficient;
4. verify the permitted environment;
5. avoid reproducing sensitive values in prompts, outputs, traces, debugging messages, intermediate artifacts, and logs.

Removing obvious names alone is not necessarily anonymization.

Re-identification may be possible through combinations of:

- timestamps;
- location;
- rare attributes;
- free text;
- demographics;
- linkage to external datasets;
- other quasi-identifiers.

When anonymization status is uncertain, treat the data as sensitive.

If the research cannot be performed without violating applicable privacy or confidentiality constraints, stop that part of the workflow and report the constraint.

## 9. Reproducible Analysis

Preserve:

- dataset version or provenance;
- preprocessing;
- inclusion criteria;
- feature construction;
- train/validation/test split logic;
- random seeds where relevant;
- model configuration;
- evaluation code;
- generated tables and figures.

Keep raw data immutable where practical.

Separate source data, intermediate data, and derived outputs.

## 10. Completion Criteria

Do not treat an empirical result as complete until the relevant subset is addressed:

- data-generating process described;
- target population clear;
- leakage assessed;
- important biases considered;
- baseline comparison performed;
- uncertainty quantified;
- robustness assessed;
- privacy constraints respected;
- analysis reproducible enough for the intended use;
- causal language matches identification strength;
- limitations documented.
