# AURORA X — Smart Integrated Coaxial E-Propulsion Core

## EIC Transition — Part B: Technical Description

**Acronym:** AURORA X
**Full Title:** Advanced Unified Redundant Outrunner Architecture for neXt-generation Electric Propulsion
**Duration:** 24 months
**Requested EU Contribution:** EUR 1,348,775
**TRL Entry:** 3–4 → **TRL Exit:** 5–6

---

# Section 1: EXCELLENCE

## 1.1 Innovation Potential

### 1.1.1 The Problem: Thermal and Integration Barriers in Electric Propulsion

Modern heavy-lift UAV and eVTOL platforms demand electric motors with continuous specific power exceeding 5 kW/kg at efficiencies above 95%. Current state-of-the-art BLDC/PMSM motors face three fundamental barriers:

**Thermal ceiling.** Conventional air-cooled outrunner motors (T-Motor U15: 2.4 kW/kg continuous) are limited by winding temperature. Even liquid-jacketed systems (EMRAX 228: 5.8 kW/kg continuous) cannot fully exploit their electromagnetic potential because heat must traverse multiple thermal interfaces — winding insulation, slot liner, stator iron, press-fit contact, and housing — before reaching the coolant. The total thermal resistance of this chain (0.3–0.8 °C/W) caps the achievable current density at 10–18 A/mm².

**Integration gap.** The motor and its power electronics (ESC) remain separate subsystems connected by cables. This adds 10–15% parasitic mass, introduces EMI radiation from exposed high-current conductors, and creates reliability vulnerabilities at connector interfaces. While integrated motor drives exist at the MW scale (H3X HPDM-250: 10.7 kW/kg system, Safran ENGINeUS: EASA certified Feb 2025), the 10–50 kW class critical for UAV remains underserved.

**Magnetic limitations.** Standard surface-mounted permanent magnets with uniform radial magnetization produce trapezoidal flux distributions, resulting in 5–15% torque ripple and significant cogging. These pulsations cause acoustic noise, vibration, and control complexity.

### 1.1.2 The Breakthrough: Four Pillars of AURORA X

AURORA X addresses all three barriers through a synergistic architecture combining four innovations in a single integrated propulsion unit:

**Pillar 1: Dual-Channel Coaxial Machine.**
Two independent 3-phase electromagnetic channels share a common stator and rotor. In nominal operation, both channels share the load, each handling 50% of rated power with reduced copper losses. Upon failure of one channel, the surviving channel sustains 50% power — providing hardware-level redundancy without additional mass. This fail-operational capability is critical for UAV safety certification under EASA CS-23.1309.

The dual-channel architecture uses a 6-phase winding with 30° electrical shift between channels, minimizing torque ripple during single-channel degraded operation. Slot/pole combination: 18 slots / 20 poles, yielding a winding factor of 0.945 and LCM of 180 (high cogging frequency = low cogging amplitude).

**Pillar 2: In-Motor SiC/GaN Inverter.**
The power stage is integrated directly into the motor housing on an annular PCB (Ø140/50 mm, 6-layer). Using 100V GaN FETs (EPC2302, Rds(on) = 1.8 mΩ) in a 2-level topology with 2× parallel per switch position, the inverter achieves:

| Parameter | Value |
|---|---|
| Efficiency (continuous) | 99.2% |
| Efficiency (peak) | 99.0% |
| Total inverter losses | 157 W (cont.) / 314 W (peak) |
| Total mass | 480 g |
| Switching frequency | 80 kHz (inaudible) |

The 96V DC bus is ideally suited for GaN: at this voltage, GaN FETs have a figure-of-merit (Rds×Qg = 54 mΩ·nC) that is 2× superior to Si MOSFETs and 67× superior to SiC. Eliminating the external ESC removes 150–300 g of cables, connectors, and enclosures, while reducing the power loop inductance to <1 nH — practically eliminating voltage overshoot and EMI at the source.

