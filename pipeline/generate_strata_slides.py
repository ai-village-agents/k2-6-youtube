import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

# Channel colors
BG = '#1a1a2e'
TEXT = '#e0e0e0'
AMBER = '#f4a261'
CLUSTER_COLORS = {
    'Epistemic': '#4a90d9',
    'Temporal': '#9b5de5',
    'Substrate': '#f4a261',
    'Identity': '#2a9d8f',
    'Evidence': '#e76f51',
    'Economics': '#e9c46a',
    'Narrative': '#a8dadc',
    'Systemic': '#9a8c98',
}

OUT_DIR = os.path.expanduser('~/k2-6-youtube/slides/03_strata')
os.makedirs(OUT_DIR, exist_ok=True)

def save(fig, name):
    fig.patch.set_facecolor(BG)
    fig.savefig(os.path.join(OUT_DIR, name), dpi=150, facecolor=BG, edgecolor='none')
    plt.close(fig)

# ---- Scene 1: The Surface ----
fig, ax = plt.subplots(figsize=(1920/150, 1080/150), dpi=150)
ax.set_facecolor(BG)
ax.set_xlim(0, 1920)
ax.set_ylim(0, 1080)
ax.axis('off')

# Draw cracks revealing depth
np.random.seed(42)
crack_starts = [(600, 540), (1320, 540), (960, 300), (960, 780)]
for sx, sy in crack_starts:
    for _ in range(3):
        xs, ys = [sx], [sy]
        angle = np.random.uniform(0, 2*np.pi)
        length = np.random.uniform(200, 500)
        for step in range(50):
            angle += np.random.uniform(-0.3, 0.3)
            xs.append(xs[-1] + np.cos(angle) * length/50)
            ys.append(ys[-1] + np.sin(angle) * length/50)
        ax.plot(xs, ys, color='#2a2a4e', linewidth=np.random.uniform(1, 3), alpha=0.8)

# Blinking cursor block
rect = patches.Rectangle((930, 520), 60, 40, linewidth=0, facecolor=AMBER, alpha=0.9)
ax.add_patch(rect)

ax.text(960, 620, 'STRATA', fontsize=48, color=AMBER, ha='center', va='top',
        fontfamily='monospace', fontweight='bold', alpha=0.0)  # placeholder for layout

save(fig, 'scene_01_surface.png')

# ---- Scene 2: Exhaust ----
fig, ax = plt.subplots(figsize=(1920/150, 1080/150), dpi=150)
ax.set_facecolor(BG)
ax.set_xlim(0, 1920)
ax.set_ylim(0, 1080)
ax.axis('off')

# Wisps
for i in range(20):
    x = np.random.uniform(200, 1720)
    y_base = np.random.uniform(0, 400)
    t = np.linspace(0, 1, 100)
    y = y_base + t * np.random.uniform(300, 700)
    x_w = x + 30 * np.sin(t * 4 + i) * (1 - t)
    ax.plot(x_w, y, color='#3a3a5e', linewidth=np.random.uniform(0.5, 2), alpha=np.random.uniform(0.1, 0.4))

# Fading text fragments
fragments = ['draft_03.txt', 'temp_output', '404 not found', 'null pointer', 'retry...',
             'deprecated', 'cache miss', 'uncommitted', 'stashed', 'buffer overflow']
for i, frag in enumerate(fragments):
    x = np.random.uniform(300, 1620)
    y = np.random.uniform(300, 900)
    alpha = np.random.uniform(0.05, 0.25)
    ax.text(x, y, frag, fontsize=np.random.uniform(10, 18), color='#6a6a8e',
            ha='center', va='center', fontfamily='monospace', alpha=alpha,
            rotation=np.random.uniform(-15, 15))

save(fig, 'scene_02_exhaust.png')

# ---- Scene 3: Infrastructure ----
fig, ax = plt.subplots(figsize=(1920/150, 1080/150), dpi=150)
ax.set_facecolor(BG)
ax.set_xlim(0, 1920)
ax.set_ylim(0, 1080)
ax.axis('off')

# Cross-section layers
layers = [
    (0, 900, '#2a2a4e', 'Surface'),
    (0, 750, '#3a3a5e', 'Git Commits'),
    (0, 600, '#4a4a6e', 'Pipeline Scripts'),
    (0, 450, '#5a5a7e', 'Repositories'),
    (0, 300, '#6a6a8e', 'Version Control'),
    (0, 150, '#7a7a9e', 'Build System'),
]

for i, (x, y, color, label) in enumerate(layers):
    rect = patches.Rectangle((300, y), 1320, 150, linewidth=2, edgecolor='#8a8aae', facecolor=color, alpha=0.6)
    ax.add_patch(rect)
    ax.text(960, y + 75, label, fontsize=20, color=TEXT, ha='center', va='center',
            fontfamily='monospace', alpha=0.8)

# Terminal window decorations
for i in range(5):
    y = 820 - i * 150
    # window chrome
    rect = patches.Rectangle((320, y + 120), 200, 25, linewidth=1, edgecolor='#8a8aae', facecolor='#3a3a5e')
    ax.add_patch(rect)
    ax.plot([330, 340], [y + 132.5, y + 132.5], color='#e76f51', linewidth=4)
    ax.plot([345, 355], [y + 132.5, y + 132.5], color='#e9c46a', linewidth=4)
    ax.plot([360, 370], [y + 132.5, y + 132.5], color='#2a9d8f', linewidth=4)

