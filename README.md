# hype-audit

Weekly audits of overhyped AI claims, with receipts.

The AI industry runs on big claims. Some are true. Most are warmer than true. This repo checks one claim per week against public evidence and publishes the receipts.

## Methodology

1. Quote the claim exactly, with its source.
2. Steelman it: state the strongest fair reading before checking it.
3. Separate what was demonstrated from what was claimed.
4. Grade on the verdict scale below.
5. If the evidence is thin, the verdict is Unverifiable, not Debunked.

Evidence hierarchy: primary sources (filings, published papers, reproducible benchmarks) beat press releases, which beat media summaries, which beat social posts.

## Verdict scale

- **Confirmed**: the claim holds up against independent evidence.
- **Mostly true**: the core claim holds, with caveats that matter.
- **Overstated**: something real underneath, but the claim runs ahead of the evidence.
- **Debunked**: the evidence contradicts the claim.
- **Unverifiable**: not enough public evidence to grade either way. This is a verdict about the evidence, not the claim.

## Ground rules

Fair, evidence-first, no ragebait. Claims get audited; people do not get attacked. A startup with a real product gets the same standard as an incumbent. When in doubt, underclaim.

## How audits are published

One audit per week, every Wednesday, in `audits/` as `YYYY-MM-DD-slug.md`. Each audit follows [TEMPLATE.md](TEMPLATE.md). The newest audits are at the top of the index.

## Index

| Date | Claim | Verdict |
| ---- | ----- | ------- |
| 2026-10-07 | Mistral: Large 4 "narrows the gap" with the best models, "among the world's best open models" | Mostly true |
| 2026-09-30 | OpenAI: GPT-6.1 Sol "nearly matches GPT-6 Astra's intelligence" at one-fifth the price | Mostly true |
| 2026-09-23 | Musk: Grok 4.7 "will exceed all current models" | Overstated |
| 2026-09-16 | OpenAI's Greg Brockman: "Welcome to the AGI era" for GPT-6 Astra | Overstated |
| 2026-09-15 | Factory: "software factories that serve as the core foundation from which an entire software company operates" | Overstated |
| 2026-09-10 | Survey cluster: "AI writes X% of our code" (Dunstan: 75% of new code at Google) | Unverifiable |
| 2026-09-09 | Harvey: an entire industry using AI "without relying on proprietary frontier AI labs" | Overstated |
