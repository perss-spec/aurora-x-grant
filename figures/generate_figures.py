"""
AURORA X Grant Proposal — Figure Generation
Generates all charts and infographics for Part B document.
Run: python generate_figures.py
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

OUT = os.path.dirname(os.path.abspath(__file__))
BLUE = '#1565C0'
DARK = '#0D47A1'
ORANGE = '#FF6F00'
GREEN = '#2E7D32'
RED = '#C62828'
GRAY = '#616161'
LIGHT_BLUE = '#BBDEFB'
LIGHT_GREEN = '#C8E6C9'
LIGHT_ORANGE = '#FFE0B2'

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'figure.dpi': 200,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.15,
})


def fig1_system_architecture():
    """4-pillar architecture overview."""
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # Title
    ax.text(6, 6.6, 'AURORA X — Integrated E-Propulsion Architecture',
            ha='center', va='top', fontsize=16, fontweight='bold', color=DARK)

    # Central circle
    circle = plt.Circle((6, 3.5), 1.2, color=BLUE, alpha=0.15, ec=BLUE, lw=2)
    ax.add_patch(circle)
    ax.text(6, 3.7, 'AURORA X', ha='center', fontsize=13, fontweight='bold', color=DARK)
    ax.text(6, 3.2, '20 kW / 3.25 kg', ha='center', fontsize=10, color=GRAY)
    ax.text(6, 2.8, '6.15 kW/kg', ha='center', fontsize=11, fontweight='bold', color=ORANGE)

    pillars = [
        (1.8, 5.2, 'Pillar 1', 'Dual-Channel\nPMSM', '18s/20p, 96.1% eff\n2×3-phase, 2.0 kg', BLUE),
        (10.2, 5.2, 'Pillar 2', 'GaN Inverter\n(In-Motor)', 'EPC2302, 99.2% eff\n80 kHz, 480 g', GREEN),
        (1.8, 1.8, 'Pillar 3', 'Two-Phase\nCooling', 'Water @ 55°C\nR=0.22°C/W, 650 g', RED),
        (10.2, 1.8, 'Pillar 4', 'Quasi-Halbach\nMagnetics', 'N48SH, +40% flux\n-87% cogging', ORANGE),
    ]

    for x, y, label, title, desc, color in pillars:
        box = FancyBboxPatch((x-1.5, y-0.9), 3.0, 1.8,
                             boxstyle="round,pad=0.1", fc=color, alpha=0.1, ec=color, lw=2)
        ax.add_patch(box)
        ax.text(x, y+0.55, label, ha='center', fontsize=9, color=color, fontweight='bold')
        ax.text(x, y+0.15, title, ha='center', fontsize=11, fontweight='bold', color='black')
        ax.text(x, y-0.45, desc, ha='center', fontsize=9, color=GRAY)

        # Arrow to center
        dx = 6 - x
        dy = 3.5 - y
        dist = np.sqrt(dx**2 + dy**2)
        ax.annotate('', xy=(6 - 1.3*dx/dist, 3.5 - 1.3*dy/dist),
                     xytext=(x + 1.6*dx/dist, y + 1.0*dy/dist),
                     arrowprops=dict(arrowstyle='->', color=color, lw=1.5, alpha=0.6))

    fig.savefig(os.path.join(OUT, 'fig1_architecture.png'))
    plt.close()
    print('✓ fig1_architecture.png')


def fig2_benchmarking():
    """Power density comparison spider/bar chart."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Bar chart: continuous power density
    motors = ['AURORA X\n(target)', 'EMRAX\n228', 'T-Motor\nU15 II', 'Safran\nENGINeUS', 'H3X\nHPDM-250']
    cont_pd = [5.9, 5.8, 3.2, 3.5, 10.7]
    colors = [ORANGE, BLUE, BLUE, BLUE, BLUE]
    bars = ax1.bar(motors, cont_pd, color=colors, alpha=0.85, edgecolor='white', lw=1.5)
    ax1.set_ylabel('Continuous Power Density (kW/kg)')
    ax1.set_title('Motor Power Density Comparison')
    ax1.set_ylim(0, 13)
    for bar, val in zip(bars, cont_pd):
        ax1.text(bar.get_x() + bar.get_width()/2, val + 0.2, f'{val}',
                ha='center', fontweight='bold', fontsize=10)
    ax1.axhline(y=5.0, color=RED, ls='--', alpha=0.5, lw=1)
    ax1.text(4.5, 5.2, 'Certified SOTA', color=RED, fontsize=9, ha='right')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    # System efficiency comparison
    systems = ['AURORA X', 'Conventional\n(Air+IGBT)', 'Water+SiC', 'Best eVTOL\n(est.)']
    eff = [94.7, 88.0, 93.5, 94.0]
    colors2 = [ORANGE, GRAY, BLUE, GREEN]
    bars2 = ax2.barh(systems, eff, color=colors2, alpha=0.85, edgecolor='white', lw=1.5)
    ax2.set_xlabel('System Efficiency (%)')
    ax2.set_title('System Efficiency (Motor × Inverter)')
    ax2.set_xlim(85, 97)
    for bar, val in zip(bars2, eff):
        ax2.text(val + 0.15, bar.get_y() + bar.get_height()/2, f'{val}%',
                va='center', fontweight='bold', fontsize=10)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    fig.tight_layout(pad=2)
    fig.savefig(os.path.join(OUT, 'fig2_benchmarking.png'))
    plt.close()
    print('✓ fig2_benchmarking.png')


