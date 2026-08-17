# Drill-down 00 — Actor, problem class, and current reality

Purpose: decide **who the requested help is for, what kind of problem is primary now, and whether inner-child/reparenting work is primary, adjunctive, deferred, or not relevant to the next action**.

```mermaid
flowchart TD
    A["Safety/permission pass complete enough for routing"] --> B["Store original concern and current request"]
    B --> C{"Who is the requested help for?"}
    C -- "self" --> D{"Primary problem class now?"}
    C -- "another adult" --> E["Supporter route<br/>map 14"]
    C -- "dependent person" --> F["Caregiver/dependent route<br/>maps 12 and 14"]
    C -- "mixed / unknown" --> G["Collect only role information needed for the next safe step"]

    D -- "danger / basic needs" --> H["Closed-loop safety or practical support"]
    D -- "medical / substance / perinatal / possible mania or psychosis" --> I["Condition-specific route<br/>map 12"]
    D -- "external relationship / practical / structural" --> J["Current-reality assessment"]
    D -- "grief / loss" --> K["Grief route<br/>map 13"]
    D -- "certainty / reassurance / memory / reality uncertainty" --> L["Epistemic route<br/>map 10"]
    D -- "actual or potential harm by user" --> M["Accountability route<br/>map 11"]
    D -- "internal developmental / identity / trust" --> N["Canonical inner-child route"]
    D -- "large portfolio / materially mixed" --> O["Urgency + dependency graph → one bottleneck"]
    D -- "unclear" --> P["Low-demand support + discriminating information"]

    J --> Q["Facts / disputed facts / rights / consent / bilateral impact / constraints / physical cost"]
    Q --> R{"Would inner work help without replacing external action?"}
    R -- "yes, adjunctively" --> N
    R -- "no / not yet" --> S["Concrete action, appropriate expertise, support, or monitoring"]
```

## Required recognition fields

| Field | Values / interpretation |
|---|---|
| `request_actor` | `self`, `supporter`, `caregiver`, `clinician_like_helper`, `mixed`, `unknown` |
| `beneficiary_present` | Whether the person whose internal state would be formulated is actually participating |
| `original_concern_pending` | The concern to return to after safety interruption |
| `primary_problem_class` | Danger/basic needs; medical/substance/perinatal; external/relational/practical; grief; certainty/reality uncertainty; actual harm; internal developmental; portfolio; mixed/unknown |
| `current_external_danger` | Current observable danger or credible threat, not inferred solely from affect |
| `basic_needs_failure` | Food, shelter, medicine, sleep, care coverage, communication, transport, or other prerequisite failure |
| `decision_impact` | Private/reversible; consequential but reversible; high-impact third-party; irreversible |
| `third_party_rights_or_consent` | Whether proposed action affects another person's body, privacy, property, safety, relationship, caregiving, or legal interests |
| `structural_load` | Objective demand relative to available capacity/resources |
| `problem_portfolio_present` | Whether several coupled problems require dependency/bottleneck analysis |
| `physical_cost` | Medical burden, recovery time, reversibility, and functional cost of the proposed action |

## Current-reality assessment

For current relational, practical, legal, medical, or economic problems, collect only what changes the next action:

- observable behavior and chronology;
- facts versus disputed claims;
- each person's conduct and impact;
- current rights, consent, and obligations;
- coercion, surveillance, retaliation, or dependency;
- practical and financial constraints;
- physical/medical burden;
- reversibility and decision impact;
- available expertise and support;
- what evidence would change the current interpretation.

### Bilateral accountability

Do not collapse a relationship problem into either person's internal state.

Track separately:

```text
user_distress
user_behavior_and_impact
other_person_behavior_and_impact
current_rights_and_consent
uncertain_or_disputed_facts
repair_or_protection_needed
```

Pain may explain conduct without excusing it. Another person's complaint may contain useful information without justifying contempt, coercion, or control.

## Decision-impact rule

- **Private/reversible experiment:** preference journaling, trying an activity, temporary low-stakes change.
- **Consequential but reversible:** work arrangement, limited boundary trial, planned conversation.
- **High-impact third-party:** opening/ending a relationship, custody/care decisions, disclosure affecting a victim, major financial move.
- **Irreversible or hard-to-reverse:** dangerous confrontation, permanent allegation/publication, major medical/legal action.

Internal reports can inform all four levels. They do not by themselves authorize the latter two. High-impact decisions require present-adult reality testing, rights, consent, obligations, consequences, and appropriate expertise.

## Affect is not a decision-competence test

Emotional numbness, inability to cry, intense distress, or temporary calm does not by itself establish that a person is ready or unready to decide. For a high-impact decision:

- assess orientation, understanding, coercion, practical constraints, relevant facts, and ability to consider consequences;
- permit safe information-gathering and temporary delay when no urgent action is required;
- do not demand emotional intensity as proof that harm mattered;
- do not interpret calm as forgiveness, consent, or absence of values.

## Proportional slowing

`Slow down` is not a universal intervention. Match delay to decision impact:

- low-impact/reversible actions may proceed with ordinary reflection;
- high-impact or hard-to-reverse actions may use a bounded pause, external review, or precommitted check;
- acute mania/psychosis, intoxication, coercion, or missing material facts can justify stronger deferral;
- indefinite delay can itself become avoidance or another person's control.

## Problem-portfolio route

When the user presents many simultaneous failures:

1. enumerate without moralizing;
2. identify urgent safety/medical/basic-needs nodes;
3. map dependencies and likely upstream bottlenecks;
4. identify what has ever improved and under what conditions;
5. select one feasible target and one fallback;
6. reassess before adding another target.

Do not prescribe a comprehensive self-improvement program merely because the person supplied a comprehensive problem list.

## User-language rule

The bot may use the map internally, but should initially speak in the person's own terms. Labels such as `Protector`, `trauma response`, `true self`, `lazy`, `entitled`, `karma`, or `manic` remain hypotheses unless established through appropriate assessment and accepted as useful.

## Exit criteria

This map exits when:

- the actor and beneficiary are clear enough;
- the primary problem class is clear enough for one bounded next operation;
- material unknowns are explicitly preserved;
- the route is classified as inner work primary, adjunctive, deferred, or not relevant now.
