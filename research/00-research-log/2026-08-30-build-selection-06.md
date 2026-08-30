# Research Round 06 — Build Selection

Date: 2026-08-30

## Decision

Build 01 Stage 0 will use the Bosch Research CPS Challenge `LateralMotionControl` FMU as the reference computational plant.

## Why this was selected

The public FMU already exposes the elements needed to isolate the research variables without inventing a simulator:

- physical state;
- sensor output;
- estimator output;
- controller and actuator;
- explicit communication/task triggers;
- configurable sensor noise;
- network/scheduling effects;
- ground-truth performance metrics;
- a fixed 0.1 ms base step;
- FMI 2.0 Co-Simulation interface.

This gives a strong Stage-0 test substrate for measurement quality, state estimation, timing degradation and closed-loop control.

## Evidence basis

The source repository describes the FMU as a complete simplified lateral-control loop and explicitly exposes ground-truth, sensed and estimated states for comparison. The repository also provides examples and describes timing/task-trigger semantics.

## Why not start with a new physical plant

A new plant would mix too many uncertainties:

```text
plant-model validity
+
sensor hardware
+
controller design
+
experimental setup
+
measurement calibration
```

The first experiment should isolate the hypothesis with the smallest possible confounding surface.

## Threats to validity

1. Vehicle lateral control is only one domain.
2. The FMU is a model, not the physical world.
3. Its reference controller may create an easier/harder problem than other domains.
4. Results can be affected by implementation details of the FMI master.
5. Ground truth is available in simulation and therefore cannot be assumed in deployment.

## Transfer requirement

A positive Stage-0 result is a prerequisite for choosing a second domain, not evidence of cross-domain generality. The same measurement/state-estimation/model/control/uncertainty pattern must subsequently be tested on a materially different physical process.

## Build principle

Reuse existing validated components first. Build only the missing capability required to test the hypothesis.

## Source

Bosch Research, `boschresearch/CPSChallenge`, public repository, 2026: Physics-Driven Real-Time CPS Challenge / LateralMotionControl FMU.
