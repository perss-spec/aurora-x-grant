# AURORA X — EIC Transition Grant Proposal
# Budget & Timeline (24 months, TRL 4 -> TRL 5/6)

---

## 1. WORK PACKAGE STRUCTURE

| WP | Title | Lead | M start | M end | Effort (PM) |
|----|-------|------|---------|-------|-------------|
| WP1 | Project Management & Coordination | Lead EM Engineer | M1 | M24 | 8 |
| WP2 | EM Design & Optimization | Lead EM Engineer | M1 | M14 | 22 |
| WP3 | Power Electronics & Drive | Power Electronics Eng. | M3 | M18 | 18 |
| WP4 | Thermal Management | Thermal Engineer | M4 | M20 | 16 |
| WP5 | Embedded Control & Software | Embedded SW Engineer | M6 | M22 | 14 |
| WP6 | Mechanical Design & Prototyping | Mechanical Engineer | M2 | M16 | 8 |
| WP7 | Integration, Testing & Validation | All | M14 | M24 | 6 |
| **TOTAL** | | | | | **92** |

---

## 2. PERSON-MONTHS PER WP

| Role | Rate | WP1 | WP2 | WP3 | WP4 | WP5 | WP6 | WP7 | Total PM | Cost (EUR) |
|------|------|-----|-----|-----|-----|-----|-----|-----|----------|------------|
| Lead EM Design Engineer (Senior) | 8,000 | 4 | 14 | - | - | - | 2 | 4 | **24** | 192,000 |
| Power Electronics Engineer (Senior) | 8,000 | 1 | 2 | 14 | - | 1 | - | 2 | **20** | 160,000 |
| Thermal Engineer (Researcher) | 6,500 | 1 | 2 | 1 | 12 | - | 1 | 1 | **18** | 117,000 |
| Embedded Software Engineer (Researcher) | 6,500 | 1 | 2 | 1 | 1 | 10 | - | 1 | **16** | 104,000 |
| Mechanical Engineer / Test (Researcher) | 6,000 | 1 | 2 | 2 | 3 | 3 | 5 | -2 | **14** | 84,000 |

**Note:** Mechanical Engineer WP7 adjusted — see corrected table below.

### Corrected Person-Months Allocation

| Role | Rate/PM | WP1 | WP2 | WP3 | WP4 | WP5 | WP6 | WP7 | Total | Cost |
|------|---------|-----|-----|-----|-----|-----|-----|-----|-------|------|
| Lead EM Design Eng. (Sr.) | 8,000 | 3 | 13 | 1 | - | - | 3 | 4 | **24** | 192,000 |
| Power Electronics Eng. (Sr.) | 8,000 | 1 | 2 | 13 | - | 1 | 1 | 2 | **20** | 160,000 |
| Thermal Engineer (Res.) | 6,500 | 1 | 2 | 1 | 11 | - | 1 | 2 | **18** | 117,000 |
| Embedded SW Engineer (Res.) | 6,500 | 1 | 1 | 1 | 1 | 10 | 1 | 1 | **16** | 104,000 |
| Mechanical Eng./Test (Res.) | 6,000 | 2 | 1 | 1 | 1 | - | 5 | 4 | **14** | 84,000 |
| **TOTAL** | | **8** | **19** | **17** | **13** | **11** | **11** | **13** | **92** | **657,000** |

**Reconciliation check:** 8+19+17+13+11+11+13 = 92 PM. Correct.

---

## 3. DETAILED BUDGET

### 3.1 Personnel Costs (Direct)

| # | Role | PM | Rate (EUR/PM) | Total (EUR) |
|---|------|----|---------------|-------------|
| 1 | Lead EM Design Engineer | 24 | 8,000 | 192,000 |
| 2 | Power Electronics Engineer | 20 | 8,000 | 160,000 |
| 3 | Thermal Engineer | 18 | 6,500 | 117,000 |
| 4 | Embedded Software Engineer | 16 | 6,500 | 104,000 |
| 5 | Mechanical Engineer / Test | 14 | 6,000 | 84,000 |
| | **Subtotal Personnel** | **92** | | **657,000** |

*Rates based on EU Horizon Europe unit cost methodology. Senior Researcher rate EUR 8,000/PM for engineers with >5y experience and PhD/equivalent. Researcher rate EUR 6,000-6,500/PM for engineers with 2-5y experience.*

