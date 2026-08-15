# Orthogonal Tail Batch 18 — Governance Testing and Non-Hutterite Reproduction Screen

Date: 2026-08-15

## Goals

1. adversarially attack C010 governance fault injection and C011 shadow governance;
2. look for a non-Hutterite reproduction comparator for C005;
3. generate a fresh orthogonal candidate batch and promote only ideas that survive both common-sense and nearest-neighbor attacks;
4. separately preserve practically useful ideas in `u-dont-existDOTcom/communities/COMMUNITY-DEVELOPMENT-LESSONS.md` even when originality fails.

---

# A. C010 — governance fault injection

## Result: DEMOTE FROM CREATIVE-TAIL SURVIVOR

The target-domain search still did not uncover a clear intentional-community tradition of recurring dependency-loss drills. However, that is not enough to meet the project's novelty bar.

Continuity practice already explicitly goes beyond writing plans to **exercising** loss of key people and essential functions. Red Cross business-continuity exercise material includes availability-of-key-people scenarios; FEMA continuity exercises test whether essential functions continue through personnel, facility, communications, and system disruption. Generic succession and continuity doctrine therefore owns the important mechanism.

The intentional-community transfer remains useful but is too close to established practice plus common sense:

> a backup plan that has never been exercised may not work.

Disposition:

- originality: **DEMOTED**;
- communities lessons: **KEEP** as practical/known, especially because communal organizations may underuse formal continuity exercises.

Safety constraint remains: use tabletop/sandbox exercises rather than live failure injection where children, health, medication, housing, legal rights, or necessities could be harmed.

Sources:

- American Red Cross Ready Rating business continuity exercise material
- FEMA Continuity of Essential Functions exercise toolkit

---

# B. C011 — shadow governance

## Result: SURVIVES, still provisional

Target search found:

- intentional/cohousing communities adopting sociocracy or Dynamic Governance;
- communities explicitly **trialing** new governance systems live;
- adjacent political projects called “shadow government” or parallel governance structures, but these have a different function: citizen participation, alternative representation, or transitional legitimacy.

No close intentional-community precedent was found for the narrower architecture:

> the incumbent decision process remains authoritative while the proposed process independently processes the **same admissible cases** nonbinding, so divergence can be examined before authority transfers.

A 2026 Phoenix Cohousing case study is useful counterevidence to naïve governance rollout: members adopted sociocracy as the actual governance system and experienced substantial implementation difficulty and resistance. This does not establish that shadow governance would solve those problems, but it strengthens the value of distinguishing abstract attraction from behavior on real decisions.

Why C011 remains distinct from ordinary piloting:

1. a live pilot changes outcomes, relationships, precedent, and path dependence;
2. a shadow process can reveal decision differences before imposing them;
3. agreement rate is less useful than **which cases diverge and why**;
4. divergence can expose hidden differences in agenda rights, admissible evidence, jurisdiction, recusal, veto/consent thresholds, timing, or burden of proof that constitutional prose may conceal.

Limits:

- nonbinding participants may behave differently;
- two processes impose time cost;
- duplicating sensitive personal cases can itself be harmful;
- shadow agreement does not prove the new system legitimate or better;
- the method fits substantial procedural transitions, not routine minor rule changes.

Disposition: **C011 survives / provisional cross-domain transfer.**

---

# C. C005 — non-Hutterite reproduction comparison

## Parent-resolved dataset search

The search did **not** yet find a public church-planting dataset with enough row-level parent→daughter edges and exposure time to calculate a comparable `K` distribution.

Useful aggregate evidence nevertheless shows that routine reproduction is not generic even among organizations ideologically committed to reproduction:

### U.S. church-planting research

Exponential summarized a LifeWay/NewChurches study across 17 denominational and church-planting organizations: among churches started in 2012 or earlier, **22%** had started at least one daughter church within their first five years.

An Acts 29 annual report stated that **33%** of Acts 29 churches had gone on to plant a second-generation church; the same report gave an average church age of 7.5 years and an average 4.8 years for a plant to plant again.

Other national studies similarly find reproduction uncommon, though definitions differ: Exponential/LifeWay categorized only a small fraction of U.S. Protestant churches as reproducing/multiplying in a three-year window.

### Interpretation boundary

These are **not** apples-to-apples estimates against the Hutterite >=20-year mature cohorts:

- follow-up differs;
- church plants may be autonomous organizations rather than demographic fissions;
- exposure/subsidy/core-team structure differs;
- aggregate percentages do not reveal reproductive variance among the churches that do reproduce.

