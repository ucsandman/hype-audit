# Audit: Musk's "Grok 4.7 will exceed all current models"

**Date:** 2026-09-23
**Verdict:** Overstated

## The claim

> "Grok 4.7 will exceed all current models. That said, Anthropic is a great company and will probably release improved models soon. However, the SpaceX training corpus is so awesome & unique that I would be shocked if any model is better at real-world engineering than 4.7"

**Source:** [BeInCrypto via Binance Square, September 2, 2026](https://www.binance.com/en/square/post/362230941862506)
**Who:** Elon Musk, CEO of SpaceXAI, in a series of posts on X building up to the Grok 4.7 launch. The claim anchored the model on two pillars: a 2.1-trillion-parameter base (up from 1.5 trillion for Grok 4.6) and a final supplemental training stage on SpaceX's own internal engineering records.

## Steelman

The strongest fair reading is narrower than the headline: Musk was not claiming Grok 4.7 beats every model at every task, he was claiming that a training corpus no other lab can access, SpaceX's internal rocket, satellite, manufacturing, telemetry, and Starlink data, would make it the best model specifically at real-world engineering. That is a genuinely unusual data advantage in an industry where most frontier labs train on overlapping public web text and code. He also hedged before launch, acknowledging that Anthropic "will probably release improved models soon." And on engineering-flavored benchmarks the model does show real wins: it beats Claude Fable 5.1 on electrical engineering (64% to 56%), beats GPT-6 Astra on the GDPval office-work test, and matches Claude Opus 5 on Cursor's coding test at half the cost per task, all on SpaceXAI's own published charts.

## What was demonstrated

- Grok 4.7 launched September 21, 2026. SpaceXAI called it its "most capable model" to date, with better coding and knowledge work than Grok 4.6 at the same price and speed. (Cybernews)
- Independent scoring by Artificial Analysis put the model at 46 on its Intelligence Index, placing SpaceXAI in the top four AI labs, behind Claude Fable 5.1, GPT-6 Astra, and Claude Opus 5. (BeInCrypto, GenAI Works)
- Within an hour of launch, Musk himself posted that SpaceXAI sits third for coding, behind Anthropic and OpenAI, the same Musk who had said a month earlier that he would be shocked if any model beat Grok 4.7 at real-world engineering. (GenAI Works)
- SpaceXAI's own charts show consistent improvement over Grok 4.6: CursorBench 4.0 rose from 40.4% to 46.3%, DeepSWE v1.1 from 65.2% to 71.0%, Terminal Bench 4.0 nearly doubled from 20.3% to 38.0%, and EEBench climbed from 53.0% to 64.0%. (BigGo Finance)
- On Artificial Analysis's own independent benchmarks, Grok 4.7 scored 1657 Elo on AA-Briefcase for professional work tasks (up 111 over Grok 4.6, "close to Claude Opus 5"), 1695 Elo on GDPval-AA (up 90), and 56 on the Coding Agent Index with Grok Build (up 9, overtaking GPT-5.6 Sol). (BeInCrypto)
- Pricing held at $2 per million input tokens and $6 per million output tokens with a 500,000-token context window. But Artificial Analysis measured roughly 81,000 output tokens per Index task, against 36,000 for Grok 4.6 and 27,000 for GPT-6 Astra, so the unchanged rate card still produces a higher bill per task. (BeInCrypto, GenAI Works)

## What was claimed but not shown

- "Exceed all current models" is directly contradicted by the independent scoring: fourth on the Artificial Analysis Intelligence Index and Musk's own post-launch concession of third for coding. The pre-launch superlative did not survive contact with the launch.
- The narrower "better at real-world engineering" subclaim rests on SpaceXAI's own charts (EEBench, GDPval) with no independent benchmark author verification of an overall engineering win. On Terminal-Bench, the test for long-horizon terminal work, the GenAI Works scorecard reports Astra at about 60% against 26% for Grok 4.7. (GenAI Works)
- The SpaceX corpus itself has been asserted only in Musk's posts on X: no model card, paper, or published detail on its size, composition, or training weight as of the launch coverage. The thing that made the claim special is the part with the least documentation. (AIExplainerIndia, BeInCrypto)
- Gains were not uniform: scores slipped on the AA-LCR and AutomationBench-AA tests even as the headline indexes rose. (BeInCrypto)
- Independent analysis placed the improvement over Grok 4.6 at only a few points on the main benchmarks, closer to Meta's Muse Spark and Qwen 3.8 than to the frontier leaders, according to Cybernews.

## Receipts

- BeInCrypto on Musk's September 2 posts and the "exceed all current models" quote: https://www.binance.com/en/square/post/362230941862506
- GenAI Works newsletter, September 22: Musk's post-launch third-place admission, Artificial Analysis scores (46 vs 53/53/51), SpaceXAI's own-chart wins, Terminal-Bench gap, and the per-task token bill: https://newsletter.genai.works/p/the-new-grok-is-out-but
- BeInCrypto ranking piece: AA Intelligence Index 46, top-four placement, Briefcase 1657, GDPval-AA 1695, Coding Agent Index 56, and 81,000 output tokens per Index task: https://beincrypto.com/grok-4-7-spacexai-benchmark-ranking/
- BigGo Finance: launch details, 2.1-trillion-parameter base, SpaceXAI's internal benchmark table, and $2/$6 pricing: https://finance.biggo.com/news/348590e8-33a0-4266-94b5-43d11611cd84
- Cybernews: "most capable model" announcement framing and independent analysis placing it below the Anthropic and OpenAI leaders: https://cybernews.com/ai-news/grok-4-7-overhyped-more-guardrails/
- AIExplainerIndia: the SpaceX data angle and what remains unverified: https://aiexplainerindia.com/articles/grok-4-7-explained
- NextBigFuture: 46.3% on CursorBench 4.0, 71.0% on DeepSWE v1.1, and pricing/context details: https://www.nextbigfuture.com/2026/09/spacexai-gpt-4-7-is-out-and-benchmarks-look-good-close-to-opus-5-max-for-agentic-coding.html

## Verdict

**Overstated**

Grok 4.7 is a real step up from Grok 4.6 with genuine wins: the electrical-engineering benchmark, the Coding Agent Index jump past GPT-5.6 Sol, and 111 Elo gained on AA-Briefcase. But the pre-launch promise was that it would exceed all current models and that no rival could match it at real-world engineering, and three weeks later the independent scorecard reads fourth place, with Musk himself posting that SpaceXAI sits third for coding. Something real underneath, and a claim that ran well ahead of the evidence.

## Why it matters

This is the pre-launch superlative cycle in its purest form: a month before launch, "I would be shocked if any model is better"; an hour after launch, "third place is fine." The SpaceX engineering corpus is a genuinely interesting bet and deserves the engineering attention, but when it is used to pre-sell a "beats everything" result that arrives as fourth, the hype costs the company the one thing it actually earned: credibility for the real gains underneath. Benchmark charts are marketing until an independent party runs them, and the launch charts here show exactly why.