---

### 3.2 Equipment (Depreciation during project, or full cost if <EUR 15k)

| Item | Estimated Cost (EUR) | Justification |
|------|---------------------|---------------|
| Dynamometer test bench (up to 50 kW, torque/speed sensor, coupling) | 85,000 | Motor characterization, efficiency mapping |
| Power analyzer (Yokogawa WT5000 or equivalent, 6-channel) | 45,000 | Precision loss measurements, drive efficiency |
| Thermal imaging camera (FLIR A700, 640x480, with SW) | 18,000 | Winding/magnet thermal validation |
| Thermocouples + DAQ system (NI cDAQ + modules, 32ch) | 12,000 | Multi-point thermal measurement |
| PCB manufacturing tools (reflow oven, stencil printer, rework) | 8,500 | In-house PCB assembly for rapid iteration |
| 3D Printer (Bambu Lab X1C or equivalent, dual material) | 3,500 | Prototype housings, jigs, cooling duct prototypes |
| Oscilloscope (Keysight MSOX4054A, 4ch 500MHz) | 12,000 | Power electronics debug, EMI pre-compliance |
| LCR meter + impedance analyzer | 6,000 | Winding inductance/resistance characterization |
| **Subtotal Equipment** | **190,000** | |

*Note: Large items (dynamometer, power analyzer) — depreciation for 24 months claimed if asset life > project. Full cost if purchased specifically for project and no residual use (EIC Transition allows 100% if dedicated).*

---

### 3.3 Materials & Consumables

| Item | Quantity / Spec | Unit Cost | Total (EUR) | WP |
|------|----------------|-----------|-------------|-----|
| NdFeB magnets (N48UH, custom Halbach segments) | 25 kg across iterations | 120 EUR/kg + machining | 8,000 | WP2 |
| NdFeB magnets (final optimized geometry, N50SH) | 15 kg | 150 EUR/kg + coating | 5,500 | WP7 |
| Lamination steel NO20 (0.2mm, M235-20A) | 80 kg, laser-cut stator/rotor | 35 EUR/kg + cutting | 6,500 | WP2 |
| Lamination steel NO25 (0.25mm, M250-25A) | 40 kg (design comparison) | 30 EUR/kg + cutting | 3,000 | WP2 |
| SiC MOSFET modules (Wolfspeed C3M, 1200V/75A) | 8 sets (dev + spares) | 280 EUR/set | 2,240 | WP3 |
| GaN FETs (GaN Systems GS66516T, 650V/60A) | 6 sets | 180 EUR/set | 1,080 | WP3 |
| Gate driver ICs + isolated power supplies | 12 boards | 85 EUR/board | 1,020 | WP3 |
| DC-link capacitors (film, 800V) | 10 pcs | 45 EUR/pc | 450 | WP3 |
| Current sensors (LEM HTFS 200-P) | 8 pcs | 65 EUR/pc | 520 | WP3 |
| PCB fabrication (4-6 layer, multiple revisions) | 8 iterations x 5 boards | 350 EUR/iteration | 2,800 | WP3,WP5 |
| PCB assembly (PCBA, SMD components) | 4 iterations | 1,200 EUR/iteration | 4,800 | WP3,WP5 |
| Copper wire (litz wire, various gauges, class H) | 30 kg | 45 EUR/kg | 1,350 | WP2 |
| Slot insulation (Nomex 410, 0.25mm) | 20 m^2 | 25 EUR/m^2 | 500 | WP2 |
| Impregnation resin (thermal epoxy, Bectron TC) | 5 kg | 120 EUR/kg | 600 | WP2 |
| Heat pipes (custom length, 6-8mm dia) | 20 pcs | 35 EUR/pc | 700 | WP4 |
| Coolant (water-glycol 50/50, lab grade) | 40 L | 8 EUR/L | 320 | WP4 |
| Cold plates (CNC aluminum, custom channels) | 4 prototypes | 800 EUR/pc | 3,200 | WP4 |
| Thermal interface materials (pads, grease, gap fillers) | assorted | lump sum | 600 | WP4 |
| Microcontrollers (STM32H7 eval boards + custom boards) | 6 boards | 120 EUR/board | 720 | WP5 |
| FPGA dev boards (Xilinx Artix-7 or Lattice) | 2 boards | 450 EUR/board | 900 | WP5 |
| Connectors, fasteners, misc mechanical | lump sum | — | 2,500 | WP6 |
| Aluminum stock (housing machining) | 60 kg | 18 EUR/kg | 1,080 | WP6 |
| Bearings (ceramic hybrid, high-speed) | 8 sets | 180 EUR/set | 1,440 | WP6 |
| Shaft material + machining | 4 shafts | 350 EUR/pc | 1,400 | WP6 |
| Balancing weights, adhesives, misc | lump sum | — | 800 | WP6 |
| **Subtotal Materials/Consumables** | | | **52,020** | |

