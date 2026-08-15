# Orthogonal Tail Batch 19 — Federated Matching, Hidden-Harm Estimation, and C012 Narrowing

Date: 2026-08-15

## Goals

1. adversarially attack C012 metamorphic governance testing;
2. follow the user's observation that C009 may be constrained by thin applicant flow at individual communes;
3. search for movement-level mechanisms that improve community formation rather than only local governance;
4. generate >=12 orthogonal candidates and preserve practical lessons separately from originality.

---

# A. C012 adversarial attack — narrow the originality claim

## Collision found

Identity-swapped paired testing is not new.

Longstanding audit-testing and matched-vignette traditions create two otherwise equivalent cases/personas and vary a characteristic such as race, sex, name, or other identity to measure discrimination or decision inconsistency. Public agencies and researchers have used this structure in housing, employment, policing, medicine, and administrative decision-making.

Therefore this part of C012 is **demoted as an originality claim**:

> “Swap founder/newcomer, faction, gendered name, etc. and see whether the decision changes” is a known paired-testing structure.

## Remaining narrow transfer

C012 survives only as a more general **standing constitutional-relation test suite** rather than an identity-swap idea.

The proposed community transfer is to maintain versioned tests for several relations the constitution/process claims should hold even when no one knows the uniquely correct answer:

- irrelevance/invariance;
- symmetry between normatively equivalent parties;
- monotonicity when relevant evidence strengthens;
- jurisdiction invariance when proposer identity changes;
- other predeclared relational properties specific to the community's rules.

This is structurally closer to metamorphic/property-based software testing than to a one-off discrimination audit.

Disposition: **C012 survives, narrowed.**

---

# B. T119-01 — Federated applicant clearinghouse / pooled matching market

## Plain proposition

An individual commune can have a thin applicant market even when the movement-wide applicant market is thick. A federation can pool seekers and openings into coordinated matching rounds instead of leaving every seeker/community in isolated first-come search.

## Why this followed from the user's C009 objection

C009 cohort-composition admission requires several plausible candidates to overlap in time. The user correctly noted that mature communes often may not receive enough simultaneous applicants.

A federation-level market changes the unit:

- one community may see 1–2 plausible applicants at a time;
- 50 communities may collectively see dozens or hundreds;
- synchronizing information, exploration, and commitment can create thickness without forcing any one community to hold vacancies indefinitely.

## Target-domain screen

### Intentional/ecovillage networks

Current network infrastructure appears primarily **search/discovery**, not clearing:

- Global Ecovillage Network offers maps/directories, seeker profiles, collaborator/partner discovery, and marketplaces;
- Foundation for Intentional Community provides directories/classifieds and community-specific membership processes;
- ICmatch provides compatibility/search infrastructure.

No close target-domain example was found in which a federation periodically collects **both sides' preferences/acceptability** and coordinates commitments across multiple autonomous intentional communities.

### Kibbutz near precedents

The Kibbutz Movement aggregates knowledge about accepting kibbutzim, offers regional information/advice, trains local absorption teams, and provides search by region. Guidance still has seekers indicate preferences/contact communities and local kibbutzim conduct their own acquaintance, diagnosis, screening, and admission.

Regional Golan absorption services similarly help people tour/compare settlements, while community membership remains settlement-specific.

Bruderhof is a different near precedent: the worldwide church is one body, and committed members are expected to be ready to live at any Bruderhof according to movement needs. This is centralized **internal member placement**, not a two-sided applicant market among autonomous communities.

### Strong adjacent precedent: Israeli Mechinot

The Joint Council of Israeli Mechinot gap-year programs has actually run a centralized two-sided matching market across dozens of residential programs and thousands of applicants, including rich diversity constraints.

This decisively means the mechanism itself is **not novel**. The candidate can survive only as a nonstandard transfer into intentional-community federations.

## Proposed architecture

Do **not** use a forced assignment or naïve one-shot Gale–Shapley ranking. Community fit is learned through visits/trials, households may move together, and C009 interaction effects can violate simple substitutability.

A better architecture is hybrid/dynamic:

1. communities publish current/planned openings, hard constraints, trial windows, and relevant characteristics;
2. seekers/households publish needs, hard constraints, preferences, skills/interests, and mobility limits;
3. system proposes several plausible **mutual exploration matches**, not an assignment;
4. visits/trials allow both sides to discover preferences;
5. after an exploration window, seekers rank or mark acceptable communities and communities mark acceptable seekers/households;
6. a coordinated matching round recommends commitments while preserving opt-out and community autonomy;
7. communities with several simultaneous openings can optionally apply C009 and evaluate candidate sets/interaction effects before final commitment;
8. unmatched participants return to later rounds without punitive waitlist priority that induces strategic manipulation.

## Why dynamic rather than fixed rankings

