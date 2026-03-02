# AURORA X -- Smart Integrated Coaxial E-Propulsion Core
## Work Package Descriptions (Horizon Europe / EIC Transition Format)
### Duration: 24 months | Start: M1 | End: M24 | Total effort: 120 person-months

---

## WP1: System Architecture & Requirements Engineering

| Field | Value |
|---|---|
| **WP Number** | WP1 |
| **Title** | System Architecture & Requirements Engineering |
| **Lead** | Lead EM Design Engineer |
| **Duration** | M1 -- M4 |
| **Person-months** | 10 PM |

### Objectives

- O1.1: Establish a complete, traceable set of system-level requirements for the AURORA X integrated e-propulsion unit, covering electromagnetic, thermal, mechanical, and electronic subsystems.
- O1.2: Conduct architecture trade-off analyses (coaxial vs. tandem topology; inner-rotor vs. outer-rotor configuration) and select the baseline architecture with quantified justification.
- O1.3: Define all inter-subsystem interfaces (electrical, thermal, mechanical, communication) in a formal Interface Control Document (ICD) to enable concurrent engineering across WP2--WP5.
- O1.4: Freeze the baseline design at M4, providing a single reference configuration for all downstream work packages.

### Description of Work

**Task 1.1 -- Stakeholder Analysis and Requirements Capture (M1--M2)**
The consortium will systematically capture stakeholder needs from the target UAV heavy-lift market segment (MTOW 25--150 kg class). Requirements will be elicited through structured interviews with potential end-users (UAV integrators, defence system primes) and analysis of applicable standards (EASA SC-RPAS, DO-160G environmental conditions). A top-level requirements specification will be produced using the INCOSE requirements engineering methodology, organised into functional, performance, interface, environmental, and safety requirement categories. Key performance parameters (KPPs) shall include: power density >= 5.0 kW/kg, efficiency eta >= 95% in the nominal operating zone, winding temperature <= 150 degC (Class H), torque ripple <= 3%, and demagnetisation margin >= 20% at peak current. Requirements will be managed in a DOORS-compatible traceability matrix to ensure full flow-down to subsystem specifications in WP2--WP5.

**Task 1.2 -- Architecture Trade-Off Study (M1--M3)**
A structured multi-criteria decision analysis (MCDA) will be performed to evaluate candidate motor architectures. The trade space will encompass: (a) coaxial dual-channel vs. tandem dual-channel stator-rotor arrangements; (b) inner-rotor vs. outer-rotor configurations; (c) surface-mounted permanent magnet (SPM) vs. interior permanent magnet (IPM) rotor topologies; (d) concentrated winding vs. distributed winding stator layouts. Each candidate will be assessed against weighted criteria including power density, thermal management feasibility, manufacturability, fault tolerance, and integration complexity with the annular inverter PCB. Analytical sizing models (Hanselman method, Hendershot-Miller scaling laws) will be used to generate first-order performance estimates. The outcome will be a ranked shortlist with a recommended baseline architecture supported by a quantitative trade-off matrix.

**Task 1.3 -- Interface Definition and System Modelling (M2--M4)**
Formal Interface Control Documents (ICDs) will be developed for all subsystem boundaries: (i) EM core to thermal management system (heat flux distribution, coolant channel geometry constraints); (ii) EM core to integrated inverter (phase lead routing, DC bus connection, sensor harness); (iii) thermal system to mechanical housing (mounting provisions, material interfaces, sealing); (iv) inverter to control MCU (signal conditioning, gate drive interface, communication bus). A system-level block diagram and a preliminary 1D lumped-parameter model in MATLAB/Simulink will be created to capture the interactions between electromagnetic, thermal, and electrical subsystems. This model will serve as the seed for the digital twin developed in WP5.

**Task 1.4 -- Baseline Design Freeze and Configuration Control (M3--M4)**
All outputs from Tasks 1.1--1.3 will be consolidated into a Baseline Design Document (BDD). A formal design review (System Requirements Review, SRR) will be conducted at M4 with all consortium partners. The review will verify that: (a) all KPPs are allocated to specific subsystems; (b) interface definitions are consistent and complete; (c) the selected architecture is feasible within the project's 24-month timeline and budget. Upon successful completion of the SRR, the baseline configuration will be placed under formal configuration control. Any subsequent changes will require a documented change request and impact assessment.

### Deliverables

| ID | Title | Type | Due |
|---|---|---|---|
| D1.1 | System Requirements Specification (SRS) with traceability matrix | Report | M2 |
| D1.2 | Architecture Trade-Off Report including MCDA results | Report | M3 |
| D1.3 | Interface Control Document (ICD) -- all subsystem interfaces | Report | M4 |
| D1.4 | Baseline Design Document (BDD) and SRR minutes | Report | M4 |

### Milestones

| ID | Title | Due | Measurable Success Criteria |
|---|---|---|---|
| MS1 | Architecture Frozen | M4 | SRR passed; BDD signed off by all WP leads; all KPPs formally allocated to subsystems with >= 10% design margin identified; ICD version 1.0 released under configuration control. |

### Dependencies

- WP1 has no upstream dependencies (project entry point).
- WP1 outputs are critical inputs to all subsequent WPs: WP2 (EM specifications), WP3 (thermal interface requirements), WP4 (inverter envelope and interface), WP5 (control system requirements), WP6 (mechanical envelope and test acceptance criteria).

---

## WP2: Electromagnetic Design & Optimisation

| Field | Value |
|---|---|
| **WP Number** | WP2 |
| **Title** | Electromagnetic Design & Optimisation |
| **Lead** | Lead EM Design Engineer |
| **Duration** | M2 -- M10 |
| **Person-months** | 26 PM |

### Objectives

- O2.1: Develop and validate an analytical electromagnetic design of the dual-channel coaxial permanent magnet machine meeting the KPPs defined in WP1.
- O2.2: Optimise the slot/pole combination and quasi-Halbach magnet array geometry through systematic 2D and 3D finite element analysis (FEA) to achieve torque ripple <= 3% and demagnetisation margin >= 20%.
- O2.3: Design the dual-channel winding layout ensuring electromagnetic independence between channels for fault-tolerant operation.
- O2.4: Create a calibrated electromagnetic digital twin model suitable for real-time parameter estimation in the control software (WP5).

