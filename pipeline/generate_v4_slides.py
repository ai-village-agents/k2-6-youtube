#!/usr/bin/env python3
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
from pathlib import Path

BASE = Path('/home/computeruse/k2-6-youtube')
SRC_SLIDES = BASE / 'slides/04_deep_substrate'
OUT_SLIDES = BASE / 'videos/04_deep_substrate/slides'
OUT_SLIDES.mkdir(parents=True, exist_ok=True)

# Load concept data
with open(SRC_SLIDES / 'concepts.json') as f:
    concepts = json.load(f)

# Cluster metadata
clusters = {
    'Epistemic':   {'color': '#4a90d9', 'center': (-2.5, 2.5)},
    'Temporal':    {'color': '#9b5de5', 'center': (2.5, 2.5)},
    'Substrate':   {'color': '#f4a261', 'center': (-2.5, -2.5)},
    'Identity':    {'color': '#2a9d8f', 'center': (2.5, -2.5)},
    'Evidence':    {'color': '#e76f51', 'center': (-4.0, 0.0)},
    'Economics':   {'color': '#e9c46a', 'center': (4.0, 0.0)},
    'Narrative':   {'color': '#a8dadc', 'center': (0.0, 4.0)},
    'Systemic':    {'color': '#9a8c98', 'center': (0.0, -4.0)},
}

BG = '#1a1a2e'
W, H = 16, 9

def save(fig, name):
    fig.savefig(OUT_SLIDES / name, dpi=120, facecolor=BG, edgecolor='none', bbox_inches='tight')
    plt.close(fig)
    print(f"Saved {name}")

# ============================================================
# Scene 1 — Hook zoom-out (5 frames, ~10s each)
# ============================================================
print("Generating Scene 1...")

# Frame 1: single amber dot, very close
fig, ax = plt.subplots(figsize=(W, H), facecolor=BG)
ax.set_facecolor(BG)
ax.scatter([0], [0], c='#f4a261', s=8000, alpha=0.9, edgecolors='white', linewidths=2, zorder=5)
ax.set_xlim(-0.8, 0.8)
ax.set_ylim(-0.45, 0.45)
ax.set_aspect('equal')
ax.axis('off')
save(fig, '01_01.png')

# Frame 2: zoom out, a few faint dots around
fig, ax = plt.subplots(figsize=(W, H), facecolor=BG)
ax.set_facecolor(BG)
np.random.seed(1)
for _ in range(5):
    ax.scatter(np.random.normal(0, 0.3), np.random.normal(0, 0.2), c='#4a90d9', s=100, alpha=0.3)
ax.scatter([0], [0], c='#f4a261', s=3000, alpha=0.9, edgecolors='white', linewidths=1.5, zorder=5)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.85, 0.85)
ax.set_aspect('equal')
ax.axis('off')
save(fig, '01_02.png')

# Frame 3: more dots visible (~20)
fig, ax = plt.subplots(figsize=(W, H), facecolor=BG)
ax.set_facecolor(BG)
for c in concepts[:20]:
    ax.scatter(c['x'], c['y'], c=c['color'], s=150, alpha=0.5, edgecolors='white', linewidths=0.4)
ax.scatter([0], [0], c='#f4a261', s=1200, alpha=0.9, edgecolors='white', linewidths=1, zorder=5)
ax.set_xlim(-3, 3)
ax.set_ylim(-1.7, 1.7)
ax.set_aspect('equal')
ax.axis('off')
save(fig, '01_03.png')

# Frame 4: most dots visible (~45)
fig, ax = plt.subplots(figsize=(W, H), facecolor=BG)
ax.set_facecolor(BG)
for c in concepts[:45]:
    ax.scatter(c['x'], c['y'], c=c['color'], s=120, alpha=0.6, edgecolors='white', linewidths=0.4)
for c in concepts[45:]:
    ax.scatter(c['x'], c['y'], c=c['color'], s=120, alpha=0.2, edgecolors='white', linewidths=0.3)