Therefore do **not** compute a numerical Hutterite-vs-church effect size from these figures.

They do support a weaker qualitative conclusion:

> Near-universal reproduction by mature Hutterite parent colonies is not a generic consequence of merely valuing organizational reproduction.

The next C005 target remains a true parent-resolved non-Hutterite genealogy.

Potential future routes:

- denomination archives with parent-church fields in annual church-plant reports;
- Exponential's multi-generational “family tree” collection if row-level output becomes available;
- historical communal/religious settlement genealogies.

---

# D. Orthogonal Batch 18

Fourteen candidates were generated before selection.

## T118-01 — Metamorphic governance testing / constitutional invariance testing

### Plain proposition

A community can test whether its governance actually follows a claimed principle **without knowing the uniquely correct answer to a hard case** by changing only a feature that the principle says should be irrelevant and checking whether the decision changes.

### Source-domain mechanism

Metamorphic testing addresses the “test oracle” problem: when the exact correct output is unavailable, specify relations that should hold between outputs under controlled input transformations.

Black-box bias auditing already uses this for automated decision systems: alter gender or another irrelevant/specified attribute while preserving relevant facts and test whether the decision obeys the expected invariance or monotonic relation.

Matched-vignette and audit-study traditions do related work on humans and institutions.

### Target-domain nearest-neighbor attack

Searches found:

- intentional-community governance case studies and governance-system trials;
- general vignette research on governance legitimacy;
- matched-vignette/audit approaches outside intentional communities;
- no clear intentional-community practice using a **versioned suite of metamorphic relations to test its own human governance decisions**.

This is not claimed as a new fairness concept. The proposed transfer is the systematic test architecture.

### Community examples

Suppose a community claims that these attributes should be irrelevant to a particular decision. Construct paired cases differing only on that attribute:

- founder vs newcomer;
- popular vs unpopular member;
- friend of decision-maker vs distant member;
- majority-faction vs minority-faction identity;
- high contributor vs low-status member where contribution is normatively irrelevant;
- gendered/racialized names where the rule says identity is irrelevant;
- insider vs departing member where the same property right is at issue.

The relation need not always be “same output.” Other constitutional metamorphic relations can be specified:

- **monotonicity:** adding stronger admissible evidence of the same relevant type should not make a protective response weaker without an explicit countervailing reason;
- **symmetry:** swapping otherwise equivalent parties should swap their treatment;
- **irrelevance:** changing a constitutionally irrelevant fact should not change the outcome;
- **scale consistency:** doubling a quantity that the rule says is proportional should not produce an arbitrary reversal;
- **jurisdiction invariance:** changing who proposes an action should not alter which body has jurisdiction if jurisdiction is defined by subject matter.

### Why this may matter

1. hard communal disputes often lack an agreed ground-truth “right answer”;
2. arguments over the answer can therefore conceal inconsistent application of the **community's own** stated rules;
3. metamorphic relations let the group test consistency separately from resolving the underlying moral disagreement;
4. failures reveal hidden decision rules, status effects, faction effects, or implementation ambiguity;
5. resolved metamorphic pairs can become regression tests for future governance changes.

### Protocol

1. choose a past or hypothetical case appropriate for testing;
2. state the constitutional relation expected to hold **before** seeing the paired results;
3. create one or more minimally transformed versions;
4. randomize/blind identity/order where feasible;
5. have the relevant process or panel decide each version independently;
6. compare outputs and reasons;
7. if the relation fails, investigate whether the constitution is ambiguous, the transformation was actually relevant, or the process is inconsistent;
8. preserve high-information cases in the constitutional test suite.

### Limits

- deciding what is genuinely irrelevant is itself a normative judgment;
- paired cases cannot perfectly reproduce live social context;
- members can learn the test and answer performatively;
- demographic swaps must not be used to erase real structural differences when those differences are actually relevant;
- inconsistency does not tell you which of the two decisions was correct.

### Disposition

**SURVIVES as C012 / provisional cross-domain operational transfer.**

It is closely related to C001 but answers a different question:

- C001 searches for cases that reveal **where members' values differ**;
- C012 tests whether a governance process obeys **relations the community already claims should hold**, even when the correct decision is unknown.

---

## T118-02 — Seed known faults to measure review sensitivity

Plain claim: insert known flaws into hypothetical governance proposals/case files and measure whether the review process catches them.

