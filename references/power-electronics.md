# SiC vs GaN Power Electronics for Motor Drives

## Comparison

| Parameter | SiC MOSFET | GaN HEMT |
|---|---|---|
| Voltage Range | 650V-2000V | 100V-650V |
| Switching Freq | 20-150 kHz (drives) | 100 kHz-1 MHz+ |
| Tj max | 175-200°C | 150°C (typ.) |
| Substrate Thermal Conductivity | ~490 W/(m·K) | ~130 W/(m·K) |
| RDS(on) drift at 150°C | +20% | +50-80% |
| Optimal Power Range | 10-500+ kW | 100W-20 kW |
| Cost ($/A at 650V) | $0.3-0.8/A | $0.5-1.5/A |
| Inverter Efficiency (10-50 kW) | 98.5-99.4% | 98-99%+ (<10 kW) |

**Conclusion for 10-50 kW:** SiC is the clear choice.

## Recommended SiC MOSFETs

### Wolfspeed Gen 3 (1200V)
| Part | RDS(on) | ID | Application |
|---|---|---|---|
| C3M0021120K | 21 mΩ | 100A | 30-50 kW |
| C3M0032120K | 32 mΩ | 63A | 15-30 kW |
| C3M0075120K | 75 mΩ | 33A | 10-15 kW |

### Infineon CoolSiC (1200V)
| Part | RDS(on) | Package |
|---|---|---|
| IMZ120R045M1H | 45 mΩ | TO-247-4 |
| IMZ120R140M1H | 140 mΩ | TO-247-4 |

### ROHM (650V)
| Part | RDS(on) | ID |
|---|---|---|
| SCT3030AL | 30 mΩ | 70A |
| SCT3060AL | 60 mΩ | 39A |

## 3-Level Topologies

| Vdc | Topology | Switches | Justification |
|---|---|---|---|
| 400V | 2-level | 650V SiC | Simple, sufficient |
| 400V | 3L-TNPC | 650V GaN + 400V GaN | Max efficiency, low EMI |
| 800V | 2-level | 1200V SiC | Standard EV approach |
| 800V | 3L-NPC | 650V SiC/GaN | Better EMI |
| 800V | 3L-TNPC | 1200V SiC + 650V SiC | Highest efficiency (99.4%) |

## Switching Frequency Impact on Motor

| Fsw | Iron Loss | Acoustic Noise | Switching Loss |
|---|---|---|---|
| 4-8 kHz (Si IGBT) | High harmonics | Audible whine | Low |
| 16-20 kHz (SiC) | -20-30% | At hearing threshold | Moderate |
| 40-80 kHz (SiC) | Minimal from ripple | Inaudible | Notable but manageable |
| 100-200 kHz (GaN) | Near zero from PWM | None | Only GaN handles |

Key fact: SiC at 40+ kHz vs Si IGBT at 8 kHz = **9 dB(A) noise reduction**.
