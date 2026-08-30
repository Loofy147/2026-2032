# Stage 0 — First Valid Digital-Only Result

Date: 2026-08-30
Status: VALID DIGITAL-ONLY HARNESS / NOT PHYSICAL VALIDATION

## Critical correction

The first generated artifact was invalid because observations were generated from a separate preliminary plant trajectory and then replayed into a different closed-loop trajectory. That broke causality between action, state, and measurement and produced explosive, non-physical metrics.

The corrected harness generates each observation online from the same plant trajectory that receives the action. The invalid artifact must not be used as evidence.

## Corrected baseline

Configuration:

- `dt = 0.01 s`
- `horizon = 1000` steps
- measurement noise standard deviation `0.03`
- process noise standard deviation `0.01`
- 5 repetitions per case
- seeds `20260830..20260834`

Modes:

1. `open_loop`
2. `fixed_feedback`
3. `adaptive_uncertainty`

Cases:

1. `nominal`
2. `pulse`
3. `held_out_ramp`

## Mean results across five repetitions

### Nominal

| Mode | Position RMSE | P95 abs position | Violation rate | Estimator RMSE | 95% coverage |
|---|---:|---:|---:|---:|---:|
| Open loop | 1.0000 | 1.0000 | 1.0000 | 0.0127 | 0.9854 |
| Fixed feedback | 0.2729 | 0.8116 | 0.1906 | 0.0131 | 0.9840 |
| Adaptive uncertainty | 0.2776 | 0.8273 | 0.1948 | 0.0131 | 0.9840 |

### Pulse

| Mode | Position RMSE | P95 abs position | Violation rate | Estimator RMSE | 95% coverage |
|---|---:|---:|---:|---:|---:|
| Open loop | 3.1684 | 5.5468 | 1.0000 | 0.0155 | 0.9608 |
| Fixed feedback | 0.3262 | 0.8116 | 0.3798 | 0.0140 | 0.9732 |
| Adaptive uncertainty | 0.3296 | 0.8273 | 0.3804 | 0.0140 | 0.9734 |

### Held-out ramp

| Mode | Position RMSE | P95 abs position | Violation rate | Estimator RMSE | 95% coverage |
|---|---:|---:|---:|---:|---:|
| Open loop | 1.7772 | 3.3307 | 1.0000 | 0.0147 | 0.9712 |
| Fixed feedback | 0.3159 | 0.8116 | 0.3998 | 0.0138 | 0.9814 |
| Adaptive uncertainty | 0.3204 | 0.8273 | 0.4046 | 0.0138 | 0.9814 |

## Stress finding

Increasing sensing delay exposes estimator/calibration limits even though dropout alone has modest effect in this simple model. For the held-out ramp:

| Delay | Fixed RMSE | Fixed violation | Fixed 95% coverage |
|---:|---:|---:|---:|
| 0 steps | 0.316 | 0.400 | 0.981 |
| 2 steps | 0.319 | 0.415 | 0.969 |
| 5 steps | 0.325 | 0.444 | 0.865 |
| 10 steps | 0.338 | 0.475 | 0.666 |
| 20 steps | 0.372 | 0.636 | 0.386 |

## Interpretation

1. Feedback control materially outperforms open loop in the current toy plant.
2. The simple uncertainty attenuation policy does not improve performance over fixed feedback; it is slightly worse on the reported cases.
3. Delay is a much stronger stressor than low-rate random dropout in this harness.
4. Uncertainty coverage degrades sharply as unmodeled delay grows. The current covariance model does not represent delay uncertainty.
5. This experiment does not yet establish the broader hypothesis that predictive modeling plus uncertainty-aware correction is a high-leverage reusable capability.

## Next experiment

Do not tune the adaptive gain further yet. First add an explicit delay-aware state estimator/predictor and compare:

- fixed feedback;
- delay-aware estimation;
- delay-aware prediction + uncertainty;
- adaptive closed-loop compensation.

The decisive evaluation set must contain held-out delay/dropout combinations and at least one disturbance family not used during calibration.
