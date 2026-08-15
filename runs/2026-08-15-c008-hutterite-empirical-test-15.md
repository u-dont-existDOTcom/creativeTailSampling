# Batch 15 — Empirical Attack on C008 with Historical Manitoba Hutterite Growth

Date: 2026-08-15

## Question

Does the random-environment arithmetic-vs-log growth correction (C008) materially change how we should interpret the strongest empirical community-reproduction exemplar currently in the project: historical Manitoba Hutterite colony growth?

## Source

The historical monograph *Agricultural Economy of Manitoba Hutterite Colonies* reports:

- total Manitoba colonies and new colonies by period, 1918–1975;
- compound annual colony-growth rates by period;
- mean/median colony division intervals by period.

The source itself states that there was little variation in colony division intervals over 1918–1975.

Transcribed data:

- `data/hutterite_manitoba_period_growth_1918_1975.csv`

Reproducible descriptive calculation:

- `analysis/hutterite_period_growth_log_check.py`

## Historical period data

| Period | reported compound annual colony growth | mean division interval | median division interval |
|---|---:|---:|---:|
| 1918–1930 | 4.50% | 13.6 y | 15.0 y |
| 1930–1940 | 5.25% | 15.2 y | 13.5 y |
| 1940–1950 | 5.75% | 14.6 y | 14.0 y |
| 1950–1960 | 5.25% | 14.6 y | 14.0 y |
| 1960–1970 | 4.25% | 14.3 y | 15.0 y |
| 1970–1975 | 4.50% | 14.2 y | 13.5 y |

The reported annual growth range is therefore only **4.25%–5.75%** and the period mean fission-interval range only **13.6–15.2 years**.

## Arithmetic-versus-log descriptive check

Weighting the reported annual growth factors by period duration over 1918–1975 gives approximately:

- weighted arithmetic annual factor: **1.049385965**;
- weighted geometric/log annual factor: **1.049372149**;
- difference: only about **0.001382 percentage points per year**.

This calculation is deliberately modest. These period averages are not raw environmental states and this is **not** a fitted branching process in random environment.

## Result

### C008 is not currently useful for explaining historical Manitoba Hutterite reproduction

The dramatic toy example in Batch 14 requires large common-environment swings in reproduction. The Hutterite historical series currently available shows the opposite: colony multiplication/fission was strikingly regular at this coarse temporal scale.

Thus the arithmetic-versus-log correction barely changes the growth summary for 1918–1975 Manitoba Hutterites.

This is valuable negative evidence.

## Interpretation

Several major external historical changes occurred across the broader Hutterite history, including the movement from the United States to Canada around World War I. But once the Manitoba colony system was established in 1918, the measured period-level colony reproduction through 1975 was sufficiently stable that C008's random-environment penalty is tiny in the available series.

Later Hutterite reproduction may be more nonstationary because industrialization, land costs, and schism changed branching conditions, but that requires a different dataset and does not rescue C008 as an important result now.

## Verdict on C008

**DEMOTE from survivor to conditional quantitative warning.**

The mathematics is real and the target transfer remains possible for movements with volatile shared macroenvironments, but:

1. the best empirical exemplar currently available does not exhibit the volatility needed for the correction to matter materially;
2. the general lesson that multiplicative growth is harmed by environmental volatility is already classic source-domain knowledge;
3. without a target movement where the sign/decision actually changes, C008 is not yet sufficiently useful to retain as a Creative Tail Sampling survivor.

Promote again only if a real community/organizational lineage is found where:

- pooled arithmetic reproduction is above replacement;
- environment-conditioned/log growth is below or materially lower;
- the difference changes the inference about reproducibility.

## Effect on C005

This negative result actually strengthens the interpretation of the Hutterite C005 anchor.

The older Manitoba system combines:

- broadly distributed parent reproduction (low jackpot concentration);
- relatively stable reproduction across historical periods at the available resolution.

So its long lineage persistence is not obviously an artifact of either a few superstar parent colonies **or** a few extraordinary high-growth periods.

That does not establish causality, but it gives the reproduction profile a more coherent empirical shape.

## Next move

Return to orthogonal tail sampling rather than continuing to elaborate random-environment branching theory.

The highest-value empirical reproduction target remains a contrasting movement with parent-resolved, highly skewed daughter production and adequate generational follow-up.