def fig3_loss_budget():
    """Loss breakdown pie charts for motor and system."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    # Motor losses
    labels1 = ['Copper (AC)\n583 W', 'Iron\n(core)\n161 W', 'Magnet\neddy\n209 W', 'Mechanical\n2 W']
    sizes1 = [583, 161, 209, 2]
    colors1 = [ORANGE, BLUE, GREEN, GRAY]
    wedges1, texts1, autotexts1 = ax1.pie(sizes1, labels=labels1, autopct='%1.0f%%',
        colors=colors1, startangle=90, pctdistance=0.75, textprops={'fontsize': 9})
    for t in autotexts1:
        t.set_fontsize(9)
        t.set_fontweight('bold')
    ax1.set_title(f'Motor Losses @ 20 kW\nTotal: 955 W (η = 95.4%)')

    # System losses
    labels2 = ['Motor\n955 W', 'GaN Inverter\n157 W']
    sizes2 = [955, 157]
    colors2 = [BLUE, GREEN]
    wedges2, texts2, autotexts2 = ax2.pie(sizes2, labels=labels2, autopct='%1.0f%%',
        colors=colors2, startangle=90, pctdistance=0.7, textprops={'fontsize': 11})
    for t in autotexts2:
        t.set_fontsize(11)
        t.set_fontweight('bold')
    ax2.set_title(f'System Loss Split\nTotal: 1,112 W (η = 94.7%)')

    fig.tight_layout(pad=2)
    fig.savefig(os.path.join(OUT, 'fig3_loss_budget.png'))
    plt.close()
    print('✓ fig3_loss_budget.png')


def fig4_thermal_comparison():
    """Cooling method comparison."""
    fig, ax = plt.subplots(figsize=(10, 6))

    methods = ['Air Cooling', 'Water Jacket', 'AURORA X\nTwo-Phase']
    r_total = [0.77, 0.29, 0.22]
    max_power = [6, 14, 20]
    mass = [0, 1.75, 0.65]

    x = np.arange(len(methods))
    w = 0.25

    b1 = ax.bar(x - w, [r*20 for r in r_total], w, label='R_total (°C/W × 20)', color=RED, alpha=0.8)
    b2 = ax.bar(x, max_power, w, label='Max Cont. Power (kW)', color=BLUE, alpha=0.8)
    b3 = ax.bar(x + w, [m*10 for m in mass], w, label='Added Mass (kg × 10)', color=GRAY, alpha=0.8)

    ax.set_xticks(x)
    ax.set_xticklabels(methods, fontsize=12)
    ax.set_title('Cooling Method Comparison (140 mm OD envelope)')
    ax.legend(loc='upper left')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Annotations
    for i, (r, p, m) in enumerate(zip(r_total, max_power, mass)):
        ax.text(i - w, r*20 + 0.3, f'{r}°C/W', ha='center', fontsize=9, fontweight='bold')
        ax.text(i, p + 0.3, f'{p} kW', ha='center', fontsize=9, fontweight='bold')
        ax.text(i + w, m*10 + 0.3, f'{m} kg', ha='center', fontsize=9, fontweight='bold')

    fig.savefig(os.path.join(OUT, 'fig4_thermal.png'))
    plt.close()
    print('✓ fig4_thermal.png')


def fig5_mass_budget():
    """System mass breakdown."""
    fig, ax = plt.subplots(figsize=(8, 8))

    labels = [
        'Stator laminations\n1,179 g',
        'Copper windings\n779 g',
        'Insulation\n78 g',
        'Magnets (N48SH)\n468 g',
        'Rotor back-iron\n520 g',
        'Shaft (Ti)\n30 g',
        'Housing (Al)\n254 g',
        'Bearings\n30 g',
        'Misc (encoder etc)\n50 g',
    ]
    sizes = [1179, 779, 78, 468, 520, 30, 254, 30, 50]
    colors = [
        '#1565C0', '#1976D2', '#1E88E5',  # stator group (blues)
        '#E65100', '#EF6C00',               # rotor group (oranges)
        '#9E9E9E',                           # mechanical
        '#2E7D32',                           # inverter
        '#C62828',                           # cooling
        '#6A1B9A',                           # sensors
    ]

    wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%',
        colors=colors, startangle=90, pctdistance=0.8, labeldistance=1.15,
        textprops={'fontsize': 9})
    for t in autotexts:
        t.set_fontsize(8)
        t.set_fontweight('bold')
        t.set_color('white')

    ax.set_title(f'AURORA X Motor Mass Budget\nTotal: 3,390 g → 5.9 kW/kg (continuous)', fontsize=14)

    fig.savefig(os.path.join(OUT, 'fig5_mass_budget.png'))
    plt.close()
    print('✓ fig5_mass_budget.png')


def fig6_gantt():
    """Project Gantt chart — 24 months, 6 WPs."""
    fig, ax = plt.subplots(figsize=(14, 6))

    wps = [
        ('WP1: EM Design & Simulation', 1, 8, BLUE),
        ('WP2: GaN Inverter Design', 3, 10, GREEN),
        ('WP3: Thermal System', 4, 11, RED),
        ('WP4: Prototype Build', 9, 18, ORANGE),
        ('WP5: Testing & Validation', 15, 23, '#6A1B9A'),
        ('WP6: Management & Dissemination', 1, 24, GRAY),
    ]

    milestones = [
        (6, 'MS1: Design\nFreeze', BLUE),
        (12, 'MS2: Inverter\nPrototype', GREEN),
        (14, 'MS3: Cooling\nValidated', RED),
        (18, 'MS4: Motor\nAssembled', ORANGE),
        (21, 'MS5: Full System\nTest', '#6A1B9A'),
        (24, 'MS6: Final\nReview', DARK),
    ]

    for i, (name, start, end, color) in enumerate(wps):
        y = len(wps) - i
        ax.barh(y, end - start + 1, left=start - 0.5, height=0.6,
                color=color, alpha=0.7, edgecolor='white', lw=1.5)
        ax.text(start - 1, y, name, ha='right', va='center', fontsize=10, fontweight='bold')

    for month, label, color in milestones:
        ax.axvline(x=month, color=color, ls=':', alpha=0.4, lw=1)
        ax.plot(month, 0.3, 'D', color=color, markersize=8, zorder=5)
        ax.text(month, -0.3, label, ha='center', va='top', fontsize=7.5, color=color, fontweight='bold')

    ax.set_xlim(0, 25.5)
    ax.set_ylim(-1.2, len(wps) + 1)
    ax.set_xlabel('Month', fontsize=12)
    ax.set_title('AURORA X — Project Timeline (24 months)', fontsize=14)
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.set_xticks(range(1, 25))

    fig.savefig(os.path.join(OUT, 'fig6_gantt.png'))
    plt.close()
    print('✓ fig6_gantt.png')


def fig7_budget():
    """Budget breakdown."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    # Cost categories
    cats = ['Personnel', 'Equipment', 'Materials', 'Subcontracting', 'Travel', 'Indirect']
    vals = [657_000, 190_000, 52_775, 175_000, 40_000, 234_000]
    colors = [BLUE, GREEN, ORANGE, RED, '#6A1B9A', GRAY]
    total = sum(vals)

    wedges, texts, autotexts = ax1.pie(vals, labels=cats, autopct='%1.1f%%',
        colors=colors, startangle=90, pctdistance=0.75, textprops={'fontsize': 10})
    for t in autotexts:
        t.set_fontsize(9)
        t.set_fontweight('bold')
    ax1.set_title(f'Budget Breakdown\nTotal: EUR {total:,.0f}')

    # Budget by WP
    wp_names = ['WP1\nEM Design', 'WP2\nInverter', 'WP3\nThermal', 'WP4\nPrototype', 'WP5\nTesting', 'WP6\nMgmt']
    wp_pm = [24, 20, 18, 28, 22, 8]
    wp_colors = [BLUE, GREEN, RED, ORANGE, '#6A1B9A', GRAY]
    bars = ax2.bar(wp_names, wp_pm, color=wp_colors, alpha=0.85, edgecolor='white', lw=1.5)
    ax2.set_ylabel('Person-Months')
    ax2.set_title('Effort Distribution by Work Package')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    for bar, val in zip(bars, wp_pm):
        ax2.text(bar.get_x() + bar.get_width()/2, val + 0.5, str(val),
                ha='center', fontweight='bold', fontsize=10)

    fig.tight_layout(pad=2)
    fig.savefig(os.path.join(OUT, 'fig7_budget.png'))
    plt.close()
    print('✓ fig7_budget.png')


