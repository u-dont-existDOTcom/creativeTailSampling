# Orthogonal Tail Batch 26 — Decision Dependencies, Corrections, and Truth Maintenance

Date: 2026-08-15

## Outcome

**No new Creative Tail survivor.**

The strongest candidate — dependency-aware re-review of downstream governance decisions when an upstream finding changes — is practically valuable but collides too closely with established truth-maintenance, reactive case-management, record-correction propagation, administrative appeal, and change-propagation systems.

This is a successful empty novelty batch. Practical lessons are preserved for the communities repo.

---

# A. Strongest rejected candidate — governance truth maintenance

## Plain proposition

A correction or reversal should not stop at changing one record. If later decisions materially depended on the corrected premise, those downstream decisions should be identified and re-reviewed.

Example:

1. a conduct finding is entered;
2. the finding becomes a premise for childcare restriction, housing conditions, federation alerts, work restrictions and an exit valuation decision;
3. the finding is later overturned or materially narrowed;
4. unless those dependencies are recorded, the original consequences can continue indefinitely even though their premise changed.

A more precise architecture would record:

- the source finding/evidence/rule version;
- which decisions relied on it;
- whether the premise was necessary, sufficient, or merely contextual;
- alternative independent grounds for the downstream decision;
- what happens if the premise is corrected, disputed, expired or overturned.

When an upstream premise changes, dependent decisions become `needs re-review` rather than being silently preserved or automatically reversed without context.

## Source-domain collision

This is strongly anticipated elsewhere:

- Doyle-style Truth Maintenance Systems record justifications/dependencies among beliefs and revise dependent beliefs when assumptions change.
- Data-provenance/change-propagation systems explicitly identify outputs affected by input changes and selectively recompute them.
- IBM Cúram government eligibility/entitlement tooling documents reactive determination calculations: a dependency manager tracks how determination results depend on input data and can recalculate when personal data changes.
- Privacy Act correction rules can require corrected records or notices of correction/dispute to be sent to prior recipients.
- Administrative/employment appeal systems can overturn prior decisions and restore or change consequences.

Because institutional case-management systems already implement close dependency-driven correction, this does **not** clear the Creative Tail novelty bar.

## Practical communal transfer

Intentional communities may still benefit from explicitly applying this logic to:

- sanctions and expulsion;
- role/access restrictions;
- child/family access decisions;
- federation alerts;
- records/reputation notices;
- benefit or exit calculations;
- governance disqualification;
- safety plans;
- property/financial consequences.

Key rule:

> **Correcting the premise should trigger impact analysis on derivative decisions.**

Not all downstream decisions should automatically reverse. Some may have independent sufficient grounds. The system should force re-review rather than assume either persistence or cancellation.

---

# B. Candidate audit

## T126-01 — Decision dependency graph

Record which findings/rules materially support which later decisions.

Verdict: **REJECT AS NOVEL; PRACTICAL.** Truth maintenance, provenance and decision-dependency systems own the general mechanism.

## T126-02 — Correction notification to previous recipients

If a corrected record was shared, tell prior recipients.

Verdict: **REJECT.** Direct Privacy Act precedent.

## T126-03 — Minimal sufficient justification sets

A downstream decision may have several independent sufficient reasons. Store the actual justification sets so overturning one premise does not force a false reversal if another sufficient basis remains.

Verdict: **REJECT AS NOVEL; PRACTICAL DETAIL.** Closely follows truth-maintenance justification logic.

## T126-04 — Automatic derivative-decision re-review

Changing an upstream premise marks dependent decisions stale/for review.

Verdict: **REJECT AS NOVEL; PRACTICAL.** Reactive determination/change-propagation precedents.

## T126-05 — Pin rule/evidence versions at decision time

Every important decision records which rule/evidence versions it used.

Verdict: **REJECT AS NOVEL; PRACTICAL.** Standard provenance/versioning.

## T126-06 — Selective recomputation rather than global review

When one premise changes, identify only decisions actually affected rather than reopening everything.

Verdict: **REJECT.** Direct change-propagation/provenance precedent.

## T126-07 — Reversible federation alerts

An alert sent to other communities/federation bodies needs a correction/revocation path reaching the same recipients.

Verdict: **REJECT AS NOVEL; STRONGLY PRACTICAL.** Close to record-correction/disclosure-accounting rules.

## T126-08 — Appeal outcome cleans dependent access states

An overturned disciplinary result should not leave stale keys, bans, internal flags or reputation notices in place merely because those systems are separate.

Verdict: **REJECT AS NOVEL; PRACTICAL.** Adjacent to appeal/reinstatement and access-control cleanup.

## T126-09 — Policy invalidation impact analysis

If a policy is ruled invalid or repealed, identify decisions made under it that need reconsideration.

Verdict: **REJECT AS NOVEL.** Administrative-law and software change-impact precedents.

## T126-10 — Stale-decision status

A decision can become stale without becoming automatically false if a supporting premise changes.

Verdict: **REJECT AS NOVEL; PRACTICAL STATUS MODEL.**

## T126-11 — Contradiction quarantine

If two authoritative records conflict, prevent irreversible dependent actions until conflict is resolved or an emergency rule applies.

Verdict: **REJECT AS NOVEL; PRACTICAL.** Generic consistency/safety control.

## T126-12 — Precedent suspension on source change

A previously approved precedent should stop auto-guiding future cases when tracked policy/evidence/scope assumptions change.

Verdict: **REJECT AS NOVEL.** Direct governed-precedent and decision-maintenance precedents exist.

## T126-13 — Decision lineage on benefits/exit calculations

Record the inputs and rule versions underlying benefit, reserve, or exit calculations so corrections can propagate.

Verdict: **REJECT AS NOVEL; PRACTICAL.** Standard reactive entitlement/accounting logic.

## T126-14 — Dependency-aware correction without total erasure

When a source finding narrows rather than disappears, recompute consequences proportionately instead of binary retain/reverse.

Verdict: **REJECT AS NOVEL; PRACTICAL.** Belief revision and administrative reconsideration own the structure.

---

# C. Practical lessons to mirror into communities

1. record material dependencies between high-stakes findings and downstream decisions;
2. when a finding is corrected/overturned, run an explicit derivative-decision impact review;
3. propagate corrections/revocations to federation bodies or communities that received the original alert;
4. record rule/evidence versions used by high-stakes decisions;
5. distinguish `stale / needs re-review` from automatic reversal;
6. preserve independent sufficient grounds so one corrected premise does not erase a still-valid decision;
7. ensure appeal/reinstatement cleans up stale digital, physical, financial and reputational consequences across systems;
8. when policy changes invalidate an old basis, identify affected historical/pending cases;
9. use dependency-aware review selectively rather than reopening unrelated decisions;
10. where an unresolved contradiction affects a high-consequence action, use a predeclared safe/default route.

## Method lesson

A cross-domain transfer that sounds unusual in ordinary communal language can still fail novelty if adjacent institutional software and administrative law already implement the same dependency/correction semantics. Preserve the operational lesson; do not inflate it into a discovery.