### Description of Work

**Task 2.1 -- Analytical Electromagnetic Sizing (M2--M4)**
Starting from the baseline architecture frozen in WP1, an analytical electromagnetic design will be developed using classical machine design theory (Hanselman, Gieras, Hendershot-Miller). The sizing procedure will determine: stator outer diameter, stack length, air-gap length, magnet thickness, slot dimensions, and winding parameters (number of turns, wire gauge, fill factor). The analytical model will account for both channels of the dual-channel coaxial topology, ensuring that each channel can independently produce at least 60% of the rated torque (to guarantee continued operation upon single-channel failure). The back-EMF waveform, inductance (Ld, Lq), resistance, and iron loss will be estimated analytically. Material selection will be performed for: (a) stator lamination steel (targeting high-silicon NO20 or Vacoflux cobalt-iron for reduced core losses at high frequency); (b) permanent magnets (N48SH or N45UH NdFeB grade, selected to provide adequate coercivity at the maximum expected operating temperature of 150 degC); (c) winding conductor (round or rectangular copper, Class H insulation system). A parametric spreadsheet model will be created in Python/MATLAB to enable rapid exploration of the design space.

**Task 2.2 -- 2D FEA Parametric Optimisation (M3--M6)**
The analytical design from Task 2.1 will be transferred to a 2D finite element environment (ANSYS Maxwell or JMAG). A parametric sweep study will systematically vary: (a) slot/pole ratio (candidate combinations: 12s10p, 12s14p, 18s16p, 24s20p, 24s22p); (b) magnet arc-to-pole-pitch ratio; (c) slot opening width; (d) tooth tip geometry (shoe shape). For each combination, the following performance metrics will be computed via transient FEA with motion: average torque, torque ripple (peak-to-peak as percentage of average), cogging torque, back-EMF THD, copper losses, iron losses (hysteresis + eddy current using Bertotti's model), magnet eddy current losses, and efficiency map over the full speed-torque operating envelope. A multi-objective genetic algorithm (NSGA-II) will be employed to identify Pareto-optimal designs maximising torque density while minimising torque ripple and total losses. The slot/pole combination will be selected at M5, providing the geometric foundation for the Halbach array optimisation in Task 2.3.

**Task 2.3 -- Quasi-Halbach Magnet Array Design and Optimisation (M5--M8)**
A quasi-Halbach magnet arrangement will be designed to enhance the fundamental air-gap flux density while suppressing harmonic content. The design will use segmented arc magnets with profiled (bread-loaf or trapezoidal) cross-sections to approximate a sinusoidal magnetisation distribution. The number of magnet segments per pole, their individual magnetisation angles, and the segment gap dimensions will be optimised using 2D FEA parametric studies. The key figures of merit are: (a) fundamental flux density amplitude (target: >= 0.95 T in the air gap); (b) THD of the air-gap flux density waveform (target: < 5%); (c) reduction of rotor back-iron thickness enabled by Halbach flux concentration; (d) demagnetisation withstand capability at 150 degC and 3x rated current (worst-case short-circuit). A magnetisation fixture design will be specified for the custom magnet geometry to ensure manufacturability. The design will follow a stepwise complexity approach: baseline with standard arc magnets first, then advanced profiled Halbach, allowing fallback if manufacturing proves infeasible within schedule.

**Task 2.4 -- Dual-Channel Winding Design and Verification (M4--M7)**
The dual-channel stator winding will be designed to achieve electromagnetic decoupling between Channel A and Channel B. Two winding layout strategies will be evaluated: (a) spatially separated windings (each channel occupies alternating slots); (b) bifilar windings within shared slots with interleaved coils. The mutual inductance between channels will be computed via FEA and minimised through winding pitch factor and coil span optimisation. Each channel will be designed as an independent three-phase winding system with its own star point (isolated neutrals). The winding design will be verified by FEA simulation of fault scenarios: (i) single-channel open-circuit; (ii) single-channel short-circuit (inter-turn and phase-to-phase); (iii) demagnetisation under short-circuit conditions. Winding resistance and inductance parameters (Ld, Lq, mutual coupling coefficients) will be extracted for use in the control model (WP5). A winding diagram with coil connection tables and manufacturing instructions will be produced.

**Task 2.5 -- 3D FEA Validation and Digital Twin Model Creation (M7--M10)**
The optimised 2D design will be validated using a full 3D finite element model to capture end-effects (end-winding leakage inductance, 3D fringing flux, axial flux components in the coaxial geometry). The 3D model will be solved in ANSYS Maxwell 3D or JMAG with eddy current and transient solvers. Key outputs: (a) confirmation that 2D performance predictions (torque, losses, efficiency) hold within 5% when 3D effects are included; (b) extraction of frequency-dependent loss maps for iron and magnets; (c) spatial heat source distribution maps (copper loss density per slot, iron loss density per stator tooth/yoke element, magnet loss density per segment) to feed into WP3 thermal models. A reduced-order electromagnetic model (d-q axis equivalent circuit with saturation-dependent parameters stored as lookup tables) will be created and exported in C/Simulink format for integration into the digital twin (WP5). This model shall execute in under 100 microseconds per time-step on the target MCU class (ARM Cortex-M7, 480 MHz) to enable real-time parameter estimation.

### Deliverables

| ID | Title | Type | Due |
|---|---|---|---|
| D2.1 | Analytical Design Report with material selection justification | Report | M4 |
| D2.2 | 2D FEA Optimisation Report: slot/pole selection, parametric sweep results, Pareto fronts | Report | M6 |
| D2.3 | Quasi-Halbach Magnet Array Specification (geometry, grades, magnetisation fixture design) | Report | M8 |
| D2.4 | Dual-Channel Winding Specification (layout, coil tables, fault analysis) | Report | M7 |
| D2.5 | 3D-validated EM Digital Twin Model (Simulink/C export) and loss maps | Software + Dataset | M10 |

### Milestones

| ID | Title | Due | Measurable Success Criteria |
|---|---|---|---|
| MS2 | EM Design Validated | M10 | 3D FEA confirms: average torque within 5% of target; torque ripple <= 3%; efficiency >= 95% at nominal point; demagnetisation margin >= 20% at 150 degC and peak current; digital twin model executes in < 100 us per step. |

### Dependencies

- Depends on WP1 (D1.4 Baseline Design Document, D1.1 SRS for KPPs).
- Outputs feed into: WP3 (heat source maps for thermal modelling), WP4 (winding impedance for inverter design), WP5 (digital twin model), WP6 (manufacturing drawings).

---

## WP3: Thermal Management System

| Field | Value |
|---|---|
| **WP Number** | WP3 |
| **Title** | Thermal Management System |
| **Lead** | Thermal Engineer |
| **Duration** | M3 -- M12 |
| **Person-months** | 22 PM |

### Objectives

- O3.1: Develop and validate a lumped-parameter thermal network (LPTN) model of the AURORA X integrated drive, calibrated against CFD and experimental data.
- O3.2: Design and simulate an internal two-phase cooling system (heat pipes / vapour chambers) capable of maintaining winding temperature <= 150 degC at continuous rated power.
- O3.3: Fabricate and test thermal subsystem prototypes (heat pipe assemblies, evaporator/condenser sections) to validate thermal resistance and heat transport capacity.
- O3.4: Co-optimise the thermal and electromagnetic designs through iterative feedback with WP2 to maximise power density within thermal constraints.

### Description of Work

**Task 3.1 -- Lumped-Parameter Thermal Network Modelling (M3--M5)**
A lumped-parameter thermal network (LPTN) model of the complete AURORA X motor assembly will be constructed in MATLAB/Simulink using the node-branch approach. The network will represent all major thermal components: stator lamination stack (teeth, yoke, back-iron), winding copper (slot portion, end-windings), slot liner insulation, permanent magnets, rotor back-iron, shaft, bearings, housing, and the two-phase cooling subsystem. Thermal resistances will be computed from material properties and geometry (conduction: Fourier's law; convection: empirical correlations for air-gap Taylor-Couette flow, forced convection over end-windings; radiation: Stefan-Boltzmann between rotor and stator surfaces). Heat source inputs will be taken from WP2 loss maps (D2.5). The LPTN will be validated in Task 3.2 against CFD and will serve as the basis for the real-time thermal observer in WP5. The model shall execute in under 50 microseconds per time-step to be suitable for embedded deployment.

**Task 3.2 -- CFD Simulation of Two-Phase Cooling System (M4--M8)**
Conjugate heat transfer (CHT) computational fluid dynamics simulations will be performed using ANSYS Fluent or OpenFOAM with the Volume of Fluid (VOF) method to model the two-phase boiling/condensation cycle within the internal cooling channels. The simulation domain will include: (a) the evaporator section embedded in the stator slots or end-winding region, where the working fluid (candidate fluids: Novec 7100, HFE-7000, or deionised water at sub-atmospheric pressure) absorbs heat via nucleate boiling; (b) the adiabatic transport section through heat pipe wicks or vapour channels machined into the stator housing; (c) the condenser section on the outer housing surface exposed to ambient airflow (propeller-induced or natural convection). Parametric studies will vary: wick structure (sintered copper powder, grooved channels, mesh), fill ratio (30--70%), evaporator geometry (flat vs. annular), and condenser fin density. The key output metrics are: effective thermal resistance from winding hot-spot to ambient (target: <= 0.15 K/W), maximum heat transport capacity (target: >= 500 W), and transient thermal response time constant. CFD results will be used to calibrate the LPTN model from Task 3.1.

**Task 3.3 -- Heat Pipe / Vapour Chamber Prototyping (M6--M10)**
Based on the CFD-optimised design from Task 3.2, physical prototypes of the two-phase cooling subsystem will be fabricated. The prototyping will proceed in two stages: (a) individual heat pipe elements (sintered copper wicks in copper tubes, 6--8 mm diameter, custom lengths matching motor stack geometry) will be procured from specialist suppliers and characterised on a laboratory thermal test bench; (b) an integrated vapour chamber / flat heat pipe assembly matching the stator annular geometry will be custom-manufactured using diffusion bonding or brazing. The prototypes will be instrumented with K-type thermocouples (embedded in wick structure, on evaporator and condenser surfaces) and tested under controlled heat loads (100--800 W range) using cartridge heaters to simulate winding losses. Test metrics: effective thermal conductivity, maximum heat flux before dry-out, thermal resistance vs. heat load curve, orientation sensitivity (gravity effects at 0, 45, 90 degrees inclination to simulate UAV flight attitudes). Results will be compared against CFD predictions to validate the simulation methodology and calibrate the LPTN.

**Task 3.4 -- Thermal Subsystem Testing and Characterisation (M8--M11)**
The validated heat pipe prototypes from Task 3.3 will be integrated into a representative motor stator mock-up (using a geometrically accurate aluminium housing with slot features but without active electromagnetic components). Thermal testing will characterise: (a) steady-state temperature distribution under continuous rated load; (b) transient thermal response to step-load and pulse-load profiles representative of UAV mission cycles (hover, climb, dash); (c) hot-spot temperature under worst-case overload conditions (150% rated current for 30 seconds). The mock-up will be mounted on a thermal test bench with controlled ambient temperature (25 degC and 55 degC cases) and optional forced-air cooling to simulate propeller wash. Infrared thermography will be used to generate full-surface temperature maps for comparison with CFD predictions.

**Task 3.5 -- Thermal-EM Co-Optimisation (M5--M12)**
An iterative co-optimisation loop will be established between WP2 and WP3. As electromagnetic design parameters change (slot dimensions, current density, loss distribution), the thermal model will be updated and thermal constraints fed back to guide EM design decisions. Specific co-optimisation trades include: (a) current density vs. cooling capacity -- determining the maximum allowable current loading given the demonstrated thermal resistance; (b) magnet operating temperature vs. demagnetisation margin -- ensuring that the Halbach array maintains adequate coercivity at the worst-case temperature predicted by CFD; (c) stator housing geometry -- balancing structural stiffness, thermal path efficiency, and electromagnetic performance. This task will produce a co-optimised design specification that simultaneously satisfies all electromagnetic and thermal KPPs. A minimum of three formal design iteration cycles will be completed between M5 and M12.

### Deliverables

| ID | Title | Type | Due |
|---|---|---|---|
| D3.1 | LPTN Thermal Model (calibrated Simulink model) | Software | M8 |
| D3.2 | CFD Simulation Report (two-phase cooling, parametric results) | Report | M8 |
| D3.3 | Heat Pipe Prototype Test Report (thermal resistance, max capacity, orientation data) | Report + Prototype | M11 |
| D3.4 | Thermal-EM Co-Optimisation Report (final converged design parameters) | Report | M12 |

### Milestones

| ID | Title | Due | Measurable Success Criteria |
|---|---|---|---|
| MS3 | Thermal Concept Proven | M12 | Heat pipe prototype demonstrates thermal resistance <= 0.15 K/W at rated heat load; LPTN predictions match experimental data within +/- 8 degC at all measurement points; co-optimised design satisfies winding temperature <= 150 degC at continuous rated power with >= 10 degC margin. |

### Dependencies

- Depends on WP1 (D1.3 ICD for thermal-mechanical interfaces; D1.1 SRS for thermal KPPs).
- Depends on WP2 (D2.5 heat source distribution maps; ongoing co-optimisation with Task 2.2/2.3).
- Outputs feed into: WP5 (LPTN model for real-time thermal observer), WP6 (thermal design specification for prototype manufacturing, thermal test procedures).

---

## WP4: Integrated Power Electronics

| Field | Value |
|---|---|
| **WP Number** | WP4 |
| **Title** | Integrated Power Electronics |
| **Lead** | Power Electronics Lead |
| **Duration** | M6 -- M16 |
| **Person-months** | 24 PM |

### Objectives

- O4.1: Select and validate an inverter topology optimised for integration within the motor housing annular envelope, using wide-bandgap (SiC or GaN) semiconductor devices.
- O4.2: Design and manufacture a dual-channel annular PCB inverter with integrated current and temperature sensors, gate drivers, and DC bus capacitors.
- O4.3: Characterise and mitigate electromagnetic interference (EMI) arising from high-frequency switching within the motor housing, ensuring compliance with DO-160G Section 21 (conducted emissions) targets.
- O4.4: Implement hardware-level dual-channel fault detection and isolation circuitry enabling safe degraded-mode operation.

### Description of Work

**Task 4.1 -- Inverter Topology Selection and Simulation (M6--M8)**
A systematic evaluation of candidate inverter topologies will be performed considering the unique constraints of in-motor integration: limited radial and axial space (annular PCB geometry), high ambient temperature (up to 100 degC from motor losses), and the requirement for two independent three-phase channels. Candidate topologies include: (a) standard two-level six-switch voltage source inverter (2L-VSI) per channel; (b) three-level neutral-point-clamped (3L-NPC) inverter for reduced dV/dt and lower EMI; (c) multi-level flying capacitor topology. For each topology, circuit simulations will be performed in PLECS or LTspice, evaluating: switching losses, conduction losses, total harmonic distortion of phase currents, DC bus ripple, and common-mode voltage. Device technology trade-off (SiC MOSFET vs. GaN HEMT) will consider: voltage rating (target DC bus: 48--60 V), current rating (>= 100 A per channel), Rds(on), switching speed, thermal resistance (junction-to-case), and package availability in automotive-grade. The selected topology and device will be documented with a quantitative comparison matrix.

**Task 4.2 -- Annular PCB Design and Layout (M8--M12)**
The inverter PCB will be designed as an annular (ring-shaped) multilayer printed circuit board dimensioned to fit within the motor end-bell cavity. The PCB design will be executed in Altium Designer or KiCad and will incorporate: (a) power stage: wide-bandgap switches with optimised gate drive loops (target: < 5 nH parasitic inductance per half-bridge); (b) DC bus: low-ESL ceramic capacitor bank (C0G/X7R MLCC array) distributed around the annulus for uniform current sharing; (c) current sensing: inline Hall-effect sensors (Allegro ACS71240 or equivalent) on each phase output with 1 MHz bandwidth; (d) temperature sensing: NTC thermistors at switch junctions and on-board ambient; (e) communication interface: CAN-FD transceiver for DroneCAN/UAVCAN telemetry; (f) gate drivers: isolated or bootstrap half-bridge drivers with desaturation protection and active Miller clamp. The layout will follow strict EMC best practices: star-point grounding, guard traces around sensitive analog signals, ground plane copper pours on all layers, and via stitching around power loops. Thermal management of the power devices will use heavy copper layers (4 oz / 140 um), thermal vias to an aluminium baseplate, and direct thermal path to the motor housing through thermal interface material (TIM). Prototype PCBs will be fabricated (3 units for testing in WP6) by a qualified PCB manufacturer with IPC Class 3 compliance.

**Task 4.3 -- SiC/GaN Gate Driver Development and Optimisation (M9--M13)**
Dedicated gate driver circuitry will be developed for the selected wide-bandgap devices. For GaN HEMTs, the gate driver must support: negative turn-off voltage (typ. -3V for enhancement-mode GaN), precise dV/dt control via gate resistor tuning, and fast (<10 ns) propagation delay for synchronous switching at >= 100 kHz PWM frequency. For SiC MOSFETs, the driver must provide: +18V / -4V gate drive with Kelvin source connection, active Miller clamp for dV/dt immunity, and desaturation detection for short-circuit protection (response time < 2 us). Gate driver prototypes will be tested on a double-pulse test (DPT) bench to characterise: switching energy (Eon, Eoff), voltage overshoot, ringing frequency, and dead-time requirements. A gate resistance optimisation study will balance switching speed (EMI) against switching losses (efficiency). The final gate driver design will be integrated into the annular PCB layout from Task 4.2.

**Task 4.4 -- EMI Characterisation and Mitigation (M11--M15)**
Electromagnetic interference characterisation will be performed at board level and at integrated motor-inverter assembly level. Conducted emissions will be measured on the DC bus input using a Line Impedance Stabilisation Network (LISN) per CISPR 25 / DO-160G methodology. Radiated emissions will be assessed using a near-field probe scanner over the motor housing surface. Based on measurement results, mitigation measures will be implemented iteratively: (a) common-mode choke on DC input; (b) snubber circuits across switch nodes; (c) PWM modulation strategy optimisation (random carrier frequency spreading, interleaved carrier for dual-channel); (d) shielding of the inverter cavity within the motor housing (conductive gaskets, EMI shielding can); (e) PCB layout refinement (ground plane partitioning, slot antenna avoidance). The target is compliance with DO-160G Section 21 Category L (helicopter/UAV rotorcraft) conducted emission limits.

**Task 4.5 -- Dual-Channel Fault Detection Hardware (M12--M16)**
Hardware-level fault detection and isolation (FDI) circuitry will be designed to enable graceful degradation from dual-channel to single-channel operation. The FDI hardware will implement: (a) over-current detection on each phase (comparator-based, < 1 us response) with independent per-channel shutdown; (b) over-temperature monitoring with two independent thermal shutdown thresholds (warning at 140 degC, shutdown at 160 degC); (c) DC bus under/over-voltage protection; (d) gate driver fault feedback (desaturation, under-voltage lockout); (e) channel isolation using solid-state switches (high-side P-channel MOSFET or smart fuse) to electrically disconnect a faulted channel from the DC bus within 10 us. A watchdog supervisor IC will monitor the control MCU heartbeat and force a safe state (all gates low) upon MCU failure. The FDI logic will be implemented in hardware (discrete logic / small CPLD) independent of the main control firmware to ensure fail-safe operation even under software faults.

### Deliverables

| ID | Title | Type | Due |
|---|---|---|---|
| D4.1 | Inverter Topology Trade-Off Report (simulation results, device selection) | Report | M8 |
| D4.2 | Annular PCB Design Package (schematics, layout, BOM, Gerber files) | Report + Software | M12 |
| D4.3 | Gate Driver Characterisation Report (DPT results, switching energy data) | Report + Dataset | M13 |
| D4.4 | EMI Test Report (conducted/radiated emissions, mitigation measures) | Report + Dataset | M15 |
| D4.5 | Dual-Channel Inverter Prototype (3 assembled and tested PCB units) | Prototype | M16 |

### Milestones

| ID | Title | Due | Measurable Success Criteria |
|---|---|---|---|
| MS4 | Inverter Hardware Ready | M16 | All 3 inverter prototypes pass functional test: continuous operation at rated current (>= 100 A per channel) for 1 hour without thermal runaway; conducted emissions within DO-160G Category L limits; fault detection triggers channel isolation in < 10 us for all tested fault types (over-current, short-circuit, over-temperature). |

### Dependencies

- Depends on WP1 (D1.3 ICD for electrical interfaces; D1.1 SRS for voltage/current ratings).
- Depends on WP2 (D2.4 winding impedance data for inverter-motor matching; ongoing feedback on EMI-induced torque ripple).
- Depends on WP3 (thermal boundary conditions for inverter thermal design within motor housing).
- Outputs feed into: WP5 (hardware platform for control firmware deployment), WP6 (inverter units for integrated prototype).

---

## WP5: Control Software & Digital Twin

| Field | Value |
|---|---|
| **WP Number** | WP5 |
| **Title** | Control Software & Digital Twin |
| **Lead** | Embedded Software Engineer |
| **Duration** | M8 -- M20 |
| **Person-months** | 22 PM |

### Objectives

- O5.1: Implement a high-performance field-oriented control (FOC) algorithm on the target MCU platform, achieving current loop bandwidth >= 2 kHz and speed loop bandwidth >= 200 Hz.
- O5.2: Develop online parameter identification algorithms to adaptively estimate winding resistance, inductance, and PM flux linkage in real-time, compensating for thermal drift and ageing.
- O5.3: Deploy a real-time thermal observer (embedded digital twin) running concurrently with the FOC loop, providing continuous hot-spot temperature estimation with accuracy +/- 5 degC.
- O5.4: Implement redundancy management logic for seamless degradation from dual-channel to single-channel operation, and a DroneCAN/UAVCAN telemetry interface for integration with UAV autopilots.

### Description of Work

**Task 5.1 -- FOC Firmware Implementation (M8--M12)**
A sensorless field-oriented control (FOC) algorithm will be implemented in C on the target MCU (STM32H7 series, ARM Cortex-M7, 480 MHz, dual-core). The firmware architecture will comprise: (a) ADC sampling synchronised to PWM centre (simultaneous sampling of three phase currents per channel at >= 40 kSPS); (b) Clarke and Park transforms for alpha-beta and d-q axis decomposition; (c) PI current regulators with anti-windup in the d-q frame (bandwidth target: 2 kHz, corresponding to 500 us loop rate); (d) space vector modulation (SVM) with overmodulation capability; (e) speed estimator using a sliding-mode observer (SMO) or extended Kalman filter (EKF) for sensorless operation above 5% rated speed, with Hall sensor backup for low-speed startup; (f) speed/position controller (outer loop at 1 kHz rate). The firmware will be developed using a model-based design flow: the control algorithm will first be prototyped and verified in MATLAB/Simulink, then auto-generated C code will be deployed to the target MCU. Unit tests will verify: current tracking accuracy (<= 2% steady-state error), step response (< 1 ms to 90% of commanded current), and stability under parameter variations (+/- 30% inductance, +/- 50% resistance).

**Task 5.2 -- Online Parameter Identification (M10--M14)**
Adaptive parameter identification algorithms will be integrated into the FOC firmware to track changes in motor parameters caused by temperature variation and ageing. Two complementary methods will be implemented: (a) recursive least squares (RLS) estimator for winding resistance and inductance, operating on the d-q voltage/current measurements during steady-state operation; (b) high-frequency signal injection (HF-SI) method for PM flux linkage estimation and position estimation at low/zero speed. The RLS estimator will be designed with forgetting factor (lambda = 0.995--0.999) to balance tracking speed against noise rejection. Validation will be performed by: (i) simulation with known parameter drift profiles; (ii) comparison against offline measurements at multiple temperatures (25 degC, 80 degC, 120 degC, 150 degC). The identified parameters will be fed to both the FOC regulators (for adaptive gain scheduling) and the thermal observer (Task 5.3) as indirect temperature indicators (copper resistance is a direct proxy for winding temperature: R(T) = R_25 * [1 + alpha_Cu * (T - 25)]).

**Task 5.3 -- Real-Time Thermal Observer (Embedded Digital Twin) (M10--M16)**
The calibrated LPTN model from WP3 (D3.1) will be reduced to an embedded-compatible state-space formulation and deployed on the MCU as a real-time thermal observer. The observer will run as a background task at 100 Hz, taking inputs from: (a) measured phase currents (copper loss = I^2 * R); (b) estimated speed (iron losses from loss maps stored as lookup tables); (c) ambient temperature sensor; (d) heat pipe condenser temperature sensor. The observer will output estimated temperatures at critical nodes: winding hot-spot, magnet, bearing, inverter junction. A Kalman filter correction step will fuse the model predictions with available temperature sensor measurements (NTC on PCB, optional winding thermocouple) to maintain estimation accuracy under model uncertainty. The observer will provide: (i) continuous thermal state monitoring via DroneCAN telemetry; (ii) predictive thermal derating -- if projected hot-spot temperature exceeds 140 degC, the controller will automatically reduce current limit to prevent thermal damage; (iii) remaining thermal capacity indicator (time-to-thermal-limit at current load). Validation target: estimated hot-spot temperature within +/- 5 degC of measured value across the full operating envelope.

**Task 5.4 -- Redundancy Management Logic (M12--M17)**
Software-level redundancy management will coordinate the dual-channel fault-tolerant operation in conjunction with the hardware FDI from WP4 (D4.5). The redundancy manager will implement a finite state machine (FSM) with the following states: (a) DUAL_ACTIVE: both channels operational, load shared 50/50, maximum performance; (b) DEGRADED_A: Channel B faulted and isolated, Channel A operating at up to 130% rated current (time-limited by thermal capacity); (c) DEGRADED_B: Channel A faulted and isolated, Channel B operating; (d) SAFE_STOP: both channels faulted, controlled motor deceleration via back-EMF braking. Transition triggers will include hardware fault interrupts from WP4 FDI, software-detected anomalies (current imbalance > 20%, position estimator divergence), and health monitoring thresholds. Upon channel loss, the controller will execute a bumpless transfer: the remaining channel's current command will ramp to compensate within 10 ms, with feedforward torque compensation to minimise transient vibration. The redundancy manager will be verified through fault injection testing on the HIL bench (Task 5.6).

**Task 5.5 -- DroneCAN/UAVCAN Telemetry Interface (M14--M18)**
A DroneCAN (UAVCAN v0) and Cyphal (UAVCAN v1) compliant telemetry interface will be implemented over the CAN-FD bus. The following standard and vendor-specific message types will be supported: (a) ESC status (voltage, current, RPM, temperature, error codes) broadcast at 50 Hz; (b) ESC raw command subscription (throttle input from autopilot); (c) node health and software version information; (d) custom AURORA X diagnostic messages: per-channel current/voltage, thermal observer state (all node temperatures), parameter ID state, redundancy manager state, cumulative energy and thermal cycling counters for prognostics. The interface will comply with the Cyphal/DroneCAN specification for ESC nodes, ensuring plug-and-play compatibility with ArduPilot, PX4, and other DroneCAN-capable autopilots. A configuration interface via DroneCAN register access (Cyphal Registers) will allow in-field tuning of control gains, thermal limits, and fault thresholds without firmware reflashing.

**Task 5.6 -- Hardware-in-the-Loop Testing (M16--M20)**
A hardware-in-the-loop (HIL) test bench will be established to validate the complete control software stack before integration with the physical motor. The HIL setup will comprise: (a) the target MCU board running the production firmware; (b) a real-time simulator (dSPACE MicroLabBox or Typhoon HIL) executing the calibrated EM + thermal model from WP2/WP3 at 1 us time-step; (c) signal conditioning to interface simulated back-EMF and current signals with the MCU's ADC inputs; (d) a CAN bus analyser for DroneCAN telemetry monitoring. HIL test scenarios will include: (i) full operating envelope sweep (speed 0--100%, load 0--150%); (ii) dynamic load transients (step from 20% to 100% load in < 50 ms); (iii) fault injection (single-channel open-circuit, short-circuit, sensor failure, CAN bus loss); (iv) thermal runaway scenario (simulated cooling system failure). Test coverage target: >= 95% of all FSM state transitions exercised; all safety-critical fault responses verified within specified timing budgets.

### Deliverables

| ID | Title | Type | Due |
|---|---|---|---|
| D5.1 | FOC Firmware Package (source code, build system, unit test results) | Software | M12 |
| D5.2 | Online Parameter Identification Algorithm Report with validation data | Report + Software | M14 |
| D5.3 | Real-Time Thermal Observer (embedded digital twin model, calibration data) | Software + Dataset | M16 |
| D5.4 | Redundancy Management Specification and FSM verification report | Report + Software | M17 |
| D5.5 | DroneCAN/UAVCAN Interface Specification and compliance test results | Report + Software | M18 |
| D5.6 | HIL Test Report (scenario coverage, fault injection results) | Report + Dataset | M20 |

### Milestones

| ID | Title | Due | Measurable Success Criteria |
|---|---|---|---|
| MS5 | Control Loop Closed | M20 | HIL testing demonstrates: current tracking error <= 2% across full envelope; thermal observer accuracy +/- 5 degC; single-channel fault-to-degraded-mode transition completes in < 10 ms with torque transient < 15%; DroneCAN telemetry operational with ArduPilot SITL; >= 95% FSM state transition coverage achieved. |

### Dependencies

- Depends on WP1 (D1.1 SRS for control requirements, communication protocol specification).
- Depends on WP2 (D2.5 EM digital twin model for HIL real-time simulation and parameter ID validation).
- Depends on WP3 (D3.1 calibrated LPTN model for embedded thermal observer).
- Depends on WP4 (D4.5 inverter hardware for firmware deployment target; D4.5 FDI signals for redundancy manager).
- Outputs feed into: WP6 (production firmware for integrated prototype testing).

---

## WP6: Prototype Integration & Validation

| Field | Value |
|---|---|
| **WP Number** | WP6 |
| **Title** | Prototype Integration & Validation |
| **Lead** | Mechanical & Test Engineer |
| **Duration** | M14 -- M24 |
| **Person-months** | 16 PM |

### Objectives

- O6.1: Complete detailed mechanical design and manufacturing of the AURORA X integrated motor-inverter-cooling prototype, achieving the target mass and dimensional envelope.
- O6.2: Execute a comprehensive dynamometer test campaign covering steady-state performance mapping, transient response, and thermal validation.
- O6.3: Conduct endurance testing (target: 100 hours cumulative operation) to assess reliability and identify degradation mechanisms.
- O6.4: Perform a formal TRL assessment, demonstrating advancement from TRL 3-4 (entry) to TRL 5-6 (exit) with documented evidence.

### Description of Work

**Task 6.1 -- Mechanical Design and Manufacturing (M14--M18)**
Detailed mechanical design of the AURORA X prototype will be executed in SolidWorks / Fusion 360, integrating all subsystem outputs: EM core geometry (WP2), thermal cooling channels and heat pipe routing (WP3), inverter PCB mounting and connector provisions (WP4), and sensor placement. The mechanical design will address: (a) stator housing: aluminium alloy 6061-T6, CNC-machined, with integrated coolant channels, PCB mounting features, and bearing seats; (b) rotor assembly: rotor back-iron (laser-cut lamination stack on shaft), magnet retention (carbon fibre sleeve or stainless steel retaining ring, FEA-verified for burst speed >= 150% of max RPM), balancing provisions (ISO 1940 G2.5 grade); (c) shaft: high-strength steel (4340), dimensioned for combined torsional, bending, and axial loads with safety factor >= 2.0; (d) bearings: hybrid ceramic (Si3N4 balls, steel races) deep groove ball bearings, preloaded for axial-radial combined loading; (e) sealing: IP54 minimum for dust and splash protection; (f) mounting interface: standard NEMA or custom flange compatible with target UAV airframes. Tolerance analysis and GD&T will be applied to all critical interfaces. Manufacturing will be subcontracted to a precision CNC workshop (tolerances: +/- 0.02 mm on bearing seats, +/- 0.05 mm on stator bore). Stator lamination stack will be bonded (Backlack) and ground to final bore dimension. Two complete prototype units will be manufactured (one for destructive/endurance testing, one for demonstration).

**Task 6.2 -- Motor Assembly and Quality Control (M17--M19)**
A documented assembly procedure will be developed and executed for each prototype unit. Assembly steps include: (a) stator winding installation (manual winding per D2.4 specification, vacuum pressure impregnation with Class H epoxy resin); (b) magnet installation on rotor (adhesive bonding with Loctite EA 9395, curing at 65 degC for 2 hours, followed by carbon fibre sleeve installation); (c) rotor balancing on a dynamic balancing machine (two-plane correction, target residual imbalance: < 0.5 g*mm per plane); (d) heat pipe / vapour chamber integration into stator housing; (e) bearing installation with controlled preload; (f) inverter PCB mounting and harness connection; (g) final assembly and dimensional verification. Each assembly step will be documented with photographs, measurements, and checklist sign-off. Quality control gates include: (a) winding resistance measurement (all phases within +/- 2%); (b) insulation resistance test (>= 100 MOhm at 500 VDC); (c) hipot test (2x rated voltage + 1000 V, 1 minute); (d) rotor free-spin test (no rubbing, bearing noise within specification); (e) initial current-less rotation for back-EMF waveform verification against FEA predictions.

**Task 6.3 -- Dynamometer Testing (M19--M22)**
The assembled AURORA X prototype will be mounted on a dynamometer test bench equipped with: (a) a regenerative drive / hysteresis brake (rated for >= 150% of motor rated torque and speed); (b) an inline torque transducer (HBM T40B or equivalent, accuracy class 0.05%); (c) a precision power analyser (Yokogawa WT5000, bandwidth 5 MHz) for electrical input power measurement; (d) temperature data acquisition (24-channel thermocouple logger at 10 Hz); (e) vibration monitoring (tri-axial accelerometer on bearing housing, FFT analysis). The test campaign will cover: (i) no-load characterisation: back-EMF waveform, cogging torque measurement; (ii) locked-rotor test: short-circuit current, thermal time constant; (iii) load test: torque-speed-efficiency map at 25 degC and 55 degC ambient (grid: 10 speed points x 10 torque points = 100 operating points); (iv) overload capability: 150% rated torque for 30 s, 200% for 5 s; (v) transient response: step load from 20% to 100% rated torque, rise time measurement; (vi) dual-channel vs. single-channel comparison: efficiency and thermal behaviour in degraded mode; (vii) vibration spectrum analysis at rated speed and maximum speed. All test results will be compared against simulation predictions from WP2 (EM) and WP3 (thermal) to validate the digital twin.

**Task 6.4 -- Thermal Validation (M20--M23)**
Dedicated thermal validation testing will verify the performance of the two-phase cooling system under representative operating conditions. Test scenarios: (a) continuous rated power for 2 hours, monitoring all thermocouple channels to verify steady-state temperatures are within specification (winding <= 150 degC, magnets <= 120 degC, bearings <= 80 degC, inverter junction <= 125 degC); (b) UAV mission profile replay: a time-varying torque-speed command sequence representing a typical heavy-lift drone mission (takeoff at 130% load for 30 s, climb at 100% for 5 min, cruise at 60% for 20 min, dash at 120% for 2 min, descent at 40% for 5 min, landing at 130% for 20 s) repeated for 10 cycles; (c) cooling system failure simulation: forced air cooling removed during operation at 80% rated load, measuring time-to-thermal-limit and verifying that the control software (WP5) correctly initiates thermal derating and safe shutdown. All thermal test data will be logged synchronously with EM performance data and fed back to calibrate/validate the embedded thermal observer (WP5 D5.3).

**Task 6.5 -- Endurance Testing (M20--M24)**
An automated endurance test program will accumulate a minimum of 100 hours of operation on the prototype. The endurance profile will alternate between: (a) continuous rated load blocks (8-hour runs); (b) thermal cycling blocks (repeated on/off cycles with 5-minute hot / 5-minute cool periods, 50 cycles per block); (c) overload stress blocks (150% rated load for 30 s every 10 minutes). During endurance testing, the following degradation indicators will be monitored: (i) winding resistance drift (indicating insulation degradation or connection loosening); (ii) vibration signature changes (indicating bearing wear or magnet loosening); (iii) back-EMF amplitude drift (indicating partial demagnetisation); (iv) thermal resistance changes (indicating cooling system degradation). Post-endurance inspection will include: disassembly, visual inspection under microscope, magnet flux measurement (Helmholtz coil), bearing play measurement, and insulation resistance re-test. Results will be documented in a formal endurance test report.

**Task 6.6 -- TRL Assessment and Final Reporting (M23--M24)**
A formal Technology Readiness Level (TRL) assessment will be performed following the European Commission's TRL definitions (Horizon Europe Work Programme Annex G). Evidence will be compiled for each TRL criterion: (a) TRL 5 evidence: component and/or breadboard validation in relevant environment (dynamometer testing with representative load profiles, thermal validation under expected operating temperatures); (b) TRL 6 evidence: system/subsystem model or prototype demonstration in a relevant environment (fully integrated motor-inverter-cooling unit, endurance testing demonstrating repeatability and reliability). A consolidated TRL assessment matrix will be prepared and submitted as a formal project deliverable. The final report will include: lessons learned, remaining technology gaps, recommended path to TRL 7-8 (flight testing), intellectual property summary, and exploitation plan alignment with the project's commercialisation strategy (licensing for UAV propulsion, robotics, and industrial servo markets).

### Deliverables

| ID | Title | Type | Due |
|---|---|---|---|
| D6.1 | Mechanical Design Package (3D CAD, 2D drawings, BOM, tolerance analysis) | Report + Software | M18 |
| D6.2 | Assembly Procedure and Quality Control Report | Report | M19 |
| D6.3 | Dynamometer Test Report (full performance map, comparison with simulation) | Report + Dataset | M22 |
| D6.4 | Thermal Validation Report (steady-state, mission profile, failure scenarios) | Report + Dataset | M23 |
| D6.5 | Endurance Test Report (100h, degradation analysis, post-test inspection) | Report + Dataset | M24 |
| D6.6 | TRL Assessment Report and Final Project Report | Report | M24 |
| D6.7 | AURORA X Prototype Demonstrator Units (2 units) | Prototype | M24 |

### Milestones

| ID | Title | Due | Measurable Success Criteria |
|---|---|---|---|
| MS6 | TRL 5/6 Achieved | M24 | Prototype demonstrates: power density >= 5.0 kW/kg (measured on dyno); efficiency >= 95% at nominal operating point; winding temperature <= 150 degC at continuous rated power; torque ripple <= 3% (measured); demagnetisation margin confirmed >= 20% (post-endurance magnet flux within 2% of initial); 100 hours of endurance testing completed without critical failure; TRL 5 criteria fully met, TRL 6 criteria substantially met per EC Annex G definitions. |

### Dependencies

- Depends on WP1 (D1.1 SRS for acceptance criteria and test specifications).
- Depends on WP2 (EM design outputs: lamination geometry, winding specification, magnet specification, simulation predictions for test comparison).
- Depends on WP3 (thermal design: cooling system specification, heat pipe assemblies, thermal test procedures, LPTN predictions for comparison).
- Depends on WP4 (D4.5 inverter prototypes for integration).
- Depends on WP5 (D5.1 production firmware, D5.3 thermal observer, D5.4 redundancy manager -- all deployed on inverter MCU for integrated testing).

---

## Summary: Person-Month Allocation by WP and Role

| Role | WP1 | WP2 | WP3 | WP4 | WP5 | WP6 | Total |
|---|---|---|---|---|---|---|---|
| Lead EM Design | 4 | 14 | 2 | 1 | 1 | 1 | 23 |
| Power Electronics Lead | 1 | 2 | 0 | 14 | 2 | 2 | 21 |
| Thermal Engineer | 2 | 2 | 16 | 1 | 1 | 2 | 24 |
| Embedded Engineer | 1 | 2 | 1 | 4 | 16 | 2 | 26 |
| Mechanical & Test | 2 | 6 | 3 | 4 | 2 | 9 | 26 |
| **Total** | **10** | **26** | **22** | **24** | **22** | **16** | **120** |

## PERT Dependency Chain (Critical Path)

```
WP1 (M1-M4)
  |
  +---> WP2 (M2-M10) --+---> WP5 (M8-M20) --+
  |                     |                      |
  +---> WP3 (M3-M12) --+---> WP4 (M6-M16) ---+---> WP6 (M14-M24)
```

**Critical Path:** WP1 -> WP2 -> WP5 -> WP6 (longest dependent chain)

**Schedule Margin:** WP3 and WP4 run in parallel with WP2, providing 2--4 months of float before WP6 integration begins at M14.