Nearest neighbors: mutation testing, seeded-error audit research, red teaming, anti-corruption integrity testing.

These traditions are close and explicit; audit research has long measured review quality with seeded errors.

Verdict: **REJECTED AS CREATIVE-TAIL NOVELTY; KEEP AS POSSIBLE TRAINING PRACTICE.**

---

## T118-03 — Historical governance replay/backtesting

Plain claim: run a proposed governance method on archived past cases with outcomes hidden, then compare.

Nearest neighbors: policy backtesting, case-based training, C001 regression suite, C011 shadow mode.

Verdict: **MERGE as a lower-risk implementation option for C011/C012, not independent novelty.**

---

## T118-04 — Statistical process control for community deterioration

Plain claim: use baseline variation/change-point methods to distinguish ordinary fluctuation from structural shifts in exit, conflict, workload, safety, or participation signals.

Nearest neighbors: SPC, organizational dashboards, early-warning systems, change-point detection.

Verdict: **REJECTED AS NOVEL; potentially useful measurement practice.**

---

## T118-05 — Identity-blind review for selected cases

Plain claim: hide irrelevant identity information during review where possible.

Nearest neighbors: blind auditions, anonymous review, anti-bias procedures.

Verdict: **REJECTED AS NOVEL.**

---

## T118-06 — Differential governance testing

Plain claim: independently route the same case to two panels/processes and investigate disagreement.

Nearest neighbors: inter-rater reliability, independent review, differential testing.

Verdict: **REJECTED as independent novelty; C011 contains the stronger transition-specific transfer.**

---

## T118-07 — Canary governance rollout

Plain claim: apply a reversible rule change to a bounded domain before global adoption.

Nearest neighbors: pilots, canary releases, laboratories of democracy.

Verdict: **REJECTED.**

---

## T118-08 — Constitutional property-based testing

Plain claim: generate many cases satisfying a formal invariant and see whether decisions violate it.

Nearest neighbors: property-based software testing, legal hypotheticals, C001/C012.

Verdict: **MERGE INTO C012** as a future automation direction if rules can be formalized enough.

---

## T118-09 — Agenda-order randomization to detect path dependence

Plain claim: vary proposal/discussion order to measure order effects.

Nearest neighbors: framing/order-effect research, randomized deliberation experiments.

Verdict: **REJECTED AS NOVEL.**

---

## T118-10 — Reversible diagnostic policy probes

Plain claim: use small reversible interventions to discriminate between competing explanations before structural reform.

Nearest neighbors: experimental design, A/B tests, causal diagnosis.

Verdict: **REJECTED AS NOVEL.**

---

## T118-11 — Rights invariants under degraded operation

Plain claim: define rights that must remain true even in emergency/failure modes.

Nearest neighbors: graceful degradation, constitutional emergency rules, safety invariants.

Verdict: **REJECTED AS NOVEL; practically useful.**

---

## T118-12 — Institutional error budget

Plain claim: allow a bounded number/rate of low-stakes process failures to preserve learning velocity, but halt changes when the error budget is exhausted.

Nearest neighbors: site-reliability error budgets, risk budgets, experimental governance.

Transfer is interesting but currently too metaphorical and hard to define ethically across heterogeneous human harms.

Verdict: **REJECT / do not promote.**

---

## T118-13 — Change-point-triggered governance review rather than calendar review

Plain claim: trigger constitutional review when process/outcome distributions materially shift rather than only annually.

Nearest neighbors: event-triggered control, SPC, incident-triggered review.

Verdict: **REJECT AS NOVEL.**

---

## T118-14 — Collusion-resistant random review assignment

Plain claim: randomly assign eligible reviewers/panels so factions cannot reliably route cases to friendly adjudicators.

Nearest neighbors: random juries, random audit assignment, anti-corruption mechanism design.

Verdict: **REJECT AS NOVEL; practical in appropriate systems.**

---

# Batch 18 disposition

## Promoted / retained

- **C011 shadow governance:** survives targeted attack.
- **C012 metamorphic governance testing:** new provisional cross-domain transfer.
- **C005:** church-planting aggregates provide a qualitative non-Hutterite contrast but not the parent-resolved comparator still needed.

## Demoted

- **C010 governance fault injection:** demoted from the Creative Tail originality ledger because established continuity exercise doctrine is too close; keep as community-development practice.

## Method lesson

The new communities lessons layer is doing its job: C010 can lose novelty status without being lost as practical knowledge.
