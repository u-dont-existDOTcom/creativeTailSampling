# Orthogonal Tail Batch 51 — Winner's Curse in Best-Practice Discovery

Date: 2026-08-15

## Outcome

**No Creative Tail survivor.**

Winner's-curse, multiple-comparison, selective-inference, replication, cross-validation and policy-selection literatures directly own the mechanism.

The communal research-center implementation remains foundational:

> **The practice selected because it looked best in discovery data must not be advertised using the same unadjusted discovery estimate as its expected effect.**

---

# Core problem

Suppose the federation research center tests:
- 40 governance features;
- 25 labor/family arrangements;
- 20 admission practices;
- 30 outcome measures;
- many subgroups/contexts.

Even if most real effects are small, some combination will look spectacular by chance.

If researchers then select that apparent winner and report its discovery effect as the expected benefit, selection has conditioned on positive noise.

This is the **winner's curse**.

## Literature collision

Policy-evaluation research explicitly studies inference on the best policies when many candidates are estimated. Conventional inference is overly optimistic because the selected best policy is more likely to have been overestimated.

Economic selective-inference work develops corrections for winners chosen from noisy estimates.

GWAS research provides a clear large-scale analogue: threshold-selected discoveries systematically overestimate effect size unless selection is accounted for and independent replication is used.

**Disposition: no novelty claim.**

---

# Practical architecture

## B51-L01 — Separate discovery from confirmation

Use one dataset/community-period set to discover candidate practices and an independent or meaningfully held-out set to estimate confirmation effects where feasible.

Do not recycle the same observations as if selection had not occurred.

## B51-L02 — Publish the search universe

For every highlighted `best practice`, record how many:
- candidate practices;
- outcomes;
- subgroups;
- model specifications;
- time windows

were searched before the winner was chosen.

A winner among 500 looks different from a predeclared one-hypothesis test.

## B51-L03 — Predeclare primary outcomes where possible

Exploration is legitimate, but distinguish:
- confirmatory primary outcomes;
- exploratory outcomes;
- post-hoc subgroup discoveries.

Do not relabel an exploratory winner as preplanned evidence.

## B51-L04 — Report selection-aware uncertainty

Where statistical modeling is used, use methods appropriate for:
- multiplicity;
- selected best-policy effects;
- shrinkage/hierarchical estimates;
- held-out/cross-fitted evaluation.

The exact method depends on sample structure; do not bolt on one ritual correction.

## B51-L05 — Replicate effects, not just directions

A practice that remains positive but falls from `+40%` to `+5%` has not replicated the advertised effect magnitude.

Report:
- discovery estimate;
- confirmation estimate;
- uncertainty;
- context changes.

## B51-L06 — Preserve negative and null searches

If the center tested 100 ideas and one looked impressive, the other 99 are part of the evidence environment.

Maintain a searchable experiment ledger so failed searches do not disappear.

## B51-L07 — Do not select communities and practices on the same noise

Example failure:
1. find highest-performing communities;
2. inventory what they uniquely do;
3. call those features best practices;
4. evaluate them using the same communities.

This compounds selection on community outcomes with selection on practices.

Use independent comparison/validation logic.

## B51-L08 — Regression to the mean is not evidence the adopter implemented badly

When a discovery winner's effect shrinks in later communities, first consider expected selection bias before blaming implementation fidelity.

## B51-L09 — Stop rankings from resetting the search every reporting cycle

Repeatedly selecting the current top community/practice from noisy annual data creates continual winner selection.

Use longer horizons, shrinkage, preregistered decision rules or explicit anytime-valid/selection-aware methods where needed.

## B51-L10 — Separate `best observed` from `best expected`

Rankings based on raw point estimates answer `who looked best in this sample?`, not necessarily `which practice has highest expected true effect?`.

Use uncertainty and selection-aware estimates.

## B51-L11 — Confirmation must test transportability too

An independent replication in nearly identical conditions may confirm a local effect but not worldwide applicability.

Combine with Batch 32 scaling/transportability controls.

## B51-L12 — Value pluralism still applies after statistical correction

Even a perfectly estimated effect vector does not define `best` across communities with different value tradeoffs.

Combine with Batch 39 rather than creating one corrected universal leaderboard.

## B51-L13 — Small federation samples make winner's curse especially severe

When each practice is estimated from few communities, noise is large and selected maxima are particularly unstable.

Favor:
- modest claims;
- pooling across time where valid;
- independent confirmation;
- transparent uncertainty.

## B51-L14 — Do not reserve all communities as permanent holdouts

The movement is small. Confirmation can use:
- later cohorts/time periods;
- new daughter communities;
- staggered voluntary adoption;
- cross-validation at the community/lineage level;
- independent external movements.

Avoid leakage from closely related daughter communities (C006).

---

# Suggested finding lifecycle

1. **Exploratory signal** — discovered in search.
2. **Selection-aware estimate** — shrink/correct uncertainty.
3. **Independent confirmation** — new community/time/lineage data.
4. **Transportability test** — contexts/values/scaling regime.
5. **Provisional recommendation** — with effect range.
6. **Ongoing outcome monitoring** — watch regression/context change.

Do not jump from step 1 to `best practice`.

---

## Disposition

No Creative Tail survivor.

Foundational practical rule:

> **The more broadly the research center searches for communal innovations, the less it can trust the raw effect size of whichever idea wins that search. Preserve discovery/confirmation separation and selection-aware inference before promoting a best practice.**
