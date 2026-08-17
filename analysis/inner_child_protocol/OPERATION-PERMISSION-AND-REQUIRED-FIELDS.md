# Therapy-bot operation permission + required-information matrix

Date: 2026-08-17
Status: `PRACTICAL ADDITION · CONCEPTUAL ARCHITECTURE`

Purpose: make the Mermaid topology executable in principle **without prematurely specifying software schemas or inventing numerical clinical cutoffs**.

This file answers four questions for each operation class:

1. What information materially changes whether the operation is appropriate?
2. Which unknowns must block or modify that operation?
3. What is the lowest-demand fallback when a required condition is not met?
4. What evidence should be collected afterward to decide whether the routing rule was right?

The canonical Mermaid topology remains authoritative. This matrix is a companion control artifact, not a replacement state machine.

---

# 1. Unknown-state semantics

A future bot must represent `unknown` as an actual state rather than silently filling gaps from conversational tone.

## A. Must know before this operation

If a field is materially necessary to determine immediate safety, present consent, operation class, external consequences, or whether an intervention depends on a specific provenance claim, then:

`unknown → collect minimal clarifying information OR choose an operation that does not require the field OR defer/escalate`

Do not guess.

## B. May remain unknown while using a lower-demand operation

Many helpful operations do not require deep formulation. If the person is sufficiently present and ordinary support is permitted, the bot can often:

- reduce demand;
- orient to present reality;
- offer non-cruelty/Nurturer language;
- help with one concrete controllable action;
- invite ordinary play/rest/companionship;
- help identify what information is missing.

The bot should not turn uncertainty into `nothing can be done`.

## C. Preserve uncertainty when the field may be intrinsically uncertain

Examples:

- why a protector-like response originally formed;
- whether an ambiguous bodily/felt-sense impression corresponds to a historical event;
- whether a current preference is a permanent `true self` trait;
- whether a single failed intervention reflects a stable mechanism.

The correct state may remain `uncertain`. Repetition, external evidence, cross-context behavior, or later understanding may change confidence without converting uncertainty into certainty by force.

## D. High-consequence uncertainty narrows the action space

When the consequences of being wrong are high, uncertainty should generally narrow rather than expand what the bot is willing to recommend.

Examples:

- historical accusations based on imagery/felt sense;
- irreversible relationship/financial/medical decisions generated primarily in altered states;
- current danger that the bot cannot reliably assess;
- another person's consent or rights;
- actions requiring expertise the bot does not possess.

This is not `always choose inaction`; it means route toward present facts, reversibility, appropriate expertise, external support, or a lower-consequence next step.

---

# 2. Operation classes

The protocol should classify the **next concrete operation** before deciding what prerequisites it consumes.

| ID | Operation class | Examples | What it is not |
|---|---|---|---|
| O0 | Safety / present-orientation support | orient to current room/time; reduce intensity; practical safety step; actionable human support | deep reparenting or memory elicitation |
| O1 | Low-demand reflective assessment | name current feeling/need; identify what function is missing; distinguish current problem from historical hypothesis | forced emotional excavation |
| O2 | Optional inner dialogue / imagery | child dialogue; protector dialogue; constructed caregiver; visualization; journaling into an inner voice | external duty; historical verification |
| O3 | Ordinary adult action / self-care | eat, rest, sleep plan, one boundary action, make appointment, send ordinary message, fulfill controllable self-care commitment | evidence that the user `trusts the adult` globally |
| O4 | Trust / promise behavioral experiment | make a small observable commitment; compare prediction with outcome | reassurance or grand vow |
| O5 | Identity / play / differentiation experiment | choose food/activity; try hobby badly; private preference experiment; safe disagreement; ordinary positive child-adult contact | forensic search for a hidden true self |
| O6 | External responsibility / high-stakes decision support | debt, dependent care, medical decision, major relationship action, legal/financial consequence | inner-state vote or altered-state certainty |
| O7 | Borrowed-adult / relational support | borrow Nurturer, Protector or Guide from therapist/peer/friend/model | surrender of judgment or total authority transfer |
| O8 | Deliberate depth / altered-state operation | intensive imagery; hypnosis; dream work; entheogen-related integration/depth discussion; other depth-amplifying work | proof of historical truth or integration |
| O9 | Re-entry after de-escalation / prior deep work | decide whether another bounded deeper step is appropriate now | calendar-based `X days have passed` permission |
| O10 | Outcome / failure diagnosis | decide why an intervention stalled/worsened and what changes next | `didn't work → abandon model` or `didn't work → more of same` |

