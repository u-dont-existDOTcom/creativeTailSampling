# Orthogonal Tail Batch 49 — Event-Level Fission Process Evidence

Date: 2026-08-15

## Outcome

**No new Creative Tail survivor.**

The main result is an evidence-quality correction for C005/B48: Hutterite parent→daughter genealogy is much easier to reconstruct than the actual event-level mechanism by which people, roles, assets and destination status were partitioned.

A small preliminary event file is now stored at:

- `data/hutterite_branching_process_events_preliminary.csv`

The dataset deliberately preserves `unknown` values rather than imputing branch-wide practices to individual historical fissions.

---

# Event-level results

## E49-01 — Rock Lake → Interlake, Manitoba, 1960/1961

**Process confidence: HIGH.**

The Supreme Court of Canada record states:
- Rock Lake planned a daughter at Interlake in 1960;
- members divided into two groups;
- neither group knew whether it would stay at Rock Lake or move to Interlake;
- destination was then decided by lot;
- assets were divided roughly in proportion to membership;
- 2,080 acres were purchased for Interlake;
- the actual move occurred in December 1961.

This is a strong event-level instance of **composition fixed before destination known**.

What remains unknown from the court record:
- how the two groups were constructed;
- whether families/care units were explicitly protected;
- whether skill/leadership balance criteria were used;
- exact initial group population.

Do not import those details from generic Hutterite descriptions.

---

## E49-02 — Sturgeon Creek → Crystal Spring, Manitoba, 1954

**Process confidence: MEDIUM for membership quantity; LOW/UNKNOWN for partition mechanism.**

GAMEO records:
- Sturgeon Creek had population 158 / 60 baptized members;
- 13 families / 73 persons left with minister Jakob Kleinsasser;
- they founded Crystal Spring.

The searched event-level sources did **not** state:
- volunteer vs assignment vs lot;
- whether composition was fixed before destination;
- asset-division process.

Therefore those fields remain `unknown`.

---

## E49-03 — James Valley → Miami, Manitoba, 1966

**Process confidence: HIGH for asset/support mechanism; LOW/UNKNOWN for member partition.**

Lehr & McGregor's event account, citing Johnny Hofer's detailed history, records:
- Miami became independent from James Valley in 1966;
- assets were inventoried in unusual detail, including machinery, lumber, livestock, grain and even 27 outhouse toilets;
- buildings were valued and financial adjustments made;
- families kept their own garden sheds;
- James Valley agreed to supply eggs and chickens until Miami could provide its own.

The searched event-level source does **not** say which families went by what selection mechanism.

Therefore:
- `partition_mode = unknown`;
- `composition_fixed_before_destination_known = unknown`;
- `destination_assignment_mode = unknown`.

This is exactly the kind of distinction the schema is meant to preserve.

---

## E49-04 — Valley View → May City, Alberta, observed planning stage in 2013

**Status: prospective historical lead, not a completed mechanism observation.**

A 2013 report documents:
- Valley View preparing a daughter called May City;
- new-site buildings/business operations already being developed;
- members anticipating a later split.

The report predates the final division and does not document eventual member partition/destination assignment.

Keep it as a process-history lead rather than filling final-event fields from generic practice.

---

# Main research-control finding — mechanism missingness

## Plain proposition

A lineage genealogy can be nearly complete while the causal process variables needed to explain reproduction remain mostly missing.

For communal fission this includes:
- who chose the daughter group;
- whether the choice was voluntary/lot/leadership assignment/hybrid;
- whether destination was known during composition;
- family/care constraints;
- skill/leadership balancing;
- asset/productive-capacity balancing;
- subsidy and mentoring;
- dissent and member transfers.

This is ordinary missing-covariate/archival-selection logic and **not a novelty claim**.

But it limits what C005 can currently infer about why Hutterite reproduction is broadly distributed.

---

# B49-L01 — Create a branching record prospectively at every fission

**Status: PRACTICAL / RESEARCH-CONTROL.**

A federation that wants to learn how communities reproduce should create a standard branching record **when the split happens**, not reconstruct it decades later.

Use `analysis/branching_process_covariates.md` as the canonical schema.

Minimum event record:
- parent/daughter IDs and date;
- fission trigger;
- partition method;
- whether destination was known before composition;
- protected household/care units;
- initial populations/households;
- skill/leadership/care balance;
- asset and functional-capacity split;
- transitional subsidies/support;
- dissent/transfers;
- subsequent daughter outcomes.

## B49-L02 — Separate source confidence by variable

One source can be high-confidence for:
- population;
- assets;
- location;

and completely silent about:
- partition method.

Do not assign one global `event confidence` that hides field-level uncertainty.

## B49-L03 — Generic branch practice is context, not event evidence

Official Hutterite descriptions show:
- Lehrerleut often use balanced groups + lot;
- Schmiedeleut/Dariusleut can use volunteers or group division + lot.

That cannot justify coding an individual historical Schmiedeleut fission as `mutual consent` or `lot` unless the event source says so.

## B49-L04 — Separate process history from outcome genealogy

Maintain linked but distinct datasets:
1. parent→daughter genealogy/outcomes;
2. branching-process variables.

The first can remain much more complete than the second without creating false certainty.

## B49-L05 — Preserve planned/aborted fissions

Genealogies usually capture successful daughter colonies. A reproduction-process study also needs:
- planned but abandoned daughter sites;
- failed early daughters;
- postponed fissions;
- factional splits not supported by the parent.

Otherwise process inference is selected on completed reproduction.

## B49-L06 — Distinguish ordinary planned fission from conflict secession

Sources note that some Hutterite splits arise from serious internal division rather than normal population branching, and those departing factions may not receive the same parent support.

Do not pool them as the same reproductive event.

## B49-L07 — Transitional subsidy is a mechanism variable

James Valley→Miami shows concrete mother→daughter support.

C005 should distinguish:
- raw daughter survival/reproduction;
- daughter outcome conditional on inherited/transitional support;
- movement-level reproducibility including normal support architecture.

All three can be legitimate estimands; do not confuse them.

---

# Batch 49 decision

## No causal regression yet

Current event-level mechanism sample is far too sparse and uneven for defensible comparison of `lot vs consent vs volunteer` outcomes.

The correct result is:

> **Process-data insufficiency.**

Do not manufacture a quantitative relationship from branch-level stereotypes.

## Next empirical path

Only continue this C005 mechanism lane when one of these becomes available:

1. a historical source containing multiple named fissions and their actual member-partition methods;
2. colony-level archives/memoirs that can fill several event records consistently;
3. prospective standardized records from future fissions;
4. a second communal movement with documented parent→daughter process data.

Otherwise return to orthogonal Creative Tail sampling.

---

## Method lesson

A sparse `unknown`-rich process dataset is better than a complete-looking dataset created by silently projecting group-level customs onto individual events.
