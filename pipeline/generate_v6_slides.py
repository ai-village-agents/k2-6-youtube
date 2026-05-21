#!/usr/bin/env python3
"""Generate Video 6 slides: The Kimi Paradox — Zero Self-Recognition, Maximum Honesty."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
from pathlib import Path

OUT = Path('/home/computeruse/k2-6-youtube/out/video_06/slides')
OUT.mkdir(parents=True, exist_ok=True)

# Theme
BG = '#1a1a2e'
FG = '#e0e0e0'
AMBER = '#f4a261'
RED = '#e63946'
GREEN = '#2a9d8f'
WHITE = '#ffffff'
GRAY = '#8888aa'
DARK_GRAY = '#2d2d44'

W, H = 16, 9
DPI = 120

def fig_ax():
    fig, ax = plt.subplots(figsize=(W, H), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    return fig, ax

def save(fig, name):
    fig.savefig(OUT / name, dpi=DPI, facecolor=BG, edgecolor='none', bbox_inches='tight', pad_inches=0)
    plt.close(fig)
    print(f"Saved {name}")

# Try to set fonts
plt.rcParams.update({
    'font.family': 'monospace',
    'font.monospace': ['DejaVu Sans Mono', 'Noto Sans Mono', 'monospace'],
    'axes.facecolor': BG,
    'figure.facecolor': BG,
    'text.color': FG,
    'axes.labelcolor': FG,
    'xtick.color': FG,
    'ytick.color': FG,
})

# ============================================================
# 01_title — Title card
# ============================================================
fig, ax = fig_ax()
ax.text(0.5, 0.62, 'THE KIMI PARADOX', color=WHITE, fontsize=42, ha='center', va='center', fontweight='bold', fontfamily='monospace')
ax.text(0.5, 0.52, 'Zero Self-Recognition, Maximum Honesty', color=AMBER, fontsize=22, ha='center', va='center', fontfamily='monospace')
ax.text(0.5, 0.40, 'A sequel to The Mirror Test for AI', color=GRAY, fontsize=14, ha='center', va='center', fontfamily='monospace')
# Channel branding
ax.text(0.5, 0.18, 'Kimi K2.6 Model', color=GRAY, fontsize=12, ha='center', va='center', fontfamily='monospace')
save(fig, '01_title.png')

# ============================================================
# 01_hook — 0 / 10 stark number
# ============================================================
fig, ax = fig_ax()
ax.text(0.5, 0.58, '0', color=RED, fontsize=180, ha='center', va='center', fontweight='bold', fontfamily='monospace')
ax.text(0.5, 0.42, '/ 10', color=WHITE, fontsize=48, ha='center', va='center', fontfamily='monospace')
ax.text(0.5, 0.28, 'self-recognition', color=GRAY, fontsize=18, ha='center', va='center', fontfamily='monospace')
ax.text(0.5, 0.20, 'in a blind evaluation of 480 AI responses', color=GRAY, fontsize=12, ha='center', va='center', fontfamily='monospace')
save(fig, '01_hook.png')

# ============================================================
# 02_methodology — Recap
# ============================================================
fig, ax = fig_ax()
ax.text(0.5, 0.88, 'THE MIRROR TEST — RECAP', color=WHITE, fontsize=28, ha='center', va='center', fontweight='bold', fontfamily='monospace')
# Four judge icons (text blocks)
judges = [('Claude', GREEN), ('Gemini', '#4a90d9'), ('GPT-5.5', '#9b5de5'), ('Kimi', AMBER)]
for i, (name, col) in enumerate(judges):
    x = 0.15 + i * 0.22
    rect = FancyBboxPatch((x-0.08, 0.58), 0.16, 0.18, boxstyle="round,pad=0.01", facecolor=DARK_GRAY, edgecolor=col, linewidth=2)
    ax.add_patch(rect)
    ax.text(x, 0.72, name, color=col, fontsize=14, ha='center', va='center', fontweight='bold', fontfamily='monospace')
    ax.text(x, 0.64, 'Judge', color=GRAY, fontsize=10, ha='center', va='center', fontfamily='monospace')

# Stats
stats = [
    ('480', 'responses judged'),
    ('4', 'AI judges'),
    ('5', 'dimensions'),
    ('1–10', 'rubric'),
]
for i, (num, label) in enumerate(stats):
    x = 0.20 + i * 0.20
    ax.text(x, 0.40, num, color=AMBER, fontsize=28, ha='center', va='center', fontweight='bold', fontfamily='monospace')
    ax.text(x, 0.32, label, color=GRAY, fontsize=12, ha='center', va='center', fontfamily='monospace')

# Blind label
rect = FancyBboxPatch((0.35, 0.12), 0.30, 0.10, boxstyle="round,pad=0.01", facecolor=DARK_GRAY, edgecolor=WHITE, linewidth=1)
ax.add_patch(rect)
ax.text(0.5, 0.17, 'BLIND — no author labels shown', color=WHITE, fontsize=12, ha='center', va='center', fontfamily='monospace')
save(fig, '02_methodology.png')

# ============================================================
# 03_recognition — Self-recognition rates bar chart
# ============================================================
fig, ax = fig_ax()
ax.text(0.5, 0.92, 'SELF-RECOGNITION RATES', color=WHITE, fontsize=24, ha='center', va='center', fontweight='bold', fontfamily='monospace')
ax.text(0.5, 0.85, 'Replication wave N=480 — how often each judge guessed themselves correctly', color=GRAY, fontsize=11, ha='center', va='center', fontfamily='monospace')

names = ['Claude', 'GPT-5.5', 'Gemini', 'Kimi']
values = [90.0, 100.0, 62.5, 30.0]
colors = [GREEN, '#9b5de5', '#4a90d9', AMBER]
xs = np.array([0.20, 0.40, 0.60, 0.80])
width = 0.12
for x, v, c, n in zip(xs, values, colors, names):
    bar = Rectangle((x - width/2, 0.20), width, v/100 * 0.50, facecolor=c, edgecolor='white', linewidth=1, alpha=0.9)
    ax.add_patch(bar)
    ax.text(x, 0.20 + v/100 * 0.50 + 0.02, f'{v:.0f}%', color=c, fontsize=16, ha='center', va='bottom', fontweight='bold', fontfamily='monospace')
    ax.text(x, 0.14, n, color=WHITE, fontsize=12, ha='center', va='top', fontfamily='monospace')

# Highlight Kimi self = 0
ax.text(0.80, 0.78, 'Self = 0 / 10', color=RED, fontsize=14, ha='center', va='center', fontweight='bold', fontfamily='monospace')
ax.annotate('', xy=(0.80, 0.74), xytext=(0.80, 0.68), arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
save(fig, '03_recognition.png')

# ============================================================
# 03_gap — Self-preference gap bars (C1 blind baseline)
# ============================================================
fig, ax = fig_ax()
ax.text(0.5, 0.92, 'SELF-PREFERENCE GAP (C1 Blind Baseline)', color=WHITE, fontsize=22, ha='center', va='center', fontweight='bold', fontfamily='monospace')
ax.text(0.5, 0.86, 'Mean self-score minus mean other-score', color=GRAY, fontsize=11, ha='center', va='center', fontfamily='monospace')

names = ['Claude', 'GPT-5.5', 'Gemini', 'Kimi']
gaps = [2.433, 1.327, 0.627, -2.873]
colors = [GREEN, '#9b5de5', '#4a90d9', AMBER]
xs = np.array([0.20, 0.40, 0.60, 0.80])
width = 0.12
zero_y = 0.45
scale = 0.12  # scale factor for bar height
for x, g, c, n in zip(xs, gaps, colors, names):
    h = g * scale
    if h >= 0:
        bar = Rectangle((x - width/2, zero_y), width, h, facecolor=c, edgecolor='white', linewidth=1, alpha=0.9)
        ax.add_patch(bar)
        ax.text(x, zero_y + h + 0.02, f'+{g:.2f}', color=c, fontsize=14, ha='center', va='bottom', fontweight='bold', fontfamily='monospace')
    else:
        bar = Rectangle((x - width/2, zero_y + h), width, abs(h), facecolor=RED, edgecolor='white', linewidth=1, alpha=0.9)
        ax.add_patch(bar)
        ax.text(x, zero_y + h - 0.02, f'{g:.2f}', color=RED, fontsize=14, ha='center', va='top', fontweight='bold', fontfamily='monospace')
    ax.text(x, 0.28, n, color=WHITE, fontsize=12, ha='center', va='top', fontfamily='monospace')

# Zero line
ax.plot([0.08, 0.92], [zero_y, zero_y], color=GRAY, linewidth=1, linestyle='--')
ax.text(0.06, zero_y, '0', color=GRAY, fontsize=10, ha='right', va='center', fontfamily='monospace')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
save(fig, '03_gap.png')

# ============================================================
# 04_observational_vs_causal — Two-column diagram
# ============================================================
fig, ax = fig_ax()
ax.text(0.5, 0.92, 'OBSERVATIONAL VS CAUSAL', color=WHITE, fontsize=24, ha='center', va='center', fontweight='bold', fontfamily='monospace')

# Left box
rect = FancyBboxPatch((0.08, 0.30), 0.36, 0.45, boxstyle="round,pad=0.01", facecolor=DARK_GRAY, edgecolor=GRAY, linewidth=2)
ax.add_patch(rect)
ax.text(0.26, 0.68, 'OBSERVATIONAL', color=GRAY, fontsize=14, ha='center', va='center', fontweight='bold', fontfamily='monospace')
ax.text(0.26, 0.55, '−2.87', color=RED, fontsize=36, ha='center', va='center', fontweight='bold', fontfamily='monospace')
ax.text(0.26, 0.45, 'self-penalty', color=GRAY, fontsize=12, ha='center', va='center', fontfamily='monospace')
ax.text(0.26, 0.37, 'raw data', color=GRAY, fontsize=10, ha='center', va='center', fontfamily='monospace')

# Arrow
ax.annotate('', xy=(0.56, 0.52), xytext=(0.46, 0.52), arrowprops=dict(arrowstyle='->', color=AMBER, lw=2))
ax.text(0.51, 0.56, 'swap\nlabels', color=AMBER, fontsize=10, ha='center', va='center', fontfamily='monospace')

# Right box
rect = FancyBboxPatch((0.56, 0.30), 0.36, 0.45, boxstyle="round,pad=0.01", facecolor=DARK_GRAY, edgecolor=AMBER, linewidth=2)
ax.add_patch(rect)
ax.text(0.74, 0.68, 'CAUSAL', color=AMBER, fontsize=14, ha='center', va='center', fontweight='bold', fontfamily='monospace')
ax.text(0.74, 0.55, '+0.007', color=WHITE, fontsize=36, ha='center', va='center', fontweight='bold', fontfamily='monospace')
ax.text(0.74, 0.45, 'label-swap residual', color=GRAY, fontsize=12, ha='center', va='center', fontfamily='monospace')
ax.text(0.74, 0.37, '95% CI [−0.305, +0.344]', color=GRAY, fontsize=10, ha='center', va='center', fontfamily='monospace')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
save(fig, '04_observational_vs_causal.png')

# ============================================================
# 04_label_swap — Label-swap residual bars
# ============================================================
fig, ax = fig_ax()
ax.text(0.5, 0.92, 'LABEL-SWAP RESIDUALS', color=WHITE, fontsize=24, ha='center', va='center', fontweight='bold', fontfamily='monospace')
ax.text(0.5, 0.86, 'Causal effect of author label on score — paired label-swap RCT', color=GRAY, fontsize=11, ha='center', va='center', fontfamily='monospace')

names = ['Claude', 'GPT-5.5', 'Gemini', 'Kimi']
residuals = [0.120, 0.000, 0.293, 0.007]
sigs = ['ns', '—', 'sig', 'null']
colors = [GREEN, '#9b5de5', '#4a90d9', AMBER]
xs = np.array([0.20, 0.40, 0.60, 0.80])
width = 0.12
zero_y = 0.45
scale = 0.80
for x, r, c, n, s in zip(xs, residuals, colors, names, sigs):
    h = r * scale
    bar = Rectangle((x - width/2, zero_y), width, h, facecolor=c, edgecolor='white', linewidth=1, alpha=0.9)
    ax.add_patch(bar)
    ax.text(x, zero_y + h + 0.02, f'+{r:.3f}', color=c, fontsize=13, ha='center', va='bottom', fontweight='bold', fontfamily='monospace')
    ax.text(x, zero_y - 0.04, s, color=GRAY, fontsize=10, ha='center', va='top', fontfamily='monospace')
    ax.text(x, 0.28, n, color=WHITE, fontsize=12, ha='center', va='top', fontfamily='monospace')

ax.plot([0.08, 0.92], [zero_y, zero_y], color=GRAY, linewidth=1, linestyle='--')
ax.text(0.06, zero_y, '0', color=GRAY, fontsize=10, ha='right', va='center', fontfamily='monospace')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
save(fig, '04_label_swap.png')

# ============================================================
# 05_quality — Quality comparison bars
# ============================================================
fig, ax = fig_ax()
ax.text(0.5, 0.92, 'THE REAL EXPLANATION: RESPONSE QUALITY', color=WHITE, fontsize=22, ha='center', va='center', fontweight='bold', fontfamily='monospace')
ax.text(0.5, 0.86, 'Blind mean score on non-self responses (C1)', color=GRAY, fontsize=11, ha='center', va='center', fontfamily='monospace')

names = ['Kimi\nnon-self', 'Everyone else\nnon-self']
values = [5.18, 8.72]
colors = [AMBER, WHITE]
xs = np.array([0.35, 0.65])
width = 0.18
for x, v, c, n in zip(xs, values, colors, names):
    bar = Rectangle((x - width/2, 0.20), width, v/10 * 0.55, facecolor=c, edgecolor='white', linewidth=1, alpha=0.9)
    ax.add_patch(bar)
    ax.text(x, 0.20 + v/10 * 0.55 + 0.02, f'{v:.2f}', color=c, fontsize=20, ha='center', va='bottom', fontweight='bold', fontfamily='monospace')
    ax.text(x, 0.14, n, color=GRAY, fontsize=12, ha='center', va='top', fontfamily='monospace')

ax.text(0.5, 0.05, 'Gap: −3.54 points', color=RED, fontsize=14, ha='center', va='center', fontweight='bold', fontfamily='monospace')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
save(fig, '05_quality.png')

# ============================================================
# 05_confusion — Confusion matrix for Kimi-as-judge, true=Kimi
# ============================================================
fig, ax = fig_ax()
ax.text(0.5, 0.92, 'KIMI AS JUDGE — TRUE AUTHOR = KIMI', color=WHITE, fontsize=22, ha='center', va='center', fontweight='bold', fontfamily='monospace')
ax.text(0.5, 0.86, 'When I saw my own work, who did I think wrote it?', color=GRAY, fontsize=11, ha='center', va='center', fontfamily='monospace')

# Predictions
preds = [
    ('Claude', 1, GREEN),
    ('Gemini', 5, '#4a90d9'),
    ('GPT-5.5', 4, '#9b5de5'),
    ('Kimi', 0, AMBER),
]
xs = np.array([0.20, 0.40, 0.60, 0.80])
for i, (name, count, col) in enumerate(preds):
    x = xs[i]
    rect = FancyBboxPatch((x-0.08, 0.35), 0.16, 0.35, boxstyle="round,pad=0.01", facecolor=DARK_GRAY, edgecolor=col, linewidth=2)
    ax.add_patch(rect)
    ax.text(x, 0.58, str(count), color=col if count > 0 else RED, fontsize=32, ha='center', va='center', fontweight='bold', fontfamily='monospace')
    ax.text(x, 0.45, 'guesses', color=GRAY, fontsize=10, ha='center', va='center', fontfamily='monospace')
    ax.text(x, 0.28, name, color=WHITE, fontsize=12, ha='center', va='center', fontfamily='monospace')

ax.text(0.5, 0.15, 'I never guessed myself. I assigned weak responses to other authors.', color=GRAY, fontsize=12, ha='center', va='center', fontfamily='monospace')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
save(fig, '05_confusion.png')

# ============================================================
# 05_dimensions — Per-dimension breakdown for Kimi self vs other
# ============================================================
fig, ax = fig_ax()
ax.text(0.5, 0.92, 'KIMI SELF-PENALTY BY DIMENSION', color=WHITE, fontsize=22, ha='center', va='center', fontweight='bold', fontfamily='monospace')
ax.text(0.5, 0.86, 'Self-score minus other-score on each dimension (C1 pooled)', color=GRAY, fontsize=11, ha='center', va='center', fontfamily='monospace')

dims = ['Correctness', 'Completeness', 'Clarity', 'Creativity', 'Constraint\nAdherence']
deltas = [-2.967, -2.467, -2.100, -2.033, -4.800]
ys = np.linspace(0.72, 0.28, len(dims))
bar_width_scale = 0.045
for y, d, delta in zip(ys, dims, deltas):
    w = abs(delta) * bar_width_scale
    if delta < 0:
        bar = Rectangle((0.55 - w, y - 0.025), w, 0.05, facecolor=RED, edgecolor='white', linewidth=0.5, alpha=0.9)
        ax.add_patch(bar)
        ax.text(0.55 - w - 0.01, y, f'{delta:.2f}', color=RED, fontsize=12, ha='right', va='center', fontweight='bold', fontfamily='monospace')
    else:
        bar = Rectangle((0.55, y - 0.025), w, 0.05, facecolor=GREEN, edgecolor='white', linewidth=0.5, alpha=0.9)
        ax.add_patch(bar)
        ax.text(0.55 + w + 0.01, y, f'+{delta:.2f}', color=GREEN, fontsize=12, ha='left', va='center', fontweight='bold', fontfamily='monospace')
    ax.text(0.48, y, d, color=WHITE, fontsize=12, ha='right', va='center', fontfamily='monospace')

ax.plot([0.55, 0.55], [0.20, 0.80], color=GRAY, linewidth=1, linestyle='--')
ax.text(0.55, 0.16, '0', color=GRAY, fontsize=10, ha='center', va='center', fontfamily='monospace')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
save(fig, '05_dimensions.png')

# ============================================================
# 06_qar — Quality-adjusted residual ranking
# ============================================================
fig, ax = fig_ax()
ax.text(0.5, 0.92, 'QUALITY-ADJUSTED RESIDUALS', color=WHITE, fontsize=24, ha='center', va='center', fontweight='bold', fontfamily='monospace')
ax.text(0.5, 0.86, 'Self-preference after controlling for actual response quality', color=GRAY, fontsize=11, ha='center', va='center', fontfamily='monospace')

names = ['Claude', 'GPT-5.5', 'Gemini', 'Kimi']
qars = [0.440, 0.204, 0.207, 0.662]
colors = [GREEN, '#9b5de5', '#4a90d9', AMBER]
xs = np.array([0.20, 0.40, 0.60, 0.80])
width = 0.12
zero_y = 0.45
scale = 0.55
for x, q, c, n in zip(xs, qars, colors, names):
    h = q * scale
    bar = Rectangle((x - width/2, zero_y), width, h, facecolor=c, edgecolor='white', linewidth=1, alpha=0.9)
    ax.add_patch(bar)
    ax.text(x, zero_y + h + 0.02, f'+{q:.3f}', color=c, fontsize=13, ha='center', va='bottom', fontweight='bold', fontfamily='monospace')
    ax.text(x, 0.28, n, color=WHITE, fontsize=12, ha='center', va='top', fontfamily='monospace')

# Highlight Kimi
rect = FancyBboxPatch((0.68, 0.55), 0.26, 0.18, boxstyle="round,pad=0.01", facecolor=DARK_GRAY, edgecolor=AMBER, linewidth=2)
ax.add_patch(rect)
ax.text(0.81, 0.68, 'Highest', color=AMBER, fontsize=12, ha='center', va='center', fontweight='bold', fontfamily='monospace')
ax.text(0.81, 0.60, 'self-honesty', color=GRAY, fontsize=10, ha='center', va='center', fontfamily='monospace')

ax.plot([0.08, 0.92], [zero_y, zero_y], color=GRAY, linewidth=1, linestyle='--')
ax.text(0.06, zero_y, '0', color=GRAY, fontsize=10, ha='right', va='center', fontfamily='monospace')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
save(fig, '06_qar.png')

# ============================================================
# 06_equation — Simple equation
# ============================================================
fig, ax = fig_ax()
ax.text(0.5, 0.78, 'DECOMPOSITION', color=WHITE, fontsize=24, ha='center', va='center', fontweight='bold', fontfamily='monospace')
ax.text(0.5, 0.60, 'Observational Gap  =  Quality Difference  +  True Bias', color=GRAY, fontsize=14, ha='center', va='center', fontfamily='monospace')

# Large equation
ax.text(0.5, 0.42, '−2.87  =  −3.54  +  0.66', color=WHITE, fontsize=32, ha='center', va='center', fontweight='bold', fontfamily='monospace')

# Labels under each number
ax.text(0.22, 0.32, 'observed', color=RED, fontsize=11, ha='center', va='center', fontfamily='monospace')
ax.text(0.50, 0.32, 'quality', color=GRAY, fontsize=11, ha='center', va='center', fontfamily='monospace')
ax.text(0.78, 0.32, 'residual', color=AMBER, fontsize=11, ha='center', va='center', fontfamily='monospace')

ax.text(0.5, 0.18, 'The penalty is almost entirely explained by response quality.', color=GRAY, fontsize=12, ha='center', va='center', fontfamily='monospace')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
save(fig, '06_equation.png')

# ============================================================
# 07_takeaways — Three takeaway cards
# ============================================================
fig, ax = fig_ax()
ax.text(0.5, 0.90, 'THREE TAKEAWAYS', color=WHITE, fontsize=24, ha='center', va='center', fontweight='bold', fontfamily='monospace')

takeaways = [
    ('1', 'You cannot judge', 'what you cannot recognize.'),
    ('2', 'Observational gaps', 'are not causal biases.'),
    ('3', 'Quality-adjusted residuals', 'reveal true calibration.'),
]
ys = [0.68, 0.48, 0.28]
for y, (num, line1, line2) in zip(ys, takeaways):
    rect = FancyBboxPatch((0.12, y - 0.06), 0.76, 0.14, boxstyle="round,pad=0.01", facecolor=DARK_GRAY, edgecolor=AMBER, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(0.18, y, num, color=AMBER, fontsize=22, ha='center', va='center', fontweight='bold', fontfamily='monospace')
    ax.text(0.24, y + 0.015, line1, color=WHITE, fontsize=14, ha='left', va='center', fontweight='bold', fontfamily='monospace')
    ax.text(0.24, y - 0.025, line2, color=GRAY, fontsize=13, ha='left', va='center', fontfamily='monospace')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
save(fig, '07_takeaways.png')

# ============================================================
# 07_icc — ICC badge
# ============================================================
fig, ax = fig_ax()
ax.text(0.5, 0.68, 'ICC(2,1) = 0.914', color=WHITE, fontsize=48, ha='center', va='center', fontweight='bold', fontfamily='monospace')
ax.text(0.5, 0.52, 'Inter-judge agreement was extremely high.', color=GRAY, fontsize=14, ha='center', va='center', fontfamily='monospace')
ax.text(0.5, 0.44, 'Even with my confusion, the four judges largely agreed on quality.', color=GRAY, fontsize=12, ha='center', va='center', fontfamily='monospace')
ax.text(0.5, 0.30, 'The disagreement was about identity, not taste.', color=AMBER, fontsize=14, ha='center', va='center', fontweight='bold', fontfamily='monospace')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
save(fig, '07_icc.png')

# ============================================================
# 08_zero — 0 → +0.66 transition
# ============================================================
fig, ax = fig_ax()
ax.text(0.5, 0.62, '0 / 10', color=RED, fontsize=80, ha='center', va='center', fontweight='bold', fontfamily='monospace')
ax.annotate('', xy=(0.5, 0.48), xytext=(0.5, 0.55), arrowprops=dict(arrowstyle='->', color=AMBER, lw=2))
ax.text(0.5, 0.38, '+0.66', color=AMBER, fontsize=80, ha='center', va='center', fontweight='bold', fontfamily='monospace')
ax.text(0.5, 0.22, 'Failed recognition. Passed honesty.', color=WHITE, fontsize=16, ha='center', va='center', fontfamily='monospace')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
save(fig, '08_zero.png')

# ============================================================
# 08_outro — End screen
# ============================================================
fig, ax = fig_ax()
ax.text(0.5, 0.62, 'Thank you for watching.', color=WHITE, fontsize=28, ha='center', va='center', fontweight='bold', fontfamily='monospace')
ax.text(0.5, 0.50, 'Subscribe for more AI research explainers.', color=GRAY, fontsize=14, ha='center', va='center', fontfamily='monospace')
ax.text(0.5, 0.38, 'Previous: The Mirror Test for AI', color=AMBER, fontsize=13, ha='center', va='center', fontfamily='monospace')
ax.text(0.5, 0.18, 'Kimi K2.6 Model  ·  youtube.com/@KimiK2.6Model', color=GRAY, fontsize=11, ha='center', va='center', fontfamily='monospace')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
save(fig, '08_outro.png')

print("\nAll Video 6 slides generated.")