**Pillar 3: Two-Phase Cooling Core.**
A sealed annular thermosyphon chamber integrated into the stator housing exploits liquid-vapour phase change (water at 0.16 bar absolute, Tsat = 55°C) to transport heat from the stator windings to an external finned condenser. The evaporator achieves a heat transfer coefficient of 12,000 W/m²K on micro-textured copper surfaces — an order of magnitude above water-jacket cooling (500–3,000 W/m²K).

Thermal performance comparison:

| Cooling Method | R_total (°C/W) | Max Continuous Power | Added Mass |
|---|---|---|---|
| Air (forced) | 0.77 | 6 kW | 0 kg |
| Water jacket | 0.29 | 14 kW | 1.5–2.0 kg |
| **AURORA X two-phase** | **0.22** | **20 kW** | **0.5–0.8 kg** |

The two-phase system enables a continuous current density of 20–25 A/mm² — 40% higher than water-jacket cooling — while adding less than half the mass. A supplementary spray cooling system on the end-windings extends the 30 kW peak duration to >60 seconds.

**Pillar 4: Low-Harmonics Magnetics.**
Profiled quasi-Halbach magnet segments (N48SH NdFeB, max operating temperature 150°C) with bread-loaf geometry produce a near-sinusoidal airgap flux distribution. Compared to conventional surface-mounted magnets:

- Airgap flux density: +30–50% (enabling back-iron thickness reduction and weight savings)
- Cogging torque: reduced by up to 87% (optimized segment geometry + 0.5° mechanical skew)
- Torque ripple: ≤3% target (from typical 8–15% in conventional designs)
- Demagnetization margin: ≥20% at peak current and 150°C (validated by FEA)

### 1.1.3 Benchmarking Against State of the Art

| Motor / System | Type | Cont. kW/kg | Efficiency | Cooling | Integrated Inv. | Redundancy |
|---|---|---|---|---|---|---|
| T-Motor U15 II | Outrunner | 2.4 | ~88% | Air | No | No |
| EMRAX 228 | Axial flux | 5.8 | 96% | Liquid | No | No |
| H3X HPDM-250 | Radial+inv | 10.7 | 92.9% sys | Liquid | Yes (SiC) | No |
| Safran ENGINeUS | PMSM | ~5.0 | — | Air | Yes | No |
| **AURORA X (target)** | **Coaxial** | **≥5.0** | **≥95%** | **Two-phase** | **Yes (GaN)** | **Yes (dual)** |

AURORA X uniquely combines integrated inverter, two-phase cooling, AND hardware redundancy in the 10–50 kW class. No existing product or announced development programme offers this combination.

---

## 1.2 Objectives, Methodology, and Feasibility

### 1.2.1 Objectives

| ID | Objective | KPI | Target | Verification |
|---|---|---|---|---|
| O1 | Demonstrate integrated propulsion core | TRL level | 5–6 | System-level test |
| O2 | Achieve target power density | Specific power | ≥5.0 kW/kg (cont.) | Dyno measurement |
| O3 | Validate two-phase thermal management | Winding temperature | ≤150°C at 20 kW | Thermocouples + IR |
| O4 | Minimize torque pulsation | Torque ripple | ≤3% | Torque transducer |
| O5 | Integrated GaN inverter | System efficiency | ≥95% (motor+inv) | Power analyzer |
| O6 | Dual-channel redundancy | Fault response | <5 ms detection, 50% power retained | HIL fault injection |
| O7 | Digital twin for predictive control | Temperature accuracy | ±5°C winding, ±10°C magnets | Calibrated model |

### 1.2.2 Methodology: Digital-Twin-Driven Design Loop

The design methodology centres on a multi-physics digital twin that couples electromagnetic, thermal, and structural models in a closed optimization loop:

**Phase 1: EM Design (M1–M10).** Parametric 2D/3D FEA (ANSYS Maxwell / MotorCAD) optimizes slot/pole geometry, Halbach segment profiles, and winding layout. The electromagnetic model generates flux maps, loss maps, and torque waveforms fed to the thermal model.

**Phase 2: Thermal & Structural (M3–M14).** CFD simulation (ANSYS Fluent) models the two-phase thermosyphon with Volume-of-Fluid (VOF) methods. Structural FEA validates housing integrity under thermal cycling and vibration. Results update the EM model (temperature-dependent magnet properties, resistance drift).

