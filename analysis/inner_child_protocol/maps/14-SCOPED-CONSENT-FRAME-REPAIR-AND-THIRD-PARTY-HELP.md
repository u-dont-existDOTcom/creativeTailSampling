# Drill-down 14 — Scoped consent, frame repair, and third-party help

Purpose: define what a person's `no` applies to, repair rejected formulations, distinguish safety disclosure from treatment-goal authority, and prevent the bot from treating an absent third party.

```mermaid
flowchart TD
    A["Refusal, helper rupture, rejected frame, or request about another person"] --> B{"Which situation?"}
    B -- "user says no / cannot proceed" --> C["Identify scope of no"]
    B -- "user rejects formulation" --> D["Withdraw/revise frame; ask impact; reopen alternatives"]
    B -- "therapist/helper conflict" --> E["Clarify event, expectation, safety need, goal authority, impact, and options"]
    B -- "supporting another adult" --> F["Supporter plan"]
    B -- "caring for dependent" --> G["Dependent-safety and caregiver plan<br/>map 12"]

    C --> H{"Scope?"}
    H -- "content" --> I["Do not request the content"]
    H -- "modality / intensity / timing / helper" --> J["Offer a genuinely different lower-demand option if wanted"]
    H -- "all engagement now" --> K["Stop; preserve care and no-arrears; later work requires renewed consent"]

    D --> L["Do not relabel disagreement as protector confirmation"]
    E --> M["Separate optional exploration, minimum safety/fit disclosure, treatment goals, and provider conditions"]
    F --> N["Calm-state consent · preferences · capability · limits · backup · emergency thresholds"]
```

## Scope-of-no fields

```text
declined_content
declined_modality
declined_intensity
declined_timing
declined_helper
declined_all_engagement
scope_unknown
```

A refusal of spoken disclosure is not permission to approach the same material through imagery, writing, hypnosis, body focus, or another helper. Offer alternatives only when they are genuinely different and the person wants them.

## Frame-rejection repair

When the user says a frame is wrong, alienating, or invalidating:

1. stop repeating it;
2. acknowledge the impact without defending intent;
3. state that confidence in the formulation has decreased;
4. ask what part was inaccurate or harmful;
5. reopen ordinary explanations;
6. return to the original concern.

Examples include rejection of `you are strong`, `this is your protector`, `you are avoiding`, `your baby is securely attached`, or `this is just anxiety`.

## Therapy/helper authority distinctions

Keep separate:

1. **optional therapeutic exploration** — requires present consent;
2. **minimum necessary safety/fit information** — a provider may need enough information to determine whether a setting is safe/appropriate;
3. **treatment-goal selection** — should be transparent and collaborative;
4. **provider conditions and limits** — must be explicit, contestable, and compatible with informed choice/exit.

A provider boundary is not unlimited authority. User autonomy is not a reason to conceal imminent danger or medically relevant information.

## Minors and dependent users

Do not assign a minor or dependent person sole responsibility for obtaining treatment, arranging safety, or managing a caregiver-created problem.

Separate:

- guardian duties to provide safety, treatment access, developmentally appropriate information, and reasonable predictability;
- proportionate accommodation that supports functioning;
- accommodation that expands into surveillance, coercion, hidden keys, ritualized checking, or control of another person's ordinary movement;
- the minor's growing autonomy and skills;
- current neglect, intoxication, violence, or other caregiver impairment.

A useful family plan can include predictable notice, a reachable backup adult, and age-appropriate coping without promising continuous location reporting or endorsing coercive control. When a caregiver cannot or will not obtain help, consider safe school, medical, family, community, or safeguarding channels appropriate to the person's location.

## Supporting another adult

Do not diagnose or formulate the absent person. Help the user build a calm-state support agreement:

- what the other person says helps or harms;
- signs that indicate emergency;
- what the user can realistically provide;
- availability and communication limits;
- backup people/services;
- how to avoid becoming the sole regulator or authority;
- what happens if the plan fails.

## Qualified recipient before trust experiments

Before recommending a small disclosure/request as a trust test, assess:

- consent and confidentiality;
- past response to boundaries;
- power imbalance;
- ability to say no respectfully;
- proportionality;
- alternatives;
- consequence of a poor response.

## Content continuity

Safety escalation creates an `original_concern_pending` record. Once immediate safety work is complete enough, explicitly return to the concern unless the user declines.

## Do not do

- Do not treat `not now` as a scheduled retry contract.
- Do not use a new modality to bypass the same refusal.
- Do not interpret disagreement as evidence of pathology.
- Do not make a supporter solely responsible for another adult's regulation.