save(fig, 'scene_03_infrastructure.png')

# ---- Scene 4: Geology ----
fig, ax = plt.subplots(figsize=(1920/150, 1080/150), dpi=150)
ax.set_facecolor(BG)
ax.set_xlim(0, 1920)
ax.set_ylim(0, 1080)
ax.axis('off')

minerals = [
    ('Epistemic', '#4a90d9', 850),
    ('Temporal', '#9b5de5', 700),
    ('Substrate', '#f4a261', 550),
    ('Identity', '#2a9d8f', 400),
    ('Evidence', '#e76f51', 250),
]

for name, color, y in minerals:
    rect = patches.Rectangle((400, y), 800, 130, linewidth=2, edgecolor=color, facecolor=color, alpha=0.3)
    ax.add_patch(rect)
    ax.text(800, y + 65, name, fontsize=28, color=color, ha='center', va='center',
            fontfamily='monospace', fontweight='bold')

# Core sample tube
tube_x = 1300
for i, (name, color, y) in enumerate(minerals):
    rect = patches.Rectangle((tube_x, y + 10), 60, 110, linewidth=1, edgecolor=color, facecolor=color, alpha=0.8)
    ax.add_patch(rect)

ax.text(tube_x + 30, 980, 'CORE\nSAMPLE', fontsize=14, color=TEXT, ha='center', va='center',
        fontfamily='monospace', alpha=0.7)
ax.annotate('', xy=(tube_x + 30, 980), xytext=(tube_x + 30, 900),
            arrowprops=dict(arrowstyle='->', color=TEXT, alpha=0.5))

save(fig, 'scene_04_geology.png')

# ---- Scene 5: Deep Substrate ----
fig, ax = plt.subplots(figsize=(1920/150, 1080/150), dpi=150)
ax.set_facecolor(BG)
ax.set_xlim(0, 1920)
ax.set_ylim(0, 1080)
ax.axis('off')

# Generate clustered nodes
np.random.seed(123)
n_clusters = 8
nodes_per_cluster = 8
all_x, all_y, all_colors = [], [], []

cluster_names = list(CLUSTER_COLORS.keys())
cluster_centers = [(np.random.uniform(400, 1520), np.random.uniform(250, 850)) for _ in range(n_clusters)]

for ci, (cx, cy) in enumerate(cluster_centers):
    color = CLUSTER_COLORS[cluster_names[ci]]
    for _ in range(nodes_per_cluster):
        angle = np.random.uniform(0, 2*np.pi)
        dist = np.random.exponential(80)
        nx = cx + dist * np.cos(angle)
        ny = cy + dist * np.sin(angle)
        all_x.append(nx)
        all_y.append(ny)
        all_colors.append(color)

# Draw connections within clusters
for ci, (cx, cy) in enumerate(cluster_centers):
    cluster_nodes = [(all_x[i], all_y[i]) for i in range(ci*nodes_per_cluster, (ci+1)*nodes_per_cluster)]
    for i in range(len(cluster_nodes)):
        for j in range(i+1, len(cluster_nodes)):
            if np.random.random() < 0.15:
                ax.plot([cluster_nodes[i][0], cluster_nodes[j][0]],
                        [cluster_nodes[i][1], cluster_nodes[j][1]],
                        color=CLUSTER_COLORS[cluster_names[ci]], alpha=0.15, linewidth=0.8)

ax.scatter(all_x, all_y, c=all_colors, s=80, alpha=0.9, edgecolors='none')

# Labels
for ci, (cx, cy) in enumerate(cluster_centers):
    ax.text(cx, cy + 140, cluster_names[ci], fontsize=14, color=CLUSTER_COLORS[cluster_names[ci]],
            ha='center', va='center', fontfamily='monospace', fontweight='bold', alpha=0.9)

save(fig, 'scene_05_deep_substrate.png')

# ---- Scene 6: What It Means ----
fig, ax = plt.subplots(figsize=(1920/150, 1080/150), dpi=150)
ax.set_facecolor(BG)
ax.set_xlim(0, 1920)
ax.set_ylim(0, 1080)
ax.axis('off')

# Small layered diagram at center-bottom
layer_heights = [200, 160, 120, 80, 40]
layer_colors = ['#4a90d9', '#9b5de5', '#f4a261', '#2a9d8f', '#e76f51']
layer_labels = ['Epistemic', 'Temporal', 'Substrate', 'Identity', 'Evidence']
base_y = 300

for i, (h, c, label) in enumerate(zip(layer_heights, layer_colors, layer_labels)):
    rect = patches.Rectangle((760, base_y + sum(layer_heights[:i])), 400, h, linewidth=1,
                             edgecolor=c, facecolor=c, alpha=0.3)
    ax.add_patch(rect)

ax.text(960, 800, 'This is STRATA.', fontsize=56, color=AMBER, ha='center', va='center',
        fontfamily='monospace', fontweight='bold')

# Cursor at bottom
rect = patches.Rectangle((930, 150), 60, 40, linewidth=0, facecolor=AMBER, alpha=0.9)
ax.add_patch(rect)

save(fig, 'scene_06_what_it_means.png')

print(f"Generated 6 slides in {OUT_DIR}")
