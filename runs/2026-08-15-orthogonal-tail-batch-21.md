# Orthogonal Tail Batch 21 — Rights Liveness, Revocation, and Multi-Step Recovery

Date: 2026-08-15

## Outcome

One narrow provisional survivor:

- **C015 — Governance rights-liveness verification**

Most other candidates collapsed into established access-control, process-mining, business-continuity, distributed-transaction, or legal-procedure ideas. Those can still be practical community-development lessons.

---

# A. Search boundary

Batch 21 intentionally left the previous evolutionary/matching/surveillance analogies and sampled distributed systems, formal methods, authorization, workflow verification, and irreversible multi-stage transactions.

The strongest historical collision is important:

- formal institutional/bylaw specification and model checking already exist;
- formal access-control systems already distinguish safety and liveness properties;
- legal/institutional literature already distinguishes rights that exist formally from remedies that are unavailable, ineffective, or unduly prolonged.

Therefore **none of those ingredients is claimed as new**.

The candidate only survives if the target transfer is narrower:

> Treat a communal right as a temporal/reachability property of the governance process, and automatically search realistic adverse states for a counterexample where the right remains written but cannot actually complete.

---

# B. C015 — Governance rights-liveness verification

## Plain proposition

A constitution can grant a right in text while its own procedural dependencies make the right impossible to exercise in some reachable states.

For a right that promises review, appeal, exit settlement, records access, emergency bypass, succession, or another remedy, the relevant design question is not only:

> Is the right stated?

but:

> From every realistic state in which a valid request is made, is there still a permitted path that reaches the promised review/remedy/closure within an acceptable bound?

This is a **liveness** question rather than merely a static-rights question.

## Nearest-neighbor attack

### Direct ancestors

Formal-methods research already models:

- organizational/bylaw rules as states, roles, actions and transitions suitable for model checking;
- institutional design and enactment constraints formally;
- access-control systems using reachability, safety and liveness properties;
- workflow deadlock/completeness properties;
- legal contracts/normative requirements as interaction protocols with permissions, prohibitions, obligations and remedies.

Legal doctrine also recognizes that a nominal remedy may be unavailable, inadequate, ineffective, or unduly prolonged.

### What the search did not find

Targeted searches did not locate a close intentional-community practice, nor a clear legal/institutional formal-methods implementation whose central test is:

> model-check whether a human governance **right/remedy remains live under adverse combinations of recusal, vacancy, quorum, jurisdiction, deadline, appointment and delegation state**.

The distinction is narrower than “formalize bylaws” or “check for deadlock.”

## Example counterexample trace

Suppose the constitution says every member may appeal an expulsion to an independent five-person review body.

The text looks adequate.

Model state:

1. member invokes appeal;
2. two review members must recuse because they participated in the original decision;
3. one seat is vacant;
4. the remaining two cannot meet the three-person quorum;
5. vacancies can only be filled by the local governing body;
6. that body is also implicated and barred by conflict rules from acting on the appeal;
7. no alternative appointing authority or timeout escalation exists.

The appeal right exists in prose but is **dead** in this reachable state.

A model checker/state-space search should produce the trace as a counterexample.

## Property classes

For each important procedure, specify at least:

### Safety

Something prohibited never happens.

Examples:

- an implicated adjudicator never participates in final review;
- an emergency temporary restriction never silently becomes permanent;
- an authority never exercises a power outside its jurisdiction;
- a person cannot lose a protected necessity solely because an appeal is pending.

### Liveness

Something promised remains reachable/eventually occurs under explicit assumptions.

Examples:

- a valid appeal can eventually reach a competent nonconflicted reviewer;
- a valid records request can reach production or an appealable denial;
- a leadership vacancy can eventually be filled;
- an exit valuation can eventually reach binding settlement;
- an emergency bypass can reach an authorized decision even if ordinary officers are unavailable.

### Bounded liveness

The right/remedy is reachable within a defined procedural/time bound rather than “eventually” in an unbounded sense.

This matters because a remedy delayed for years can be formally live but practically useless.

## Minimal implementation protocol

