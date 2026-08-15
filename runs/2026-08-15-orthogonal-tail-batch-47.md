# Orthogonal Tail Batch 47 — Cumulative Privacy Failure in Small-Community Research

Date: 2026-08-15

## Outcome

One provisional cross-domain survivor:

- **C023 — Cumulative disclosure-budget / differencing guard for small-community research**

The source theory—database reconstruction, statistical disclosure control, differential privacy, composition, and continual observation—is established. The surviving target transfer is the requirement that a federation research center protect privacy **across the joint history of overlapping aggregate releases**, not certify each table/dashboard independently.

---

# C023 — Cumulative disclosure-budget / differencing guard

## Plain proposition

In a small commune, a publication can reveal an individual's sensitive answer even if every released table is individually aggregated and contains no names.

The danger is **composition**:

- release A reveals the mean for eight residents;
- one member leaves;
- release B reveals the mean for the remaining seven;
- subtraction can reveal the leaver's approximate/actual value.

Or:

- publish total satisfaction;
- publish parents' satisfaction;
- publish nonparents' satisfaction;
- if one subgroup contains one person, their answer is derived.

Therefore:

> **Privacy review must consider all prior and planned releases together, including time-series, subgroup, community, lineage and federation aggregates.**

## Source-domain collision boundary

Dinur & Nissim show a fundamental reconstruction problem: releasing sufficiently many accurate aggregate statistics can allow reconstruction of confidential underlying data.

Differential privacy was developed partly to provide privacy guarantees robust to auxiliary information and repeated statistical querying. Composition/continual-observation work treats privacy loss across repeated releases as a first-class problem.

So neither differencing attacks nor privacy composition is new.

## Target-domain evidence

Intentional-community research already acknowledges unusual small-N anonymity risk:

- Cloughjordan Ecovillage's research guidance explicitly warns that it is a small community and details about members' homes/views can easily identify them, requiring additional anonymity care.
- The EVIST ecovillage survey excludes communities with fewer than eight permanent members and describes formal anonymization/data-protection rules.
- Existing IC wellbeing research has used anonymous online questionnaires, but `anonymous collection` does not by itself guarantee safe repeated commune-level publication.

No screened target practice was found that explicitly manages a **cross-release cumulative privacy budget / differencing ledger** for repeated intentional-community outcome reporting.

**Disposition: survives provisionally as a target-domain research architecture.**

---

# Operational architecture

## C023-01 — Maintain a release ledger

For every public/member-visible release, log:
- variables;
- community/subgroup;
- time window;
- denominator N;
- suppression/noise/transformation;
- prior overlapping releases;
- whether an individual's contribution can be isolated by differencing.

Privacy review checks the **release set**, not only the new table.

## C023-02 — Run differencing attacks before publication

At minimum test:
- before/after one entrant/leaver;
- total vs subgroup complements;
- overlapping age/gender/parent/role groups;
- community total vs federation total;
- monthly vs quarterly totals;
- outcome combinations that isolate a rare person/household.

If an analyst can derive an individual's value from published numbers, `anonymous aggregate` is false.

## C023-03 — Use minimum-cell rules, but do not rely on them alone

`N >= k` in each table is insufficient if several tables intersect to isolate one person.

Cell suppression must consider complementary/overlapping cells and time-series releases.

## C023-04 — Prefer federation-level publication for sensitive outcomes

For small communes, public results may need to be reported at:
- pooled federation level;
- broad measurement-compatible cluster;
- multi-year window;

while keeping community-specific sensitive estimates available only under controlled researcher/member access.

## C023-05 — Decouple useful local feedback from public benchmarking

A community may need private local diagnostic feedback even when public release is unsafe.

Use different access tiers:
- individual private report;
- community-internal aggregate where safe;
- federation research access;
- public release.

Do not assume every useful statistic should be public.

## C023-06 — Delay/suppress updates after single-person membership changes

