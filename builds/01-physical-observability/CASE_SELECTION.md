# Build 01 — Case Selection

## Decision

Use the open Bosch Research CPS Challenge LateralMotionControl FMU as the Stage-0 reference case.

Repository: https://github.com/boschresearch/CPSChallenge

## Why this case

The FMU already contains nearly the complete experimental substrate we need:

- a discrete-time physical vehicle model;
- sensor task and noisy sensed outputs;
- estimator producing a 6-state estimate;
- controller and actuator;
- explicit network/task timing and trigger interfaces;
- ground-truth physical state;
- estimated-state performance metrics;
- a fixed simulation base step of 0.1 ms;
- FMI 2.0 Co-Simulation packaging.

This makes it unusually suitable for testing observability and timing effects without first building a simulator or a vehicle model.

The source repository describes the system as a complete simplified control loop with sensing, estimation, control and actuation, and explicitly exposes ground-truth, sensed and estimated states for comparison. It was published as part of the IEEE RTAS 2026 Physics-Driven Real-Time CPS Challenge. 

## Important limitation

The FMU is a vehicle lateral-control benchmark, not evidence that the general research hypothesis is true across manufacturing, energy, biology or other domains. It is a controlled probe.

## What we will test

We will separate four effects that are often conflated:

1. observation quality;
2. state-estimation quality;
3. model/prediction value;
4. closed-loop correction value.

## Stage-0 baselines

### A — Ground-truth oracle
Use physical state directly only as an upper-bound reference. This is not deployable and must never be counted as an operational baseline.

### B — Existing sensor/estimator/control path
Reproduce the reference pipeline without modification.

### C — Measurement stress
Vary sensor noise, missing observations, delay and sampling/trigger schedules while keeping controller structure fixed.

### D — Model-assisted path
Add an explicit predictive/residual model and uncertainty/applicability record around the existing state estimate.

### E — Closed-loop compensation
Allow the controller/scheduler to react to predicted degradation of observability or performance.

## Primary hypothesis

> A system with explicit observability measurement, state estimation, predictive modeling and uncertainty-aware correction can preserve or improve control performance under held-out sensing/timing disturbances better than monitoring alone or naive fixed control.

This is a hypothesis, not an established result.

## Primary independent variables

- sensor noise variance;
- sensor dropout probability;
- sensor-to-controller delay;
- actuator/network delay;
- estimator update period;
- velocity profile;
- reference trajectory/curvature;
- model mismatch;
- disturbance class.

## Primary dependent variables

- lateral-error RMSE;
- high-quantile lateral error;
- threshold violation rate;
- settling time;
- control effort;
- correction latency;
- estimator error;
- prediction residual;
- uncertainty coverage;
- computation time.

## Required split

Do not tune and evaluate on the same disturbance set.

Use:

```text
training / calibration disturbances
            ↓
      model/controller tuning
            ↓
     held-out disturbances
            ↓
          evaluation
```

Include at least one disturbance family not represented in calibration.

## Kill conditions

The case is a failure as a research probe if:

- the reference FMU cannot be reproduced deterministically;
- the observed effect is dominated by an implementation artifact;
- a simpler fixed controller matches the model-assisted approach on all held-out cases;
- uncertainty estimates are not calibrated enough to support decisions;
- added complexity increases tail failures without measurable compensating benefit.

## Future transfer tests

If Stage 0 is informative, repeat the same experimental pattern with a second domain. Candidate domains:

- thermal process;
- battery model;
- fluid/transport process;
- manufacturing process.

Transfer is required before making a cross-domain claim.
