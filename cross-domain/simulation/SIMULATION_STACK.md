# Simulation Stack — Baseline v0.1

## Core thesis
Simulation is not one technology. It is a stack that connects physical reality, measurement, computation, design, and control.

```text
PHYSICAL WORLD
      ↕
Measurement
      ↓
State estimation / data assimilation
      ↓
Calibrated physical model
      ↓
Discretization
      ↓
Numerical solver
      ↓
Multiphysics / multiscale coupling
      ↓
High-fidelity simulation
      ↓
Reduced-order model / surrogate
      ↓
Neural operator / learned emulator
      ↓
UQ / VVUQ
      ↓
Optimization / inverse design
      ↓
Decision / control
      ↓
PHYSICAL WORLD
```

## Layers under active investigation

1. Governing equations and model-form error.
2. Discretization and adaptive mesh refinement.
3. Sparse linear algebra, preconditioners, Krylov methods, multigrid, domain decomposition.
4. Multiphysics coupling.
5. Multiscale coupling and homogenization.
6. High-fidelity solvers.
7. Reduced-order modelling.
8. Surrogate/emulator models.
9. Neural operators and physics-informed learning.
10. ML interatomic potentials.
11. Calibration and parameter identification.
12. Data assimilation and state estimation.
13. Uncertainty quantification and verification/validation.
14. Differentiable and adjoint simulation.
15. Inverse design and generative engineering.
16. Multi-fidelity and active learning.
17. Real-time simulation.
18. Digital twin composition.
19. Simulation data management and provenance.
20. Autonomous experiment planning.

## Key hypothesis
The likely high-leverage transition is not numerical solver → AI replacement. It is hybrid composition:

```text
Physics solver + measurement + learned surrogate + UQ + optimizer + experiment
```

## Direct connections

- Semiconductors: computational lithography, thermal/package co-design, defect simulation.
- Materials: atomistic → phase-field → continuum → component.
- Robotics: contact dynamics, sim-to-real, state estimation.
- Batteries: electrochemical + thermal + degradation models.
- Biology: molecular/cell/process/bioreactor models.
- Fusion: plasma/material/heat-transport digital twins.
- Water: transport, membrane fouling, selective ion separation.

## Critical warning
Fast simulation is not automatically trustworthy. A surrogate outside its validated regime must be treated as uncertain or rejected for the intended decision.
