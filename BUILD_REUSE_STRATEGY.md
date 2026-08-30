# Build-via-Reuse Strategy

## Principle

Prefer composition over reinvention. The research project should first identify mature/open components, standards, datasets, simulators, protocols, hardware modules, and experimental platforms that can be assembled to test a hypothesis. Build custom technology only where a measured gap remains.

## Why this belongs in the research method

A future capability may become feasible without a new fundamental invention if existing components can be composed across domains. Therefore each research signal should be evaluated in two directions:

```text
Signal
  ↓
What capability is missing?
  ↓
Can existing components provide 70–90% of it?
  ├── Yes → compose and test
  └── No  → identify the smallest missing primitive
```

The goal is not to minimize engineering. It is to avoid spending effort where an existing component already establishes the relevant capability.

## Current reusable building blocks

### Scientific simulation
- OpenFOAM: open-source CFD for fluid motion, heat transfer, thermodynamics and chemistry. Use as a ready numerical base before implementing a new solver. [R1]
- PyBaMM: open-source physics-based battery models including SPM, SPMe and DFN, with experiment and solver support. Use for battery digital-twin experiments before creating new electrochemical models. [R2]
- FMI: an established open standard for exchanging dynamic simulation models, supported by a broad tool ecosystem. Use for composable simulation interfaces rather than inventing a proprietary interchange layer. [R3]

### Robotics / physical experimentation
- ROS 2 + Gazebo: ready simulation and robotics middleware for building and testing robot models before custom infrastructure. [R4]
- Opentrons: programmable laboratory automation with Python API, protocol libraries and AI-assisted protocol design; useful as an execution layer for laboratory experiments. [R5]
- RoboChem-Flex: recent modular self-driving laboratory architecture combining customizable hardware, Python control and Bayesian optimization; especially relevant for low-cost autonomous experimentation. [R6]

### Digital twins / industrial semantics
- Eclipse BaSyx: open-source AAS/digital-twin middleware with registries and containerized deployment. [R7]
- OPC UA ecosystem: semantic interoperability, companion specifications, edge/cloud gateways and current open-source components such as UA Edge Translator. [R8]
- ISO 23247-6:2026 and ISO/TS 25271:2026 provide standardized concepts for digital-twin composition and industrial digital-twin interfaces. These are standards to align with, not code libraries. [R9]

### Batteries / product lifecycle
- Digital Battery Passport / DPP ecosystem: EU implementation is moving into operational registry and mandatory battery-passport stages, making lifecycle data a ready-made test domain for provenance/interoperability experiments. [R10]
- Open-source battery degradation simulators can supply initial degradation models for state-estimation experiments. [R11]

## Composition candidates

### Candidate A — Simulation credibility loop

```text
OpenFOAM / PyBaMM
   +
measurement dataset
   +
parameter estimation
   +
UQ / VVUQ
   +
provenance schema
   +
model applicability envelope
```

Research question: can an existing simulator be wrapped with machine-checkable evidence about assumptions, validation scope, uncertainty and intended use?

### Candidate B — Physical process observability

```text
low-cost sensor
   +
existing simulator
   +
state estimator
   +
real-time controller
   +
measurement loop
```

Research question: when does observability + model-based correction produce a large reduction in physical error?

### Candidate C — Composable industrial twin

```text
OPC UA
+
AAS / BaSyx
+
FMI models
+
Digital Twin interface
+
provenance / identity
```

Research question: can independently sourced components be composed while preserving semantic meaning, validity conditions and traceability?

### Candidate D — Autonomous scientific loop

```text
simulation
+
Bayesian optimization
+
Opentrons / robotic executor
+
analytical measurement
+
experiment provenance
```

Research question: can a low-cost closed loop maximize useful information per unit experiment cost without losing reproducibility?

## Reuse rules

1. Reuse standards before inventing protocols.
2. Reuse mature numerical solvers before implementing custom solvers.
3. Reuse validated models where their applicability envelope matches the experiment.
4. Treat integration boundaries as research objects; composition can fail even when each component works independently.
5. Record versions, licenses, assumptions and provenance of every reused component.
6. Do not call a composed system "validated" until the composition itself has evidence.
7. Build the smallest custom layer necessary to test the hypothesis.

## Important caution

Reuse reduces development cost, but it does not transfer validity automatically. A validated battery model is not automatically validated for a new cell chemistry; a digital-twin middleware is not proof of correct semantics; a simulator plus a sensor is not automatically a credible digital twin.

## Sources

[R1] OpenFOAM Foundation / OpenFOAM v14, July 2026. https://openfoam.org/
[R2] PyBaMM documentation v26.6.0, June 2026. https://docs.pybamm.org/en/v26.6.0.0/
[R3] FMI Association / FMI specification. https://github.com/modelica/fmi-standard
[R4] ROS 2 documentation, current Gazebo integration. https://docs.ros.org/en/rolling/Tutorials/Advanced/Simulators/Gazebo/Gazebo.html
[R5] Opentrons, 2026. https://opentrons.com/
[R6] Nature Synthesis, 31 July 2026, RoboChem-Flex self-driving laboratory. https://www.nature.com/articles/s44160-026-01053-0
[R7] Eclipse BaSyx documentation. https://www.basyx.org/get-started/introduction
[R8] OPC Foundation, 2026 Cloud Initiative and interoperability work. https://opcconnect.opcfoundation.org/2026/06/cloud-corner-june-2026/
[R9] ISO 23247-6:2026 and ISO/TS 25271:2026. https://www.iso.org/standard/87426.html ; https://www.iso.org/standard/89689.html
[R10] European Commission, Digital Product Passport for batteries, August 2026 update. https://single-market-economy.ec.europa.eu/single-market/digital-product-passport/batteries_en
[R11] Battery-Intelligence-Lab/SLIDE. https://github.com/Battery-Intelligence-Lab/SLIDE
