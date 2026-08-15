# Orthogonal Tail Batch 25 — Replicated Governance, Stale State, and Institutional Memory

Date: 2026-08-15

## Outcome

One narrow provisional cross-domain survivor:

- **C018 — Replicated-governance tombstones**

Most other candidates collapsed into established polycentric governance, business continuity, policy experimentation, causal inference under interference, secure logging, access-control revocation, conflict-of-laws, version-control, and change-management ideas.

The useful rejected candidates are preserved for the communities practical-lessons layer.

---

# A. C018 — Replicated-governance tombstones

## Plain proposition

When a rule, institutional pattern, or template component is retired because it produced a known failure, a movement that copies governance across daughter communities should propagate a durable **negative record of the retirement** alongside the positive rules it continues to replicate.

The goal is not merely to preserve history. It is to prevent stale copies, old handbooks, forked daughter constitutions, or later template merges from silently resurrecting a pattern the movement already learned to reject.

## Source-domain mechanism

Distributed databases use deletion markers/tombstones because a replica that missed a deletion can later reintroduce the old value as if it were current state. DataStax documentation explicitly describes this zombie-record failure mode.

Architecture Decision Record practice independently preserves superseded decisions, rationale, context, and consequences rather than erasing old decisions after replacement.

These source mechanisms are established; they are not claimed as new.

## Target-domain nearest neighbors

The intentional-community/commons target domain already contains substantial institutional-memory practice:

- FEC maintains an archive of systems-and-structures documents from member communities;
- East Wind policy documents sometimes explicitly say that a provision replaced prior legislation or that an old part was deleted;
- FIC has advocated community archiving;
- commons research has shown that revoked village bylaws can be archived yet become forgotten or unusable, and has proposed systematically comparing historical and current bylaws to recover institutional knowledge.

Therefore **"keep old policies and rationale" is not a Creative Tail discovery**.

The surviving transfer is narrower:

> **Treat certain retired governance patterns as active deprecation state that must propagate through the same replication channels as the rules/templates that could otherwise reintroduce them.**

## Required tombstone contents

A useful governance tombstone should identify at least:

1. the retired rule/pattern and its semantic scope;
2. the version/date and communities or conditions in which it operated;
3. why it was retired;
4. the evidence/counterexample/failure mode that motivated retirement;
5. the current replacement or safer alternative, if any;
6. whether the problem was universal or context-specific;
7. conditions under which reconsideration would be legitimate;
8. the authority/process required to override the tombstone;
9. references to relevant incident/decision records without exposing protected private data.

The **semantic scope** matters. A movement should not defeat the system by renaming the same functional pattern.

Example: if a founder-veto arrangement was retired because the founder could control both accusation and appeal, the tombstone should capture that functional conflict, not only the literal old clause. A later rule saying "founder confirmation required for exceptional cases" should trigger review if it recreates the same authority relation.

## Replication rule

Whenever a community or federation:

- copies a governance template;
- creates a daughter community;
- imports policies from another community;
- merges an old handbook with a current one;
- restores records from an archive;
- forks a constitution;
- publishes a starter packet for new communities;

it should import/check relevant tombstones as well as current positive rules.

A tombstone is not an eternal prohibition. It is a **forced-memory / forced-review object**. Reintroduction is allowed only by explicitly confronting the old failure and documenting why the present context changes the inference.

## Why the distributed-systems mapping changes operations

Ordinary archiving answers:

> What did we used to do?

A replicated-governance tombstone answers:

> What did we deliberately stop doing, why, and what mechanism prevents a stale branch from making it current again without review?

That adds an operational propagation requirement. Negative knowledge must travel with the positive template.

## Distinctive predictions

If the mechanism matters:

- decentralized movements with many copied/forked policy sets should periodically reintroduce deprecated practices through stale documentation or independent reconstruction;
- ordinary archives will reduce complete forgetting but will not reliably stop resurrection when current templates and deprecated-state records travel separately;
- daughter communities inheriting explicit semantic tombstones should detect/review more attempted functional reintroductions before adoption;
- the benefit should rise with document/template replication, community fission, personnel turnover, and long intervals between policy revisions.

## Critical limits

