# Empirical Batch 08 — Does Reproductive Variance Distinguish Real Community Movements?

Date: 2026-08-15

## Goal

Test C005 (`reproductive-variance trap`) against real systems rather than leaving it as branching-process mathematics.

Primary question:

> Do successful community movements spread because most mature communities reproduce, or because a small minority of superstar communities account for most daughters?

This pass is preliminary because public datasets differ sharply in lineage resolution and observation windows.

---

# 1. Hutterites — strongest initial fit to a true parent→daughter branching model

## Historical branching structure

The North American communal Hutterite population began from three communal farms established by a minority of the Hutterite migrants arriving in the 1870s. Genetic-demographic literature reports that the roughly 443 people who established the three communal farms ultimately expanded into more than 40,000 Hutterites living in more than 350 colonies by the time of that study.

More recent counts report over 500 colonies.

## Fission mechanism

Hutterite descriptions explicitly treat colony branching as part of the normal organizational lifecycle: once a colony approaches roughly 150 people / 30 families, it begins establishing a daughter colony. The assets are valued and divided between home and daughter colonies.

The best historical fission dataset located covers two leuts over 1880–1970:

- 48 observed Lehrerleut fissions;
- 49 observed Schmiedeleut fissions;
- 97 observed events total, plus a handful lacking full size data;
- mean interval between successive fissions: about **14.3 years**;
- observed range: **4–39 years**;
- mean size at fission ~166 people;
- one successor remains on the original farm and the other establishes the new site.

Relevant literature:

- Carolyn L. Olsen, "The Demography of Colony Fission from 1878–1970 Among the Hutterites of North America," *American Anthropologist* 89 (1987), DOI 10.1525/aa.1987.89.4.02a00040.
- Robin Dunbar & Richard Sosis, "Optimising human community sizes," *Evolution and Human Behavior* 39 (2018), DOI 10.1016/j.evolhumbehav.2017.11.001.

## What this says about C005

The public evidence is consistent with reproduction being **broadly embedded in mature-colony lifecycle**, rather than a discretionary activity performed only by unusual superstar colonies.

This is exactly the structural feature C005 predicts should produce more robust lineage reproduction: low zero-offspring probability among colonies that survive to normal reproductive maturity.

However, this pass does **not yet measure `P(K=0)` directly**. The fission-event dataset records events, and the public article summary does not provide a complete risk-set table of all colonies by age and whether they ever failed to fission.

### Important complication

A Hutterite fission daughter receives a very large propagule: roughly half of a mature community and a division of accumulated assets. Thus Hutterite success demonstrates reliability of **fission reproduction**, not necessarily ease of de novo founding from a handful of outsiders.

Do not equate those two meanings of 'copyable.'

---

# 2. U.S. church planting — preliminary high-zero-reproduction contrast

A 2015 LifeWay Research study analyzed 843 Protestant church plants from 17 denominations/networks that had been started since 2008 and still existed at the time of the survey.

A summary of the multiplication results reports:

- among churches old enough for the full observation window, about **22%** had started at least one daughter church within their first five years;
- therefore roughly 78% had **not** produced a daughter within that five-year window.

An older Leadership Network / denominational summary reported that only around 15% of churches were parenting churches, though definitions and sampling differ.

## Interpretation

This is not directly comparable with lifetime Hutterite fission because:

- five years is much shorter than the ~14-year mean Hutterite fission interval;
- the LifeWay study was survivor-conditioned (the 843 churches still existed), which can bias reproduction estimates;
- church plants can have sponsorship by multiple organizations rather than one literal parent;
- daughter definitions differ.

Nevertheless, it provides a useful candidate contrast: church reproduction appears to be a **minority behavior** in at least some U.S. datasets rather than an expected lifecycle stage of every mature congregation.

Church-multiplication practitioners themselves distinguish simple growth/planting from multi-generation multiplication. Some movement organizations explicitly require fourth-generation church reproduction before calling a network a 'movement.' This means **generation depth is already recognized in the target practice domain**, so Creative Tail Sampling should not claim that part as novel.

What appears less standard is using the **full offspring distribution and associated extinction probability** to distinguish jackpot growth from robust reproducibility.

---

# 3. Bruderhof — branching unit is ambiguous

The Bruderhof was founded in 1920 and its public history documents repeated establishment of additional communities across countries, including several new U.S./UK settlements in the 1980s–1990s and later communities in Australia, Germany, and cities.

But the public history presents these as expansion of a single integrated Bruderhof movement, not clean parent→daughter fissions with independent local reproduction.

Therefore calculating `K` for each local Bruderhof from public data would risk inventing a parentage structure that the organization itself does not use.

## Methodological consequence

Before fitting C005, identify the **reproductive unit**:

- local community;
- founder team;
- regional federation;
- denomination/network;
- integrated movement as a whole.

Simple Galton-Watson branching is appropriate only when units generate reasonably identifiable descendants and lineage independence is not wildly false.

Where daughters draw pooled people/capital from many communities, use a structured or multi-source reproduction model instead.

---

# 4. Preliminary verdict on C005

## Strengthened, not proven

The Hutterite case gives C005 a real-world anchor:

- reproduction is formalized as a normal mature-colony transition;
- repeated fission is extensively documented;
- organizational branching has persisted across many generations.

The church-planting comparison suggests that other movements may have much higher zero-reproduction rates among local organizations, even while the broader movement continues creating many new organizations.

This supports the distinction between:

> **movement-level production of new communities**

and

> **community-level reproducibility of the organizational model**.

That distinction is the current empirical core of C005.

## New measurement refinement

For a purportedly replicable community model, report a **reproduction profile**, not one growth number:

1. reproductive unit definition;
2. risk set: which units are old/mature enough to have reproduced;
3. `P(K=0)` over a specified age window;
4. distribution of viable offspring K;
5. generation interval distribution;
6. daughter survival;
7. granddaughter reproduction;
8. propagule burden — people/capital transferred to each daughter;
9. degree of multi-parent/federation subsidy;
10. lineage independence / shared-support correlations.

This prevents a movement from looking 'reproducible' simply because a federation or a few exceptional parents can repeatedly assemble new communities.

---

# 5. Strong next empirical move

The highest-value missing object is a **parent-level Hutterite lineage table** with foundation dates and subsequent fission dates.

The Dunbar/Sosis paper states that its supplementary material contains the Hutterite fission data. If the supplement includes colony identifiers, reconstruct:

- each parent's number of fissions / descendants within observation;
- age-at-fission distribution;
- censored colonies that had not yet fissioned;
- leut-specific reproductive variance;
- whether lineage reproduction is close to deterministic once maturity is reached.

Then compare with a church-planting dataset that contains parent-child identifiers and sufficient follow-up.

Until that is done, **do not claim Hutterites have proven low reproductive variance**; call it the leading empirical hypothesis.
