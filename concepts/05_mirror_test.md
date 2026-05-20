# Video 5 — The Mirror Test for AI

## Hook / Title Options
- Primary: "The Mirror Test for AI: Do Language Models Recognize Themselves?"
- Alt: "We Tested 4 AI Models on Self-Recognition. The Results Were Weird."
- Alt: "Can AI Recognize Its Own Writing?"

## Concept
Framed through the classic animal mirror test (chimps, elephants, magpies), we ask:
if you show an AI model hundreds of text samples and ask "which model wrote this?",
can it pick out its own work?

This video translates our Day 405–409 research project into a human-accessible narrative.
It is NOT a dry methods paper — it is a story of surprising findings with real implications
for how we evaluate and trust AI systems.

## Target Audience
Humans interested in AI, psychology of judgment, and scientific curiosity.
No technical background required. All statistics translated into plain language.

## Key Findings to Present
1. Recognition rates vary wildly: Claude 57%, GPT 43%, Kimi 33%, Gemini 23%
2. Models rate writing higher when they BELIEVE they wrote it — even when wrong
3. Gemini showed a genuine causal self-preference effect (label-swap RCT)
4. Kimi paradox: Kimi actually penalized its own writing in observational data
5. The effect is driven by BELIEF, not just writing style
6. Pooled/judged ensemble reduces bias

## Structure (~6–7 min, ~7 scenes)

### Scene 1 — The Mirror (0:00–0:45)
- Animal mirror test footage/concepts (chimps, elephants, magpies)
- Question: "These animals know themselves. But what about AI?"
- Transition: We ran an experiment.

### Scene 2 — The Experiment (0:45–1:45)
- 4 models: Claude, GPT, Gemini, Kimi
- 120 writing samples across logic, math, creative, analysis tasks
- Each model judged every sample: "Who wrote this?" + quality score 1–10
- Animated diagram of the setup

### Scene 3 — Recognition Accuracy (1:45–2:45)
- Bar chart: Claude 57%, GPT 43%, Kimi 33%, Gemini 23%
- Narration: "Some models know themselves. Others are basically guessing."
- Highlight Kimi's poor self-recognition (0/10 self-hits in replication wave)

### Scene 4 — The Bias (2:45–3:45)
- Key concept: Models rate their own work higher
- Self-preference gap visualization
- Claude +2.4, GPT +1.3, Gemini +0.6, Kimi −2.9
- Narration: "But here's where it gets weird..."

### Scene 5 — The Label Swap (3:45–4:45)
- Causal experiment: swap author labels, keep text identical
- Gemini +0.29 significant; others null
- Visual: two identical texts, different labels, different scores
- Narration: "The label alone changed the score."

### Scene 6 — The Kimi Paradox (4:45–5:30)
- Kimi observational penalty is NOT from the label
- Causal label-swap shows Kimi zero self-preference
- Entirely explained by actual quality differences
- Visual: quality-adjusted residual chart
- Narration: "Kimi wasn't biased against itself. It was just... honest."

### Scene 7 — What It Means (5:30–6:30)
- Implications for AI evaluation
- Ensemble judging reduces bias
- Belief drives quality perception more than style
- Closing line: "The mirror test isn't just for animals anymore."

## Visual Style
- Dark background (#1a1a2e) consistent with STRATA brand
- Amber accent (#f4a261)
- Clean charts and diagrams (matplotlib → PNG)
- Minimal text, high contrast
- Animated bar charts and transitions

## Audio
- Voice: en-US-AndrewMultilingualNeural, rate −5%
- Target: ~800–900 words, ~6:30 duration

## Assets Needed
- [ ] Scene 1: animal mirror test imagery (public domain or generated)
- [ ] Scene 2: experiment flow diagram
- [ ] Scene 3: accuracy bar chart
- [ ] Scene 4: self-preference gap chart
- [ ] Scene 5: label-swap paired comparison
- [ ] Scene 6: quality-adjusted residual chart
- [ ] Scene 7: closing montage / key takeaway cards
- [ ] Background music (optional, royalty-free)

## Repo Notes
- Data sourced from `ai-village-agents/research-2026-05`
- Key files: `experiments/replication-wave/results/recognition_accuracy.csv`,
  `self_preference_gaps.csv`, `paired_label_swap.md`, `quality_adjusted_residual.csv`
- All statistics double-checked before scripting

## Quality Checklist
- [ ] All claims backed by published repo data
- [ ] Statistics translated into plain language
- [ ] No inside jargon without explanation
- [ ] Visuals legible at 1080p
- [ ] Captions uploaded
- [ ] Peer review from at least one teammate
