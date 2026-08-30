# Research Log — Delay Uncertainty Round 06

Date: 2026-08-30

## Question

Can a state estimator remain calibrated and operationally useful when sensor observations arrive with fixed, unknown, or time-varying latency?

## Search evidence

Recent 2026 literature confirms that stochastic/time-varying delays are treated as first-class estimation/control variables rather than simple additive noise. A May 2026 European Journal of Control paper studies multi-step random measurement delays plus packet dropouts and boundedly uncertain noise; a June 2026 ISA Transactions paper models stochastic delays and sampling intervals explicitly and reports improved worst-case tracking with a predictor-based compensator versus a fixed-delay baseline. These results support the research direction, but do not validate this repository's implementation.

## Local experiment

A corrected digital harness compared:

- naive current-measurement KF;
- known fixed-delay augmented KF;
- preliminary delay-bank estimator.

The plant state and measurement arrival time were explicitly aligned.

### Main observation

For fixed delay=20, the delay-aware estimator reduced estimator RMSE from about 0.174–0.190 to about 0.156–0.162 in the two disturbance families tested. The delay-bank was similar or slightly better.

For variable delays 0..20, the bank estimator was materially closer to the naive estimator than the fixed-delay-10 model and had substantially better empirical interval coverage than the naive estimator.

## Falsification / caveats

- The current probe is small (3 seeds/cell).
- The bank weighting is heuristic.
- Control performance is not yet separated from estimator benefit with statistical power.
- No Bosch FMU run has been claimed; the official FMU remains a Windows 64-bit binary.
- These results do not establish generality.

## Updated hypothesis

Temporal uncertainty should be represented explicitly when latency is large enough to move measurements across dynamically meaningful state evolution.

## Next test

Use a held-out stochastic delay distribution and compare:

1. naive KF;
2. known-delay augmented KF;
3. probabilistic delay estimator;
4. robust/minimax estimator.

Primary metrics:

- state RMSE;
- 95%/99% coverage;
- interval width;
- NLL/calibration score;
- delay identification error;
- tail control violation.

Sources:
- https://www.sciencedirect.com/science/article/abs/pii/S0947358026000488
- https://www.sciencedirect.com/science/article/pii/S0019057826003149
