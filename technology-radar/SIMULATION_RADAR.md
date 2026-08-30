# Simulation Technology Radar — v0.1

## Core stack

| Layer | Capability | Status | Leverage | Main risk |
|---|---|---|---:|---|
| S1 | Governing equations / model-form analysis | Mature | High | model inadequacy |
| S2 | Adaptive discretization / AMR | Mature-active | Very high | complexity / load balancing |
| S3 | Sparse linear algebra | Mature-active | Very high | conditioning / hardware mapping |
| S4 | Preconditioners / multigrid | Mature-active | Very high | problem specificity |
| S5 | Multiphysics coupling | Mature-active | Very high | coupling stiffness |
| S6 | Multiscale modelling | Active | Very high | scale-transfer validity |
| S7 | High-fidelity simulation | Mature | High | computational cost |
| S8 | Reduced-order modelling | Active | Very high | loss of fidelity |
| S9 | Surrogate/emulator models | Active | Very high | OOD failure |
| S10 | Neural operators | Emerging | Very high | generalization / validation |
| S11 | ML interatomic potentials | Emerging-active | Very high | transferability |
| S12 | Calibration / parameter identification | Mature-active | Very high | non-identifiability |
| S13 | Data assimilation / state estimation | Mature-active | Very high | noisy/sparse observations |
| S14 | UQ / VVUQ | Active | Very high | computational cost |
| S15 | Differentiable / adjoint simulation | Active | High | differentiability / stability |
| S16 | Inverse design | Active | Very high | manufacturability constraints |
| S17 | Multi-fidelity learning | Emerging-active | Very high | fidelity mismatch |
| S18 | Active learning | Emerging-active | Very high | acquisition bias |
| S19 | Real-time simulation | Emerging-active | Very high | accuracy-speed tradeoff |
| S20 | Composable digital twins | Emerging | Very high | semantics/interfaces |
| S21 | Simulation data management | Emerging standardization | High | provenance/interoperability |
| S22 | Autonomous experiment planning | Emerging | Transformative | closed-loop robustness |

## Highest-priority research questions

1. How far can numerical acceleration go before model error dominates?
2. How should uncertainty be propagated between simulation fidelities?
3. How can learned surrogates detect when they leave their validity domain?
4. Can simulation models expose machine-checkable applicability conditions?
5. How should physical measurements update model parameters in real time?
6. Can one compose independently validated twins without invalidating their assumptions?
7. What simulation primitives provide the highest cross-domain leverage per unit compute?