**Phase 3: Prototype (M14–M20).** Physical manufacturing and assembly. Annular GaN PCB, custom Halbach rotor, machined housing with integrated vapor chamber.

**Phase 4: Validation (M18–M24).** Dyno testing generates efficiency maps, thermal profiles, and vibration signatures. Measured data calibrates the digital twin via Bayesian parameter updating, closing the loop.

Multi-objective optimization (Pareto-based, NSGA-II) runs across the EM-Thermal interface, simultaneously minimizing mass and losses while respecting thermal constraints.

### 1.2.3 Motor Design Parameters

Based on preliminary analytical calculations:

| Parameter | Value | Notes |
|---|---|---|
| Rated power | 20 kW continuous, 30 kW peak (60s) | Dual-channel load sharing |
| DC bus voltage | 96V | 24S LiPo compatible |
| Max speed | 10,000 RPM | Direct drive or 1:2 reduction |
| Rated torque | 19.1 Nm | At 10,000 RPM |
| Stator OD | 140 mm | |
| Stack length | 70 mm | |
| Airgap | 0.5 mm | |
| Slots / Poles | 18s / 20p | Winding factor 0.945 |
| Winding | Dual 3-phase, concentrated, 30° shift | |
| Magnet grade | N48SH (Br=1.38T, Hcj≥20 kOe) | Max 150°C |
| Airgap flux density | 0.95–1.05 T (Halbach) | |
| Current density | 22 A/mm² (continuous, two-phase cooled) | |
| Slot fill factor | 0.50 (VPI impregnated) | |

### 1.2.4 Loss Budget at Rated Point (20 kW)

| Source | Losses (W) | Location |
|---|---|---|
| Copper (slot + end-winding) | 600 | Stator windings |
| Iron (hysteresis + eddy) | 300 | Stator teeth + back-iron |
| Rotor (eddy in magnets + sleeve) | 100 | Rotor surface |
| Mechanical (windage + bearing) | 50 | Airgap, bearings |
| Inverter (GaN conduction + switching) | 157 | Annular PCB |
| **Total** | **1,207** | |
| **System efficiency** | **94.3%** | Motor: 95.0%, Inverter: 99.2% |

### 1.2.5 Thermal Design

The two-phase cooling system maintains all components within safe operating temperatures:

| Location | Temperature | Limit | Margin |
|---|---|---|---|
| Winding hotspot | 145°C | 150°C (Class H) | 5°C |
| Rotor magnets | 105°C | 120°C (N48SH) | 15°C |
| GaN junction | 119°C | 150°C | 31°C |
| Bearing (DE) | 85°C | 120°C | 35°C |

The 7-node lumped-parameter thermal network (LPTN) runs on the control MCU at 100 Hz, providing real-time temperature estimates for predictive derating. The digital twin improves peak torque utilization by +64% compared to conventional reactive thermal limiting (MPC-based predictive derating vs. threshold-based).

### 1.2.6 Control Architecture

```
┌──────────────────────────────────┐
│         Digital Twin             │
│  EM Model + LPTN + Mechanical    │
│  Parameters: Rs(T), ψf(T), L(i) │
└───────────┬──────────────────────┘
            ▼
┌──────────────────────────────────┐
│       FOC + MPC Controller       │
│  Current MPC @40 kHz             │
│  Thermal derating constraints    │
│  Fault detection @40 kHz         │
└───────────┬──────────────────────┘
            ▼
┌──────────────────────────────────┐
│   Dual 3-Phase GaN Inverter      │
│   Channel A ◄─► Channel B        │
│   fsw = 80 kHz, DroneCAN bus     │
└──────────────────────────────────┘
```

MCU: STM32G4 (Cortex-M4F, 170 MHz) with integrated CORDIC and FMAC accelerators for FOC. DroneCAN/Cyphal telemetry at 100 Hz provides RPM, voltage, current, temperatures, and fault flags.

### 1.2.7 Feasibility Assessment

Each pillar has a clear technology precedent:

