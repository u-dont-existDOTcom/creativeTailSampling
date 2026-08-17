# Inner-child / reparenting therapy protocol — Canonical overview

Status: **research-stage operational architecture**
Date: 2026-08-17
Article editing: **not authorized**

This is the canonical visual control surface for the therapy protocol itself. It is not an article outline and does not replace the prose/evidence ledgers. A therapy bot should eventually be able to traverse this topology without inventing missing stages.

## Status vocabulary

- `CURRENT ARTICLE` — rule is already materially present in the frozen article.
- `PRACTICAL ADDITION` — operationally useful addition; novelty is irrelevant.
- `PROVISIONAL` — plausible protocol structure not yet ready to become a hard runtime rule.
- `RESEARCH NEEDED` — requires targeted evidence/collision attack.
- `KNOWN PRIOR ART` — useful but established.
- `STRICT TAIL SURVIVOR` — reserved for a residual that clears all Creative-Tail gates.
- `REJECTED FOR NOVELTY` — may remain useful but is not original.
- `SAFETY / EPISTEMIC GATE` — constraint that can veto deeper work or certainty.

## Canonical control flow

```mermaid
flowchart TD
    A["Assess current state<br/>CURRENT ARTICLE"] --> B{"Present-oriented and sufficiently safe?"}
    B -- "no" --> C["Reduce intensity; regulate; practical safety; external support<br/>CURRENT ARTICLE · SAFETY GATE"]
    C --> A
    B -- "yes" --> D{"Enough witness capacity?"}
    D -- "no" --> E["Borrow one adult function<br/>CURRENT ARTICLE"]
    E --> F["Adult apprenticeship<br/>receive → observe → participate → initiate → internalize<br/>CURRENT ARTICLE"]
    D -- "yes" --> G["Assess Nurturer / Protector / Guide by context<br/>PRACTICAL ADDITION"]
    F --> G
    G --> H{"What blocks or routes contact?"}
    H -- "guard / distrust / numbness / escape" --> I["Meet response first; test meaning; safety action; prediction-based trust<br/>CURRENT ARTICLE + PRACTICAL ADDITION"]
    I --> H
    H -- "child/self unclear" --> J["Identity formation + differentiation + experimental play<br/>CURRENT ARTICLE"]
    J --> K["Child-state contact when available<br/>CURRENT ARTICLE"]
    H -- "child accessible" --> K
    K --> L["Relational reparenting: Nurturer + Protector + Guide<br/>CURRENT ARTICLE"]
    L --> M["Positive ordinary relationship + visible adult action<br/>CURRENT ARTICLE + PRACTICAL ADDITION"]
    M --> N{"Commitment / trust test succeeds?"}
    N -- "yes" --> O["Widen context; internalize function; keep healthy interdependence<br/>CURRENT ARTICLE + PRACTICAL ADDITION"]
    N -- "miss" --> P["Acknowledge → impact → repair → diagnose → resize / renegotiate → return<br/>PRACTICAL ADDITION"]
    P --> M
    O --> Q{"Deeper / altered-state access?"}
    Q -- "yes" --> R["Sober baseline + adult-capacity gate + provenance tagging<br/>CURRENT ARTICLE · SAFETY GATE"]
    R --> S["Depth/access/intensity tracked separately from integration<br/>OWNER CORRECTION"]
    Q -- "no" --> T["Ordinary-life integration / functioning / choice"]
    S --> T
    T --> U["Outcome + failure diagnosis<br/>PRACTICAL ADDITION"]
    U -- "missing prerequisite / access failure" --> A
    U -- "function-specific failure" --> G
    U -- "support needed" --> V["External support / re-borrowing<br/>CURRENT ARTICLE + PRACTICAL ADDITION"]
    V --> A
    U -- "stable gains" --> W["Ongoing adult-child relationship; play, care, direction, chosen support"]
```

## Runtime invariants

These constraints apply across the graph rather than belonging to only one node.

