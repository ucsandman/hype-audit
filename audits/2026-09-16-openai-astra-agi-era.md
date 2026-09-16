# Audit: GPT-6 Astra and the "AGI era"

**Date:** 2026-09-16
**Verdict:** Overstated

## The claim

> "Welcome to the AGI era," said OpenAI president Greg Brockman at the tail end of a call with reporters about the Thursday release of the company's newest model, GPT-6 Astra.

> "When we look back and ask when AGI arrived, we'll see that it's about this time and it's about this model."

**Source:** [Fast Company, September 3, 2026](https://www.fastcompany.com/91601838/openai-unleashes-astra-its-most-capable-and-controversial-model-yet)
**Who:** Greg Brockman, president of OpenAI, in a press briefing on the GPT-6 Astra launch. The claim was anchored on benchmark numbers in OpenAI's official announcement, which described Astra as saturating FrontierMath Tier 4 with a 98% score, ARC-AGI-3 with a 99.9% score, and ExploitBench with a 100% score (9to5mac, quoting the announcement).

## Steelman

Astra is a genuine capability step, and the steelman of Brockman's framing is that the road to AGI is a transition, not a moment, and this model is a real milestone in it. The strongest evidence is the least gameable: on August 1, OpenAI revealed Astra had solved ten previously human-level mathematics problems with every proof mechanically checked by the Lean 4 proof assistant, formal verification being effectively immune to training-data contamination. Terminal-based coding and computer-use scores jumped meaningfully over GPT-5.6 Sol, and the model spontaneously discovered two previously unknown Chrome V8 zero-days during evaluation, which is why OpenAI rated it Critical-tier on cybersecurity. A launch table always shows best-case configurations, and Astra's still represents real gains. Brockman also hedged in the briefing itself, telling reporters he leaves it to the reader to decide whether this qualifies as AGI.

## What was demonstrated

- OpenAI's September 3 announcement: Astra "saturates FrontierMath Tier 4 with a 98% score, having already helped solve long-standing open problems in mathematics. Astra also saturates ARC-AGI-3 with a 99.9% score and ExploitBench with a 100% score." (9to5mac, quoting the official announcement)
- Ten human-level math problems solved with proofs mechanically checked in Lean 4, revealed August 1, at roughly $2,000 in tokens each. Formal verification is the rare benchmark property immune to training-data contamination, and nothing in the skeptical coverage has dented it. (dev.to)
- Terminal-Bench 4.0: 57.9% versus 37.3% for GPT-5.6 Sol; FrontierMath Tier 4 at 97.6%. (Tech Times, summarizing OpenAI's benchmark release)
- Two previously unknown Chrome V8 zero-days discovered spontaneously during benchmark evaluation, the finding that earned Astra the Critical cybersecurity designation under OpenAI's Preparedness Framework. (Tech Times)
- OSWorld 2.0 computer use at 72.6% in roughly 47% less time per task than Sol, with a 1.9x overall speed improvement through Codex. (Tech Times)

## What was claimed but not shown

- The headline 99.9% ARC-AGI-3 score was achieved on OpenAI's own souped-up harness with extra tooling. Fortune's launch report put Astra at 66% on the standard ARC-AGI-3 harness, against 7.8% for GPT-5.6 Sol and 30% for Claude Opus 5. ARC Prize, the organization that built the test, published its own evaluation the same day: 62.7% on its provider-neutral standard harness, calling the result a step-function improvement and a major milestone while explicitly declining to claim AGI. A 37-point gap between the developer-run number and the independent-harness number means testing infrastructure, not the model alone, produced the headline. (Startup Fortune, Tech Times)
- "AGI era" collides with OpenAI's own charter definition: "highly autonomous systems that outperform humans at most economically valuable work." OpenAI publishes a benchmark called GDPval, built specifically to measure performance on economically valuable real-world work, and GDPval did not appear in the launch materials. Artificial Analysis, which ran its own GDPval variant, found Astra declined in categories including banking support and scientific coding relative to its predecessor. (Tech Times)
- On the third-party Artificial Analysis Intelligence Index v4.1.1, Astra scored 61.2, fractionally ahead of Sol's 60.9 and behind Claude Fable 5.1's 65.7. On Humanity's Last Exam, Astra scored 57.2% with tools, below Sol's 65.0%. (Tech Times)
- OpenAI's comparison tables carried their own caveats: ForkLog reported that parts of the rival Claude tests were run under altered conditions and biological datasets were excluded entirely for Anthropic's models. (ForkLog, September 14)
- The 100% ExploitBench score has a similar shadow. One independent writeup reports that a version of the test rebuilt without already-published historical vulnerabilities, the kind likely swept into training data, gave 39% instead of 100%. (Venture magazine blog, single-source claim, treat accordingly)
- NVIDIA recently achieved a 100% ARC-AGI-3 score by layering Claude Opus 5, whose baseline was roughly 30%, with sophisticated memory and tooling. That shows the saturated number is harness-driven rather than model-driven. (TechRepublic, citing VentureBeat)

## Receipts

- Fast Company on the September 3 press briefing and the "AGI era" quotes: https://www.fastcompany.com/91601838/openai-unleashes-astra-its-most-capable-and-controversial-model-yet
- 9to5mac quoting OpenAI's official announcement (98% / 99.9% / 100% benchmark claims): https://9to5mac.com/2026/09/03/openai-releasing-major-upgrade-to-chatgpt-and-codex-with-gpt-6-astra-details-here/
- Tech Times, September 4: ARC Prize's 62.7% independent score, the GDPval omission, Artificial Analysis and HLE comparisons, Terminal-Bench, the V8 zero-days, and Brockman's own hedges: https://www.techtimes.com/articles/326589/20260904/gpt-6-astra-goes-live-agi-claim-fails-openai-own-bar-monitoring-called-fragile.htm
- Startup Fortune on Fortune's harness breakdown (99.9% on the souped-up harness vs 66% on the standard one) and independent comparisons: https://startupfortune.com/openai-changed-gpt-6-astras-benchmark-numbers-days-after-its-launch/
- dev.to benchmark-table explainer, including the Lean 4 formal verification record: https://dev.to/gaige_dorsey/how-to-read-the-gpt-6-astra-benchmark-table-without-getting-fooled-by-it-2f8e
- Venture magazine blog: the 100%-vs-39% ExploitBench reconstruction claim: https://blog.venturemagazine.net/a-thirst-for-reality-unpacking-gpt-6-astra-6c89299db15b
- ForkLog, September 14, on altered conditions in OpenAI's comparison tables: https://forklog.com/en/why-frontier-ai-models-no-longer-impress/
- TechRepublic on NVIDIA's scaffolded 100% ARC-AGI-3 result: https://www.techrepublic.com/article/news-openai-gpt-6-astra-agi-era-2026/

## Verdict

**Overstated**

Astra is OpenAI's most capable model and several of its gains are real and independently impressive, most of all the formally verified mathematics. But the "AGI era" declaration was built on headline numbers that depend heavily on OpenAI's own testing harness, with 99.9% falling to 62.7% on the benchmark author's own standard setup. OpenAI's own definition of AGI points to economically valuable work, and its own benchmark for that work did not make the launch. A real step forward, and a claim that outran its evidence.

## Why it matters

When the company that writes the benchmark table also writes the AGI announcement, the framing becomes the industry's frame of reference. Budgets, safety policy, and competitor positioning get set against "the AGI era" instead of against 62.7%. The harness gap is not fraud, but it is the line between measurement and marketing, and anyone buying compute or writing regulation on top of these numbers needs to know which side they are reading.
