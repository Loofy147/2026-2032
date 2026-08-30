# Build 01 — Stage-0 Experiment Matrix

## Goal

Determine whether explicit observability and model-assisted closed-loop correction provide measurable value under sensing and timing degradation, using an existing validated CPS simulation substrate.

## Cases

| Case | Sensor | Estimator | Predictive model | Adaptive action | Purpose |
|---|---|---|---|---|---|
| A | clean/reference | reference | none | fixed/reference | oracle/reference envelope |
| B | noisy | reference | none | fixed/reference | monitoring/control baseline |
| C | noisy + delay/dropout | reference | none | fixed/reference | stress baseline |
| D | noisy + delay/dropout | reference | residual model | fixed | isolate prediction value |
| E | noisy + delay/dropout | reference | residual model + UQ | adaptive | test closed-loop value |

## Disturbance matrix

The Stage-0 matrix must vary one mechanism at a time before combined stress:

1. zero/nominal noise;
2. increased Gaussian noise;
3. bounded bias/drift;
4. random packet dropout;
5. deterministic delay;
6. jitter;
7. combined noise + delay;
8. combined delay + dropout;
9. model mismatch;
10. held-out combined disturbance.

## Experimental discipline

- Fix the random seed for reproducibility, then repeat with independent seeds.
- Record exact simulator, FMU, runner, estimator and controller versions.
- Keep calibration/tuning and evaluation disturbance sets separate.
- Report distributions, not only means.
- Preserve all raw outputs required to reconstruct derived metrics.
- Measure wall-clock runtime separately from simulated time.

## Statistical reporting

Report:

- mean and standard deviation;
- median and interquartile range;
- 95th and 99th percentile error where sample size permits;
- constraint-violation frequency;
- estimator error;
- prediction residual;
- uncertainty interval coverage;
- paired differences between modes.

Avoid claiming superiority from overlapping or underpowered samples.

## Required ablations

At minimum:

```text
full system
- no uncertainty
- no prediction
- no adaptive action
- no state estimator
- measurement-only
```

The purpose is to identify which component actually provides the observed benefit.

## Expected outputs

```text
artifacts/
├── raw/
├── normalized/
├── manifests/
├── metrics/
├── figures/
└── reports/
```

Each run should generate a machine-readable manifest and a summary record linked to `claim_id`, `hypothesis_id`, and the exact component versions.

## Decision rules

### Promote
If adaptive/model-assisted control improves held-out performance without worsening calibrated tail risk or practical overhead.

### Revise
If gains exist only under limited disturbance families, or if uncertainty/applicability is insufficient for decisions.

### Kill
If the additional stack has no measurable value over a simpler baseline, or increases tail risk/complexity without compensating benefit.

## Stage-1 trigger

Do not buy or build physical hardware merely because Stage 0 succeeds. Stage 1 begins only after the dominant effect and its uncertainty are identified and the cheapest meaningful hardware test is selected.