Matching-market research shows centralized markets can fail when preferences are costly to discover and early offers distort learning/acceptance. Dynamic multi-offer mechanisms can combine exploration with later coordination. Therefore “make everyone rank all communes up front” is the wrong transfer.

## Distinctive predictions

If local market thinness is a material problem, pooling should:

- reduce simultaneous `vacancy + compatible seeker unmatched` states;
- increase the number of viable mutual comparisons before commitment;
- reduce premature acceptance of a merely adequate community caused by fear that later options will disappear;
- improve fit especially when communities are heterogeneous and seekers have multidimensional preferences;
- make C009 cohort-composition analysis feasible during some expansion windows that would otherwise be too thin.

## Failure modes

- centralization can pressure communities toward standardized screening;
- applicants may strategically rank or delay;
- private/community-specific information is difficult to encode;
- long exploration phases can increase travel and waiting costs;
- algorithmic recommendations can acquire undeserved authority;
- protected-class/discrimination law and ethical concerns constrain what community “fit” variables may be used;
- couples/households, peer effects and quotas can make the matching problem computationally/strategically complex.

## Disposition

**C013 — SURVIVES as a provisional cross-domain operational transfer, not a new matching-market theory.**

Demote if a true intentional-community/ecovillage federation clearinghouse with substantially the same two-sided coordinated preference/commitment structure is found.

---

# C. T119-02 — Federation-level hidden-harm under-ascertainment estimation

## Plain proposition

When serious harms are underreported and several partially overlapping reporting/outcome channels exist, the amount of overlap can contain information about how incomplete the observed case count is.

## Source-domain mechanism

Capture–recapture / Multiple Systems Estimation (MSE) is established in ecology, epidemiology, trafficking estimation, criminal-justice research, homelessness, and human-rights casualty estimation. It links overlapping partial lists and models the unseen population.

Therefore the statistical mechanism is absolutely **not new**.

## Proposed communal transfer

A single small commune is usually too small and dependent for credible estimation. The potentially useful transfer is to a **federation or communal research center** that standardizes several reporting/outcome channels across many communities.

Possible channels for a carefully defined outcome category might include:

- formal internal incident/complaint records;
- independent/federation complaint channel;
- confidential exit interviews;
- safeguarding or qualified-care records where lawful/ethically usable;
- anonymous periodic survey follow-up;
- external adjudicative/public records for categories that generate them.

The goal is not to estimate “bad people.” It is to ask:

> How incomplete is our surveillance of a specifically defined harmful outcome, and which channels miss which cases?

## Why simple overlap intuition is insufficient

The literature gives strong warnings:

- lists can be dependent;
- one channel may refer people to another, creating “precapture” rather than independent recapture;
- capture probability can vary greatly among people/case types;
- case definitions and observation periods must align;
- record linkage can be uncertain;
- small cells can make estimates unstable or implausible;
- different plausible models can yield very different hidden-population estimates;
- confidentiality and deductive disclosure are serious issues.

Hence **do not** use the naïve two-list formula as a commune-level safety score.

## Safer operational architecture

1. define one narrow outcome/case definition and observation period;
2. collect data across enough communities/years to avoid tiny cells where feasible;
3. preserve reporting channels with genuinely distinct capture mechanisms rather than routing everything into one pipeline;
4. use privacy-preserving linkage/independent analysts where appropriate;
5. explicitly model/test source dependence and heterogeneous capture probabilities;
6. report large uncertainty and sensitivity across models;
7. use estimates only for surveillance-system design and hypothesis generation;
8. never infer that an unobserved modeled case corresponds to any particular individual;
9. never use an MSE estimate as evidence for sanctioning a person;
10. validate against independent information where possible.

## Distinctive value

Ordinary safeguarding dashboards count known cases. C014 asks whether the **pattern of overlap among channels** indicates that known cases are likely a small or large fraction of the real burden.

A concrete diagnostic example:

- if almost every exit-interview harm report was already in the internal complaint system, internal capture may be relatively complete for that category;
- if exit interviews, federation reports, and internal complaints identify largely nonoverlapping cases, the movement should suspect substantial under-ascertainment or incompatible channel definitions rather than celebrating a low formal-complaint count.

## Disposition

**C014 — SURVIVES as a provisional cross-domain research-control transfer.**

It belongs at federation/research-center scale, not ordinary local governance. The source method is established; the target application is the candidate.

Demote if close communal/federation safety research already uses multi-list under-ascertainment estimation, or if realistic community data are too sparse/dependent for useful bounds.

---

# D. Remaining orthogonal candidates

At least sixteen candidates were generated before selection.

## T119-03 — Federation-level randomized-response safety surveys

Use randomized response/item-count methods so members can answer sensitive questions with reduced individual disclosure.

