# Mechanism-Level Radar — v0.1

This radar descends below named technologies into physical/chemical/computational mechanisms that can become bottlenecks or multipliers across domains.

| Mechanism | Why it matters | Current signal | Domains |
|---|---|---|---|
| Thermal boundary resistance | Can dominate heat flow as cooling moves closer to devices | Strong signal | AI compute, power electronics, photonics, aerospace |
| Mass transfer / concentration polarization | Limits separation, electrochemistry and reactors | Strong signal | water, batteries, hydrogen, bioprocess |
| Interfacial reaction kinetics | Can dominate lifetime despite good bulk materials | Strong signal | batteries, fuel cells, catalysts |
| Surface engineering / coatings | Alters wear, corrosion, adhesion and chemical stability | Strong signal | robotics, engines, energy, space |
| Bonding / hybrid bonding | Determines heterogeneous integration yield and reliability | Strong signal | semiconductors, photonics, quantum |
| Deposition / etch process control | Couples feature formation to defects and device yield | Strong signal | semiconductors, photonics, coatings |
| Crystal growth / defect control | Determines material quality at device scale | Active | semiconductors, quantum, optics |
| Phase evolution / microstructure control | Links process history to final properties | Strong signal | AM, alloys, energy materials |
| Fracture / fatigue / wear | Determines long-lived system reliability | Strong signal | machines, bridges, aerospace, robotics |
| Degradation-state estimation | Converts aging from hidden risk into controllable state | Active-strong | batteries, fuel cells, machinery, infrastructure |
| Rare-event probability estimation | Needed for safety when failures are rare | Emerging-strong | aerospace, energy, civil, autonomous systems |
| Adaptive discretization | Concentrates compute where physics is difficult | Mature-active | HPC, CFD, materials, multiphysics |
| Sparse solvers / preconditioning | Can change simulation cost without new hardware | Mature-active | scientific computing, engineering, AI physics |
| Multiscale coupling | Transfers information between atomistic and system scales | Active | materials, batteries, biology |
| Active learning / experiment selection | Maximizes information gained per experiment | Emerging-active | materials, biology, chemistry |
| Defect engineering | Some defects are failure modes; others are functional design variables | Emerging-active | quantum, photonics, thermoelectrics, semiconductors |
| Precision alignment / assembly | Determines optical/electrical continuity at small scales | Strong signal | photonics, quantum, sensors |
| PNT / timing stability | Infrastructure primitive for distributed autonomous systems | Active-strong | space, telecom, power, robotics |
| Selective ion transport | Enables separation of closely related species | Strong signal | water, mining, batteries, chemistry |
| Extreme-environment materials | Enables operation where ordinary seals/electronics fail | Strong signal | geothermal, space, nuclear, aerospace |

## Mechanism-level research tests

For each mechanism ask:

1. What physical variable actually limits performance?
2. Is the limitation bulk, interface, geometry, process, or measurement?
3. Can it be measured in situ?
4. Can it be simulated at relevant scale?
5. Does improving it move the bottleneck elsewhere?
6. Can a manufacturing process reproduce it reliably?
7. Can the improvement survive realistic cycling, contamination, temperature, pressure and aging?
8. Does the mechanism recur in unrelated industries?

## Key hypothesis

The most strategically important technologies may be control technologies for difficult mechanisms rather than new end-user products. Examples include controlling thermal interfaces, ion transport, microstructure, defect formation, degradation and rare-event probability.

## Priority next searches

- phonon/electron interface transport;
- boundary layers and concentration polarization;
- interfacial reaction kinetics;
- crystal-growth defect formation;
- deposition nucleation and morphology;
- fatigue crack initiation in as-built structures;
- tribochemical wear and lubrication degradation;
- accelerated aging and online prognostics;
- rare-event sampling in multiphysics systems;
- precision assembly metrology;
- quantum-defect fabrication and stability.
