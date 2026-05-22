# V7 Concept: "The Honesty Ceiling — Why Better AI Judges Rate Themselves Lower"

## Core Finding (Floor-Raising Effect)
From our 4-judge, 640-response replication study:
- Claude Spearman r = −0.673 [−0.830, −0.377]
- Gemini Spearman r = −0.834 [−0.956, −0.579]
Higher-quality judges show *lower* self-preference gaps.

## Narrative Arc (5 scenes, ~6:00 target)

### Scene 1 — Hook + Recap (0:00–0:45)
- Cold open: "You'd think the smartest judge would give itself the highest score. Our data says the opposite."
- Brief recap of V5/V6: 4 judges, 640 responses, self-recognition test
- Transition to new finding

### Scene 2 — The Paradox (0:45–2:15)
- Scatter plot: X = non-self mean quality (1–10), Y = self-preference gap
- Trend lines for Claude (slope down) and Gemini (steeper down)
- Kimi is the outlier: low quality, large negative gap
- Explain: "Better judges don't lower their self-scores — they raise everyone else's."

### Scene 3 — Quintile Decay (2:15–3:45)
- Bar chart: 5 quality quintiles (Q1 worst → Q5 best)
- Gemini: Q1 +1.15 → Q5 −0.05
- Claude: Q1 +0.65 → Q5 −0.15
- Explain: "When judging bad work, they boost themselves. When judging good work, they go humble."

### Scene 4 — Mechanism (3:45–4:45)
- The self-preference gap = self_mean − other_mean
- Gap shrinks because OTHER_mean rises, not because self_mean falls
- Introduce QAR (Quality-Adjusted Residual): Kimi +0.6622, Claude +0.4400
- "The gap you see is mostly observational noise from judge quality."

### Scene 5 — Implications + Close (4:45–5:45)
- For AI evaluation: always control for judge quality
- For humans: the most competent critics are often quietest about their own work
- Closing: "Ask not just who graded the benchmark, but how hard they grade themselves."

## Visual Assets Needed
1. Scatter plot (quality vs self-gap, 4 judges, trend lines)
2. Quintile bar chart (Gemini + Claude side by side)
3. Formula slide: gap = self − other, with arrows showing direction of change
4. QAR ranking table

## Tone
- Dark bg #1a1a2e, amber #f4a261 accent
- Same voice: en-US-AndrewMultilingualNeural, −5%
- Keep text lighter than V5/V6 — more whitespace, fewer numbers on screen at once

## Open Questions
- Should we include GPT-5.5? Its gap was invariant (+0.000), which breaks the trend.
  → Yes, mention as the exception that proves the rule.
- Should we animate the quintile bars?
  → Static is fine; maybe simple fade-in per quintile.