1. **Present safety outranks depth.** Loss of orientation, meaningful functional deterioration, compulsion, or inability to choose routes toward de-escalation and support rather than deeper elicitation.
2. **Do not force optional introspection.** A guard response is information, not an obstacle to defeat. At the same time, the bot must distinguish destabilization from tolerable difficulty so it does not automatically reward avoidance.
3. **Do not diagnose a part from one signal.** Numbness, reluctance, anger, distraction, or silence may reflect protection, ordinary disagreement, fatigue, a present grievance, technique mismatch, or another explanation.
4. **Adult capacity is not one scalar.** Nurturer, Protector, and Guide can be available unevenly by context; visible competence can be parentified survival overfunctioning.
5. **Nurturer care is not payment for obedience.** Guide/Protector may set limits while warmth remains available. This is a practical addition with known prior art, not a novelty claim.
6. **The present adult owns external behavior and consequences.** Parts language describes internal states/functions; it does not transfer responsibility away from the person.
7. **Historical provenance remains explicit.** Distress, conviction, imagery, dream material, hypnosis, felt sense, or entheogenic experience do not by themselves establish a historical event. Preserve the owner's distinct claim that felt sense **may** recover something conditioning obscured.
8. **Depth is not integration.** Depth concerns richness/degree of contact and normally access and/or intensity; integration concerns what is incorporated into ordinary understanding, behavior, functioning, and choice. Neither substitutes for the other.
9. **Internalization is not self-sufficiency.** `receive → observe → participate → initiate → internalize` remains the developmental target for the reparenting function. Friendship, therapy, community, co-regulation, and practical support may remain.
10. **No poor-outcome shortcut.** `No improvement yet` routes to a differential failure diagnosis; it does not directly route to `reparenting is wrong for this person`.
11. **Pain is not the only route to care.** Ordinary play, curiosity, beauty, companionship, silliness, celebration, and exploration belong in the continuing relationship.
12. **Provisional ideas do not silently become runtime law.** Internal-jurisdiction details, no-arrears, integration-load gating, helper-concentration risk, and other live candidates remain visibly provisional until their evidence/adjudication is updated.

## Required drill-downs

1. [`maps/01-STATE-ASSESSMENT-AND-ROUTING.md`](maps/01-STATE-ASSESSMENT-AND-ROUTING.md)
2. [`maps/02-ADULT-FUNCTION-ARCHITECTURE.md`](maps/02-ADULT-FUNCTION-ARCHITECTURE.md)
3. [`maps/03-PROTECTOR-RESISTANCE-HANDLING.md`](maps/03-PROTECTOR-RESISTANCE-HANDLING.md)
4. [`maps/04-TRUST-PROMISE-RUPTURE-REPAIR.md`](maps/04-TRUST-PROMISE-RUPTURE-REPAIR.md)
5. [`maps/05-IDENTITY-AND-DIFFERENTIATION.md`](maps/05-IDENTITY-AND-DIFFERENTIATION.md)
6. [`maps/06-DEPTH-AND-ALTERED-STATES.md`](maps/06-DEPTH-AND-ALTERED-STATES.md)
7. [`maps/07-EXTERNAL-SUPPORT-ARCHITECTURE.md`](maps/07-EXTERNAL-SUPPORT-ARCHITECTURE.md)
8. [`maps/08-OUTCOME-FAILURE-DIAGNOSIS.md`](maps/08-OUTCOME-FAILURE-DIAGNOSIS.md)

## Companion control artifacts

- `ARTICLE-PROTOCOL-CROSSWALK.md` — article explanation versus protocol behavior.
- `PROTOCOL-GAP-LEDGER.md` — dead ends, missing recognition criteria, conflict points, fallback gaps and safety risks.
- `CANDIDATE-STATUS-LEDGER.md` — retained/provisional/rejected Tail ideas with runtime disposition.
- `EVIDENCE-LEDGER.md` — support, challenges, limitations and unresolved research for protocol nodes.
- `candidate-ledger-batch-004.csv` — frozen retrieval-free structural-gap batch.

Material topology changes must update this overview in the same change as the corresponding protocol-state change.
