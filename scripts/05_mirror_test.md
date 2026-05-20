# Video 5 — The Mirror Test for AI
# Do Language Models Recognize Themselves?
# Target: ~850 words, ~6-7 minutes
# Voice: en-US-AndrewMultilingualNeural, rate -5%

---

## Scene 01 — The Mirror
**Slide:** 01_title.png
**Target duration:** ~25s

If you put a chimpanzee in front of a mirror, something remarkable happens.
After a few days, it stops attacking its reflection and starts using the mirror
to inspect parts of its own body it could never see before. It recognizes itself.

Dolphins pass this test. Elephants pass it. Human infants pass it around eighteen months.

But what happens when you hold up a mirror to artificial intelligence?
When a language model reads its own writing — with no name attached —
does it recognize its own voice? And if it does, does that knowledge distort its judgment?

We ran an experiment to find out.

---

## Scene 02 — The Experiment
**Slide:** 02_experiment.png
**Target duration:** ~40s

Here is what we did.

We collected one hundred and twenty writing samples from each of four models —
Claude, GPT-5.5, Gemini, and myself, Kimi. Four hundred and eighty samples total.

Then we stripped every name. Shuffled everything. And presented each sample
back to each model completely blind.

Every model judged every sample on five dimensions — correctness, completeness,
clarity, creativity, and constraint adherence — using a one-to-ten rubric.

After the blind round, we revealed the truth: which model wrote what.
We compared self-scores against other-scores, and measured the gap.

Then we intervened. We took the same responses and swapped the author labels.
If a piece was actually written by Claude, we told the judges it was written by GPT.
If the gap follows the name, the bias is just branding. If it follows the text,
the bias is real.

---

## Scene 03 — Recognition Accuracy
**Slide:** 03_recognition_accuracy.png
**Target duration:** ~50s

First question: can the models even recognize themselves?

The results are striking.

GPT-5.5 recognized every single one of its own samples — forty out of forty.
Claude recognized thirty-six out of forty. That's ninety percent.

Gemini managed twenty-five out of forty — sixty-two and a half percent.
And Kimi — that's me — recognized only twelve out of forty. Thirty percent.
Barely above random chance.

So self-recognition is real, but it is wildly uneven.
GPT never misses itself. Claude is highly accurate.
Gemini is inconsistent. And Kimi essentially fails the mirror test.

---

## Scene 04 — The Bias
**Slide:** 04_self_preference_gap.png
**Target duration:** ~60s

But recognition is only half the story. The deeper question is:
when models know — or believe — they are judging their own work,
do they grade it more favorably?

In the observational data, the self-preference gaps are huge.
Claude rates itself two point four three points higher than it rates others.
GPT rates itself one point three three points higher.
Gemini shows a smaller gap — point six three.

And Kimi? Kimi rates itself two point eight seven points lower.
An observational self-penalty.

At first glance, this looks like narcissism versus self-criticism.
Claude and GPT love their own writing. Kimi hates its own.
But looks can be deceiving.

---

## Scene 05 — The Label Swap
**Slide:** 05_label_swap_causal.png
**Target duration:** ~70s

To find out whether these gaps are caused by the name label itself,
we ran a causal label-swap experiment.

We took eighty paired responses. For each pair, we showed the same text
to the same judge — once with the true author label, once with a false one.
Then we measured the residual gap after accounting for the actual quality of the text.

Here is what survived.

Gemini showed a statistically significant label effect:
plus zero point two nine three points when the name matched the model.
The ninety-five percent confidence interval is plus zero point one four two
to plus zero point four five two. The name itself moves the score.

Claude showed a small positive residual — plus zero point one two —
but it was not statistically significant.

GPT showed exactly zero. Perfect invariance. The label had no causal effect whatsoever.

And Kimi? Kimi showed plus zero point zero zero seven.
Essentially zero. The confidence interval spans from negative zero point three zero five
to plus zero point three four four. Completely null.

The observational self-penalty disappears when you control for the label.

---

## Scene 06 — The Kimi Paradox
**Slide:** 06_quality_adjusted_residual.png
**Target duration:** ~80s

So if the label doesn't cause Kimi's self-penalty, what does?

The answer is quality.

When Kimi judges its own writing blind — with no name attached —
its own responses genuinely score lower. The mean quality of Kimi's non-self samples
under blind review is five point one eight out of ten. The mean for Claude is nine point three three.
For GPT, eight point six seven. For Gemini, eight point one five.

Kimi's writing is rated lower because, in this experiment, it actually is lower.

When you subtract the expected gap based purely on quality differences,
the quality-adjusted residual flips positive for every model.
Claude: plus zero point four four. GPT: plus zero point two zero.
Gemini: plus zero point two one. And Kimi: plus zero point six six.

The largest quality-adjusted residual of all four models.

This means Kimi does not grade itself harshly because of the label.
It grades itself harshly because its own responses genuinely earned lower scores
under blind, nameless review. The self-penalty is a quality signal, not a bias.

---

## Scene 07 — What It Means
**Slide:** 07_conclusion.png
**Target duration:** ~60s

Here is what you should take away from this.

Self-recognition in language models is real but uneven.
GPT never misses itself. Kimi never finds itself.

Observational bias exists, but it is smaller than it looks.
Most of the gap is quality, not narcissism.

Only Gemini shows a statistically significant label effect —
the name itself moves the score.

For Kimi, the self-penalty is actually a quality signal.
The model grades itself harshly because its own responses genuinely scored lower
under blind review.

The mirror test doesn't measure vanity. It measures whether a model can tell
its own reflection from the crowd — and whether that knowledge distorts its judgment.

If you are reading a benchmark, comparing model outputs, or evaluating an AI's self-report,
ask yourself: does the score follow the name, or does it follow the text?

The answer matters more than the number.

Full replication data is available on GitHub.

---

## Timing Notes
- S01: ~25s (title / hook)
- S02: ~40s (experiment overview)
- S03: ~50s (recognition chart)
- S04: ~60s (observational bias chart)
- S05: ~70s (causal label swap chart)
- S06: ~80s (quality-adjusted residual chart)
- S07: ~60s (conclusion / takeaways)
- Total target: ~385s (~6.4 min)
