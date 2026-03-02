# Halbach Array Magnets: AURORA X Reference

## Quasi-Halbach vs Conventional Rotor

| Parameter | Conventional SPM | Quasi-Halbach | Improvement |
|---|---|---|---|
| Fundamental flux density B₁ | 0.85 T | 1.10-1.25 T | +30-47% |
| Back-iron flux | Full | Near-zero | Can eliminate back-iron |
| Cogging torque | Baseline | -70 to -87% | Dramatic reduction |
| THD of back-EMF | 8-12% | 2-5% | Smoother waveform |
| Eddy current losses | Baseline | -20 to -40% | Sinusoidal field |
| Rotor mass (no back-iron) | Baseline | -30 to -50% | Major weight saving |

## Magnet Grade Selection

| Grade | Br (T) | Hcj (kA/m) | T_max (°C) | Rationale |
|---|---|---|---|---|
| N52 | 1.44 | 876 | 60 | Too low temp |
| N48H | 1.40 | 1353 | 120 | Marginal |
| **N48SH** | **1.38** | **1592** | **150** | **Selected** |
| N45UH | 1.35 | 1990 | 180 | Overkill, lower Br |

**N48SH**: Best trade-off — high Br (1.38 T) with 150°C rating matching winding thermal limit.

## Slot/Pole Combinations for Dual 3-Phase

| Slots | Poles | Winding factor | LCM | Cogging | Notes |
|---|---|---|---|---|---|
| 12 | 10 | 0.933 | 60 | Medium | Common, simple |
| **18** | **20** | **0.945** | **180** | **Very low** | **Selected** |
| 24 | 20 | 0.933 | 120 | Low | Larger stator |
| 36 | 30 | 0.945 | 180 | Very low | Complex |

**18s/20p**: High winding factor, very low cogging (LCM=180), natural dual 3-phase (2×9 slots).

## Halbach Manufacturing Methods

| Method | Tolerance | Cost | Volume |
|---|---|---|---|
| Discrete segments (4-6/pole) | ±2° | Low | Any |
| Bonded ring (compression) | ±1° | Medium | >1000 |
| Sintered arc segments | ±0.5° | High | >5000 |

AURORA X approach: **4 segments/pole** (0°, 45°, 90°, 135°) — practical for prototype, 90% of ideal Halbach performance.

## Key References
- Z.Q. Zhu & D. Howe, "Halbach permanent magnet machines," IEEE Trans. on Magnetics, 2001
- K. Atallah et al., "Armature reaction field and winding inductances of slotless PM machines," IEEE, 1998
- EMRAX 228: Production Halbach-type motor, 5.8 kW/kg continuous