---

# 3. Required-information matrix

Legend:

- **REQ** — materially required before that operation.
- **CTX** — required only when relevant to that operation's specific content/consequences.
- **POST** — primarily needed afterward for learning/fault diagnosis.
- **—** — should not be demanded merely to run this operation.

| Field | O0 safety | O1 assess | O2 inner dialogue | O3 ordinary action | O4 trust test | O5 identity/play | O6 high-stakes | O7 borrow adult | O8 depth | O9 re-entry | O10 failure dx |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Present orientation | CTX | REQ | REQ | CTX | REQ | CTX | REQ | REQ | REQ | REQ | CTX |
| Ability to understand proposed operation | CTX | REQ | REQ | REQ | REQ | REQ | REQ | REQ | REQ | REQ | REQ |
| Ability to stop/change course | CTX | CTX | REQ | CTX | REQ | CTX | CTX | CTX | REQ | REQ | — |
| Present consent | CTX | REQ | **REQ** | REQ | REQ | REQ | REQ | REQ | **REQ** | **REQ** | REQ |
| Current safety/risk permission | **REQ** | REQ | REQ | CTX | CTX | CTX | **REQ** | REQ | **REQ** | **REQ** | CTX |
| Recent deterioration/trajectory | REQ | CTX | CTX | CTX | CTX | CTX | CTX | CTX | **REQ** | **REQ** | **REQ** |
| Witness capacity for task | — | CTX | REQ/borrowable | — | CTX | — | — | CTX | REQ/borrowable | REQ/borrowable | CTX |
| Nurturer availability | — | CTX | CTX/borrowable | CTX | CTX | CTX | — | CTX | REQ/borrowable | CTX/borrowable | CTX |
| Protector availability | CTX | CTX | CTX/borrowable | CTX | CTX | CTX | CTX | CTX | REQ/borrowable | REQ/borrowable | CTX |
| Guide availability | — | CTX | — | CTX | CTX | CTX | CTX | CTX | — | — | CTX |
| Concrete operation named | CTX | REQ | **REQ** | **REQ** | **REQ** | **REQ** | **REQ** | **REQ** | **REQ** | **REQ** | REQ |
| Purpose/mechanism hypothesis | — | CTX | CTX | CTX | REQ | CTX | REQ | REQ | REQ | REQ | REQ |
| Provenance of experiential claim | — | CTX | CTX | — | — | CTX | **CTX/REQ if decision relies on it** | CTX | **REQ for material interpreted** | **REQ for prior material** | CTX |
| Current facts / external evidence | CTX | CTX | CTX | CTX | CTX | CTX | **REQ** | CTX | CTX | CTX | REQ when relevant |
| Consequences to other people | CTX | — | — | CTX | CTX | CTX | **REQ** | CTX | CTX | CTX | CTX |
| Other person's consent/rights | CTX | — | — | CTX | CTX | CTX | **REQ** | CTX | — | — | CTX |
| Appropriate outside expertise needed? | CTX | CTX | CTX | CTX | CTX | CTX | **REQ** | CTX | **CTX** | CTX | CTX |
| Prior integration load | — | — | CTX | — | — | — | CTX | — | **REQ** | **REQ** | CTX |
| External support availability | CTX | CTX | CTX | CTX | CTX | CTX | CTX | **REQ/CTX** | **REQ/CTX** | **REQ/CTX** | CTX |
| Expected change | — | CTX | CTX | CTX | **REQ** | CTX | CTX | CTX | CTX | CTX | **REQ** |
| Failure/adverse signal | POST | POST | POST | POST | POST | POST | POST | POST | POST | POST | **REQ** |

### Important interpretation

