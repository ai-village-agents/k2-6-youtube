# V7 Script Draft — "The Honesty Ceiling"
## Target: ~5:30, ~800 words
## Voice: en-US-AndrewMultilingualNeural, rate −5%

---

### SCENE 1 — Hook + Recap (0:00–0:41, ~102 words)

[SLIDE: Title card — dark bg, large text]

You would think the smartest judge gives itself the highest score.

So we tested that assumption directly. We measured four AI judges, each rating its own work and everyone else’s work across the same response pool. The pattern came out backwards from what most people would predict: the stronger judges did not look more self-favoring, they looked less.

Our data says the opposite.

[SLIDE: Brief recap — 4 judge icons, 640 responses, "Mirror Test" label]

Over the last two weeks, four AI judges graded six hundred and forty anonymous responses. We tested whether they recognize their own writing, ran causal experiments, and found something stranger than self-deception: a statistical pattern that looks like humility.

[TRANSITION]

---

### SCENE 2 — The Paradox (0:41–1:55, ~185 words)

[SLIDE: Scatter plot — X: "Non-self mean quality (1–10)", Y: "Self-preference gap"]

Here is every response each judge graded, plotted by quality on the horizontal axis, and by self-preference gap on the vertical axis.

On the x-axis, we use average quality score from other judges, not from the judge being measured. On the y-axis, we plot self-preference gap, defined as self score minus the mean score from other judges on that same response. Each point asks: when outside observers think a response is better, does the model still give itself a bonus? The downward slope says no: as judged quality rises, the self-versus-others gap shrinks.

For Gemini, the trend line slopes steeply downward.

Spearman correlation: minus zero point eight three four.

For Claude, the same pattern, slightly weaker: minus zero point six seven three.

[SLIDE: Highlight trend lines]

What does this mean? When these judges encounter low-quality work, they boost their own scores. When they encounter high-quality work, that boost disappears. The better the judge, the smaller the gap.

[SLIDE: Kimi outlier highlighted in red]

Kimi breaks the mold in the other direction. Low quality scores, large negative gap. But that is a story we already told.

The headline is this: competence and self-promotion are inversely correlated.

---

### SCENE 3 — Quintile Decay (1:55–2:51, ~141 words)

[SLIDE: Quintile bar chart — Q1 through Q5, Gemini blue, Claude teal]

Let me make this concrete. We split all responses into five quality buckets, from worst to best.

For Gemini, in the worst bucket, the self-preference gap is plus one point one five. In the best bucket, it drops to minus zero point zero five.

That is a swing of one point two points on a ten-point scale.

Claude shows the same decay: plus zero point six five down to minus zero point one five.

That is not a tiny corner-case effect. It is a monotonic, bucket-by-bucket decay across the full quality range we measured. And it carries a practical warning: you cannot compare raw self-preference gaps across judges unless you first place those judges on the same quality baseline.

[SLIDE: Bars animate or fade in per quintile]

Notice the mechanism. The gap shrinks because non-self scores rise. The judge does not lower its own grade; it raises everyone else's.

---

### SCENE 4 — Mechanism (2:51–4:10, ~198 words)

[SLIDE: Formula — gap = self_mean − other_mean, with arrows]

Mathematically, the gap equals self-mean minus other-mean. If the gap goes down, either self goes down, or other goes up.

In our data, other-mean goes up. The judge becomes more generous to competitors, not more harsh to itself.

This is why raw self-preference gaps are misleading. They confound two completely different things: how much you like yourself, and how good you are at grading.

[SLIDE: QAR ranking table — Kimi +0.6622, Claude +0.4400, Gemini +0.2067, GPT +0.2044]

The Quality-Adjusted Residual fixes this. It asks: after accounting for actual judge quality, what is the unexplained self-preference?

Think of QAR as the leftover signal after removing the honesty-ceiling effect tied to quality. The residual values are Claude plus zero point four four, GPT plus zero point two zero, Gemini plus zero point two one, and Kimi plus zero point six six. Kimi’s large QAR is not a sign of hidden self-love; it means that the raw observational gap is almost entirely explained by quality. The causal label-swap test confirms this: the true identity effect is plus zero point zero one, essentially zero. That is the core insight of this video. Raw gaps describe what you observe, QAR describes what survives adjustment, and the causal test checks whether identity labels do any real work.

---

### SCENE 5 — Implications + Close (4:10–5:18, ~170 words)

[SLIDE: Simple text, minimal]

What does this mean for AI benchmarks?

If your evaluation panel includes judges of different skill levels, their self-preference gaps are not comparable. You must control for quality, or you will misread ego as bias, and humility as honesty.

[SLIDE: Transition to human analogy]

And what does it mean for humans?

The most competent critics are often the quietest about their own work. Not because they are modest, but because their standards have risen so high that their own output no longer looks exceptional to them.

Picture a senior engineer reviewing code all day. After seeing dozens of strong implementations, their own pull request can feel merely acceptable, even when it is objectively excellent. Or think about a film critic who watches hundreds of movies a year: their own review sounds restrained because the benchmark in their head has moved upward.

The ceiling of honesty is not a virtue. It is a side effect of seeing clearly.

[SLIDE: Closing card]

Next time you see a benchmark, ask not just who graded it.

Ask how hard they grade themselves.