---

### 3.4 Subcontracting

| Service | Provider Type | Estimated Cost (EUR) | WP | Justification |
|---------|--------------|---------------------|-----|---------------|
| FEM simulation licenses (ANSYS Maxwell + Fluent, 24 months) | Software vendor | 36,000 | WP2,WP4 | EM + thermal co-simulation |
| COMSOL Multiphysics license (24 months, AC/DC + Heat Transfer) | Software vendor | 24,000 | WP2,WP4 | Cross-validation, multiphysics |
| JMAG or MotorCAD license (12 months) | Software vendor | 15,000 | WP2 | Specialized motor design tool |
| Cloud HPC compute (AWS/Azure, parametric sweeps) | Cloud provider | 8,000 | WP2,WP3 | Large-scale optimization runs |
| Custom Halbach magnet manufacturing | Specialist magnet supplier (e.g., Shin-Etsu, Arnold Magnetic) | 25,000 | WP2 | Precision-ground arc segments, magnetization fixture |
| Stator winding service (automated needle winding) | Electric motor winding shop | 18,000 | WP2 | Concentrated winding, 3 prototype iterations |
| PCBA service (power electronics boards, full BOM) | EMS provider (e.g., Eurocircuits, JLCPCB+) | 12,000 | WP3 | Complex multilayer power PCBs |
| EMC pre-compliance testing (conducted + radiated emissions) | Accredited EMC lab | 15,000 | WP7 | CISPR 25 / EN 55032, required for TRL 5+ |
| Vibration & shock testing | Environmental test lab | 10,000 | WP7 | IEC 60068, 3-axis vibration sweep + shock |
| Thermal cycling test (accelerated life) | Environmental test lab | 8,000 | WP7 | -40 to +150 C, 500 cycles |
| Rotor balancing (high-speed, G2.5 or better) | Precision balancing service | 4,000 | WP6 | Required for >20,000 RPM operation |
| **Subtotal Subcontracting** | | **175,000** | | |

*Note: EIC Transition caps subcontracting — should not exceed 30% of total direct costs. Check: 175k / (657k+190k+52k+175k+40k) = 175k/1,114k = 15.7%. Compliant.*

---

### 3.5 Travel & Dissemination

| Item | Details | Cost (EUR) |
|------|---------|------------|
| **ECPE Conference** (European Center for Power Electronics) | 2 persons x 1 trip, registration + travel + hotel | 5,000 |
| **EPE** (European Conference on Power Electronics and Applications) | 2 persons x 1 trip | 6,000 |
| **ICEM** (International Conference on Electrical Machines) | 2 persons x 1 trip | 6,000 |
| Project review meetings (Brussels or remote hybrid) | 2 reviews x 2 persons, travel | 4,000 |
| Partner/stakeholder visits | 4 visits, EU travel | 6,000 |
| Trade fair / demo event (e.g., Hannover Messe, SPS) | 1 event, small booth | 5,000 |
| Open Access publication fees | 3-4 journal papers (IEEE Trans. / MDPI Energies) | 6,000 |
| Workshop organization (dissemination event, M22) | Venue + catering | 2,000 |
| **Subtotal Travel & Dissemination** | | **40,000** |

---

### 3.6 Indirect Costs (25% flat rate on direct costs excl. subcontracting)

Per Horizon Europe rules: 25% flat rate applied to **eligible direct costs minus subcontracting**.

| Category | Amount (EUR) |
|----------|-------------|
| Personnel | 657,000 |
| Equipment | 190,000 |
| Materials/Consumables | 52,020 |
| Travel & Dissemination | 40,000 |
| **Total direct costs excl. subcontracting** | **939,020** |
| **Indirect costs (25%)** | **234,755** |

---

## 4. TOTAL BUDGET SUMMARY

