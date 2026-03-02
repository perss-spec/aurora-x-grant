# AURORA X: In-Motor GaN Inverter — Design Calculations

## Design Point

| Parameter | Value |
|---|---|
| Continuous power | 20 kW (10 kW/channel) |
| Peak power | 30 kW (15 kW/channel) |
| DC bus | 96V nominal |
| Channels | 2x independent 3-phase |
| Phase current | 104A RMS continuous / 156A peak per channel |
| Switching frequency | 80 kHz |
| Diameter constraint | 120-150 mm |
| Ambient (inside motor) | up to 100°C |

## Topology: 2-Level Inverter

96V bus is too low for 3-level benefits. 2-level with GaN at 100V exploits optimal FOM.

## Switch Selection: EPC2302 (100V GaN, 1.8 mΩ)

2x parallel per position → effective Rds(on) @125°C: 1.6 mΩ. Total 24 FETs.

## Loss Breakdown (Continuous, Both Channels)

| Component | Loss (W) |
|---|---|
| Conduction | 103.6 |
| Switching | 37.6 |
| Dead-time | 15.8 |
| Gate drive | 0.3 |
| **Total** | **157.3** |

## Efficiency

- Continuous: **99.22%**
- Peak: **98.97%**

## DC Link: 80x MLCC + 4x film (hybrid)

Ripple current: ~88A RMS. Effective capacitance: ~120 µF per channel.

## Gate Drivers: TI LMG1210 (x6)

5V GaN-specific, 150 V/ns CMTI, integrated bootstrap.

## EMI: Nanocrystalline CM choke + Y-caps

Meets DO-160G / EN 55032 Class B.

## PCB: Annular Ø140/50mm, 6-layer, high-Tg FR4

Total component height: ~12 mm. CM filter adds ~25 mm axially.

## Mass Summary

| Assembly | Mass |
|---|---|
| 2x channel power stages | 210g |
| CM filter | 150g |
| DC filter + connectors | 50g |
| MCU board | 30g |
| TIM + hardware | 40g |
| **Total** | **~480g** |

## Thermal: Tj = 119°C (margin 31°C to limit)

Requires liquid-cooled motor housing (shared with motor cooling).