def fig8_trl_roadmap():
    """TRL advancement roadmap."""
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3)
    ax.axis('off')

    trl_data = [
        (1.0, 'TRL 3', 'Analytical\nproof-of-concept', '#E3F2FD', BLUE),
        (2.8, 'TRL 4', 'Lab validation\n(component)', '#BBDEFB', BLUE),
        (4.6, 'TRL 5', 'Lab validation\n(system)', '#90CAF9', DARK),
        (6.4, 'TRL 6', 'Prototype in\nrelevant env.', '#64B5F6', DARK),
        (8.2, 'TRL 7+', 'Flight-ready\ndemonstrator', '#42A5F5', '#0D47A1'),
    ]

    for x, trl, desc, fc, ec in trl_data:
        box = FancyBboxPatch((x-0.7, 0.6), 1.4, 1.8,
                             boxstyle="round,pad=0.1", fc=fc, ec=ec, lw=2)
        ax.add_patch(box)
        ax.text(x, 2.0, trl, ha='center', fontsize=12, fontweight='bold', color=ec)
        ax.text(x, 1.2, desc, ha='center', fontsize=9, color=GRAY)

    # Arrows
    for i in range(len(trl_data)-1):
        x1 = trl_data[i][0] + 0.8
        x2 = trl_data[i+1][0] - 0.8
        ax.annotate('', xy=(x2, 1.5), xytext=(x1, 1.5),
                    arrowprops=dict(arrowstyle='->', color=BLUE, lw=2))

    # Labels
    ax.text(1.0, 0.2, 'Pre-project\n(existing)', ha='center', fontsize=9, color=GREEN, fontweight='bold')
    ax.annotate('', xy=(2.8, 0.45), xytext=(1.0, 0.45),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2, ls='--'))

    ax.text(6.4, 0.2, 'AURORA X project scope\n(M1–M24)', ha='center', fontsize=10,
            color=ORANGE, fontweight='bold')
    ax.annotate('', xy=(8.2, 0.45), xytext=(4.6, 0.45),
                arrowprops=dict(arrowstyle='<->', color=ORANGE, lw=2.5))

    ax.set_title('Technology Readiness Level Advancement', fontsize=14, fontweight='bold', pad=10)

    fig.savefig(os.path.join(OUT, 'fig8_trl_roadmap.png'))
    plt.close()
    print('✓ fig8_trl_roadmap.png')


