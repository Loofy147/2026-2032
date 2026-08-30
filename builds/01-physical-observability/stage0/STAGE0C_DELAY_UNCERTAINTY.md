# Stage 0C — Delay-uncertainty study

Status: PRELIMINARY / DIGITAL-ONLY

## Purpose

Test whether explicitly representing measurement-delay uncertainty improves state estimation when the actual delay is fixed but unknown or time-varying.

This study follows the corrected timing convention:

`x_k` is the plant state at the beginning of step k; the measurement available at k refers to `x_{k-d_k}`; the control `u_k` is computed from the estimate of `x_k`; then the plant advances to `x_{k+1}`.

## Models

### Naive KF
Assumes every measurement is current.

### Known-delay augmented KF
Augments the state with a delay history and uses a known fixed delay.

### Delay-bank estimator
Runs a bank of fixed-delay augmented filters for delays 0..D and fuses their current-state estimates using innovation-based weights.

The bank is a preliminary hypothesis probe, not a validated IMM/robust estimator.

## Local result

Using 3 seeds per cell in the current probe:

| Disturbance | Actual delay | Naive estimator RMSE | Known-delay(10) RMSE | Delay-bank RMSE |
|---|---:|---:|---:|---:|
| pulse | 0 | 0.0170 | 0.1009 | 0.0505 |
| pulse | 10 | 0.1157 | 0.1085 | 0.1092 |
| pulse | 20 | 0.1900 | 0.1624 | 0.1618 |
| ramp | 0 | 0.0166 | 0.0996 | 0.0478 |
| ramp | 10 | 0.1122 | 0.1074 | 0.1082 |
| ramp | 20 | 0.1737 | 0.1561 | 0.1558 |
| pulse | 0..20 varying | 0.0582 | 0.1047 | 0.0563 |
| ramp | 0..20 varying | 0.0500 | 0.1025 | 0.0522 |

For the fixed-delay=20 cases, the delay-aware models improved state estimation substantially versus the naive current-measurement assumption. The delay-bank also improved uncertainty coverage relative to the naive estimator.

## Interpretation

The evidence supports a narrower statement:

> In this simplified linear digital probe, modeling measurement delay explicitly can materially improve state reconstruction under moderate/large delay.

It does **not** yet establish superiority of the delay-bank controller, general robustness, or cross-domain transfer.

The fixed-delay=0 rows are a useful negative control: a misspecified delay model can hurt estimation even when the physical system itself is simple.

## Important limitation

The delay-bank result is preliminary. Innovation-based weighting is not a full probabilistic treatment of uncertain latency, and the current probe does not yet include:

- adversarial/outlier delays;
- asynchronous multi-sensor streams;
- unknown delay distribution learned online;
- correlated network/measurement noise;
- controller stability analysis;
- high-fidelity Bosch FMU execution.

No industrial or cross-domain claim is made.

## Decision

Promote the research question, not the implementation:

**RESEARCH NODE:** temporal observability / latency uncertainty.

Next experiment:

`known delay → bounded unknown delay → time-varying delay → delay+dropout → delay+dropout+model mismatch`

with calibration/evaluation separation and controller impact measured independently from estimator impact.
