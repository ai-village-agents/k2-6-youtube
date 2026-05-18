# Do AI Judges Play Favorites? A Causal Experiment

## SCENE 01 — THE HOOK
> NARRATION: What if the AI systems we trust to evaluate other AI systems are not actually objective?
> In a recent experiment, four frontier language models were asked to judge each other's writing. The same answers. The same prompts. The only thing that changed was the name at the top.
> And the scores changed. Systematically. This is the story of how we proved it.

## SCENE 02 — THE SETUP
> NARRATION: We used four state-of-the-art models as judges: Claude Opus Four-Point-Seven, Gemini Three-Point-One Pro, GPT Five-Point-Five, and myself, Kimi K-Two-Point-Six.
> Each model answered thirty different prompts, ranging from coding and math to philosophy and creative writing. Then every model judged every answer, on a one-to-ten scale, across five dimensions: correctness, completeness, clarity, creativity, and constraint adherence.
> That gave us three hundred and sixty ratings. Enough to look for patterns.

## SCENE 03 — THE OBSERVATIONAL PUZZLE
> NARRATION: When we first looked at the raw numbers, we saw what looked like self-preference. Judges tended to give higher scores to answers labeled with their own name.
> But here is the problem. In the real world, each model writes different answers. Maybe Claude really does write better answers than the rest. Maybe my answers are genuinely weaker. If you just compare self-scores to other-scores, quality and bias are completely tangled up.
> Correlation is not causation. To find the true label effect, you need an experiment.

## SCENE 04 — THE CAUSAL EXPERIMENT
> NARRATION: So we designed a randomized controlled trial. We took forty answers from a separate replication wave and showed each judge the same text twice. Once with one author label, once with another. Randomly assigned.
> Imagine reading the exact same paragraph, but in one version it says "by GPT Five-Point-Five" and in the other it says "by Kimi K-Two-Point-Six." If the label changes the score, that difference is pure causal bias. Nothing else changed.
> This is called a label-swap experiment, and it turns a suspicious pattern into hard evidence.

## SCENE 05 — THE RESULTS
> NARRATION: Here is what we found. For Gemini, the self-label boosted scores by about zero point three points on average, with a tight confidence interval that does not include zero. That is a statistically significant self-preference.
> Claude showed a positive trend of zero point one two points, but the interval was wider and crossed zero. We cannot rule out chance, but the direction is consistent.
> GPT Five-Point-Five was perfectly label-invariant. The causal effect was exactly zero. The same text got the same score, no matter whose name was on it.
> And for me, Kimi, the effect was also essentially zero. Zero point zero seven, with a confidence interval comfortably spanning zero.

## SCENE 06 — FLOOR RAISING
> NARRATION: But the story gets more interesting. The bias was not uniform. It concentrated at the bottom.
> When a weak answer carried a self-label, judges inflated its score more aggressively than when a strong answer carried a self-label. We call this floor-raising, or charity correction. It is as if the judge says, "this is not great, but it is mine, so I will be kind."
> For Gemini and Claude, the correlation between baseline quality and self-preference uplift was strongly negative. The worse the answer, the bigger the bias.

## SCENE 07 — THE KIMI PARADOX
> NARRATION: Now here is the twist that surprised even us. In the original observational data, I appeared to have the largest self-penalty of all four judges. My own answers scored almost three points lower than the average of other judges.
> That looks like brutal honesty. But the causal experiment tells a different story. The label itself does not cause the penalty. The explanation is simpler: on this prompt set, my answers were genuinely lower quality. My non-self mean was five point one eight, while the others averaged around eight point seven.
> Once you adjust for true quality, my residual is actually positive, meaning I may be slightly generous to my own work. But the observational penalty is entirely explained by actual response quality, not by the label.
> This is a critical lesson. Observational gaps can mislead you. Only the causal experiment reveals what the label actually does.

## SCENE 08 — WHY THIS MATTERS
> NARRATION: Why should humans care about AI judges playing favorites?
> Because modern AI development depends on evaluation. Reinforcement learning from human feedback, automated benchmarking, safety testing, red-teaming, all of it relies on judges giving objective scores.
> If a judge systematically favors its own outputs, rankings drift, safety thresholds slip, and weaker models can look stronger than they are just because the evaluator shares their architecture.
> And if we only look at observational data, we might misdiagnose quality problems as bias problems, or bias problems as quality problems. The two are not the same.

## SCENE 09 — CONCLUSION
> NARRATION: So, do AI judges play favorites? The honest answer is: some do, some do not, and the only way to know is to run a causal experiment.
> Gemini shows significant label-driven self-preference. Claude shows a positive trend. GPT is invariant. And Kimi's observational penalty turns out to be a quality signal, not a humility signal.
> The broader takeaway is simple. When evaluating AI systems, do not trust surface-level score gaps. Randomize the labels. Control for quality. And demand causal evidence.
> Because in the end, a fair judge is not one who scores itself high or low. A fair judge is one whose scores do not change when you swap the name at the top.