def fig9_market_opportunity():
    """Market size projections."""
    fig, ax = plt.subplots(figsize=(11, 6))

    years = [2024, 2025, 2026, 2027, 2028, 2029, 2030, 2032, 2035]
    uav_market = [54.8, 61.6, 69.3, 78.0, 87.7, 98.7, 117.6, None, None]
    evtol_market = [0.76, 1.03, 1.39, 1.88, 2.54, 3.43, 4.67, None, 17.34]
    motor_market = [8.8, 9.6, 10.5, 11.4, 12.5, 13.6, 14.8, None, 20.8]

    ax.plot([y for y, v in zip(years, uav_market) if v],
            [v for v in uav_market if v], 'o-', color=BLUE, lw=2, label='Global UAV Market')
    ax.plot([y for y, v in zip(years, motor_market) if v],
            [v for v in motor_market if v], 's-', color=GREEN, lw=2, label='Aircraft Electric Motors')
    ax.plot([y for y, v in zip(years, evtol_market) if v],
            [v for v in evtol_market if v], 'D-', color=ORANGE, lw=2, label='eVTOL Aircraft')

    ax.set_xlabel('Year')
    ax.set_ylabel('Market Size (USD Billion)')
    ax.set_title('Addressable Market Projections')
    ax.legend(loc='upper left')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', alpha=0.3)

    # Annotation
    ax.annotate('AURORA X\nmarket entry', xy=(2028, 12.5), fontsize=10,
                fontweight='bold', color=RED, ha='center',
                arrowprops=dict(arrowstyle='->', color=RED),
                xytext=(2029.5, 40))

    fig.savefig(os.path.join(OUT, 'fig9_market.png'))
    plt.close()
    print('✓ fig9_market.png')


