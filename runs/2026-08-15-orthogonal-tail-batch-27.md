# Orthogonal Tail Batch 27 — Feedback, Queueing, Aggregation, and Shared-Resource Dynamics

Date: 2026-08-15

## Outcome

**No new Creative Tail survivor.**

The strongest candidates collided with humanitarian/supply-chain bullwhip research, safety-reporting measurement literature, polycentric resource externalities, queueing/scheduling theory, control-system feedback delay, and statistical aggregation problems.

Practical lessons are preserved for the communities repo.

---

## T127-01 — Federation request-signal amplification / bullwhip

Plain claim: local communities can each react rationally to uncertain supply, expected rationing, lead time or batching by padding/lumping requests, causing upstream federation demand to fluctuate much more than actual underlying need.

Nearest neighbors: canonical bullwhip-effect literature; humanitarian/NGO relief supply chains explicitly study bullwhip amplification under information and transport delays.

Verdict: **REJECT AS NOVEL; PRACTICAL.**

Operational lesson: where a federation manages replenishable shared goods/resources, track actual consumption/need, local inventory, pipeline and requests separately; do not infer real demand from request volume alone.

---

## T127-02 — Rationing-game request inflation

If communities expect scarce shared resources to be allocated proportionally to requested amount, they may rationally inflate requests.

Nearest neighbor: rationing gaming is one of the classic bullwhip mechanisms; mechanism-design/allocation literature also covers strategic demand.

Verdict: **REJECT.**

---

## T127-03 — Local buffering hides synchronized depletion

Communities can look independent while all drawing down local buffers under one common shock, causing a late synchronized demand spike at the federation.

Nearest neighbors: inventory pooling/systemic risk/common shocks.

Verdict: **REJECT AS NOVEL; PRACTICAL.**

---

## T127-04 — Transparency penalty in incident counts

Communities with better reporting culture can show more incidents/near misses than opaque communities, causing naïve federation rankings to punish transparency.

Nearest neighbors: healthcare/aviation safety-reporting literature explicitly warns that report counts reflect reporting culture/willingness, exposure and definitions as well as underlying harm.

Verdict: **REJECT AS NOVEL; STRONGLY PRACTICAL.**

---

## T127-05 — Separate reporting volume from harm rate

Use reporting activity, exposure, severity, actual harm and safety-culture indicators as separate dimensions.

Nearest neighbors: direct current near-miss and safety-reporting frameworks.

Verdict: **REJECT; PRACTICAL.**

---

## T127-06 — Shared-actuator capture

Multiple independent reviewers are not truly independent remedies if every corrective action still requires execution by one captured landowner/treasurer/local authority.

Nearest neighbors: enforceability, separation of powers, control-system actuator bottlenecks, existing communities synthesis S-16/S-17.

Verdict: **REJECT / ALREADY WITHIN EVIDENCE-SUPPORTED FRONTIER.**

---

## T127-07 — Priority inversion in rights processing

An urgent safety/rights case can be blocked by a low-priority case/resource holder because both need the same reviewer/quorum/record custodian.

Nearest neighbors: priority inversion/scheduling and grievance triage.

Verdict: **REJECT AS NOVEL; PRACTICAL.**

---

## T127-08 — Head-of-line blocking in serial governance

One complex unresolved case can block unrelated cases if a committee/process handles them strictly in order.

Nearest neighbors: queueing theory and case-management design.

Verdict: **REJECT; PRACTICAL.**

---

## T127-09 — Feedback-lag policy oscillation

If a community changes policy faster than the outcome delay, it can reverse direction repeatedly before learning whether the prior change worked.

Nearest neighbors: control theory, policy feedback, earlier governance-feedback-lag demotion.

Verdict: **REJECT / ALREADY DEMOTED.**

---

## T127-10 — Governance-mediated apparent competition

Two groups can harm each other indirectly through a shared scarce governance/care/mediation resource even without direct conflict.

Nearest neighbors: apparent competition, common-pool allocation and policy externalities.

Verdict: **REJECT AS NOVEL; PRACTICAL CAPACITY WARNING.**

---

## T127-11 — Lossy aggregation erases rare severe signals

Movement dashboards can compress routine data so aggressively that rare high-severity rights/safety failures disappear inside averages.

Nearest neighbors: tail-risk statistics, safety engineering and ordinary aggregation bias.

Verdict: **REJECT AS NOVEL; PRACTICAL.**

---

## T127-12 — Preserve a lossless severe-event channel

Aggregate routine information but retain case-level or severity-preserving treatment for designated high-consequence events.

Nearest neighbors: exception reporting, safety case review, tail-risk management.

Verdict: **REJECT AS NOVEL; PRACTICAL.**

---

## T127-13 — Monitoring displacement

Once members know exactly what is monitored, strategic misconduct can move into unmonitored channels.

Nearest neighbors: adversarial adaptation, audit evasion, displacement; C016 already addresses unpredictable sampling in bounded audit contexts.

Verdict: **REJECT.**

---

## T127-14 — Local request smoothing can shift risk upstream

A community can hide variability from itself by smoothing/batching resource requests, while increasing upstream timing/forecast risk for the federation.

Nearest neighbors: supply-chain smoothing/bullwhip control.

Verdict: **REJECT AS NOVEL; practical logistics point.**

---

# Practical lessons to mirror into communities

1. do not infer underlying need from federation request volume alone;
2. track actual use/need, local reserves, outstanding pipeline and requests separately where shared-resource replenishment matters;
3. avoid allocation rules that reward inflated requests under expected rationing;
4. size shared resources for synchronized local-buffer depletion under common shocks;
5. never rank community safety by raw incident/near-miss report count alone;
6. treat reporting volume as partly a safety-culture/observability variable;
7. preserve near misses and severity/exposure denominators;
8. ensure independent reviewers have a route to actual remedy execution, not merely recommendation;
9. prevent urgent rights/safety cases from being blocked by low-priority queue/resource dependencies;
10. separate unrelated cases when one complex case would otherwise block a serial process;
11. preserve high-severity low-frequency events against aggregation loss;
12. assume known monitoring can redirect strategic behavior; combine transparent rules with appropriate unpredictable review where justified.

## Method lesson

A non-obvious dynamic imported from operations research can still fail Creative Tail novelty when adjacent humanitarian and safety systems already implement or study the same structure. Preserve communal application value without calling it a discovery.