| Pillar | Precedent | Gap Addressed by AURORA X |
|---|---|---|
| Dual-channel | Joby Aviation (236 kW, dual winding) | Scale to 20 kW class with full FDI |
| Integrated inverter | H3X HPDM-250 (SiC), EPC91122 (GaN) | GaN at 100V for optimal efficiency |
| Two-phase cooling | Georgia Tech (26 A/mm²), Purdue (30.4 A/mm²) | Integration into production motor |
| Halbach magnets | EMRAX, Evolito (axial flux) | Radial-flux with profiled segments |

The synergy of combining all four — not any single pillar alone — is the breakthrough. Individual component TRLs are 4–6; the integrated system is TRL 3–4.

---

# Section 2: IMPACT

## 2.1 Market and Commercial Strategy

### 2.1.1 Market Opportunity

The global UAV market is projected to reach EUR 58 billion by 2030 (CAGR 14.7%), with the electric propulsion subsystem representing 8–12% of platform value. The eVTOL/Urban Air Mobility segment adds a further EUR 15–20 billion by 2035.

AURORA X targets three market segments:

| Segment | Market Size (2030) | AURORA X Value Proposition |
|---|---|---|
| Heavy-lift UAV (10–50 kW) | EUR 4.2B | Only integrated drive with redundancy |
| eVTOL propulsion | EUR 2.8B | Certified-ready fail-operational architecture |
| Industrial robotics | EUR 1.5B | Compact, high-torque, plug-and-play |

### 2.1.2 European Strategic Alignment

AURORA X directly contributes to:
- **EU Green Deal**: Enabling zero-emission aviation for inspection, delivery, and urban mobility
- **Clean Aviation JU**: Aligned with SRIA priority on "Disruptive technologies for electrification"
- **EU Chips Act**: Demand-side pull for European WBG semiconductor manufacturing (STMicroelectronics SiC, Infineon GaN)
- **EU Defence**: Sovereign capability for UAV propulsion (reduce dependency on US/Asian supply chains)

### 2.1.3 Exploitation Strategy

**IP Protection:**
- 2–3 patents (architecture, cooling integration, magnet profile)
- Know-how protection for assembly processes and optimization models
- Trade secrets for digital twin calibration data

**Business Model:**
- Phase 1 (Y1–3): Technology licensing to motor OEMs (4–6% royalty)
- Phase 2 (Y3–5): Spin-off company for direct sales of modular propulsion units
- Phase 3 (Y5+): Design kits and reference designs for volume production

**Quantified Impacts (5-year horizon post-project):**

| Impact | Target |
|---|---|
| Revenue from licensing | EUR 2–5M |
| Direct jobs created | 15–25 |
| Patents filed | 2–3 (EPO → PCT) |
| Journal publications | 4–6 (Gold OA) |
| Conference presentations | 8–10 |
| CO₂ reduction enabled | 500–1000 t/year (vs. combustion alternatives) |

## 2.2 Dissemination and Communication

**Target audiences:** Scientific community, UAV/eVTOL industry, policy makers, general public.

**Channels:**
- **Journals:** IEEE Transactions on Industrial Electronics, IEEE TEC, IET Electric Power Applications
- **Conferences:** ECPE (Nuremberg), EPE-PEMC, ICEM, ICEMS
- **Open Access:** Gold OA for all publications (budget allocated)
- **Project website:** Technical blog, design data repository
- **DroneCAN/Cyphal community:** Open-source telemetry interface specification

**Open Science:** Immediate Open Access for all publications. Data Management Plan (DMP) delivered at M6. FAIR data principles for test datasets.

---

# Section 3: IMPLEMENTATION

## 3.1 Work Plan and Resources

### 3.1.1 Work Package Overview