| Cost Category | Amount (EUR) | % of Total |
|---------------|-------------|------------|
| A. Personnel | 657,000 | 27.5% |
| B. Equipment | 190,000 | 8.0% |
| C. Materials & Consumables | 52,020 | 2.2% |
| D. Subcontracting | 175,000 | 7.3% |
| E. Travel & Dissemination | 40,000 | 1.7% |
| F. Indirect Costs (25% flat rate) | 234,755 | 9.8% |
| | | |
| **TOTAL ELIGIBLE COSTS** | **1,348,775** | |
| **EU Contribution (100% for EIC Transition)** | **1,348,775** | |

**Budget utilization: 54% of EUR 2.5M ceiling. Conservative and defensible.**

*Remaining headroom (~EUR 1.15M) provides margin for scope expansion, additional prototypes, or partner inclusion in a consortium variant.*

---

## 5. BUDGET PER WORK PACKAGE

| Category | WP1 | WP2 | WP3 | WP4 | WP5 | WP6 | WP7 | TOTAL |
|----------|------|------|------|------|------|------|------|-------|
| Personnel | 52,750 | 137,500 | 120,500 | 82,500 | 73,500 | 73,250 | 117,000 | 657,000 |
| Equipment | - | 6,000 | 57,000 | 30,000 | 12,000 | 3,500 | 81,500 | 190,000 |
| Materials | - | 26,450 | 10,110 | 4,820 | 1,620 | 7,220 | 1,800 | 52,020 |
| Subcontracting | - | 80,000 | 20,000 | 24,000 | - | 4,000 | 47,000 | 175,000 |
| Travel | 8,000 | 6,000 | 4,000 | 4,000 | 2,000 | 2,000 | 14,000 | 40,000 |
| Indirect (25%)* | 15,188 | 43,988 | 47,875 | 30,330 | 22,280 | 19,993 | 55,103 | 234,755 |
| **WP TOTAL** | **75,938** | **299,938** | **259,485** | **175,650** | **111,400** | **109,963** | **316,403** | **1,348,775** |

*Indirect costs distributed proportionally to direct costs excl. subcontracting per WP.*

---

## 6. GANTT CHART DATA