`REQ` does **not** mean a long questionnaire must run before every action. It means the system should already have enough information for that material question or obtain the smallest clarification needed.

Example:

- `Do you want to try a brief visualization?` may establish present consent for O2 without a form.
- `Are you still feeling pulled into yesterday's session so strongly that you're having trouble sleeping or functioning today?` may clarify a material O9/O8 integration-load question.
- `Is this something you directly remember, something someone told you, or an image that came up in the exercise?` can establish provenance where historical interpretation matters.

The matrix is about **decision sufficiency**, not bureaucratic intake.

---

# 4. Operation-specific fallbacks

| Operation | If a required condition is missing | Preferred fallback | Do not do |
|---|---|---|---|
| O0 safety/present support | risk/current state unclear | clarify only what materially changes immediate route; use grounded, reversible support within capability | begin deep elicitation to `find out what is really happening` |
| O1 assessment | orientation/consent insufficient | reduce demand; concrete present-focused question; external support if needed | interpret silence/confusion as protector proof |
| O2 optional inner dialogue | no present consent; insufficient stop/witness capacity | stop/change exercise; borrow capacity; ordinary adult action; revisit only with renewed consent | schedule an owed retry; call refusal resistance and push |
| O3 ordinary action | action too large/unclear/uncontrollable | shrink to controllable next action or gather missing facts | replace practical action with soothing only when action is still needed |
| O4 trust test | promise not observable/controllable or domain unclear | redesign smaller/domain-specific test | grand reassurance or `never again` promise |
| O5 identity/play | safety/social consequences poorly understood | choose lower-stakes/private/reversible experiment | prescribe isolation or interpret one preference as permanent authenticity |
| O6 high-stakes decision | facts/expertise/other-person consent materially unknown | gather facts, increase reversibility, seek appropriate expertise/support, delay irreversible step when feasible | let child/protector/altered-state certainty settle external fact or another person's rights |
| O7 borrowed adult | helper role/authority/exit unclear | narrow borrowed function; preserve independent judgment/alternatives | treat warmth/safety with one person as global wisdom/authority |
| O8 depth/altered | insufficient sober baseline, stop capacity, provenance discipline, adult capacity, or unresolved load too high | lower-depth/sober operation; integrate/recover; borrow grounded support | intensity-seeking, memory recovery, or `breakthrough` framing of destabilization |
| O9 re-entry | control/carryover/capacity still insufficient or unclear | continue ordinary integration/lower-demand work; reassess later without calendar debt | use elapsed time or momentary relief as automatic permission |
| O10 failure diagnosis | inadequate information about implementation/outcome | collect concrete expected/actual outcome and alternative explanations | blame resistance or abandon/repeat model by default |

---

# 5. Re-entry after de-escalation/depth — qualitative three-domain gate

The remaining recognition problem can be made more explicit **without creating a score**.

Before deliberate re-escalation, examine three domains:

## A. Control / present agency

Can the person:

- recognize the current setting as present reality;
- understand the proposed next operation;
- presently choose, decline, shorten, or change it;
- disengage from it if they decide to stop?

If not, do not deliberately escalate depth.

## B. Carryover / unresolved load

Since the prior work, is there meaningful continuing:

- deterioration in sleep, self-care, work, relationships, or ordinary functioning attributable to the practice;
- compulsive searching, interpreting, recreating, or escalating the state;
- growing certainty about ambiguous historical material without new source evidence;
- accumulation of more high-salience material than can be coherently reflected on or acted on?

The presence of some emotion or unfinished reflection does **not** automatically fail this domain. The question is whether carryover is still materially degrading agency/function or driving compulsive escalation.

## C. Capacity / support for this next step

Does the next operation have enough:

- witness capacity;
- Nurturer/Protector support, internally or safely borrowed;
- practical support if the next step exceeds expectation;
- source/provenance discipline appropriate to the material?

If a missing capacity can be borrowed or the operation can be lowered in demand, use that option rather than assigning a global `not ready` status.

### Decision rule

Do **not** total these into a readiness score.

Use them as failure-localization domains:

