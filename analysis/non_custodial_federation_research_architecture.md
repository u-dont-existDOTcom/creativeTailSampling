# Non-Custodial Federation Research Architecture

Updated: 2026-08-15
Status: conceptual implementation architecture derived from C023/C024; not a deployed software specification.

## Goal

Allow a federation/community research center to compute useful sensitive aggregate evidence while reducing the need for any single organization—including the research center—to possess readable individual raw responses.

This architecture has **four distinct layers**. They should never be collapsed into one claim that the survey is `anonymous`.

---

# Layer 1 — Participant eligibility without answer identity

Goal: allow eligible members/former members to contribute while preventing duplicate/fake submissions, without attaching identity to answer contents.

Possible structure:

1. independent eligibility authority verifies participation right;
2. participant receives one-time anonymous/pseudonymous token;
3. research response system validates token but cannot map it back to identity;
4. eligibility authority never sees response contents.

Threats to handle:
- leadership submitting for members;
- duplicate tokens;
- outsiders flooding results;
- token issuance revealing who participated;
- small groups inferring participants from timing.

---

# Layer 2 — Input confidentiality / non-custody

Goal: no local leader or central research analyst sees plaintext individual answers.

Candidate architectures, from simpler to heavier:

## A. Independent trusted custodian

Not fully non-custodial, but simplest baseline. Raw data held by an independent research/ombuds entity rather than local community/federation leadership.

## B. Split-key / secret-sharing trustees

Individual input is split/encrypted so no single trustee can reconstruct it alone.

Possible trustees:
- federation research office;
- independent ombud/research nonprofit;
- elected privacy trustee.

## C. Secure aggregation

Participant inputs are cryptographically masked and only an aggregate can be recovered after enough participants contribute.

Good for:
- counts;
- sums;
- means;
- histograms;
- simple vectors.

## D. General secure multiparty computation

Use when parties must jointly calculate more complex functions without revealing inputs.

## E. Federated analytics

Data stays on participant/community-controlled clients/silos and only protected aggregate computations are combined.

Do not use heavy crypto by default where independent custody is sufficient and trustworthy.

---

# Layer 3 — Output disclosure control (C023)

Input privacy does **not** guarantee safe output.

An exact aggregate of eight people can reveal an individual under auxiliary information or differencing.

Required controls:

- release/query ledger;
- cumulative overlap analysis;
- subgroup/complement checks;
- entrant/leaver differencing checks;
- minimum aggregation scope;
- pooling across communities/time when needed;
- output suppression/coarsening;
- differential privacy when justified;
- access tiers;
- rare-event privacy handling.

If formal DP is used, document:
- privacy unit;
- neighboring-data definition;
- epsilon/delta or equivalent parameters;
- composition budget;
- query/adaptive release policy;
- entrant/leaver treatment.

---

# Layer 4 — Query governance

Even encrypted data can be reconstructed through malicious/overlapping queries if analysts have unrestricted output access.

Every query/output request should declare:
- research purpose;
- variables;
- population/time window;
- overlap with previous releases;
- requested precision;
- output audience;
- privacy impact;
- authorization.

Possible governance:
- preapproved standard queries;
- independent privacy review for new queries;
- rate/precision limits;
- cumulative disclosure budget;
- public query history for non-sensitive metadata.

---

# Member-facing trust statement

The privacy explanation should be technically true and understandable.

Example architecture-specific wording:

> Your individual response is encrypted/secret-shared before federation researchers receive anything. No community leader and no single research administrator receives your readable individual answers. Researchers receive only approved aggregate results once enough responses exist. Aggregate releases are separately checked to prevent small-group identification.

Do not use this wording unless the implementation actually provides each property.

---

# Research-center integration

## Batch 43/44 disclosure-incentive diagnostics

Where feasible, randomize/compare:
- ordinary independent confidential custody;
- stronger non-custodial secure aggregation.

Measure whether:
- privacy confidence changes;
- sensitive reporting changes;
- participation changes.

This tests whether technical custody risk materially affects data validity.

## C022 measurement canaries

Canary classifications can be securely aggregated across communities when individual/coder identities are sensitive.

## Batch 41 leaver cohorts

Former-member responses can enter the same non-custodial system without exposing their identities to former local leadership.

## C023 release composition

All public outputs still pass cumulative privacy review.

---

# Threat model checklist

Before implementation specify:

- trusted/nontrusted parties;
- maximum colluding trustees;
- malicious vs honest-but-curious participants;
- server compromise;
- metadata/timing leakage;
- participant device compromise;
- denial/dropout;
- fake/duplicate participation;
- query reconstruction;
- output auxiliary information;
- legal compulsion/subpoena;
- future key compromise;
- software update/supply-chain risk.

---

# Deployment ladder

Do not jump directly to custom MPC software.

## Stage 0 — organizational independence

Independent external custodian + strong access control + C023 release ledger.

## Stage 1 — anonymous eligibility tokens

Separate eligibility from answers.

## Stage 2 — simple secure aggregation pilot

One federation-wide low-complexity statistic where raw custody is unnecessary.

## Stage 3 — privacy/mode validation

Test whether non-custody changes trust/participation/reporting relative to ordinary confidential research.

## Stage 4 — expand only if justified

Add more aggregate queries, MPC/federated analytics, formal DP or private linkage only when demonstrated benefit exceeds complexity/error costs.

---

# Stop conditions

Do not deploy complex non-custodial computation when:
- sample is too small for safe output regardless of input protection;
- participants cannot use/access the system reliably;
- qualitative/contextual raw data are necessary;
- independent trusted custody already solves the practical threat at much lower cost;
- security implementation cannot be competently audited/maintained.

---

# Core principle

> **Minimize entrusted information by architecture, not only by policy—while remembering that a privacy-preserving computation can still produce a privacy-violating result.**