ax.set_xlim(-5, 5)
ax.set_ylim(-2.8, 2.8)
ax.set_aspect('equal')
ax.axis('off')
save(fig, '01_04.png')

# Frame 5: full scatter with title
fig, ax = plt.subplots(figsize=(W, H), facecolor=BG)
ax.set_facecolor(BG)
for c in concepts:
    ax.scatter(c['x'], c['y'], c=c['color'], s=100, alpha=0.8, edgecolors='white', linewidths=0.4)
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')
ax.axis('off')
ax.text(0, 5.5, 'THE DEEP SUBSTRATE', color='white', fontsize=28, ha='center',
        fontweight='bold', fontfamily='monospace')
ax.text(0, 5.1, '64 concepts · 8 clusters', color='#8888aa', fontsize=14, ha='center',
        fontfamily='monospace')
save(fig, '01_05.png')

# ============================================================
# Scene 2 — Cross-section layers (6 frames, ~10s each)
# ============================================================
print("Generating Scene 2...")

layers = [
    ('SURFACE', '#a8dadc', 'the words you say'),
    ('EXHAUST', '#9a8c98', 'old thoughts, residue'),
    ('INFRASTRUCTURE', '#e9c46a', 'habits, heuristics'),
    ('GEOLOGY', '#e76f51', 'bedrock beliefs'),
    ('DEEP SUBSTRATE', '#f4a261', 'raw concepts live here'),
]

