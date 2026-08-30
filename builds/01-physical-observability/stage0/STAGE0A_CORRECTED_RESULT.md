# Stage 0A — Corrected Observation / Delay Study

Status: PROVISIONAL DIGITAL-ONLY RESULT

This result uses the local synthetic point-mass harness, not the Bosch FMU. It is a methodology/debugging artifact and must not be presented as validation of the Bosch benchmark or of cross-domain generality.

## Corrections before this run

1. The initial harness mixed measurements from one plant trajectory with another; that run was invalid and is rejected.
2. The state estimate and ground truth were initially recorded at different time indices; coverage results from that run are rejected.
3. The corrected loop evaluates both estimate and truth at the same state boundary and applies delayed observations at their arrival time.

## Experiment

- 10 independent seeds per cell.
- Horizon: 1000 steps.
- Cases: nominal, pulse, held_out_ramp.
- Delays: 0, 5, 10, 20 steps.
- Dropout: 0%, 5%, 20%.
- Controllers use the same fixed feedback law; the comparison isolates estimator treatment of delayed measurements.

## Key held-out results (0% dropout)

| Delay | Estimator | Position RMSE | Violation rate | Estimator RMSE | 95% coverage | Mean |u| |
|---:|---|---:|---:|---:|---:|---:|
| 0 | naive | 0.3173 | 0.3953 | 0.0344 | 0.9945 | 0.3045 |
| 0 | delay_aware | 0.3173 | 0.3953 | 0.0344 | 0.9945 | 0.3045 |
| 5 | naive | 0.3271 | 0.4471 | 0.0805 | 0.9047 | 0.3332 |
| 5 | delay_aware | 0.3304 | 0.4111 | 0.0793 | 0.9999 | 0.3068 |
| 10 | naive | 0.3398 | 0.4771 | 0.1118 | 0.7327 | 0.3655 |
| 10 | delay_aware | 0.3434 | 0.4266 | 0.1072 | 0.9999 | 0.3090 |
| 20 | naive | 0.3755 | 0.6448 | 0.1673 | 0.4364 | 0.4337 |
| 20 | delay_aware | 0.3692 | 0.4558 | 0.1492 | 0.9979 | 0.3133 |

## Interpretation

- Delay-aware estimation materially improves state-estimation error and uncertainty coverage as delay increases.
- At 20-step delay on the held-out ramp, violation rate drops from 0.6448 to 0.4558 (~29% relative reduction) and estimator RMSE drops from 0.1673 to 0.1492 (~11% relative reduction).
- Position RMSE does not improve monotonically: at 5 and 10 steps the delay-aware estimator has slightly higher trajectory RMSE despite lower violation rates. Better state reconstruction therefore does not automatically imply better closed-loop trajectory performance.
- The delay-aware covariance is conservative in this configuration (coverage near 100% for delayed cases). Calibration quality remains open; overcoverage is not the same as useful uncertainty calibration.
- Dropout at 20% changes the same qualitative pattern only slightly in this toy system; this is not enough evidence for robustness.

## Research consequence

The immediate testable hypothesis is:

> Explicit delayed-state reconstruction can restore useful observability under delayed measurements, but the control value must be demonstrated separately; improved estimation alone is insufficient.

## Next falsification test

1. Calibrate lag-filter process noise so uncertainty intervals are neither severely under- nor over-conservative.
2. Add variable/unknown delay rather than only known fixed delay.
3. Add model mismatch and delayed dropout jointly.
4. Compare fixed feedback, delay-aware prediction, and uncertainty-aware adaptive control with identical tuning budgets.
5. Report tail metrics and paired seed-level differences.

## Evidence status

Observed computational evidence: PASS for reproducibility of the corrected harness.

Research claim: NOT ESTABLISHED.

Cross-domain generalization: OPEN.
