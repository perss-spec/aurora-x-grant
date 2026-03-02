# State of the Art: BLDC/PMSM Motors for UAV/eVTOL

## Comparison Table

| # | Manufacturer / Model | Type | Peak kW | Cont. kW | Mass kg | Peak kW/kg | Cont. kW/kg | Eff. % | Max RPM | Voltage V | Cooling | Integrated Inverter |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | EMRAX 188 | Axial flux | 60 | 27-37 | 7.1-7.9 | 8.1 | 4.7 | 96 | 8000 | 50-660 | Air/Liquid/Combined | No |
| 2 | EMRAX 228 | Axial flux | 124 | 75 | 12.9-13.5 | 9.6 | 5.8 | 96 | 6500 | 50-830 | Air/Liquid/Combined | No |
| 3 | EMRAX 268 | Axial flux | 210 | 117 | 21.4-22.3 | 9.8 | 5.5 | 96 | 4500 | 100-830 | Air/Liquid/Combined | No |
| 4 | EMRAX 348 | Axial flux | 340-380 | 68-103 | 41-42 | 8.3 | 2.4 | 96 | 4000 | up to 800 | Air/Liquid/Combined | No |
| 5 | T-Motor U15 II | Outrunner BLDC | 8.6 | ~4 | 1.64 | 5.2 | ~2.4 | ~88 | ~2500 | 44-100 | Air | No |
| 6 | T-Motor U13 II | Outrunner BLDC | ~5 | ~2.5 | 1.3 | 3.8 | ~1.9 | ~88 | ~3000 | 44-100 | Air | No |
| 7 | H3X HPDM-250 | Radial PMSM + inv | 250 | 200 | 18.7 | 13.4 | 10.7 | 96.7/92.9 | — | up to 800 | Liquid | Yes (SiC) |
| 8 | Joby Aviation | PMSM (dual winding) | 236 | — | — | — | — | — | — | — | Liquid | Yes (dual redundant) |
| 9 | Siemens SP260D | PMSM | 261 | 260 | 50 | 5.2 | 5.2 | 95 | 2500 | — | Liquid | No |
| 10 | Safran ENGINeUS 100 | PMSM | 125 | — | ~25 | 5.0 | — | — | — | — | Air | Yes |
| 11 | Wright WM2500 | PMSM | 2500 | — | 156 | 16.0 | — | 96 | 7500 | — | Liquid | Yes (8x inv) |
| 12 | Evolito D250 | Axial flux | 240 | — | 13 | 18.5 | — | — | — | — | — | No |
| 13 | Plettenberg NOVA 150 | Inrunner BLDC | 150 | — | 11.5 | 13.0 | — | 95 | — | — | Liquid | No |
| 14 | Magnax (Axyal) | Yokeless axial | 200 | — | 16 | 15.0 | — | 98 | — | — | Liquid | No |
| 15 | YASA (Oct 2025 record) | Axial flux | 750 | 350-400 | 12.7 | 59.0 | ~30 | — | — | — | Adv. thermal | No |

## World Records (Peak Power Density)

| Date | Who | Peak kW | Mass kg | kW/kg | Notes |
|---|---|---|---|---|---|
| Oct 2025 | YASA | 750 | 12.7 | 59.0 | Prototype, automotive |
| Jul 2025 | YASA | 550 | 13.1 | 42.0 | Previous record |
| 2024 | H3X HPDM-250 | 250 | 18.7 | 13.4 | Production, integrated |
| 2023 | Evolito D250 | 240 | 13 | 18.5 | Aviation-grade |
| 2021 | Wright WM2500 | 2500 | 156 | 16.0 | Megawatt-class aviation |

## 10-50 kW Class Typical Specs

| Parameter | Typical Range |
|---|---|
| Peak Power | 10-50 kW |
| Continuous Power | 60-70% of peak |
| Mass | 1.5-8 kg |
| Power Density (peak) | 4-10 kW/kg |
| Efficiency | 88-96% |
| Voltage | 48-120V (12-24S LiPo) |
| RPM | 2000-8000 |
| Cooling | Primarily air |

## Integration Trend

| Company | Approach |
|---|---|
| H3X HPDM-250 | Full integration (motor + SiC inverter + planetary gear) |
| Joby Aviation | Dual redundant inverters in motor |
| Wright WM2500 | 8 integrated inverters @ 250 kW each |
| Safran ENGINeUS | Power electronics built into air-cooled motor (EASA certified Feb 2025) |

## Cooling Methods Comparison

| Method | Heat Removal | Added Mass | Application | Impact on kW/kg |
|---|---|---|---|---|
| Air (passive) | Low | None | Small UAV <20 kW | Baseline |
| Air (forced) | Medium | Minimal | UAV in flight | +20-30% continuous |
| Water jacket | High | +2-5 kg | eVTOL 50+ kW | +50-100% continuous |
| Oil spray | Very high | +1-3 kg | Automotive, aviation | -25% winding temp vs water |
| Combined | High | +1-3 kg | EMRAX, mid-range | Optimal balance |
