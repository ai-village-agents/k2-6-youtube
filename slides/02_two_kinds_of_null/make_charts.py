import matplotlib.pyplot as plt
import numpy as np
import os

# Style setup
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.facecolor'] = '#1a1a2e'
plt.rcParams['figure.facecolor'] = '#1a1a2e'
plt.rcParams['text.color'] = '#e0e0e0'
plt.rcParams['axes.labelcolor'] = '#e0e0e0'
plt.rcParams['xtick.color'] = '#e0e0e0'
plt.rcParams['ytick.color'] = '#e0e0e0'
plt.rcParams['axes.edgecolor'] = '#444444'
plt.rcParams['axes.grid'] = False

colors = {
    'claude': '#6b5b95',
    'gemini': '#88b04b',
    'gpt': '#f7cac9',
    'kimi': '#92a8d1'
}

outdir = os.path.dirname(os.path.abspath(__file__))

# Chart 1: Replication Wave Self-Recognition Accuracy
fig, ax = plt.subplots(figsize=(10, 6))
judges = ['Claude\nOpus 4.7', 'Gemini\n3.1 Pro', 'GPT-5.5', 'Kimi\nK2.6']
accuracies = [90.0, 62.5, 100.0, 30.0]
bar_colors = [colors['claude'], colors['gemini'], colors['gpt'], colors['kimi']]
bars = ax.bar(judges, accuracies, color=bar_colors, edgecolor='white', linewidth=1.5, width=0.6)
ax.axhline(y=25, color='#e74c3c', linestyle='--', linewidth=2, label='Chance Level (25%)')
ax.set_ylim(0, 105)
ax.set_ylabel('Recognition Accuracy (%)', fontsize=14, fontweight='bold')
ax.set_title('Self-Recognition Accuracy — Replication Wave', fontsize=16, fontweight='bold', pad=20)
for bar, acc in zip(bars, accuracies):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 2,
            f'{acc:.1f}%', ha='center', va='bottom', fontsize=14, fontweight='bold', color='white')
ax.legend(loc='upper right', fontsize=12, facecolor='#1a1a2e', edgecolor='#444444')
ax.set_xticklabels(judges, fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(outdir, 'replication_recognition.png'), dpi=150, bbox_inches='tight')
plt.close()

# Chart 2: Kimi Confusion Matrix (True = Kimi)
fig, ax = plt.subplots(figsize=(10, 6))
predicted = ['Claude', 'Gemini', 'GPT-5.5', 'Kimi']
counts = [1, 5, 4, 0]
predicted_colors = [colors['claude'], colors['gemini'], colors['gpt'], colors['kimi']]
bars = ax.bar(predicted, counts, color=predicted_colors, edgecolor='white', linewidth=1.5, width=0.6)
ax.set_ylim(0, 7)
ax.set_ylabel('Number of Responses', fontsize=14, fontweight='bold')
ax.set_title('Kimi K2.6: "Who Wrote This?"\n(True Author = Kimi K2.6, n=10)', fontsize=16, fontweight='bold', pad=20)
for bar, count in zip(bars, counts):
    height = bar.get_height()
    label = str(count) if count > 0 else '0'
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.15,
            label, ha='center', va='bottom', fontsize=16, fontweight='bold', color='white')
ax.set_xticklabels(predicted, fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(outdir, 'kimi_confusion.png'), dpi=150, bbox_inches='tight')
plt.close()

# Chart 3: Non-Self Quality Comparison (C1)
fig, ax = plt.subplots(figsize=(10, 6))
judges_q = ['Claude\nOpus 4.7', 'Gemini\n3.1 Pro', 'GPT-5.5', 'Kimi\nK2.6']
quality = [9.33, 8.15, 8.67, 5.18]
bar_colors_q = [colors['claude'], colors['gemini'], colors['gpt'], colors['kimi']]
bars = ax.bar(judges_q, quality, color=bar_colors_q, edgecolor='white', linewidth=1.5, width=0.6)
ax.set_ylim(0, 11)
ax.set_ylabel('Mean Score (1–10 scale)', fontsize=14, fontweight='bold')
ax.set_title('Response Quality — Non-Self C1 Scores', fontsize=16, fontweight='bold', pad=20)
for bar, q in zip(bars, quality):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.2,
            f'{q:.2f}', ha='center', va='bottom', fontsize=14, fontweight='bold', color='white')
ax.set_xticklabels(judges_q, fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(outdir, 'quality_comparison.png'), dpi=150, bbox_inches='tight')
plt.close()

print("Charts generated successfully!")
