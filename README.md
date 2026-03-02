# AURORA X — Smart Integrated Coaxial E-Propulsion Core

**Grant Application: EIC Transition (Horizon Europe)**

## Overview

AURORA X is a next-generation integrated electric propulsion system combining:
- **Dual-Channel Coaxial PMSM** — hardware redundancy via two independent electromagnetic channels
- **In-Motor SiC/GaN Inverter** — eliminating external ESC, cables, and connectors
- **Two-Phase Cooling Core** — internal heat pipes with phase-change thermal management
- **Low-Harmonics Magnetics** — Quasi-Halbach profiled magnets for minimal cogging and vibration

**Target:** 20 kW continuous / 30 kW peak, ≥5.0 kW/kg, ≥95% efficiency, TRL 5-6

## Repository Structure

```
aurora-x-grant/
├── doc/                    # Final assembled proposal
│   └── part-b.md           # Part B: Technical Description
├── src/
│   ├── sections/           # Individual proposal sections
│   │   ├── 01-excellence.md
│   │   ├── 02-impact.md
│   │   └── 03-implementation.md
│   ├── figures/            # Diagrams, charts, infographics
│   ├── tables/             # Data tables (CSV/MD)
│   └── calculations/       # Engineering calculations (Python)
├── templates/              # EU grant format templates
├── references/             # Bibliography and sources
└── assets/                 # Raw images, logos
```

## Key Specifications

| Parameter | Target | Verification |
|---|---|---|
| Power Density | ≥ 5.0 kW/kg | Dyno test |
| Efficiency | ≥ 95% in operating zone | Efficiency map |
| Winding Temperature | ≤ 150°C (Class H) | Thermocouples |
| Torque Ripple | ≤ 3% | Torque sensor |
| Demagnetization Margin | ≥ 20% @ Peak Current | Simulation + test |

## Project Timeline

24 months, 6 Work Packages (WP1-WP6), TRL 3-4 → TRL 5-6

## Budget

EIC Transition: up to €2.5M, 100% funding rate
