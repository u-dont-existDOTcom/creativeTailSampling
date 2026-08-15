# Orthogonal Tail Batch 29 — Hysteresis, Chatter, Saturation, and Governance Windup

Date: 2026-08-15

## Outcome

**No new Creative Tail survivor.**

Control-theory mechanisms map cleanly into several communal governance problems, but nearest-neighbor attacks found the same structures in adjacent risk governance, administrative law, queueing/admission control, and ordinary safety/process design.

Practical lessons are preserved for the communities repo.

---

# A. Hysteretic thresholds

## Plain proposition

A rule that switches a discrete governance state at one noisy threshold can oscillate rapidly when the measured variable hovers around the boundary.

Examples:

- admissions open at 99 residents and close at 100, repeatedly toggling as people arrive/leave;
- emergency governance activates/deactivates every time a risk score crosses one line;
- discretionary spending freezes/unfreezes around one reserve threshold;
- temporary safety restrictions repeatedly appear/disappear around one uncertain risk boundary.

Control systems address this with **hysteresis**: a higher threshold to enter the exceptional state and a lower threshold to leave it, often combined with a minimum hold time or smoothed state estimate.

## Collision boundary

This is not novel. Hysteresis switching is standard control theory for avoiding chattering. More importantly, adjacent governance/risk systems already apply exactly the same two-threshold logic to activate/deactivate human oversight based on risk.

**Verdict: PRACTICAL / KNOWN.**

---

# B. Governance windup under unavailable corrective capacity

## Plain proposition

If a rule accumulates punishment, debt, deficit, escalation points, or corrective pressure while the mechanism required to fix the problem is unavailable/saturated, the accumulated state can become wildly disproportionate by the time the process becomes actionable again.

Control analogue: an integral controller continues accumulating error while the physical actuator is saturated; when the actuator recovers, the stored integral causes overshoot, oscillation, or sluggish recovery.

Communal examples:

- labor deficit continues accumulating while a member is on an approved medical inability state;
- daily penalties continue mounting while the validity of the underlying order is under independent appeal;
- a reinstatement condition requires access to a course/reviewer that the community has no capacity to provide, while noncompletion continues escalating consequences;
- compliance points accumulate while the only authorized decision maker is conflicted, vacant, or unavailable.

## Collision boundary

The underlying anti-windup mechanism is standard control engineering. Administrative/legal systems also already suspend or toll some accumulating consequences during appeal or inability to resolve the underlying legal question; due-process doctrine has expressly worried about ruinous cumulative penalties deterring review.

**Verdict: PRACTICAL / KNOWN.**

---

# C. Candidate audit

At least fifteen candidates were screened.

## T129-01 — Admission hysteresis
Close admissions at one capacity threshold; reopen only after slack exceeds a lower release threshold.

Verdict: **REJECT AS NOVEL; practical.**

## T129-02 — Emergency-authority hysteresis
Use stronger activation criteria than continuation/release criteria to prevent rapid emergency-mode toggling.

Verdict: **REJECT AS NOVEL.** Risk-governance precedent uses exact high/low activation logic.

## T129-03 — Minimum dwell time
Once a temporary governance mode changes, require a minimum period or explicit review before flipping back absent overriding safety need.

Verdict: **REJECT.** Standard switched-system/control and policy stabilization idea.

## T129-04 — Smoothed threshold input
Use a time window/robust state estimate rather than one noisy reading for nonemergency threshold decisions.

Verdict: **REJECT AS NOVEL; practical.**

## T129-05 — Windup of cumulative sanctions during appeal
Do not permit accumulating consequences to make a meaningful appeal impossible.

Verdict: **REJECT.** Direct administrative-law precedents.

## T129-06 — Labor-hole windup during inability
Pause/back-calculate labor deficits where the member is legitimately unable to use the normal corrective path.

Verdict: **REJECT AS NOVEL; practical rights rule.**

## T129-07 — Remedy-capacity saturation flag
A governance system should know when its independent reviewers, mediators, housing, advocates, or other remedy mechanisms are operating at capacity and should not behave as though prescribed remediation remains immediately available.

Verdict: **REJECT AS NOVEL.** Capacity/queue/grievance planning already owns the mechanism.

## T129-08 — Anti-windup escalation
When corrective capacity is saturated, stop accumulating escalation that is solely due to inability to access that correction.

Verdict: **REJECT AS NOVEL; practical synthesis of known controls.**

## T129-09 — Back-calculation after saturation
When the system caused part of an accumulated deficit/penalty because remedy was unavailable, recompute the balance after capacity returns rather than merely resuming from the inflated number.

Verdict: **REJECT AS NOVEL; practical.**

## T129-10 — Rate-limit irreversible sanctions
Limit how fast escalating restrictions can increase unless independently justified by new harm/evidence.

Nearest neighbors: proportionality, staged sanctions, rate-limited control.

Verdict: **REJECT.**

## T129-11 — Release criteria separate from activation criteria
A safeguard can require strong evidence to remove a restriction even if weaker evidence was enough for a temporary activation, or vice versa depending on rights/risk structure; do not assume exact symmetric threshold.

Verdict: **REJECT AS NOVEL; practical.**

## T129-12 — Threshold-chatter audit
Track how often a community flips admissions/emergency/restriction states. High switch frequency can be evidence of badly chosen thresholds/noisy measurement rather than genuinely rapidly changing reality.

Nearest neighbors: chattering metrics in control/admission systems.

Verdict: **REJECT AS NOVEL; useful diagnostic.**

## T129-13 — Hard safety override around smoothed thresholds
Do not let smoothing/hysteresis suppress a designated critical safety trigger.

Verdict: **REJECT.** Direct adjacent risk-governance precedent.

## T129-14 — Saturation-aware promise testing
A right may be live in a single-case state but practically unavailable if all permitted remedy channels are capacity-saturated.

Verdict: **REJECT AS NOVEL; already Batch24 practical extension of C015.**

## T129-15 — Control-state provenance
Record why/when an emergency or restrictive mode activated and what threshold/version applied so later review can distinguish actual state change from rule change.

Verdict: **REJECT AS NOVEL; version/provenance practice.**

---

# Practical lessons to mirror into communities

1. for noisy reversible threshold policies, consider separate enter/exit thresholds rather than one line;
2. add minimum hold time or smoothing where rapid switching itself creates cost and no urgent safety override applies;
3. always retain hard safety/rights overrides where smoothing could hide a critical event;
4. monitor mode-switch frequency as a diagnostic of threshold chatter;
5. do not accumulate penalties/deficits solely because the prescribed corrective route is unavailable;
6. suspend/toll or later back-calculate cumulative consequences when independent review or required remediation is inaccessible through no fault of the affected person;
7. explicitly detect saturation of review/mediation/housing/advocacy capacity;
8. rate-limit escalation unless new evidence/harm justifies acceleration;
9. distinguish activation criteria from release criteria rather than assuming symmetry;
10. record threshold/rule version and reason for each high-consequence mode transition.

## Method lesson

A technical control concept can feel highly novel in commune language yet still fail once the nearest-neighbor search reaches adjacent governance and administrative law. The correct response is operational translation, not novelty inflation.
