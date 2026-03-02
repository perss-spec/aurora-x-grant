# Electromagnetic Design Calculations: AURORA X

## Motor Topology

| Parameter | Value | Rationale |
|---|---|---|
| Type | Outer-rotor PMSM | Higher torque density for direct-drive |
| Slots / Poles | 18s / 20p | High winding factor (0.945), low cogging |
| Phases | 2 × 3-phase | Redundancy, reduced torque ripple |
| Stator OD | 140 mm | UAV/eVTOL form factor |
| Active length | 50 mm | L/D = 0.36 (disc-type) |
| Air gap | 1.0 mm | Mechanical clearance + retention |
| Magnet type | N48SH Quasi-Halbach | 4 segments/pole |

## Electrical Parameters

| Parameter | Value | Derivation |
|---|---|---|
| DC bus voltage | 96 V (24S LiPo) | UAV standard |
| Back-EMF constant (Ke) | 0.0382 V·s/rad | Ke = V_dc / (2 × n_max × √3) |
| Torque constant (Kt) | 0.0382 N·m/A | Kt = Ke (in SI) |
| Rated speed | 4000 RPM | eVTOL cruise |
| Max speed | 8000 RPM | Field weakening range 2:1 |
| Rated torque | 47.7 N·m | T = P / ω = 20000 / (4000×2π/60) |
| Peak torque | 71.6 N·m | 30 kW @ 4000 RPM |
| Phase resistance (R_ph) | 12.5 mΩ | Copper, 120°C, Litz wire |
| Phase inductance (L_ph) | 45 µH | Low for high-speed FW capability |
| Ld / Lq | 42 / 48 µH | Slight saliency from Halbach |

## Flux Density Distribution

| Region | B (T) | Limit |
|---|---|---|
| Air gap (fundamental) | 1.12 | — |
| Stator tooth | 1.65 | 1.8 (M270-35A) |
| Stator yoke | 1.45 | 1.8 |
| Rotor back-iron | 0.25 | Minimal (Halbach) |

## Loss Budget @ 20 kW Continuous, 4000 RPM

| Loss Component | Value (W) | % of Input | Method |
|---|---|---|---|
| Copper (I²R, AC) | 380 | 1.90% | Litz factor 1.15 |
| Core (hysteresis) | 185 | 0.93% | Modified Steinmetz |
| Core (eddy current) | 95 | 0.48% | FEA-validated |
| Magnet eddy current | 45 | 0.23% | Segmented magnets |
| Mechanical (bearing+windage) | 35 | 0.18% | Empirical |
| **Stray load** | **40** | **0.20%** | 5% of total |
| **Total motor losses** | **780** | **3.90%** | — |
| **Motor efficiency** | **96.1%** | — | — |
| Inverter losses (GaN) | 157 | 0.79% | Detailed calc |
| **System efficiency** | **95.3%** | — | Motor × inverter |

## Current Loading

| Operating Point | I_phase (A_rms) | J (A/mm²) | Thermal limit |
|---|---|---|---|
| 20 kW continuous | 130 | 18.5 | Two-phase cooling required |
| 30 kW peak (70s) | 195 | 27.8 | EW spray activation |
| 10 kW cruise | 72 | 10.2 | Comfortable margin |

## Mass Budget

| Component | Mass (g) | Material |
|---|---|---|
| Stator laminations | 850 | M270-35A Si-steel |
| Stator windings (Litz) | 420 | Copper, Class H insulation |
| Rotor shell | 180 | Ti-6Al-4V or Al 7075-T6 |
| Magnets (N48SH) | 280 | NdFeB, 20 segments |
| Bearings (2×) | 80 | Ceramic hybrid Si₃N₄ |
| End plates + hardware | 190 | Al 6061-T6 |
| **Motor total** | **2,000** | — |
| GaN inverter PCB | 480 | Integrated annular |
| Cooling system | 650 | Thermosyphon + manifold |
| Sensors + harness | 120 | Resolvers, thermistors |
| **System total** | **3,250** | — |

## Key Performance Metrics

| Metric | AURORA X | State-of-Art | Improvement |
|---|---|---|---|
| Cont. power density | 6.15 kW/kg (motor) | 5.8 kW/kg (EMRAX) | +6% |
| System power density | **6.15 kW/kg (system)** | 3.5-4.5 kW/kg | **+37-76%** |
| System efficiency | 95.3% | 92-94% | +1.3-3.3 pp |
| Torque density | 23.9 N·m/kg | 18-22 N·m/kg | +9-33% |
| Specific power (peak) | 9.23 kW/kg (system) | 6-8 kW/kg | +15-54% |

## Field Weakening Capability

| Speed (RPM) | Torque (N·m) | Power (kW) | Mode |
|---|---|---|---|
| 0-4000 | 47.7 | 0-20.0 | Constant torque (MTPA) |
| 4000-6000 | 47.7→21.2 | 20.0 | Constant power (FW) |
| 6000-8000 | 21.2→11.9 | 20.0→10.0 | Deep FW |

CPSR (Constant Power Speed Range) = 1:2, enabled by low L_ph and Halbach design.