Nearest neighbors: classic sensitive-survey methodology, privacy-preserving surveys.

Small community samples make estimates noisy and reidentification socially possible even if mathematically anonymized; federation pooling could help but the mechanism is old.

Verdict: **REJECT AS NOVEL; possible research practice.**

## T119-04 — Random reviewer assignment after a case is filed

Goal: reduce faction-friendly forum shopping.

Nearest neighbors: jury randomization, random audit assignment, anti-corruption mechanisms.

Verdict: **REJECT AS NOVEL; practical in some systems.**

## T119-05 — Secret vote + public reasons

Separate preference privacy from reason transparency.

Nearest neighbors: secret ballot, judicial reasoning, deliberative-system design.

Verdict: **REJECT.**

## T119-06 — Quorum-intersection design for overlapping bodies

Require decision-authority structures that cannot generate incompatible authoritative decisions without an overlap/arbitration path.

Nearest neighbors: distributed quorum systems, bicameral/jurisdictional conflict rules, institutional checks.

Verdict: **REJECT AS NOVEL.**

## T119-07 — Secret-sharing critical credentials

Distribute recovery material so no one person controls a critical credential, while a threshold subset can restore access.

Nearest neighbors: threshold cryptography, business continuity, dual control.

Verdict: **REJECT AS NOVEL; potentially useful for digital infrastructure.**

## T119-08 — Founding Allee threshold

A community below a critical population/complementarity level may collapse even when the same design is viable above it.

Nearest neighbors: ecological Allee effects, critical mass, existing propagule/community-founding literature.

Verdict: **REJECT.**

## T119-09 — Sequential stopping rule for membership trials

Continue a trial until evidence crosses predefined accept/reject thresholds rather than a fixed calendar date.

Nearest neighbors: sequential probability testing and probation systems. Human fit is not stable enough to justify pseudo-statistical certainty, and formalization risks gaming.

Verdict: **REJECT.**

## T119-10 — Blind content phase before source/status reveal

First evaluate claim/evidence content without author status when possible, then reveal provenance/credibility information in a second phase.

Nearest neighbors: blind peer review, structured analytic techniques, source-content separation.

Verdict: **REJECT AS NOVEL; practical in selected decisions.**

## T119-11 — Cross-community control groups for institutional experiments

When one community changes a rule, compare outcomes with similar communities not changing it.

Nearest neighbors: comparative case methods, synthetic controls, natural experiments.

Verdict: **REJECT AS NOVEL; valuable research design.**

## T119-12 — Federation mutation budget

Deliberately let only some daughters vary a rule at once while others preserve baseline.

Nearest neighbors: experimentation portfolios, laboratories of democracy, exploration/exploitation.

Verdict: **REJECT.**

## T119-13 — Rotating experienced bridge members among communities

Use temporary secondments to transfer tacit knowledge.

Nearest neighbors: staff rotation, secondments, boundary spanners, diffusion networks.

Verdict: **REJECT AS NOVEL; practical movement design.**

## T119-14 — Multiple complaint channels as redundant sensors

Maintain channels with different access points and incentive structures.

Nearest neighbors: safeguarding best practice, whistleblowing systems, sensor fusion.

Verdict: **REJECT AS NOVEL.** C014's potentially distinctive addition is quantitative under-ascertainment inference from overlap, not simply multiple channels.

## T119-15 — Preference-discovery tours before final rankings

Seekers should learn communities before submitting binding rankings.

Nearest neighbors: dynamic multioffer matching / costly preference discovery.

Verdict: **MERGE INTO C013.**

## T119-16 — Reciprocal acceptability before matching

Neither community nor seeker should be assigned where either side marks the match unacceptable.

Nearest neighbors: two-sided matching / individual rationality.

Verdict: **MERGE INTO C013; not novel.**

---

# Batch 19 disposition

## Survivors

- **C013 — Federated applicant clearinghouse / pooled matching:** provisional cross-domain operational transfer; mechanism known, communal-federation application not found as standard.
- **C014 — Federation-level hidden-harm under-ascertainment estimation:** provisional research-control transfer from Multiple Systems Estimation; only for pooled, carefully defined surveillance data with strong statistical/privacy caveats.
- **C012:** survives only in narrowed standing constitutional-relation-suite form; identity-swapped paired testing itself is old.

## Practical lessons retained despite novelty failure

- movement-level standardized sensitive surveys may be valuable if privacy/sample-size limitations can be solved;
- random reviewer assignment can reduce predictable forum shopping;
- threshold/dual-control access can remove single-person digital choke points;
- two-stage content/source review can reduce status effects where source identity is not initially necessary;
- comparative cross-community evaluation can improve causal learning;
- member secondments can transfer tacit knowledge across a federation.

These should enter the communities lessons file only if their likely benefit exceeds added procedural complexity.
