# Thermal Design Summary: AURORA X

## Key Results

| Parameter | Value |
|---|---|
| Cooling method | Two-phase thermosyphon (water, 0.16 bar) |
| T_sat (boiling point) | 55°C |
| Evaporator area | 211 cm² |
| h_evap (enhanced surface) | 12,000 W/m²K |
| R_total (winding → coolant) | 0.22°C/W |
| T_winding,max (20 kW cont.) | 145°C (limit 150°C, margin 5°C) |
| T_magnet,max | 105°C (limit 120°C, margin 15°C) |
| T_inverter junction | 115°C (limit 175°C, margin 60°C) |
| Peak duration (30 kW) | 70s with EW spray cooling |
| Cooling system mass | 0.5-0.8 kg |
| Digital twin accuracy | ±5°C winding, ±10°C magnets |

## Cooling Comparison

| Method | R_total (°C/W) | Max Cont. Power | Added Mass |
|---|---|---|---|
| Air | 0.77 | 6 kW | 0 |
| Water jacket | 0.29 | 14 kW | 1.5-2.0 kg |
| **Two-phase** | **0.22** | **20 kW** | **0.5-0.8 kg** |

## Conclusion
Two-phase cooling is essential for 20 kW in 140mm OD envelope. Water jacket possible but less efficient. Air cooling fundamentally insufficient.
