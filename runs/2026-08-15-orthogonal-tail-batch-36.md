# Orthogonal Tail Batch 36 — Quorum Geometry, Recusal, and Conflicting Valid Decisions

Date: 2026-08-15

## Outcome

**No new Creative Tail survivor.**

The strongest target transfer is useful but belongs as a safety extension of C015 governance rights-liveness rather than a new finding:

> **Test quorum safety under realistic recusal/vacancy states: no reachable pair of simultaneously valid decision paths should be able to authorize mutually incompatible irreversible actions unless the constitution also specifies which decision stays, supersedes, or reverses the other.**

Distributed quorum theory owns the intersection mechanism. Cooperative/community bylaws already contain quorum, conflict-of-interest, override and appeal machinery. Administrative/legal appeals already use precedence/stay/supersession rather than requiring original and appellate bodies to share personnel.

Practical lessons are mirrored to the communities repo.

---

# A. Source mechanism

Distributed quorum systems maintain consistency by constraining the **geometry of valid quorums**, not merely the size of each quorum. Classic quorum systems require pairwise intersection; Byzantine quorum systems require stronger intersections so enough nonfaulty participants remain in common. Flexible Paxos shows that intersection requirements depend on protocol phase rather than `all quorums must always overlap`.

The transferable conceptual distinction is:

- **liveness:** some valid decision path remains available;
- **safety/consistency:** two valid paths cannot both commit incompatible state without a defined reconciliation rule.

This distinction is already native to distributed systems and is not new.

---

# B. Communal governance target

Community/cooperative rules commonly contain:

- board or committee quorum thresholds;
- conflict-of-interest recusal;
- empowered committees;
- member/body overrides;
- appeal routes;
- supermajority decisions.

These ingredients can interact unexpectedly when membership changes through recusal, vacancy, absence, emergency substitution or delegated authority.

A clause-by-clause review can miss a **coalition-level contradiction**.

## Example pattern

- Local safety committee can impose a long-term access restriction with any 3 of 5 members.
- Two members recuse because of conflicts.
- A federation appeal body separately has authority to restore access.
- An emergency officer also has temporary authority to restrict access when the committee is unavailable.

Every clause can be individually reasonable while the combined state machine allows two bodies to issue incompatible live orders unless priority/stay/version rules are explicit.

---

# C. Practical quorum-safety test

For each high-consequence decision family:

1. list every role/body that can authorize, stay, reverse, extend or supersede the decision;
2. specify eligible membership under ordinary conditions;
3. enumerate realistic recusal/vacancy/absence/substitution states;
4. enumerate valid quorums/decision coalitions;
5. identify pairs of decisions that are mutually incompatible if simultaneously live;
6. test whether two valid coalitions can issue those conflicting decisions;
7. if yes, specify an explicit serialization rule: stay, epoch/version, precedence, appeal supremacy, temporary-status rule, or neutral conflict resolver;
8. rerun after amendments or structural personnel changes.

For small bodies this can be exhaustively enumerated without sophisticated software.

---

# D. Independence vs intersection

A naive transfer would say `make original and appellate quorums intersect`.

That can be **wrong** for governance because the appeal body's independence may require implicated original decision makers to be excluded.

The safer mapping is:

- within one replicated decision layer, quorum intersection/personnel overlap can support consistency;
- across original decision and independent appeal, consistency should usually come from **state/authority transition rules** rather than shared conflicted personnel.

Examples:

- filing appeal automatically stays part/all of the decision;
- appellate order explicitly supersedes local order;
- emergency order expires when ordinary/appeal authority acts;
- every order carries a case/version identifier and later valid orders supersede named earlier states;
- two coequal bodies with overlapping jurisdiction must route conflict to a designated resolver rather than race.

---

# E. Candidate audit

At least fourteen candidates were screened.

## T136-01 — Pairwise quorum intersection for all governance bodies
**Verdict:** REJECT / BAD GENERALIZATION. Appeal independence can require disjoint personnel.

## T136-02 — Quorum safety enumeration under recusal
**Verdict:** PRACTICAL extension of C015; not a separate novelty survivor.

## T136-03 — Recusal can break quorum safety as well as liveness
**Verdict:** PRACTICAL; corporate/cooperative conflict rules already confront recusal/quorum interaction.

## T136-04 — Two individually valid bodies can issue incompatible orders
**Verdict:** REJECT AS NOVEL. Jurisdiction/appeal/polycentric conflict is established.

## T136-05 — Decision epochs/version tokens
Every high-consequence order references the case/state version it modifies.

**Verdict:** REJECT AS NOVEL; versioning/administrative-order practice.

## T136-06 — Appeal-as-state-transition rather than second independent command
**Verdict:** REJECT AS NOVEL; administrative appellate systems already work this way.

## T136-07 — Automatic stay on appeal
**Verdict:** REJECT; direct legal precedent, appropriate only for selected decision types.

## T136-08 — No automatic stay for immediate safety conditions
**Verdict:** PRACTICAL boundary; ordinary law/safeguarding already distinguishes.

## T136-09 — Explicit conflict resolver for coequal bodies
**Verdict:** REJECT AS NOVEL; constitutional/federal conflict resolution.

## T136-10 — Enumerate all valid decision coalitions
**Verdict:** PRACTICAL formal-methods extension; merge with C015.

## T136-11 — Check authorization safety after vacancy substitutions
**Verdict:** PRACTICAL; merge.

## T136-12 — Same-person intersection can undermine independent review
**Verdict:** KNOWN separation-of-powers/conflict principle; useful warning against literal distributed-systems analogy.

## T136-13 — State intersection instead of personnel intersection
Independent bodies share a canonical case record/state lineage rather than people.

**Verdict:** REJECT AS NOVEL; administrative record/appeal structure.

## T136-14 — Quorum-policy regression tests after amendments
**Verdict:** MERGE into C012/C015 practical architecture.

---

# F. Practical lessons to mirror into communities

1. test quorum **safety** as well as liveness;
2. enumerate valid coalitions after realistic recusals/vacancies/substitutions;
3. identify incompatible decisions that two valid paths could issue simultaneously;
4. specify which order stays/supersedes/reverses the other before conflict happens;
5. do not force personnel overlap between original and appellate bodies when independence requires separation;
6. use case/order versioning or equivalent state lineage for high-consequence decisions;
7. distinguish immediate temporary safety orders from final adjudication and appellate state;
8. give coequal bodies an explicit jurisdiction-conflict resolver rather than a race-to-act;
9. rerun quorum safety/liveness tests after governance amendments;
10. for small bodies, exhaustively enumerate coalition states rather than relying on intuition about `majority` or `two-thirds`.

## Method lesson

Cross-domain mapping sometimes reveals a useful **negative transfer**: the source-domain rule `quorums must intersect` should not be copied literally when the target requires independent appeal. Preserve the safety property—no inconsistent committed state—but implement it through target-appropriate authority transitions rather than shared conflicted people.