- tombstones can fossilize bad old conclusions and suppress legitimate experimentation;
- semantic matching can overreach and classify genuinely different arrangements as equivalent;
- privacy may prevent preserving full incident evidence;
- movements can become bureaucratically burdened if every minor policy deletion creates permanent deprecation machinery;
- daughter communities need autonomy to override tombstones through an explicit reasoning process;
- the system only helps if replicated policy/document channels are important enough for stale-state resurrection to be plausible.

Use primarily for high-consequence rules/patterns whose retirement encodes a real lesson, not every formatting or administrative change.

## Falsifiers / demotion conditions

Demote C018 if a close intentional-community/cooperative movement precedent is found that already:

1. records retired governance patterns with rationale/failure semantics;
2. propagates those deprecation records across daughter/template replication;
3. treats stale reintroduction as an explicit governance-version conflict requiring review.

Simple archives, version history, or text saying "this replaces previous legislation" are near precedents but do not by themselves satisfy all three.

## Disposition

**SURVIVES as C018 — provisional cross-domain operational transfer.**

Claim only the replication/anti-resurrection architecture. Archival institutional memory, historical bylaw comparison, superseded decision records, and database tombstones are established source/adjacent-domain practices.

---

# B. Remaining Batch 25 candidates

At least sixteen plain candidates were generated before promotion.

## T125-02 — Split-brain governance control

Plain claim: if local and federation bodies can simultaneously exercise overlapping irreversible authority, explicitly prevent or resolve conflicting concurrent decisions rather than assuming communication.

Nearest neighbors: polycentric governance already studies multiple overlapping autonomous decision centers, coordination failure, conflict, overarching rules and conflict-resolution mechanisms; federal systems specify competence and dispute resolution.

Verdict: **REJECT AS NOVEL; PRACTICAL.**

Operational lesson: map overlapping jurisdiction, priority/serialization, temporary authority and conflict routes before a crisis.

---

## T125-03 — Partition mode for federation disconnects

Plain claim: predeclare what a local community may continue deciding when federation communication/review is unavailable and what must freeze/escalate.

Nearest neighbors: business continuity, emergency delegation, federalism, deadlock defaults, distributed-system partition policy.

Verdict: **REJECT AS NOVEL; PRACTICAL.**

---

## T125-04 — Minimum viable community / graceful degradation order

Plain claim: under severe resource shortage, intentionally shed low-priority functions before necessities, rights, records and exit routes degrade accidentally.

Nearest neighbors: continuity planning, triage, graceful degradation, emergency management.

Verdict: **REJECT AS NOVEL; STRONGLY PRACTICAL.**

---

## T125-05 — Disturbance mosaic / staggered governance reform

Plain claim: avoid synchronizing every community onto a major untested reform at once; stagger adoption so the movement retains variation and comparative evidence.

Nearest neighbors: policy experimentation, canary deployment, portfolio diversification, ecological refugia.

Verdict: **REJECT AS NOVEL; PRACTICAL.**

---

## T125-06 — Interference-aware daughter-community experiments

Plain claim: when communities exchange members, teachers, money, norms or federation services, treated and comparison communities interfere with one another; do not analyze them as independent experimental units.

Nearest neighbors: causal inference under interference/network spillovers.

Verdict: **REJECT AS NOVEL; RESEARCH-CONTROL.**

---

## T125-07 — Governance schema migrations

Plain claim: a rule change affecting membership states, benefits, offices, records or appeal rights needs an explicit migration of existing cases, not only new constitutional text.

Nearest neighbors: schema migration, legal transition/grandfathering, change management.

Verdict: **REJECT AS NOVEL; PRACTICAL.**

---

## T125-08 — Tamper-evident evidence commitments

Plain claim: where a local unit controls records later used by a federation reviewer, commit to hashes/timestamps or another tamper-evident record state before a dispute where proportionate and lawful.

Nearest neighbors: secure/audit logs, cryptographic commitments, records management.

Verdict: **REJECT AS NOVEL; PRACTICAL WITH PRIVACY LIMITS.**

---

## T125-09 — Stale-template/version check before import

Plain claim: every copied governance document should carry version/deprecation metadata and an importer should check whether it is stale before adoption.

Verdict: **MERGE INTO C018** for high-consequence retired patterns; ordinary version checking remains known.

---

## T125-10 — Local/federation rule compatibility matrix

Plain claim: explicitly map which local rules may vary, which federation floors preempt them, and how conflicts are resolved.

Nearest neighbors: federal preemption, conflict of laws, polycentric jurisdiction mapping.

