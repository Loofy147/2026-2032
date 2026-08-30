# Build 01 — Physical Observability + Simulation Closed Loop

Status: DESIGN / NOT YET VALIDATED

Issue: #1

## Purpose

Test whether an existing physical/simulated process becomes materially more predictable and controllable when five capabilities are composed:

1. measurement;
2. state estimation;
3. an existing physics model/simulator;
4. uncertainty/applicability assessment;
5. closed-loop correction.

The build is an empirical probe for the research thesis that **process observability is a high-leverage enabling capability**.

## Reuse-first architecture

Do not build a simulator unless no adequate existing model exists.

Preferred stack:

```text
Existing process/model
      ↓
measurement adapter
      ↓
normalized time-series record
      ↓
state estimator
      ↓
existing simulator/model
      ↓
residual + uncertainty
      ↓
decision / compensation policy
      ↓
process/action
      ↓
new measurement
      ↺
```

Potential reusable components:

- OpenFOAM for suitable fluid/thermal/transport problems;
- PyBaMM for battery experiments where relevant;
- FMI for model exchange/co-simulation;
- OPC UA/AAS/BaSyx for semantic asset representation when an industrial integration is needed;
- standard Python numerical/optimization libraries;
- commodity sensors or public datasets before custom hardware.

The actual component choice is a hypothesis to be tested, not predetermined.

## Minimum experiment

Select one controllable process with:

- one measurable state/output `y`;
- one disturbance `d` that can be injected or varied;
- one control input `u`;
- a model `f(x,u,d)` good enough to be useful but not perfect;
- measurement uncertainty that can be estimated.

Compare three modes:

### A — Open loop
No online correction.

### B — Monitor only
Measure and estimate the state, but do not compensate.

### C — Closed loop
Measure → estimate → simulate/predict → choose correction → act → re-measure.

## Required metrics

Primary:

- mean absolute error;
- RMSE;
- high-quantile / tail error;
- settling time;
- correction latency;
- intervention count;
- energy/compute overhead;
- robustness on held-out disturbances.

Credibility:

- calibration quality;
- uncertainty coverage;
- residual distribution;
- model validity domain;
- reproducibility across runs.

Safety/reliability:

- worst-case excursion;
- unstable-control events;
- false correction events;
- missed-disturbance events;
- out-of-distribution detection.

## Evidence contract

Every run should preserve:

```text
run_id
experiment_id
model_id
model_version
solver/version
parameters
initial_state
inputs
disturbance_definition
sensor_ids
calibration_state
measurement_uncertainty
estimator_version
controller_version
action_trace
raw_observations
predictions
residuals
uncertainty
outcome
failure_flags
software/environment metadata
```

## Acceptance logic

A positive result requires all of the following:

1. repeated trials;
2. held-out disturbance conditions;
3. improvement over both open-loop and monitor-only baselines;
4. no material increase in tail risk;
5. uncertainty estimates that remain calibrated within the stated validity domain;
6. reproducible results;
7. evidence that the improvement depends on the composed capability, not an accidental tuning artifact.

## Kill criteria

The hypothesis is weakened or killed if:

- performance gains vanish outside seen disturbances;
- measurement uncertainty is larger than the claimed benefit;
- the simulator contributes no measurable value over simpler models;
- controller complexity adds more failures than it prevents;
- a simpler monitor-only system achieves the same operational outcome;
- compute/energy cost exceeds practical benefit;
- evidence cannot be reproduced.

## Research synchronization

After each experimental batch:

```text
result
  ↓
claim update
  ↓
confidence update
  ↓
causal-edge update
  ↓
technology radar update
  ↓
next experiment
```

The build must update the research repository even when the result is negative.

## Current status

No empirical success claim is made yet. This document defines the testable architecture and evidence contract only.