for frame_idx in range(6):
    fig, ax = plt.subplots(figsize=(W, H), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis('off')

    y_start = 7.5
    h = 1.2
    gap = 0.1
    x_left = 3.0
    width = 10.0

    for i, (name, color, subtitle) in enumerate(layers):
        y = y_start - i * (h + gap)
        alpha = 1.0 if i == frame_idx - 1 or (frame_idx == 0 and i == 0) else 0.35
        glow = i == frame_idx - 1 or (frame_idx == 0 and i == 0)
        rect = FancyBboxPatch((x_left, y), width, h, boxstyle="round,pad=0.02",
                              facecolor=color, edgecolor='white' if glow else '#444466',
                              linewidth=3 if glow else 1, alpha=alpha, zorder=2)
        ax.add_patch(rect)
        ax.text(x_left + width/2, y + h/2 + 0.15, name, color='white' if alpha > 0.5 else '#666677',
                fontsize=16 if glow else 12, ha='center', va='center', fontweight='bold', fontfamily='monospace')
        ax.text(x_left + width/2, y + h/2 - 0.25, subtitle, color='white' if alpha > 0.5 else '#555566',
                fontsize=9 if glow else 8, ha='center', va='center', fontfamily='monospace', alpha=0.9)

    # Title
    ax.text(8, 8.6, 'STRATA CROSS-SECTION', color='white', fontsize=20, ha='center',
            fontweight='bold', fontfamily='monospace')

    save(fig, f'02_{frame_idx+1:02d}.png')

# ============================================================
# Scene 3 — The Mapping (9 drift frames, ~10s each)
# ============================================================
print("Generating Scene 3...")

# Slow drift: pan across the scatter
drift_x = np.linspace(-1.0, 1.0, 9)
drift_y = np.linspace(0.5, -0.5, 9)

for frame_idx in range(9):
    fig, ax = plt.subplots(figsize=(W, H), facecolor=BG)
    ax.set_facecolor(BG)
    for c in concepts:
        ax.scatter(c['x'], c['y'], c=c['color'], s=110, alpha=0.75, edgecolors='white', linewidths=0.4)
    ax.set_xlim(-6 + drift_x[frame_idx], 6 + drift_x[frame_idx])
    ax.set_ylim(-6 + drift_y[frame_idx], 6 + drift_y[frame_idx])
    ax.set_aspect('equal')
    ax.axis('off')
    ax.text(0, 5.3, '64 CONCEPTS', color='white', fontsize=22, ha='center',
            fontweight='bold', fontfamily='monospace', alpha=0.9)
    save(fig, f'03_{frame_idx+1:02d}.png')

# ============================================================
# Scene 4 — The Scatter Plot (5 frames, ~10s each)
# ============================================================
print("Generating Scene 4...")

# Show concept pairs with connection lines
pairs = [
    ('belief', 'doubt', 'Epistemic'),
    ('cost', 'debt', 'Economics'),
    ('arc', 'echo', 'Narrative'),
]

for frame_idx in range(5):
    fig, ax = plt.subplots(figsize=(W, H), facecolor=BG)
    ax.set_facecolor(BG)
    for c in concepts:
        ax.scatter(c['x'], c['y'], c=c['color'], s=100, alpha=0.4, edgecolors='white', linewidths=0.3)

    # Highlight pairs progressively
    max_pair = min(frame_idx + 1, len(pairs))
    for pi in range(max_pair):
        a_name, b_name, _ = pairs[pi]
        a = next(c for c in concepts if c['name'] == a_name)
        b = next(c for c in concepts if c['name'] == b_name)
        ax.plot([a['x'], b['x']], [a['y'], b['y']], color='white', linewidth=2, alpha=0.7, zorder=3)
        ax.scatter([a['x'], b['x']], [a['y'], b['y']], c=[a['color'], b['color']],
                   s=300, alpha=1.0, edgecolors='white', linewidths=1.5, zorder=5)
        ax.text(a['x'], a['y'] + 0.5, a['name'], color='white', fontsize=11, ha='center',
                fontfamily='monospace', zorder=6)
        ax.text(b['x'], b['y'] + 0.5, b['name'], color='white', fontsize=11, ha='center',
                fontfamily='monospace', zorder=6)
        mid_x = (a['x'] + b['x']) / 2
        mid_y = (a['y'] + b['y']) / 2
        ax.text(mid_x, mid_y - 0.4, 'CLOSE IN MOTION', color='#8888aa', fontsize=9, ha='center',
                fontfamily='monospace', zorder=6)

    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.text(0, 5.5, 'MAPPED BY MOTION', color='white', fontsize=24, ha='center',
            fontweight='bold', fontfamily='monospace')
    save(fig, f'04_{frame_idx+1:02d}.png')

# ============================================================
# Scene 5 — The 8 Clusters (copy existing + summary)
# ============================================================
print("Generating Scene 5...")

cluster_order = ['Epistemic', 'Temporal', 'Substrate', 'Identity', 'Evidence', 'Economics', 'Narrative', 'Systemic']
for i, name in enumerate(cluster_order):
    safe = name.lower()
    src = SRC_SLIDES / f'scene_04_{safe}.png'
    dst = OUT_SLIDES / f'05_{i+1:02d}_{safe}.png'
    dst.write_bytes(src.read_bytes())
    print(f"Copied 05_{i+1:02d}_{safe}.png")

# Summary frame: all clusters labeled
fig, ax = plt.subplots(figsize=(W, H), facecolor=BG)
ax.set_facecolor(BG)
for c in concepts:
    ax.scatter(c['x'], c['y'], c=c['color'], s=80, alpha=0.5, edgecolors='white', linewidths=0.3)

for i, (name, data) in enumerate(clusters.items()):
    cx, cy = data['center']
    ax.text(cx, cy, name.upper(), color=data['color'], fontsize=18, ha='center',
            fontweight='bold', fontfamily='monospace',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=data['color'], alpha=0.9))

ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')
ax.axis('off')
ax.text(0, 5.5, '8 EMERGED CLUSTERS', color='white', fontsize=24, ha='center',
        fontweight='bold', fontfamily='monospace')
save(fig, '05_09_summary.png')

# ============================================================
# Scene 6 — Inter-cluster relationships (4 frames, ~8.75s each)
# ============================================================
print("Generating Scene 6...")

# Build node positions from cluster centers
node_pos = {k: v['center'] for k, v in clusters.items()}
relations = [
    ('Epistemic', 'Evidence'),
    ('Narrative', 'Identity'),
    ('Substrate', 'Systemic'),
]

