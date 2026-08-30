# Research Round 05 — Deep Mechanisms and Falsification

Date: 2026-08-30
Horizon: 2026–2032, selective extension to 2034

## Objective
Test the current universal-enabler thesis by descending from technology labels into transport, interfaces, defects, process physics, degradation, qualification, and numerical/computational mechanisms. Prefer direct experimental or operational evidence and explicitly record uncertainty.

## Core finding
The strongest repeated pattern is not a particular product category but a closed engineering loop:

```text
physical state
  -> measurement
  -> state estimation / model
  -> simulation / prediction
  -> uncertainty / credibility
  -> control / optimization
  -> process adjustment
  -> qualification
  -> deployment
  -> degradation / failure observation
  -> model update
```

## High-confidence observations

### A. Interface engineering is real system engineering
- NIST treats surface preparation, bonding parameters, film/surface properties, and metrology as central to predictive hybrid-bonding process development.
- 2026 SiC power-device literature identifies packaging materials, low-inductance interconnects, thermal management, and electro-thermal co-design as necessary for translating SiC device properties into system benefits.
- A 2026 GaN/SiC computational study used ML interatomic potentials and molecular dynamics to engineer a nanoscale interlayer and showed device-level simulated thermal benefits. The result is a research demonstration, not production evidence.

### B. Process observability can be a direct performance multiplier
- NIST's 2026 in-process optical thermal compensation for machine tools reports under-100-second measurement-to-compensation and up-to-order-of-magnitude reduction in machined-part error in the reported experiments, with residual error below measurement uncertainty.
- This is direct evidence for the mechanism `sense -> estimate -> compensate`, rather than the generic claim that sensors are useful.

### C. Qualification remains a technology bottleneck
- NIST identifies measurement, NDE, reference data, process control, and qualification as core barriers for additive manufacturing.
- NASA continues to require fracture control, NDE, probability-of-detection evidence, fatigue/fracture analysis, and lifecycle tests for safety-critical space hardware.
- This supports treating qualification as engineering infrastructure rather than administration.

### D. Defectivity is becoming a computational/measurement problem
- High-NA EUV exposes stochastic defects and pushes inspection toward combined optical/e-beam/electrical evidence.
- ASML's multibeam inspection architecture combines high-throughput electron imaging with computational processing.
- In AM, defects such as pores, cracks and residual stress must be connected to process history and final properties.

### E. Transport mechanisms recur across domains
- Heat: thermal boundary resistance can become dominant in high-power heterogeneous devices.
- Mass/ions: concentration polarization and fouling can limit membrane and electrochemical systems.
- Charge: interfacial charge-transfer kinetics determine battery/electrochemical performance and aging.
- Mechanical: friction, contact and wear determine component lifetime.
- Optical/photon: interconnect and interface loss can limit photonic systems.

### F. Degradation must be modeled as state evolution
- 2026 power-electronics work treats remaining useful life and degradation mechanisms as explicit prediction problems.
- NASA fracture/fatigue programs continuously monitor crack growth, damage accumulation and environmental effects.
- Tribology work demonstrates that surface topography, load and lubrication state can be used for physics-informed wear prediction.

### G. Separation is a cross-domain primitive
- 2026 lithium-recovery literature explicitly distinguishes removal/rejection from actual recovery into a usable product stream and calls for harmonized reporting of chemistry, selectivity, purity, energy and durability.
- Natural-brine experiments identify a tradeoff among separation, concentration and fouling.
- Electro-membrane crystallization demonstrates a route where scaling/fouling can be converted into recoverable products under laboratory conditions.

### H. Numerical methods remain strategically relevant
- Sparse solvers, preconditioners, adaptive methods and heterogeneous/GPU numerical libraries remain core infrastructure for high-fidelity scientific computing.
- The strategic value comes from making repeated simulation, optimization and uncertainty analysis economically possible rather than from solver novelty alone.

### I. Biological scale-up remains a process problem
- 2026 review literature continues to report that strains optimized in lab DBTL loops can underperform in stressed industrial bioreactors.
- Digital twins, PAT, scale-down systems and process optimization are therefore complements to molecular design, not replacements for process engineering.

### J. Precision timing / quantum sensing still has a manufacturing gap
- DARPA's August 2026 program explicitly identifies custom small-batch assembly, non-standardized testing/calibration/assembly, packaging, ruggedization and manufacturing scale as key barriers to tactical optical clocks.

## New mechanism candidates

1. **Process observability** — ability to measure a process variable early enough to change the process before defects become irreversible.
2. **Mechanism-aware compensation** — model a physical error and modify the process in real time.
3. **Interface-state control** — actively shape boundary behavior rather than only selecting bulk materials.
4. **Defect-to-cause inference** — infer process causes from measured defect signatures.
5. **Degradation-state estimation** — represent aging/failure progression as a hidden state that can be estimated and controlled.
6. **Qualification acceleration** — reduce the cost/time needed to establish fitness-for-use without weakening evidence.
7. **Cross-scale state transfer** — move reliable information from atomistic/microstructural models into component/system models.
8. **Compute allocation** — direct scarce simulation/experiment budget toward high-information or high-uncertainty regions.