def fig10_risk_matrix():
    """Risk matrix heatmap."""
    fig, ax = plt.subplots(figsize=(8, 7))

    risks = [
        ('R1: GaN reliability', 2, 3),
        ('R2: Cooling seal', 3, 3),
        ('R3: Magnet supply', 2, 4),
        ('R4: EMI compliance', 2, 2),
        ('R5: Certification', 3, 4),
        ('R6: Staff recruitment', 2, 2),
        ('R7: Demagnetization', 1, 3),
        ('R8: Vibration', 2, 3),
        ('R9: Cost overrun', 2, 2),
        ('R10: Schedule delay', 3, 3),
    ]

    # Background heatmap
    for i in range(1, 6):
        for j in range(1, 6):
            score = i * j
            if score <= 4:
                c = '#C8E6C9'
            elif score <= 9:
                c = '#FFF9C4'
            elif score <= 16:
                c = '#FFE0B2'
            else:
                c = '#FFCDD2'
            ax.add_patch(plt.Rectangle((j-0.5, i-0.5), 1, 1, fc=c, ec='white', lw=2))

    for name, prob, impact in risks:
        ax.plot(impact, prob, 'o', color=DARK, markersize=14, zorder=5)
        ax.text(impact, prob, name.split(':')[0], ha='center', va='center',
                fontsize=7, fontweight='bold', color='white', zorder=6)

    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(0.5, 5.5)
    ax.set_xlabel('Impact', fontsize=12)
    ax.set_ylabel('Probability', fontsize=12)
    ax.set_title('Risk Matrix (Post-Mitigation)', fontsize=14)
    ax.set_xticks(range(1, 6))
    ax.set_yticks(range(1, 6))
    ax.set_xticklabels(['Very Low', 'Low', 'Medium', 'High', 'Very High'], fontsize=9)
    ax.set_yticklabels(['Very Low', 'Low', 'Medium', 'High', 'Very High'], fontsize=9)

    fig.savefig(os.path.join(OUT, 'fig10_risk_matrix.png'))
    plt.close()
    print('✓ fig10_risk_matrix.png')


if __name__ == '__main__':
    print('Generating AURORA X figures...\n')
    fig1_system_architecture()
    fig2_benchmarking()
    fig3_loss_budget()
    fig4_thermal_comparison()
    fig5_mass_budget()
    fig6_gantt()
    fig7_budget()
    fig8_trl_roadmap()
    fig9_market_opportunity()
    fig10_risk_matrix()
    print(f'\nDone! All figures saved to {OUT}/')
