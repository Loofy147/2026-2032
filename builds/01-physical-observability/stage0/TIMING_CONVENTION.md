# Stage 0 — Timing Convention

This file freezes the temporal semantics after two earlier invalidations.

## State convention

- `x_k`: physical plant state at the beginning of discrete step k.
- `y_k`: measurement delivered at step k.
- If the measurement delay is `d_k`, then `y_k = h(x_{k-d_k}) + v_k` for `k-d_k >= 0`.
- `u_k`: control selected after processing measurements available at k.
- Plant transition: `x_{k+1} = f(x_k,u_k,d_k^{phys},w_k)`.

## Evaluation convention

An estimator output at step k must be compared with `x_k`, not `x_{k+1}`.

The time index of the observation, the time index of the estimate, and the time index of the ground truth must be explicit in every record.

## Required run fields

`step`, `state_time`, `measurement_source_time`, `measurement_arrival_time`, `effective_delay`, `estimate_time`, `control_time`.

## Rejection rule

Any experiment that compares different time indices without an explicit alignment transform is invalid and must not contribute to evidence.

## Why this matters

The research question is temporal observability. Temporal misalignment in the harness would therefore contaminate the quantity being measured itself.
