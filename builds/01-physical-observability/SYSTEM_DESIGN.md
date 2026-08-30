# Build 01 — System Design

## Design principle

Use the smallest amount of custom code needed to connect existing components. The custom value should be concentrated in the evidence/credibility/control layer.

## Candidate component map

| Concern | Reusable option | Decision rule |
|---|---|---|
| Physics simulation | OpenFOAM | Use for CFD/thermal/transport cases where an existing model is adequate |
| Battery physics | PyBaMM | Use only for electrochemical/battery test cases |
| Model exchange | FMI 3.x | Prefer when multiple model environments must compose |
| Industrial semantics | OPC UA | Use when equipment/process interoperability is part of the experiment |
| Asset model | AAS / Eclipse BaSyx | Use when a digital-asset/twin registry is needed |
| Optimization | BoTorch / standard Bayesian optimization | Use for experiment selection or parameter tuning |
| State estimation | standard Kalman/Bayesian filters first | Do not introduce learned estimators before a simple baseline is established |
| Data | CSV/Parquet + explicit schema first | Escalate only when throughput requires it |
| Provenance | Git + immutable run manifests | Every run must resolve software/model/data versions |

## Preferred maturity sequence

### Stage 0 — Digital-only

```text
simulator
  ↓
synthetic sensor model
  ↓
state estimator
  ↓
controller
  ↓
simulator
```

Purpose: validate control and evidence machinery without hardware risk.

### Stage 1 — Hardware-in-the-loop / bench

```text
simulator or plant emulator
       ↕
real sensor/control interface
```

Purpose: test timing, noise, calibration and integration effects.

### Stage 2 — Physical process

```text
real process
  ↕
measurement
  ↕
model
  ↕
control
```

Purpose: test physical reality gap and process disturbance robustness.

Do not skip Stage 0 or claim physical validation from Stage 0.

## Research synchronization contract

Build artifacts must expose machine-readable records for:

- `claim_id` — research claim being tested;
- `hypothesis_id` — explicit hypothesis;
- `source_ids` — background evidence used to define the experiment;
- `component_versions`;
- `model_validity_domain`;
- `measurement_uncertainty`;
- `run_id` and `trial_id`;
- `result_status`;
- `evidence_status`;
- `confidence_before` / `confidence_after`;
- `next_action`.

## Decision gates

### Gate A — Feasibility
Can the existing components be composed without building new core infrastructure?

### Gate B — Observability
Can the hidden state/disturbance be inferred with known uncertainty?

### Gate C — Predictive value
Does the model improve prediction relative to a simple baseline?

### Gate D — Control value
Does prediction enable a measurable reduction in error/risk?

### Gate E — Generalization
Does the result survive held-out disturbances and parameter regimes?

### Gate F — Transfer
Does the result survive the move from digital-only to hardware/physical execution?

## Architectural non-goals

- building a general-purpose simulator;
- building a general-purpose robotics platform;
- building a generic digital-twin SaaS;
- replacing validated solvers with a neural model prematurely;
- claiming industrial readiness from a toy experiment.