## Direct implications for existing nodes

| Existing node | Mechanism-level reinforcement |
|---|---|
| Advanced packaging | Promote bonding/metrology/thermal co-design; packaging is not just assembly. |
| Thermal engineering | Promote boundary-resistance and transport engineering, not only coolant selection. |
| Metrology | Promote in-process measurement + compensation and uncertainty-aware measurement. |
| Qualification | Promote model-based/equivalence-based qualification and evidence packages. |
| Simulation | Promote multi-fidelity, multiscale and mechanism-aware simulation. |
| Selective separation | Pair with transport, fouling, regeneration and product-purity economics. |
| Process equipment | Treat equipment availability and reproducibility as technology variables. |
| Degradation models | Pair with online sensing and state estimation. |
| Robotics | Focus on tactile/force/actuator/tribology primitives before universal form-factor claims. |
| Quantum sensing | Focus on packaging, calibration, assembly and test infrastructure. |

## Falsification tests to run next

### F1 — Does process observability actually reduce total manufacturing cost?
Need evidence including sensor cost, latency, false alarms, correction cost, scrap reduction and calibration burden.

### F2 — Does accelerated simulation translate to physical discovery?
Need full-loop evidence including experiment throughput and qualification, not only solver speedup.

### F3 — Are interface improvements durable?
Need long-cycle measurements under realistic thermal, chemical and mechanical stress.

### F4 — Does recycling outperform new supply in total system economics?
Need collection, preprocessing, separation, purification, energy and yield, not laboratory recovery alone.

### F5 — Can degradation models predict useful life under distribution shift?
Need cross-condition validation, uncertainty calibration and rare-event handling.

### F6 — Can standards/interoperability reduce actual deployment friction?
Need evidence that semantic/physical standardization reduces integration time, defects, variants or lifecycle cost.

## Search exclusions
Future-dated articles after 2026-08-30 were excluded from the evidence base even when search engines surfaced them. Company roadmaps are treated as intent evidence, not delivery evidence. Experimental recovery/performance numbers are not treated as industrial economics without system-level validation.

## Key sources

- NIST, In-process optical measurement and compensation of machine tool thermal deformations (2026): https://www.nist.gov/publications/process-optical-measurement-and-compensation-machine-tool-thermal-deformations
- NIST, Metrology of Materials, Surfaces, and Processes for Hybrid Advanced Packaging: https://www.nist.gov/programs-projects/metrology-materials-surfaces-and-processes-hybrid-advanced-packaging
- NIST, Advanced semiconductor manufacturing processes and systems (2026): https://www.nist.gov/publications/innovations-advanced-processes-and-systems-semiconductor-manufacturing
- NIST, AM qualification: https://www.nist.gov/programs-projects/additive-manufacturing-part-qualification
- NIST, 2026 in-situ AM metrology roadmap: https://www.nist.gov/news-events/events/2026/04/roadmapping-situ-metrology-metal-alloy-additive-manufacturing
- Nature Reviews Electrical Engineering, SiC packaging and integration (2026): https://www.nature.com/articles/s44287-026-00263-0
- npj Computational Materials, GaN/SiC thermal interface engineering (2026): https://www.nature.com/articles/s41524-026-02134-6
- imec, High-NA EUV ecosystem: https://www.imec-int.com/en/articles/high-na-euv-new-generation-euv-lithography-ready-shape-our-future
- ASML, HMI eScan 1100 multibeam inspection: https://www.asml.com/en/products/metrology-and-inspection-systems/hmi-escan-1100
- IEA, Building the Future Transmission Grid: https://www.iea.org/reports/building-the-future-transmission-grid/executive-summary
- IEA, Global Critical Minerals Outlook 2026: https://www.iea.org/reports/global-critical-minerals-outlook-2026/executive-summary
- DARPA, It's about time for quantum manufacturing (2026-08-06): https://www.darpa.mil/news/2026/its-about-time
- NASA, NDE risk and fracture control (2026-03-16): https://www.nasa.gov/centers-and-facilities/nesc/nesc-develops-method-for-estimating-risk-when-reducing-nde/
- NASA, Structural Health Monitoring: https://ddtrb.larc.nasa.gov/structural-health-monitoring-laboratory/
- Wear, tribo-informatics review (2026): https://www.sciencedirect.com/science/article/pii/S0043164826002474
- Tribology International, physics-informed wear prediction (2026): https://www.sciencedirect.com/science/article/abs/pii/S0301679X26003154
- Separation and Purification Technology, lithium recovery review (2026): https://www.sciencedirect.com/science/article/pii/S1383586626001838
- Nature Communications, electro-membrane crystallization (2026): https://www.nature.com/articles/s41467-026-75277-1
- PubMed, AI-driven digital twins for bioprocess scale-up (2026): https://pubmed.ncbi.nlm.nih.gov/42190350/