Verdict: **REJECT AS NOVEL; PRACTICAL.**

---

## T125-11 — Authority epochs / fencing tokens

Plain claim: temporary/delegated authority should carry a version/epoch so stale officeholders or old credentials cannot continue acting after replacement.

Nearest neighbors: access-control revocation, fencing tokens, credential rotation; Batch 21 already captured revocation latency and derivative authority.

Verdict: **REJECT / ALREADY INSIDE PRACTICAL LESSON FRONTIER.**

---

## T125-12 — Outcome-metric schema versioning

Plain claim: when the definition of a success/safety metric changes, preserve its version so historical comparisons do not silently mix different constructs.

Nearest neighbors: data governance/schema versioning/measurement invariance.

Verdict: **REJECT AS NOVEL; RESEARCH-CONTROL.**

---

## T125-13 — Preserve rationale and consequences of superseded decisions

Nearest neighbors: Architecture Decision Records and institutional archives.

Verdict: **REJECT AS NOVEL; merge the propagation/anti-resurrection portion into C018.**

---

## T125-14 — Semantic tombstones rather than literal-text tombstones

Plain claim: record the failed authority/function relationship so a renamed functional equivalent triggers review.

Verdict: **MERGE INTO C018.** This is necessary to make the transfer meaningful rather than simple version control.

---

## T125-15 — Read-only governance mode during uncertain authority

Plain claim: when authority state cannot be verified, permit ordinary reversible operations but freeze irreversible governance changes.

Nearest neighbors: fail-safe defaults, read-only degraded service, emergency legal authority limits.

Verdict: **REJECT AS NOVEL; PRACTICAL depending on domain.**

---

## T125-16 — Preserve a stable reference community during movement-wide innovation

Plain claim: maintain at least one nonadopting reference branch during major reforms.

Nearest neighbors: policy laboratories/control groups/refugia; can be ethically or politically inappropriate.

Verdict: **REJECT.** Use only where voluntary and where spillovers do not destroy comparison validity.

---

## T125-17 — Failed-rule resurrection after personnel turnover

Plain claim: staff/member turnover can reintroduce previously rejected practices because newcomers see only current positive rules, not the negative history that bounded them.

Nearest neighbors: organizational forgetting/institutional memory.

Verdict: **REJECT AS ROOT NOVELTY; provides one target condition for C018.**

---

# C. Source notes used in screening

- DataStax documentation on Cassandra/DSE tombstones and zombie-record resurrection after missed deletion propagation.
- Cognitect / Architecture Decision Record guidance: keep reversed decisions and mark them superseded, preserving rationale/context/consequences.
- Vázquez et al., *Toward an Integrated History to Govern the Commons: Using the Archive to Enhance Local Knowledge* (International Journal of the Commons): revoked bylaws can be archived yet forgotten/unusable; systematic historical/current comparison can recover institutional memory.
- Federation of Egalitarian Communities Systems & Structures archive; East Wind membership policy includes explicit replacement/deletion history.
- Carlisle & Gruby and related polycentric-governance work: overlapping autonomous decision centers, coordination/conflict and overarching conflict-resolution rules are already central theory.

---

# Batch 25 disposition

## Creative Tail survivor

- **C018 — Replicated-governance tombstones**

## Practical-but-known lessons to mirror into `communities`

1. propagate high-consequence deprecation/tombstone metadata with replicated governance templates;
2. preserve superseded decision rationale and failure evidence;
3. explicitly map overlapping local/federation jurisdiction and conflicting-decision resolution;
4. define a federation-disconnect/partition mode;
5. predefine a graceful-degradation order that preserves necessities, direct rights, records and exit routes;
6. use staged/canary movement reforms where ethically appropriate instead of synchronizing every community onto an untested change;
7. account for cross-community interference when evaluating experiments;
8. treat governance changes as state/data migrations, including existing cases;
9. use proportionate tamper-evident commitments for high-stakes records where local evidence control is a real risk;
10. version outcome/metric definitions across time;
11. check imported policies/templates for stale versions and deprecated patterns;
12. during uncertain authority, consider fail-safe limits on irreversible action rather than silently allowing competing bodies to act.

## Method lesson

Negative institutional knowledge has to be evaluated at the **replication channel**, not only the archive. An organization can preserve its history perfectly and still reintroduce a failed rule if current templates circulate separately from the record that says why the rule was retired.
