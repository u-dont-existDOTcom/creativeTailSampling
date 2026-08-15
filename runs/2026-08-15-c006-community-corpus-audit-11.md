# Batch 11 — Apply C006 Genealogical Sampling Bias to the Existing Communities Research Corpus

Date: 2026-08-15

## Question

Does C006 (`descendant inflation / lineage-size sampling bias`) invalidate or materially distort the user's existing `u-dont-existDOTcom/communities` research checkpoint?

## Corpus inspected

The current authoritative community-research checkpoint is not on `main`; it is in draft PR #1, branch `agent/volume-44-research`.

Inspected:

- `AGENTS.md`
- `docs/INDEX.md`
- `CURRENT-STATE.md`
- `recovered/COMMUNITIES-RESEARCH-STATE.md`
- `recovered/COMMUNITIES-EVIDENCE-LEDGER.csv`
- `recovered/COMMUNITIES-ARTICLE-GAP-BANK.md`
- `recovered/COMMUNITIES-V44-RESEARCH-REPORT.md`

The checkpoint covers volumes 1–44 of *Communal Societies*: 969 PDFs triaged, 432 close reads, and 158 source-bounded findings.

## Result

### C006 does **not** currently invalidate the evidence ledger or gap synthesis

The current P0 research architecture is fundamentally **mechanism/source-bounded**, not a prevalence estimator.

The evidence ledger records, per finding:

- source and community/group;
- exact factual observation;
- what the source establishes;
- what it does not establish;
- author interpretation;
- alternative interpretation;
- response process;
- outcome;
- transferability;
- confidence and verification needs.

The gap bank then reconciles materially distinct mechanisms into 18 article-gap items rather than counting how many communities exhibit each practice.

The workflow also repeatedly refuses duplicate promotion. Across later volumes, reports explicitly label many Shaker, Oneida, Hutterite, Jonestown, kibbutz, Camphill, Bruderhof, etc. sources as **corroboration** of an existing finding rather than creating a new finding simply because another paper/site exists.

The gap bank states that the volume-44 checkpoint retained 18 material items after reconciling findings 'rather than inflating the list.' The volume-44 report similarly added only three substantive findings from three sources while classifying many other close reads as corroboration, context, source maps, or verification leads.

Therefore daughter-community proliferation is not currently being treated as independent statistical replication in the main synthesis.

## Where C006 *does* matter

### 1. Future prevalence claims

C006 becomes essential if the project moves from:

> Does mechanism X occur, and what does the case reveal?

into claims such as:

> X is common among successful communities.

or:

> Communities with X have better child/member outcomes than communities without X.

At that point, a prolific lineage can contribute many culturally related daughter communities and mechanically dominate the sample.

### 2. Future comparative scoring/ranking

If Hutterite colonies, kibbutzim, Bruderhof sites, Shaker societies, FEC daughter communities, cohousing replications, etc. are each rows in a comparative community dataset, rows sharing a reproductive lineage cannot automatically be treated as independent institutional experiments.

### 3. Source-density bias

Even in a qualitative corpus, prolific and highly institutionalized traditions can generate more communities, archives, publications, and scholarly attention. The present ledger partly controls this by promoting materially distinct mechanisms rather than article counts, but claims about frequency or evidence quantity must still avoid confusing **documentation density** with prevalence.

### 4. Gap-bank evidence lists are not vote counts

Several gap items cite many finding IDs, including multiple cases from the same broad traditions. These lists should continue to mean:

> here are source-bounded routes by which this mechanism was observed or challenged

not:

> N independent communities vote for this conclusion.

No retrospective reweighting is warranted while the synthesis remains mechanism-oriented.

## Concrete integration rule

Do **not** add genealogical weights to the current 158-finding evidence ledger merely because C006 exists.

Instead, when a future community-level comparative dataset is built, add fields such as:

- `community_id`
- `parent_community_id`
- `lineage_root_id`
- `founding_type` = independent / fission / daughter / federation-created / merger / uncertain
- `shared_parent_support`
- `founding_year`
- `lineage_depth`
- `institutional_variant_id` where distinguishable

And before any analysis, declare the estimand:

- random founding attempt/root;
- random extant community;
- random current resident;
- random lineage;
- future movement culture/reproductive contribution.

Then use the weighting/model appropriate to that question.

## Important subtlety found in the existing gap bank

The current research already contains a conceptually adjacent independence warning: G-003 states that multiple reports are not independent when they are generated, tested, edited, and approved inside one belief-and-authority chain. C006 extends the same epistemic principle **across organizational genealogy**:

> multiple communities are not automatically independent institutional evidence when one is a cultural/organizational descendant of another.

This is a genuine integration point rather than a correction of a current error.

## Verdict on C006 after target-corpus application

**RETAIN.** The application sharpened its scope:

- C006 is not a criticism of the current source-bounded mechanism ledger;
- it is a required guard for future comparative/prevalence/generalization work;
- it distinguishes source-level independence, community-level independence, lineage-level independence, and estimand choice.

## Next step

Do not modify the `communities` research checkpoint solely to retrofit C006. That project is in a bounded P0 research workflow and the current synthesis is not making the statistical claim C006 corrects.

When the project begins a whole-corpus comparative synthesis or constructs a community-level outcome table, carry C006 in as a methodology requirement from the start.
