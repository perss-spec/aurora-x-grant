# FOC & Digital Twin for PMSM Control

## FOC Strategies

| Strategy | Benefit | When to Use |
|---|---|---|
| Standard FOC (id=0) | Simple | SPMSM at base speed |
| MTPA | -10-15% copper losses | IPMSM, all speeds |
| Field Weakening | Extended speed range | Above base speed |
| Loss Minimization (LMC) | Min total losses (Cu+Fe) | High speed, light load |
| MPC | Optimal multi-objective | High-performance drives |

## Online Parameter Identification

| Method | Principle | Strengths | Weaknesses |
|---|---|---|---|
| MRAS | Model reference adaptive | Robust, fast, low compute | Sensitive to rotor position error |
| EKF | Extended Kalman Filter | Joint state/param estimation | O(n³), tuning Q/R matrices |
| HFI | High frequency injection | Works at zero speed | Acoustic noise, torque ripple |
| RLS | Recursive least squares | Fast convergence | Numerical stability issues |
| STA-SMO | Super-twisting sliding mode | Robust to parameters, no chattering | Needs medium+ speed |

**Trend:** Hybrid observers (HFI at low speed + EMF-based at medium/high) with smooth handover.

## Digital Twin Architecture

Three coupled models:
1. **Electromagnetic:** dq model with saturation, flux maps, loss models
2. **Thermal:** LPTN (4-8 nodes) + Kalman Filter, updated at 1-10 Hz
3. **Mechanical:** Inertia, friction, bearing aging

## Predictive vs Reactive Derating

| Parameter | Reactive (PI/threshold) | Predictive (MPC) |
|---|---|---|
| Overload capacity usage | Conservative (10-20°C margin) | Full (operates at Tmax boundary) |
| Peak torque | Baseline | **+64.3%** (DNMPC) |
| Energy efficiency | Baseline | **+6.2%** (RNN-MPC) |
| Smoothness | Step limiting | Smooth predictive |

## Current Loop Bandwidth with WBG

| Technology | fsw | Current BW | Notes |
|---|---|---|---|
| Si IGBT | 8-20 kHz | 1-2 kHz | Standard |
| SiC MOSFET | 20-100 kHz | 5-15 kHz | 90% reduction in switching losses vs Si |
| GaN HEMT | 100 kHz-1 MHz | 10-50 kHz | Optimal for <10 kW |

## Control Loop Frequencies

| Loop | Frequency | Rationale |
|---|---|---|
| Current (id, iq) | 20-40 kHz (SiC: up to 100 kHz) | = fsw |
| Speed/position | 1-5 kHz | 1/10 of current loop |
| Flux observer | = current loop | Synchronous with current |
| Thermal observer | 1-10 Hz | Thermal time constants: seconds-minutes |
| Fault detection | = current loop (HW) | < FTTI |
| Telemetry (CAN) | 10-100 Hz | Bus bandwidth limit |

## Redundancy Management

### Fault Detection Times

| Fault Type | Detection Method | Time |
|---|---|---|
| Open-phase | Current amplitude/phase monitoring | 1-5 ms |
| Open-switch | Current waveform analysis | 0.5-2 ms |
| Short circuit | dI/dt monitoring | <100 µs (HW) |
| Demagnetization | Back-EMF deviation | 10-100 ms |

### Applicable Standards

| Standard | Domain | Key Requirements |
|---|---|---|
| ISO 26262 | Automotive | ASIL A-D, SPFM >97% (ASIL-D) |
| DO-178C | Aviation SW | DAL A-E, MC/DC coverage |
| DO-254 | Aviation HW/FPGA | Design assurance |
| DO-160G | Aviation environment | EMI/EMC, temperature |
| ARP4754A | Aviation system | FHA, FMEA, <10⁻⁹/h catastrophic |

## Implementation Platforms

| Platform | Core | Key Feature |
|---|---|---|
| STM32G4 | Cortex-M4F @170MHz | CORDIC, FMAC, cost-effective |
| TI C2000 F28388D | Dual C28x @200MHz | CLA for parallel observers |
| STM32H7 | Cortex-M7 @480MHz | DT + MPC capable |
| NXP S32K3 | Cortex-M7 + lockstep | ASIL-D ready |
| Infineon AURIX TC3xx | TriCore @300MHz | ISO 26262 ASIL-D certified |

## Key Academic Groups

| Group | Focus |
|---|---|
| Uni Paderborn/Siegen (DE) | LPTN, data-driven thermal, MPC derating (Prof. Wallscheid) |
| ETH Zurich PES (CH) | High-perf drives, SiC/GaN, MPC (Prof. Kolar) |
| TU Munich (DE) | Automotive drives, digital twin |
| Aalborg (DK) | PE reliability, thermal DT (Prof. Blaabjerg) |
| U. Nottingham (UK) | High-speed PMSM, fault-tolerant, aerospace (Prof. Gerada) |
| Politecnico di Torino (IT) | EV drives, MTPA, sensorless |