1. select a high-value right/procedure;
2. encode only the state variables that affect it: roles, vacancies, recusals, quorum, jurisdiction, appointments, deadlines, delegations, escalation and termination;
3. specify safety and liveness properties before searching;
4. enumerate realistic fault/adversarial states rather than assuming every office is staffed and cooperative;
5. run state-space/model checking or bounded exhaustive search;
6. inspect counterexample traces;
7. modify the governance procedure, not merely the model, when the trace is realistic;
8. rerun after every material constitutional amendment;
9. preserve counterexamples as regression tests.

## Candidate rights for first use

- complaint intake and bypass;
- appeal/review of expulsion or sanction;
- child/safeguarding escalation;
- records access/correction;
- exit valuation/payment;
- emergency medical or safety bypass;
- leadership removal/succession;
- recusal and replacement of conflicted adjudicators;
- federation-level appeal from a captured local body.

## Why this could improve community design

Ordinary bylaw review is good at spotting missing clauses and obvious contradictions. Humans are worse at reasoning through combinations such as:

- vacancy + recusal + quorum;
- local capture + escalation prerequisite;
- temporary delegation + delegator removal;
- expired deadline + unavailable notice channel;
- two bodies each waiting for the other to establish jurisdiction.

Formal reachability analysis is specifically good at producing the sequence that makes a seemingly adequate procedure fail.

## Falsifiers / demotion conditions

Demote C015 if:

- a close target-domain precedent already routinely verifies human rights/remedies as temporal liveness properties under adverse governance states;
- realistic community procedures cannot be usefully abstracted without losing the very discretion that makes them work;
- most discovered counterexamples are modeling artifacts rather than plausible governance failures;
- ordinary tabletop review finds the same important failures at lower cost.

## Critical limits

- verification proves properties of the **model**, not of actual humans;
- omitted states/assumptions can create false confidence;
- liveness proofs can depend on unrealistic fairness assumptions such as “someone eventually acts”;
- discretion, interpretation and informal workarounds are difficult to formalize;
- the method should expose procedural traps, not replace human normative judgment;
- highly coercive systems can be perfectly live and still unjust, so liveness complements rather than replaces rights content and outcome evaluation.

## Disposition

**SURVIVES as C015 — provisional cross-domain operational transfer.**

Claim only the narrow target application: formal/bylaw modeling and liveness verification are old; the candidate is to make **exercisability of important communal rights under adverse procedural states** a recurring verification target.

---

# C. Remaining candidates

At least sixteen candidates were generated before selection.

## T121-02 — Expiring authority leases

Plain claim: high-impact authority should automatically expire or require renewal rather than persist until someone remembers to revoke it.

Nearest neighbors: privileged-access management, just-in-time access, time-limited credentials, emergency-power sunsets.

Verdict: **REJECT AS NOVEL; KEEP PRACTICAL.**

Useful metric: `revocation latency` — time from a person's loss/change of role to removal of all corresponding financial, digital, records, legal-signature and delegated authority.

---

## T121-03 — Cascading revocation of derivative authority

Plain claim: if A's authority was derived solely from B's office, loss of B's delegable authority should revoke downstream delegations unless an independent grant remains.

Direct collision: cascading delegation-revocation is a mature access-control research topic, with explicit delegation paths, propagation dimensions and executable revocation schemes.

Verdict: **REJECT AS NOVEL; KEEP PRACTICAL.**

---

## T121-04 — Authority attenuation under delegation

Plain claim: a delegate should not be able to pass on more authority than the delegator had or was permitted to delegate.

Nearest neighbors: capability security, RBAC delegation, XACML delegation chains.

Verdict: **REJECT.**

---

## T121-05 — Governance conformance checking from event logs

Plain claim: compare actual decision-process traces with the constitution/process model to detect where governance-in-use departs from governance-on-paper.

Direct collision: process mining/conformance checking explicitly compares event logs to normative/reference process models and is used for corporate governance/compliance.

Verdict: **REJECT AS NOVEL; KEEP PRACTICAL if record burden is reasonable.**

---

## T121-06 — Compensating transitions for non-atomic communal changes

Plain claim: multi-step actions such as admission + housing + account permissions + work assignment, or fission + asset transfer + debt + records, cannot always be atomically rolled back; define compensating actions for failure after each irreversible step.

Nearest neighbor: Saga/compensating-transaction pattern; contracts and escrow/conditions precedent provide adjacent human institutions.