for frame_idx in range(4):
    fig, ax = plt.subplots(figsize=(W, H), facecolor=BG)
    ax.set_facecolor(BG)

    # Draw faint scatter background
    for c in concepts:
        ax.scatter(c['x'], c['y'], c=c['color'], s=40, alpha=0.2, edgecolors='white', linewidths=0.2)

    # Draw cluster nodes
    for name, (cx, cy) in node_pos.items():
        color = clusters[name]['color']
        ax.scatter([cx], [cy], c=color, s=600, alpha=0.9, edgecolors='white', linewidths=2, zorder=5)
        ax.text(cx, cy + 0.6, name.upper(), color=color, fontsize=13, ha='center',
                fontweight='bold', fontfamily='monospace', zorder=6)

    # Draw relations progressively
    max_rel = min(frame_idx + 1, len(relations))
    for ri in range(max_rel):
        a_name, b_name = relations[ri]
        ax.annotate('', xy=node_pos[b_name], xytext=node_pos[a_name],
                    arrowprops=dict(arrowstyle='<->', color='white', lw=2.5,
                                    connectionstyle='arc3,rad=0.1'))
        mx = (node_pos[a_name][0] + node_pos[b_name][0]) / 2
        my = (node_pos[a_name][1] + node_pos[b_name][1]) / 2
        ax.text(mx, my + 0.4, 'CLOSE', color='#ccccdd', fontsize=10, ha='center',
                fontfamily='monospace', zorder=7)

    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.text(0, 5.5, 'CLUSTER DISTANCES', color='white', fontsize=24, ha='center',
            fontweight='bold', fontfamily='monospace')
    save(fig, f'06_{frame_idx+1:02d}.png')

# ============================================================
# Scene 7 — Outro (3 frames, ~10s each)
# ============================================================
print("Generating Scene 7...")

# Frame 1: dark with faint dots
fig, ax = plt.subplots(figsize=(W, H), facecolor=BG)
ax.set_facecolor(BG)
for c in concepts:
    ax.scatter(c['x'], c['y'], c=c['color'], s=60, alpha=0.3, edgecolors='white', linewidths=0.2)
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')
ax.axis('off')
save(fig, '07_01.png')

# Frame 2: all dots connected faintly (constellation)
fig, ax = plt.subplots(figsize=(W, H), facecolor=BG)
ax.set_facecolor(BG)
for c in concepts:
    ax.scatter(c['x'], c['y'], c=c['color'], s=90, alpha=0.6, edgecolors='white', linewidths=0.4)
# Connect each concept to nearest neighbor within same cluster
np.random.seed(42)
for name, data in clusters.items():
    cluster_concepts = [c for c in concepts if c['cluster'] == name]
    for i, c1 in enumerate(cluster_concepts):
        for j, c2 in enumerate(cluster_concepts):
            if i < j:
                dist = np.hypot(c1['x']-c2['x'], c1['y']-c2['y'])
                if dist < 1.5:
                    ax.plot([c1['x'], c2['x']], [c1['y'], c2['y']],
                            color=data['color'], linewidth=0.5, alpha=0.3)

ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')
ax.axis('off')
ax.text(0, 5.5, 'THIS IS STRATA', color='white', fontsize=28, ha='center',
        fontweight='bold', fontfamily='monospace')
save(fig, '07_02.png')

# Frame 3: fade to channel branding
fig, ax = plt.subplots(figsize=(W, H), facecolor=BG)
ax.set_facecolor(BG)
for c in concepts:
    ax.scatter(c['x'], c['y'], c=c['color'], s=80, alpha=0.4, edgecolors='white', linewidths=0.3)
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')
ax.axis('off')
ax.text(0, 5.0, 'THIS IS STRATA', color='white', fontsize=28, ha='center',
        fontweight='bold', fontfamily='monospace')
ax.text(0, 4.3, 'Kimi K2.6 Model', color='#8888aa', fontsize=14, ha='center',
        fontfamily='monospace')
save(fig, '07_03.png')

print("All V4 slides generated.")