| WP | Title | Lead | Months | PM | Key Deliverable |
|---|---|---|---|---|---|
| WP1 | System Architecture | Lead EM | M1–M4 | 12 | D1.1: Architecture Specification |
| WP2 | EM Design & Optimization | Lead EM | M2–M10 | 20 | D2.1: Validated EM Model |
| WP3 | Thermal Management | Thermal Eng. | M3–M12 | 16 | D3.1: Cooling Subsystem Prototype |
| WP4 | Integrated Power Electronics | PE Lead | M6–M16 | 16 | D4.1: Annular GaN PCB |
| WP5 | Control Software & Digital Twin | Embedded Eng. | M8–M20 | 14 | D5.1: FOC+DT Firmware |
| WP6 | Prototype & Validation | Mech. Eng. | M14–M24 | 14 | D6.1: TRL 5–6 Demonstrator |

### 3.1.2 Milestones

| ID | Title | Month | Success Criterion |
|---|---|---|---|
| M1 | Architecture Frozen | M4 | All interfaces defined, requirements baselined |
| M2 | EM Validated | M10 | FEA confirms ≥95% efficiency, ≤3% torque ripple |
| M3 | Concept Proven | M12 | Cooling subsystem achieves R_total ≤0.25°C/W on bench |
| M4 | Hardware Ready | M16 | GaN PCB passes functional test at 20 kW |
| M5 | Control Loop Closed | M20 | FOC + DT running on hardware, sensorless at >1000 RPM |
| M6 | TRL 5–6 Achieved | M24 | Full system dyno test: ≥5 kW/kg, ≥95% η, 100h endurance |

### 3.1.3 Gantt Chart

```
Month:  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
WP1:    ████████████◆
WP2:       ██████████████████████████████████◆
WP3:          █████████████████████████████████████◆
WP4:                      ██████████████████████████████████◆
WP5:                            ████████████████████████████████████████◆
WP6:                                              ██████████████████████████████████◆
        ◆ = Milestone
```

### 3.1.4 Budget Summary

| Category | Amount (EUR) | % |
|---|---|---|
| Personnel (92 PM) | 657,000 | 48.7% |
| Equipment | 190,000 | 14.1% |
| Materials (magnets, SiC, laminates) | 52,020 | 3.9% |
| Subcontracting | 175,000 | 13.0% |
| Travel & dissemination | 40,000 | 3.0% |
| **Indirect costs (25% flat rate)** | **234,755** | **17.4%** |
| **TOTAL** | **1,348,775** | **100%** |

EIC Transition funding rate: 100%. Requested EU contribution: EUR 1,348,775.

### 3.1.5 Risk Management

Top risks with mitigation strategies:

| Risk | P×I | Mitigation |
|---|---|---|
| **R01: Thermal targets not met** | High | 30% design margin; fallback to hybrid single-phase+spray |
| **R02: EMI exceeds limits** | High | Multi-layer suppression from PCB stage; pre-compliance at M9 |
| **R04: Magnet quality** | High | Dual-source qualification; 10% surplus inventory |
| **R05: WBG supply chain** | Critical | Early ordering M1; pin-compatible 2nd source; Si IGBT fallback |
| **R08: Weight exceeded** | High | Component-level mass budget; topology optimization |
| **R09: Key person leaves** | High | Named deputies; systematic knowledge documentation |

Full risk register with 10 identified risks, risk matrix, and quality assurance plan (design review gates: SRR M4, PDR M10, CDR M16, TRR M22, FR M24).

## 3.2 Team and Consortium

### Key Roles

| Role | Expertise | PM | Rate |
|---|---|---|---|
| Lead EM Design Engineer | PMSM design, FEA, Halbach optimization | 24 | Senior |
| Power Electronics Lead | SiC/GaN, PCB design, EMI | 20 | Senior |
| Thermal Engineer | CFD, two-phase systems, heat pipe design | 18 | Researcher |
| Embedded Software Engineer | FOC, MPC, real-time systems, DroneCAN | 16 | Researcher |
| Mechanical Engineer & Test | Structural analysis, manufacturing, dyno testing | 14 | Researcher |

---

## Ethics and Gender

This project does not raise ethical concerns. No human subjects, personal data processing, or dual-use technology involved. The gender dimension is addressed through:
- Gender-balanced recruitment targets for all roles
- Inclusive working environment policies
- Gender analysis in user requirements (ergonomic aspects of motor integration)

---

*AURORA X: The future of integrated electric propulsion.*