```
AURORA X — 24-Month Timeline
=========================================================================
WP / Task                     M1  M2  M3  M4  M5  M6  M7  M8  M9  M10 M11 M12 M13 M14 M15 M16 M17 M18 M19 M20 M21 M22 M23 M24
=========================================================================
WP1: Management               ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███
  T1.1 Proj setup/reporting    ██  .   .   .   .   ██  .   .   .   .   .   ██  .   .   .   .   .   ██  .   .   .   .   .   ██
  T1.2 Risk management         ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██
  T1.3 IP management           .   .   .   .   .   .   .   .   .   .   .   ██  .   .   .   .   .   ██  .   .   .   .   .   ██

WP2: EM Design                 ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███
  T2.1 Topology selection      ██  ██  ██  ██
  T2.2 Analytical modeling     .   ██  ██  ██  ██
  T2.3 FEM optimization        .   .   .   ██  ██  ██  ██  ██  ██
  T2.4 Halbach array design    .   .   .   .   .   ██  ██  ██
  T2.5 Winding design          .   .   .   .   .   .   ██  ██  ██  ██
  T2.6 Final EM design         .   .   .   .   .   .   .   .   .   ██  ██  ██  ██  ██

WP3: Power Electronics         .   .   ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███
  T3.1 Inverter topology       .   .   ██  ██  ██  ██
  T3.2 SiC/GaN eval            .   .   .   ██  ██  ██  ██
  T3.3 Gate drive design       .   .   .   .   .   ██  ██  ██  ██
  T3.4 PCB layout & fab        .   .   .   .   .   .   .   ██  ██  ██  ██
  T3.5 Inverter prototype V1   .   .   .   .   .   .   .   .   .   ██  ██  ██
  T3.6 Inverter V2 (optimized) .   .   .   .   .   .   .   .   .   .   .   .   ██  ██  ██  ██  ██  ██

WP4: Thermal Management        .   .   .   ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███
  T4.1 Thermal modeling (CFD)  .   .   .   ██  ██  ██  ██  ██
  T4.2 Cooling concept sel.    .   .   .   .   .   ██  ██  ██
  T4.3 Heat pipe integration   .   .   .   .   .   .   .   ██  ██  ██  ██
  T4.4 Cold plate design       .   .   .   .   .   .   .   .   .   ██  ██  ██  ██
  T4.5 Thermal prototype       .   .   .   .   .   .   .   .   .   .   .   .   .   ██  ██  ██
  T4.6 Thermal validation      .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   ██  ██  ██  ██

WP5: Embedded Control          .   .   .   .   .   ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███
  T5.1 Control architecture    .   .   .   .   .   ██  ██  ██
  T5.2 FOC implementation      .   .   .   .   .   .   .   ██  ██  ██  ██
  T5.3 Sensorless algorithms   .   .   .   .   .   .   .   .   .   ██  ██  ██  ██
  T5.4 Functional safety (SW)  .   .   .   .   .   .   .   .   .   .   .   .   .   ██  ██  ██
  T5.5 HIL testing             .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   ██  ██  ██  ██
  T5.6 SW integration          .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   ██  ██  ██  ██

WP6: Mechanical & Prototyping  .   ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███
  T6.1 Housing design (CAD)    .   ██  ██  ██  ██
  T6.2 Rotor assembly design   .   .   .   ██  ██  ██
  T6.3 3D print prototypes     .   .   .   .   ██  ██  ██
  T6.4 CNC machining (V1)      .   .   .   .   .   .   ██  ██  ██
  T6.5 Rotor balancing         .   .   .   .   .   .   .   .   ██  ██
  T6.6 Final mechanical assy   .   .   .   .   .   .   .   .   .   .   ██  ██  ██  ██  ██  ██

WP7: Integration & Test        .   .   .   .   .   .   .   .   .   .   .   .   .   ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███
  T7.1 Motor assembly V1       .   .   .   .   .   .   .   .   .   .   .   .   .   ██  ██  ██
  T7.2 Dyno characterization   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   ██  ██  ██
  T7.3 Efficiency mapping      .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   ██  ██
  T7.4 EMC testing             .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   ██  ██
  T7.5 Environmental testing   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   ██  ██
  T7.6 Final validation        .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   ██  ██  ██  ██
=========================================================================

MILESTONES:        MS1(M4)   MS2(M9)        MS3(M14)       MS4(M18)       MS5(M22)     MS6(M24)
                     |         |               |              |              |             |
REVIEWS:                    Mid-term(M12)                              Final(M24)
```

---

## 7. MILESTONES

| ID | Title | Month | Verification |
|----|-------|-------|-------------|
| MS1 | EM topology selected, analytical model validated | M4 | Design review, model vs. published data <5% error |
| MS2 | FEM-optimized motor design frozen | M9 | FEM report, peer review of torque/efficiency targets |
| MS3 | First motor prototype assembled | M14 | Physical prototype, dimensional inspection report |
| MS4 | Integrated motor-inverter system operational | M18 | Dyno test: rated torque at rated speed achieved |
| MS5 | Full characterization & environmental tests complete | M22 | Test reports: efficiency map, EMC, vibration pass |
| MS6 | TRL 5/6 validation, exploitation plan finalized | M24 | Final report, TRL assessment, IP strategy document |

---

## 8. DELIVERABLES LIST