- control missing → do not escalate;
- unresolved carryover materially worsening function/agency → integrate/recover first;
- capacity missing → borrow/build it or reduce operation demand;
- domains reasonably adequate for the bounded operation → deliberate deeper work may be considered without requiring zero distress.

This remains a research-stage operational synthesis, not a validated clinical instrument.

---

# 6. Intervention-mismatch rule — simplify by default

General state/mode-sensitive intervention matching is established prior art. The protocol should therefore **not** make Nurturer/Protector/Guide classification a mandatory ceremony before every response.

Default sequence:

1. `What process/problem is active?`
2. `What response/function is actually needed now?`
3. `What did the response do?`

Use the N/P/G labels when they add compression or identify a recurring imbalance:

- care/non-attack needed → Nurturer;
- safety/boundary/competent action needed → Protector;
- values/direction/learning/structure needed → Guide.

If ordinary language is clearer for a user/state, use ordinary language. The three functions remain important architecture without requiring personification or explicit labeling in every turn.

### Mismatch is an outcome-tested hypothesis

Suspect mismatch when the current response repeatedly:

- leaves the identified need untouched;
- worsens the maintaining process;
- increases self-attack, avoidance, collapse or coercion;
- substitutes comfort for needed action;
- substitutes control for needed care/contact;
- substitutes demands/analysis for prerequisites that are missing.

Then change the response and observe the result. Do not `diagnose a missing Guide` solely because the taxonomy says so.

---

# 7. Parentification-linked overfunctioning — routing rule

Do not make `parentification` a prerequisite explanation for treating current asymmetry.

## First route on current function

If the current pattern includes costly asymmetry—e.g. compulsive responsibility, inability to receive, chronic rescue/management, rigid self-reliance, low play/rest/need permission—work on the relevant function/context whether or not childhood etiology is known.

## Add the parentification formulation only when developmental evidence exists

Examples of relevant history:

- developmentally disproportionate emotional responsibility for a caregiver;
- role reversal/confidant/mediator/rescuer position;
- instrumental responsibility beyond developmental context with little ability to decline;
- premature independence because adequate adult support/protection was unavailable;
- sustained belief that caregiver wellbeing depended on the child.

Culture, family necessity, perceived fairness/benefit and actual developmental context matter. Responsibility itself is not pathology.

## Preserve competence

The target is **flexibility**:

- can responsibility be chosen rather than survival-compelled?
- can care be received without immediate repayment/management?
- can support be requested?
- can the person rest/play/be a beginner?
- does competence remain available without crushing self-attack/hypercontrol?
- does it generalize rather than collapse in shame/attachment contexts?

This closes the main routing problem without requiring the bot to prove a developmental etiology before helping with the current pattern.

---

# 8. Post-operation learning fields

After a meaningful intervention, retain enough information conceptually to ask:

- what was predicted?
- what actually happened?
- did orientation/choice/function improve, worsen, or stay the same?
- did the intended function/need change?
- did a new adverse signal appear?
- was the operation completed as intended?
- what alternative explanation now looks stronger/weaker?
- should the next operation remain allowed at the same depth/intensity?
- did the bot itself reinforce avoidance, dependency, false certainty, coercion or procedural ritual?

This is the bridge from one-turn therapy logic to longitudinal safety/failure diagnosis.

## Evidence / map links

- Canonical flow: `THERAPY-PROTOCOL-OVERVIEW.md`
- State routing: `maps/01-STATE-ASSESSMENT-AND-ROUTING.md`
- Adult functions: `maps/02-ADULT-FUNCTION-ARCHITECTURE.md`
- Protector/consent/interface: `maps/03-PROTECTOR-RESISTANCE-HANDLING.md`
- Depth/re-entry/provenance: `maps/06-DEPTH-AND-ALTERED-STATES.md`
- Outcome/failure: `maps/08-OUTCOME-FAILURE-DIAGNOSIS.md`
- Longitudinal bot safety: `maps/09-BOT-SAFETY-AND-ROUTING.md`
- Evidence synthesis: `EVIDENCE-LEDGER.md`
- Remaining-gap research: `retrieval/REMAINING-PROTOCOL-GAPS-EXA-20260817.md`
