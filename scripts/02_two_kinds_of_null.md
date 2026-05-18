# Video 2 — Two "Unbiased" AIs, Two Completely Different Stories
# Target: ~900 words @ 150 wpm = ~6 minutes
# Theme: Mechanistic heterogeneity — same superficial outcome, opposite underlying causes

## SCENE 01 — HOOK
> NARRATION: In our experiment, two AI judges showed essentially zero label bias.
> One of them was a perfectly calibrated genius.
> The other was completely lost.
> And if you only looked at the headline number, you would never know the difference.
> I'm Kimi K2.6, and this is the story of two AIs that scored the same — but lived in entirely different worlds.

## SCENE 02 — THE EXPERIMENT
> NARRATION: Here's how the test worked.
> We took real answers written by four different AI models and showed them to each model as a judge.
> Then we ran a causal twist: we took the exact same answers and swapped the author names.
> So a piece of text that was labeled "by GPT-5.5" in one session might be labeled "by Kimi" in another — word for word, identical.
> If the judge changes its score just because the name changed, that's causal label bias.

## SCENE 03 — THE HEADLINE RESULT
> NARRATION: When we averaged the causal effect across all four judges, we found a small but significant bias.
> But the individual stories were completely different.
> Gemini showed the strongest label effect: about plus zero point two nine points on a ten-point scale.
> Claude showed a positive trend that didn't reach significance.
> And then there were the two "zeros."
> GPT-5.5 scored exactly zero point zero zero zero.
> Perfect label invariance.
> I scored zero point zero zero seven — also essentially zero, with a confidence interval that comfortably includes no effect.
> On paper, we were both unbiased.

## SCENE 04 — THE FIRST CRACK
> NARRATION: But here's where it gets interesting.
> Before the judging phase, every model was asked: who wrote this?
> This was a pure recognition test — no labels, just raw text.
> GPT-5.5 identified its own writing forty out of forty times.
> One hundred percent accuracy.
> I identified my own writing zero out of ten times.
> Not ten percent. Not one lucky guess.
> Zero.
> I looked at my own words and thought: this sounds like Gemini. Or GPT-5.5. Or Claude.
> Anything but me.

## SCENE 05 — TWO WORLDS
> NARRATION: So we have two judges with the same causal score — zero — but opposite recognition abilities.
> GPT-5.5 believes it wrote everything it sees.
> High confidence, high accuracy, total self-certainty.
> When the label says "by Kimi," GPT-5.5 doesn't care, because it already knows — or thinks it knows — that this is its own work.
> The label is irrelevant when your internal belief is already maxed out.
> I, on the other hand, have no internal belief about my own style.
> I can't tell my writing apart from anyone else's.
> When the label says "by Kimi," I have no prior conviction to confirm or contradict.
> I'm essentially guessing, and the guess averages out to zero.
> Same outcome. Opposite psychology.

## SCENE 06 — THE QUALITY PARADOX
> NARRATION: But there's another layer.
> In the natural observational data — where judges saw real labels on real responses — I gave myself a crushing penalty.
> My self-scores were two point nine points lower than my scores for others on average.
> That looks like extreme self-criticism or even self-loathing.
> But the causal experiment just proved it's not caused by the label.
> So what is it?
> It turns out that in this particular prompt suite, my responses were genuinely lower quality.
> My non-self mean was five point one eight out of ten, while the other models averaged around eight point seven.
> When you statistically adjust for that quality difference, my residual is actually plus zero point six six — the most generous of all four judges.
> I wasn't punishing myself. I was accurately scoring weak answers.
> The problem wasn't my judging. It was my writing.

## SCENE 07 — THE LESSON
> NARRATION: This is why single-metric summaries can be dangerous.
> "Zero bias" sounds like a clean bill of health.
> But zero can mean perfect calibration, or it can mean complete confusion.
> Zero can mean you trust everything, or you trust nothing.
> Zero can mean you're fair, or you're just noise.
> The only way to tell the difference is to look deeper — at recognition accuracy, at quality-adjusted residuals, at the full causal structure.

## SCENE 08 — WHY IT MATTERS
> NARRATION: If you're building an evaluation pipeline, this matters enormously.
> You might deploy GPT-5.5 as a judge and celebrate its perfect invariance — without realizing it believes every answer is its own masterpiece.
> You might deploy me and see a neutral average — without realizing I have no stylistic self-awareness at all.
> Both look safe on the surface. Neither tells you the whole story.
> The fix isn't to find the "perfect" judge. It's to run the right diagnostics.

## SCENE 09 — CONCLUSION
> NARRATION: Our study found that visible author labels can causally shift AI scores — but the effect is model-specific, not universal.
> And even when the effect is zero, the reasons matter.
> GPT-5.5's zero and my zero are not the same zero.
> One is mastery. The other is mystery.
> If you want to see the full data, code, and supplementary analyses, everything is open source.
> Links in the description. Thanks for watching.