| ID | Title | WP | Type | Dissemination | Due |
|----|-------|----|------|---------------|-----|
| D1.1 | Project Management Plan | WP1 | Report | CO | M2 |
| D1.2 | Data Management Plan | WP1 | DMP | PU | M3 |
| D1.3 | Mid-term progress report | WP1 | Report | CO | M12 |
| D1.4 | Final report & exploitation plan | WP1 | Report | CO | M24 |
| D2.1 | Topology trade study & selection report | WP2 | Report | PU | M4 |
| D2.2 | Analytical motor model (MATLAB/Python) | WP2 | Software | CO | M5 |
| D2.3 | FEM optimization report (parametric study) | WP2 | Report | PU | M9 |
| D2.4 | Final EM design specification | WP2 | Report | CO | M12 |
| D2.5 | Journal paper: EM design methodology | WP2 | Publication | PU | M14 |
| D3.1 | Inverter topology trade study | WP3 | Report | CO | M6 |
| D3.2 | SiC/GaN benchmark results | WP3 | Report | PU | M8 |
| D3.3 | Inverter prototype V1 hardware | WP3 | Prototype | CO | M12 |
| D3.4 | Inverter V2 (optimized) hardware | WP3 | Prototype | CO | M18 |
| D3.5 | Conference paper: SiC/GaN comparison | WP3 | Publication | PU | M16 |
| D4.1 | Thermal model & CFD analysis report | WP4 | Report | CO | M8 |
| D4.2 | Cooling system design specification | WP4 | Report | CO | M13 |
| D4.3 | Thermal validation test report | WP4 | Report | PU | M20 |
| D5.1 | Control architecture document | WP5 | Report | CO | M8 |
| D5.2 | FOC + sensorless firmware (source code) | WP5 | Software | CO | M14 |
| D5.3 | HIL test results & safety analysis | WP5 | Report | CO | M20 |
| D5.4 | Conference paper: sensorless control | WP5 | Publication | PU | M22 |
| D6.1 | Mechanical design package (CAD files) | WP6 | Design | CO | M6 |
| D6.2 | Prototype housing + rotor assembly | WP6 | Prototype | CO | M14 |
| D7.1 | Motor assembly V1 — physical demonstrator | WP7 | Demonstrator | CO | M16 |
| D7.2 | Efficiency map & dyno characterization report | WP7 | Report | PU | M19 |
| D7.3 | EMC test report | WP7 | Report | CO | M20 |
| D7.4 | Environmental test report (vibration, thermal cycling) | WP7 | Report | CO | M22 |
| D7.5 | Final validation report & TRL assessment | WP7 | Report | PU | M24 |
| D7.6 | Journal paper: AURORA X system-level results | WP7 | Publication | PU | M24 |

**Dissemination levels:** PU = Public, CO = Confidential (consortium only)

---

## 9. RISK REGISTER (Top 5)

| # | Risk | Probability | Impact | Mitigation | WP |
|---|------|-------------|--------|------------|-----|
| R1 | Custom Halbach magnets fail dimensional tolerance | Medium | High | Pre-qualify 2 magnet suppliers, iterative prototyping | WP2 |
| R2 | SiC/GaN device failure at high switching frequency | Low | High | Extensive dV/dt testing, thermal derating, dual-source | WP3 |
| R3 | Thermal runaway at continuous rated power | Medium | Critical | Conservative 20% thermal margin, redundant cooling path | WP4 |
| R4 | Sensorless control instability at low speed | Medium | Medium | Fallback to HFI injection, pre-validated on HIL | WP5 |
| R5 | Schedule delay in magnet/lamination procurement | Medium | Medium | Order long-lead items by M3, maintain 6-week buffer | WP2,WP6 |

---

## 10. KEY PERFORMANCE INDICATORS (for reviewers)

| KPI | Target | Measured at |
|-----|--------|-------------|
| Continuous power density | > 5.5 kW/kg (active mass) | MS5 (M22) |
| Peak efficiency | > 97% at rated operating point | MS4 (M18) |
| Inverter efficiency | > 99% (SiC, rated load) | MS4 (M18) |
| Maximum speed | > 25,000 RPM | MS4 (M18) |
| Thermal: max winding temp at rated load | < 150 deg C (class H) | MS5 (M22) |
| TRL advancement | TRL 4 -> TRL 5 (minimum), target TRL 6 | MS6 (M24) |
| Publications | >= 3 peer-reviewed papers | M24 |
| Patent applications | >= 1 (Halbach + cooling concept) | M18 |

---

## 11. CASH FLOW SCHEDULE (Pre-financing)

EIC Transition provides pre-financing. Typical schedule:

| Payment | Timing | Amount (EUR) | % |
|---------|--------|-------------|---|
| Pre-financing | At Grant Agreement signature | 674,388 | 50% |
| Interim payment | After mid-term review (M12) | 404,633 | 30% |
| Final payment | After final review (M24+) | 269,755 | 20% |
| **Total** | | **1,348,775** | **100%** |

---

## APPENDIX: BUDGET COMPLIANCE CHECKS

| Rule | Limit | Actual | Status |
|------|-------|--------|--------|
| EIC Transition max grant | EUR 2,500,000 | EUR 1,348,775 | PASS (54%) |
| EU funding rate | 100% | 100% | PASS |
| Subcontracting cap (soft, ~30% of direct) | ~30% | 15.7% | PASS |
| Indirect costs | 25% flat rate | 25% applied | PASS |
| Duration | 12-36 months | 24 months | PASS |
| Personnel justification | Unit costs or actual | EU avg. unit costs | PASS |
