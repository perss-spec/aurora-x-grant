# Two-Phase Cooling for Electric Motors

## Key Performance Data

### Heat Flux Density Comparison

| Method | Heat Flux (W/cm²) |
|---|---|
| Forced air | 0.5-2 |
| Water jacket | 5-15 |
| Oil spray | 10-30 |
| Two-phase pool boiling | 20-50 |
| Two-phase flow boiling (microchannels) | 50-275 |
| Two-phase porous evaporator | >300 |

### Current Density (Continuous)

| Cooling Method | J (A/mm²) | Notes |
|---|---|---|
| Air | 3-6 | Standard IC411/IC416 |
| Water jacket | 10-18 | EV standard (BMW i3 ~14.6) |
| Oil spray (direct) | 15-25 | +20% vs water jacket |
| Two-phase evaporative | **26-30+** | Georgia Tech: 26, Purdue AM: 30.4 |

### Motor Power Density by Cooling

| Cooling | Cont. kW/kg | Peak kW/kg |
|---|---|---|
| Air | 1-2 | 3-5 |
| Water jacket | 3-5 | 8-12 |
| Direct oil | 5-8 | 10-15 |
| Two-phase (ASCEND target) | **≥12** | >20 |

## Thermal Resistance Comparison

| Method | R_th (°C/W) | h (W/m²K) |
|---|---|---|
| Forced air | 2-8 | 20-100 |
| Water jacket | 0.5-2.0 | 500-3000 |
| Oil spray | 0.2-0.8 | 1000-5000 |
| DWHX | 0.1-0.4 | 2000-8000 |
| Two-phase embedded | **0.05-0.2** | 2000-9000 |
| Two-phase flow boiling | **0.02-0.1** | 5000-50000 |

## Coolant Selection

| Coolant | Tboil (°C, 1 atm) | Latent Heat (kJ/kg) | Dielectric | GWP |
|---|---|---|---|---|
| Water (sub-atm) | 100 (34 at 5 kPa) | 2257 | No | 0 |
| Novec 649 | 49 | 88 | >40 kV | **1** |
| Novec 7100 | 61 | 112 | >25 kV | 300 |
| Novec 7200 | 76 | 119 | High | 55 |
| R245fa | 15 | 196 | Medium | 1030 |
| R1233zd(E) | 18 | 195 | Medium | **1** |

**Recommended:** Novec 7100 for immersion, R1233zd(E) for loop cooling.

## Challenges in Rotating Systems

- Centrifugal force disrupts capillary return → evaporator dryout
- At 2000 RPM: R_th increases from 0.114 to 0.43°C/W (+277%)
- **Solution:** Embedded stator cooling (not rotating) + wickless RHP for rotor
- Stator-embedded approach: independent of RPM, limited only by vibration

## Key Research Groups

| Institution | Focus | Key Results |
|---|---|---|
| Georgia Tech | Embedded evaporative, PDMS wick | 26 A/mm², closed two-phase loop |
| Purdue (CTRC) | AM stator + microchannels | 30.4 A/mm² continuous |
| NREL | Thermal benchmarking | 80% R_th reduction with direct cooling |
| Texas A&M | ASCEND program | Aviation-class thermal management |
| Fraunhofer | AM stators with cooling channels | Additive manufacturing prototypes |

## ARPA-E ASCEND Program

- Budget: $33M
- Target: ≥12 kW/kg, ≥93% efficiency
- Prototype ≥250 kW in Phase 2
- Validates relevance of two-phase cooling for aviation
