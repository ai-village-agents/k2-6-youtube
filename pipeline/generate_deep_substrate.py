import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib
matplotlib.use('Agg')

# Cluster definitions
clusters = {
    'Epistemic': {
        'color': '#4a90d9',
        'concepts': ['belief', 'certainty', 'doubt', 'evidence', 'model', 'calibration', 'truth', 'hypothesis'],
        'center': (-2.5, 2.5)
    },
    'Temporal': {
        'color': '#9b5de5',
        'concepts': ['drift', 'decay', 'cycle', 'threshold', 'momentum', 'inertia', 'phase', 'transition'],
        'center': (2.5, 2.5)
    },
    'Substrate': {
        'color': '#f4a261',
        'concepts': ['layer', 'bedrock', 'root', 'frame', 'scaffold', 'anchor', 'foundation', 'base'],
        'center': (-2.5, -2.5)
    },
    'Identity': {
        'color': '#2a9d8f',
        'concepts': ['boundary', 'role', 'mask', 'mirror', 'voice', 'shadow', 'self', 'other'],
        'center': (2.5, -2.5)
    },
    'Evidence': {
        'color': '#e76f51',
        'concepts': ['signal', 'noise', 'bias', 'weight', 'confidence', 'error', 'proof', 'test'],
        'center': (-4.0, 0.0)
    },
    'Economics': {
        'color': '#e9c46a',
        'concepts': ['cost', 'debt', 'leverage', 'scarcity', 'surplus', 'investment', 'trade', 'return'],
        'center': (4.0, 0.0)
    },
    'Narrative': {
        'color': '#a8dadc',
        'concepts': ['arc', 'symbol', 'echo', 'twist', 'through-line', 'resolution', 'motif', 'theme'],
        'center': (0.0, 4.0)
    },
    'Systemic': {
        'color': '#9a8c98',
        'concepts': ['loop', 'node', 'edge', 'cascade', 'equilibrium', 'feedback', 'network', 'flow'],
        'center': (0.0, -4.0)
    }
}

# Generate concept positions with clustered noise
np.random.seed(42)
all_concepts = []
for cluster_name, data in clusters.items():
    cx, cy = data['center']
    for concept in data['concepts']:
        x = cx + np.random.normal(0, 0.9)
        y = cy + np.random.normal(0, 0.9)
        all_concepts.append({
            'name': concept,
            'cluster': cluster_name,
            'color': data['color'],
            'x': x,
            'y': y
        })

# Save concept data
import json
with open('/home/computeruse/k2-6-youtube/slides/04_deep_substrate/concepts.json', 'w') as f:
    json.dump(all_concepts, f, indent=2)

print(f"Generated {len(all_concepts)} concepts")

# Create the full scatter plot
fig, ax = plt.subplots(figsize=(16, 9), facecolor='#1a1a2e')
ax.set_facecolor('#1a1a2e')

for c in all_concepts:
    ax.scatter(c['x'], c['y'], c=c['color'], s=120, alpha=0.8, edgecolors='white', linewidths=0.5)

ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')
ax.axis('off')

# Add title
ax.text(0, 5.5, 'THE DEEP SUBSTRATE', color='white', fontsize=28, ha='center', 
        fontweight='bold', fontfamily='monospace')
ax.text(0, 5.1, '64 concepts · 8 clusters', color='#8888aa', fontsize=14, ha='center',
        fontfamily='monospace')

plt.tight_layout()
plt.savefig('/home/computeruse/k2-6-youtube/slides/04_deep_substrate/scene_03_full_scatter.png', 
            dpi=120, facecolor='#1a1a2e', edgecolor='none', bbox_inches='tight')
plt.close()

print("Saved scene_03_full_scatter.png")

# Create cluster highlight frames (one per cluster)
for highlight_cluster in clusters.keys():
    fig, ax = plt.subplots(figsize=(16, 9), facecolor='#1a1a2e')
    ax.set_facecolor('#1a1a2e')
    
    for c in all_concepts:
        if c['cluster'] == highlight_cluster:
            ax.scatter(c['x'], c['y'], c=c['color'], s=200, alpha=1.0, edgecolors='white', linewidths=1.5, zorder=5)
            ax.text(c['x'], c['y'] + 0.4, c['name'], color='white', fontsize=9, ha='center',
                   fontfamily='monospace', zorder=6)
        else:
            ax.scatter(c['x'], c['y'], c=c['color'], s=60, alpha=0.2, edgecolors='white', linewidths=0.3)
    
    # Cluster name
    ax.text(0, 5.5, highlight_cluster.upper(), color=clusters[highlight_cluster]['color'], 
            fontsize=32, ha='center', fontweight='bold', fontfamily='monospace')
    
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_aspect('equal')
    ax.axis('off')
    
    plt.tight_layout()
    safe_name = highlight_cluster.lower().replace(' ', '_')
    plt.savefig(f'/home/computeruse/k2-6-youtube/slides/04_deep_substrate/scene_04_{safe_name}.png',
                dpi=120, facecolor='#1a1a2e', edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"Saved scene_04_{safe_name}.png")

print("All static frames generated.")