Verdict: **REJECT AS NOVEL; KEEP PRACTICAL for complex high-stakes transitions.**

Important human caveat: compensation is not literal rollback. A moved household, broken relationship, disclosed private record, or lost opportunity may not be reversible; the design should identify uncompensable steps before proceeding.

---

## T121-07 — Two-phase commitment for irreversible transitions

Plain claim: separate provisional reservation/preconditions from final irreversible commitment.

Nearest neighbors: two-phase commit, escrow, conditions precedent, probation/trial membership.

Verdict: **REJECT.**

---

## T121-08 — Explicit fail-open/fail-closed defaults for procedural deadlock

Plain claim: when a process cannot complete, define in advance whether the default preserves the status quo, permits temporary action, suspends coercive power, or escalates externally.

Nearest neighbors: safety/security fail-open/fail-closed design, legal default rules, emergency procedure.

Verdict: **REJECT AS NOVEL; KEEP PRACTICAL and integrate with C015.**

A community should not discover its deadlock default during a real sanction, medical emergency or leadership crisis.

---

## T121-09 — Worst-case recusal/quorum stress testing

Plain claim: intentionally search combinations of conflicts, recusals, absences and vacancies that make review or governance impossible.

Verdict: **MERGE INTO C015.**

---

## T121-10 — Orphaned-office detection

Plain claim: find roles that can only be filled/removed by an authority that can itself become vacant, conflicted or dissolved.

Verdict: **MERGE INTO C015.** This is one counterexample family.

---

## T121-11 — Constitutional version tagging on decisions

Plain claim: every consequential decision should record which rule/version authorized it.

Nearest neighbors: legal effective dates, policy/configuration versioning, audit logs.

Verdict: **REJECT AS NOVEL; useful for later conformance/review.**

---

## T121-12 — Procedural garbage collection

Plain claim: periodically identify powers, exceptions, committees or emergency permissions that remain technically valid but no longer have a current purpose.

Nearest neighbors: privilege creep/access review, statute/repeal cleanup, policy lifecycle management.

Verdict: **REJECT.**

---

## T121-13 — Bounded remedy timeouts with fallback escalation

Plain claim: an appeal/review route that misses a deadline should automatically escalate or switch forum rather than stall indefinitely.

Nearest neighbors: administrative/court deadlines, local-remedy doctrines recognizing undue delay or ineffectiveness, timeout/failover engineering.

Verdict: **REJECT AS NOVEL; useful implementation of C015.**

---

## T121-14 — Decision-state event sourcing

Plain claim: preserve append-only events/state changes so governance history can be reconstructed rather than overwriting current status.

Nearest neighbors: event sourcing, append-only audit logs, legal records/minutes.

Verdict: **REJECT.**

---

## T121-15 — Duplicate-resource reservation prevention

Plain claim: separate committees should not both promise the same scarce room, cash, land, vehicle, staff time or housing slot; use a shared reservation/commitment state.

Nearest neighbors: databases, inventory control, accounting encumbrances.

Verdict: **REJECT AS NOVEL.**

---

## T121-16 — Emergency-authority sunset and scope caps

Plain claim: temporary emergency powers should expire automatically and be incapable of self-extension without independent authorization.

Nearest neighbors: constitutional emergency-power sunset clauses, security leases.

Verdict: **REJECT AS NOVEL; PRACTICAL.**

---

# Batch 21 disposition

## New provisional survivor

- **C015 — Governance rights-liveness verification**

## Practical-but-known lessons worth mirroring into communities repo

1. measure revocation latency after role changes;
2. cascade revocation through derivative delegations where appropriate;
3. log the rule/version authorizing important decisions;
4. conformance-check actual procedure against written process when logs make this feasible;
5. define compensating actions before complex non-atomic transitions;
6. identify which steps are genuinely irreversible/uncompensable;
7. define fail-open/fail-closed/escalation behavior for procedural deadlocks;
8. automatically sunset temporary emergency authority;
9. use C015 to stress-test combinations of recusal, vacancy, quorum, conflict and jurisdiction.

## Method lesson

A broad technical analogy is not enough. “Model-check bylaws” failed because that has already been proposed. The candidate survived only after reducing it to a narrower target-domain object whose failure is operationally distinct: **a right can exist syntactically yet be unreachable in the governance state machine.**