If one person joins/leaves and a fresh aggregate would expose their contribution, delay publication, widen the time window, pool communities, or use a formal privacy mechanism.

## C023-07 — Treat quotations/narratives as part of the same disclosure budget

A quantitative cell can be safe until a public quote reveals who belongs to the subgroup.

Link qualitative-release review with quantitative-release review.

## C023-08 — Protect longitudinal identifiers

Research can require panel linkage while public anonymity requires separation.

Use controlled pseudonymous linkage and keep reidentification keys away from local leadership/public outputs.

Do not create quasi-identifiers that let communities infer who is who from repeated trajectories.

## C023-09 — Differential privacy is an option, not a ritual requirement

Formal differential privacy can provide composition guarantees, but in tiny samples:
- noise can swamp signal;
- implementation is nontrivial;
- members may misunderstand what it protects;
- not all outputs need public release.

First ask whether pooling/suppression/access control solves the practical need more simply.

## C023-10 — If using DP, manage privacy loss over time

A one-time epsilon statement does not cover an endless dashboard.

Specify:
- privacy unit (person/household/event);
- neighboring-data definition;
- total privacy budget;
- composition across queries/releases;
- refresh/re-enrollment policy;
- how departures/entrants are handled.

## C023-11 — Do not publish exact rare-severe-event breakdowns that identify victims

Batch 38 says rare severe events should not be averaged away; C023 adds the privacy constraint.

Possible compromise:
- preserve exact confidential registry for safety/research;
- publish broader pooled counts/ranges;
- report presence of a severe-event class without identifying timing/community where necessary.

Safety accountability and victim privacy must both be designed.

## C023-12 — Public transparency can focus on process rather than raw small-N outcomes

A small community can publish:
- survey instrument;
- methodology;
- participation rate;
- privacy protections;
- whether thresholds were met;
- whether independent review occurred;

without publishing every sensitive cell.

## C023-13 — Treat external auxiliary information as part of re-identification risk

Community members already know:
- who left;
- who has children;
- who was in conflict;
- who held a role;
- who experienced a visible event.

Privacy review must assume this background knowledge, not an ignorant outsider.

## C023-14 — Small-N threshold should depend on sensitivity and auxiliary knowledge

There is no universal safe `N=5` or `N=8`.

Risk depends on:
- sensitivity;
- subgroup uniqueness;
- distribution of responses;
- overlapping releases;
- known life events;
- household structure.

## C023-15 — Community comparison should not require public community identification

The research center can sometimes publish anonymized/pooled comparative findings while giving each community its own private result.

This reduces reputational incentives to game and disclosure risk simultaneously.

## C023-16 — Privacy failures can feed Batch 43 disclosure bias

If members see prior participants reidentified from `anonymous` results, future survey answers become less candid.

Thus privacy is not only an ethical constraint; it changes data validity.

---

# Distinctive predictions

If C023 matters:

1. repeated commune-level dashboards will become more re-identifying as membership/subgroup composition changes even without any new microdata release;
2. the riskiest disclosures will often come from combinations of innocuous tables rather than one obviously sensitive table;
3. members' confidence in anonymity will fall after visible differencing/reidentification episodes, increasing Batch 43 reporting pressure;
4. federation-pooled publication can preserve much more useful trend information than community-level publication at the same privacy risk;
5. privacy-safe public data and high-detail confidential research data will need different access layers.

---

# Falsifiers / demotion conditions

Demote C023 if:
- the intended research center never publishes/re-shares repeated overlapping small-N community statistics;
- all sensitive outputs remain individual/private under strong access control;
- target-domain federation research already systematically applies formal composition-aware disclosure control across release histories.

---

## Disposition

**SURVIVES provisionally as C023 — Cumulative disclosure-budget / differencing guard for small-community research.**

Claim only the target-domain architecture. Reconstruction attacks, statistical disclosure control, differential privacy and composition are established source theory.
