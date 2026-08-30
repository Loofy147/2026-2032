# Stage 0B — Delay-Aware Estimation Results

## Status

**Preliminary / research evidence only.** No cross-domain or physical claim is made.

## Why Stage 0B exists

Stage 0A showed that delayed measurements can break the calibration of a naive observer. Stage 0B tests whether explicitly representing the known delay in the state-space model restores state-estimation quality and improves downstream control.

## Compared estimators

1. **Naive KF** — treats the delayed measurement as if it were a current measurement.
2. **Known-delay augmented KF** — augments the state with delayed states and updates against the correct delayed observation.
3. **Delay-bank estimator** — a small bank of fixed-delay models with likelihood weighting; used only as a preliminary probe for unknown fixed delay.

## Clean experiment definition

The corrected harness uses a single causal plant trajectory:

```text
x_k
 ↓
y_{k-d}
 ↓
estimator
 ↓
u_k
 ↓
x_{k+1}
```

The evaluation includes stochastic process acceleration noise matched to the filter's process-noise assumption when testing estimator calibration. Disturbance cases are kept separate from calibration/evaluation logic.

## Preliminary known-delay results

20-seed runs were used for the estimator comparison on nominal, pulse, and ramp disturbance families.

Representative averages:

| Case | Delay | Estimator | Estimator RMSE | 95% coverage | Control RMSE | Violation rate |
|---|---:|---|---:|---:|---:|---:|
| nominal | 5 | Naive | 0.0734 | 0.7710 | 0.2828 | 0.2209 |
| nominal | 5 | Known-delay | 0.0714 | 0.9756 | 0.2850 | 0.1898 |
| nominal | 10 | Naive | 0.1069 | 0.6249 | 0.2898 | 0.2428 |
| nominal | 10 | Known-delay | 0.1007 | 0.9866 | 0.2904 | 0.1978 |
| nominal | 20 | Naive | 0.1644 | 0.3742 | 0.3210 | 0.2718 |
| nominal | 20 | Known-delay | 0.1423 | 0.9957 | 0.3053 | 0.2058 |
| pulse | 20 | Naive | 0.1828 | 0.1400 | 0.3872 | 0.5284 |
| pulse | 20 | Known-delay | 0.1440 | 0.8885 | 0.3384 | 0.3365 |
| ramp | 20 | Naive | 0.1666 | 0.2008 | 0.3396 | 0.3941 |
| ramp | 20 | Known-delay | 0.1433 | 0.9022 | 0.3380 | 0.3817 |

## Interpretation

The known-delay augmented estimator materially improves state reconstruction and uncertainty coverage when the delay is correctly modeled. The control benefit is positive in several stressed cases but is not monotonic and is not large enough to claim a general control improvement from estimator replacement alone.

At delay=20 in the pulse case, the violation rate decreases from 0.5284 to 0.3365 while estimator RMSE decreases from 0.1828 to 0.1440 and coverage rises from 0.14 to 0.8885. This is encouraging but remains simulation evidence.

## Unknown fixed-delay probe

A preliminary likelihood-weighted bank over delays 0..20 was tested with five repetitions per condition. It produced approximately:

| Actual fixed delay | Estimator RMSE | 95% coverage | Violation rate |
|---:|---:|---:|---:|
| 5 | 0.0752 | 0.8864 | 0.3542 |
| 10 | 0.1031 | 0.8930 | 0.3790 |
| 20 | 0.1443 | 0.8972 | 0.4200 |

These results are **preliminary** because the bank requires more repetitions and a better-calibrated model-selection/weighting study before it can be compared fairly against a production-quality unknown-delay observer.

## What remains unproven

- variable/unknown delay estimation under realistic timing distributions;
- delay + dropout + model mismatch simultaneously;
- whether improved state estimation transfers to consistent closed-loop control gains;
- robustness under out-of-distribution disturbance families;
- physical/hardware validation;
- computational cost versus benefit.

## Next experiment

Test an explicit **delay-uncertainty observer** against the known-delay KF and naive KF under:

1. variable delay;
2. delay uncertainty interval;
3. delay + dropout;
4. delay + dropout + model mismatch;
5. held-out timing patterns.

The next target metric is calibrated predictive intervals under timing uncertainty, not simply wider covariance.

## Research disposition

**Promote:** fixed known-delay state augmentation as a technically supported local improvement.

**Keep open:** unknown/variable-delay estimation as an unresolved primitive.

**Do not claim:** general superiority of uncertainty-aware adaptive control.
