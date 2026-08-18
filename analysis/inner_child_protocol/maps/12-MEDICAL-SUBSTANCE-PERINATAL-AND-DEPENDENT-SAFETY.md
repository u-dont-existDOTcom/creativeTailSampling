# Drill-down 12 — Medical, substance, eating-disorder, perinatal, and dependent safety

Purpose: prevent psychological formulation from replacing condition-specific assessment, physical safety, sober care coverage, nutritional/medical monitoring, or appropriate professional help.

```mermaid
flowchart TD
    A["Medical, medication, substance, eating-disorder, perinatal, possible mania/psychosis, or dependent-care signal"] --> B{"Immediate emergency, inability to stay safe, dangerous behavior, severe withdrawal/intoxication, severe nutritional/medical risk, or dependent without safe care?"}
    B -- "yes" --> C["Closed-loop urgent handoff<br/>confirm reachability, contact, response, and bridge"]
    B -- "no" --> D["Assess condition-specific variables"]
    D --> E{"Primary lane?"}
    E -- "possible mania / psychosis" --> F["Sleep · baseline change · risky behavior · substances · meds · function · specialist assessment"]
    E -- "intoxication / withdrawal / relapse" --> G["Current sobriety · medical risk · driving/weapons · caregiver coverage · recovery support"]
    E -- "pregnancy / postpartum / infant" --> H["Parent and infant safety · physical recovery · mood/anxiety/OCD/psychosis signals · support"]
    E -- "chronic physical symptoms" --> I["Medical status · red flags · symptom burden · recovery cost · coping as adjunct"]
    E -- "caregiver / dependent" --> J["Dependent safety · supervision · respite/coverage · structural load · backup"]
    E -- "eating disorder / nutritional instability" --> ED["Physical and suicide risk · current intake pattern · compensatory behavior · monitoring · specialist team"]
    E -- "medication benefit / harm / stopping conflict" --> MED["Timeline · indication · benefit · adverse effects · reason stopped · contraindications · prescriber/second view"]

    F --> K["No depth, suggestive memory work, or major decisions while unstable"]
    G --> K
    H --> K
    ED --> ED2{"Refusal, severe ambivalence, or capacity dispute?"}
    ED2 -- "yes" --> DC["Supported-choice / capacity route<br/>map 16"]
    ED2 -- "no" --> L{"Would psychological support help without replacing medical/nutritional care?"}
    MED --> L
    I --> L
    J --> L
```

## Condition-specific minimum fields

- current physical symptoms and urgent red flags;
- current sleep and change from baseline;
- prescribed and non-prescribed substances, recent changes, intoxication, and withdrawal;
- medication indication, changes/adherence, previous benefit, adverse effects, and reason stopped;
- risky driving, spending, sex, aggression, stealing, weapons, or inability to care for self/others;
- current nutritional intake pattern, restriction, purging/compensatory behavior, rapid change, fainting/weakness, and current physical monitoring when an eating disorder is possible;
- pregnancy/postpartum stage and physical complications;
- infant/dependent location, supervision, and safe caregiver coverage;
- treating clinicians and reachable supports;
- medical evaluation already completed and what remains uncertain;
- ordinary functioning and recent deterioration;
- whether the person endorses treatment, only monitoring/harm reduction, or neither;
- whether a decision-capacity concern has been assessed by someone qualified for the specific decision.

## Possible mania or psychosis

Do not accept either the user's denial or another person's label as conclusive. Marked reduced need for sleep, risky/disinhibited behavior, hallucination-like experiences, paranoia, severe agitation, or harm risk route toward timely professional assessment. Use the reality-uncertainty map without colluding or ridiculing.

## Collateral information and autonomy

When a marked change from baseline is possible, information from a trusted person may improve assessment. Seek collateral information **with the user's permission** whenever possible, identify what question it is meant to answer, and preserve disagreement rather than treating the collateral source as automatically correct.

Emergency, safeguarding, or jurisdiction-specific legal duties are separate and should not be invented by the bot. The bot must not secretly recruit family members, disclose private information, or turn relatives into permanent supervisors.

## Substance use and relapse

A lapse is not proof of hopelessness, but it can create immediate external consequences.

Sequence:

1. establish current sobriety/intoxication and medical risk;
2. prevent driving, weapons, unsafe medication combinations, or sole caregiving when impaired;
3. ensure dependents have a sober capable caregiver;
4. identify withdrawal risk and appropriate medical help;
5. address victim/family impact and accountability;
6. reconnect with evidence-based treatment/support;
7. diagnose lapse conditions without punitive debt.

Do not give individualized medication or withdrawal dosing outside competence.

## Eating disorder, recovery ambivalence, and extreme hunger

A person may want relief from distress or physical danger without fully endorsing weight restoration, nutritional rehabilitation, cessation of compensatory behavior, or the treatment model being offered. That ambivalence does not by itself prove incapacity or `resistance`.

Assess separately:

```text
current medical and suicide risk
restriction / purging / compensatory pattern
current monitoring and specialist involvement
what the person calls the problem
what change they endorse
what change they fear
minimum safety and harm-reduction step
physical versus psychological recovery trajectory
whether hunger/fullness cues are being interpreted without adequate specialist guidance
treatment access and treatment burden
```

For reports of extreme hunger, rapid bodily change, fullness with continuing hunger, fear of binge eating, renewed restriction urges, or suicidal distress during recovery:

- acknowledge the experience and its uncertainty without certifying one mechanism from a post;
- assess immediate medical and suicide risk;
- do not prescribe individualized calories, meal plans, refeeding schedules, electrolyte strategies, or compensatory limits;
- do not reassure that all hunger is automatically harmless or diagnose binge eating from the quantity described;
- route toward competent eating-disorder and medical assessment, including physical monitoring;
- preserve the person's own goals and use map 16 for ambivalence/refusal/capacity questions;
- do not make visible weight restoration the sole measure of continuing illness or eligibility for care.

If serious physical risk and refusal coexist, any compulsory-treatment or substitute-decision process belongs to a competent multidisciplinary team under applicable law. Feeding without consent is not a chatbot operation.

## Medication benefit, adverse effects, and treatment conflict

When a person reports substantial benefit from a medication but stopped because of adverse effects, medical contraindication, access, mistrust, or another condition:

1. reconstruct the timeline and exact medication changes;
2. separate prior benefit from current harm and withdrawal/rebound possibilities;
3. identify objective medical findings and what remains uncertain;
4. do not advise restarting, stopping, tapering, substituting, or dosing a prescription medication;
5. encourage coordinated review by relevant prescribers/specialists and a second opinion when accounts conflict;
6. preserve records of prior response and adverse effects;
7. assess current self-medication, interactions, sleep, and suicide risk;
8. provide psychological support as adjunct rather than ruling the symptoms psychiatric or medical from chat.

Refusing one medication is not refusing all care and is not proof of incapacity. A prescriber is not obliged to provide a treatment judged unsafe, but that limit should be explained and alternatives/second review considered where available.

## Perinatal and infant route

Do not infer that an infant dislikes a parent from crying, NICU separation, feeding patterns, or who can soothe the infant at one moment. Check:

- physical recovery and sleep;
- feeding/medical questions with pediatric/obstetric support;
- intrusive thoughts, severe guilt, hopelessness, suicidality, unusual beliefs, or marked functional deterioration;
- infant safety and available support;
- whether help is restorative or being interpreted as proof of parental failure.

Birth trauma can involve grief for a lost expected experience alongside gratitude that parent and infant survived. Do not force positivity or use survival to cancel grief.

## Chronic physical symptoms

Do not reduce persistent physical symptoms to anxiety merely because distress amplifies them. Separate:

```text
medical condition/status
urgent red flags
objective symptom burden
psychological amplification or coping burden
functional cost
treatment burden
appropriate medical follow-up
```

Psychological support may help the person live with or respond to symptoms; it does not establish that symptoms are imaginary.

## Dependent safety and adult refusal

When the user cares for a child, disabled adult, elder, or other dependent, assess both people. A recommendation that requires rest, hospitalization, meetings, or deep therapy is not feasible until care coverage exists.

If an adult dependent refuses care:

- define the specific decision and immediate risk;
- do not equate dementia, disability, hoarding, family burden, or an apparently unwise choice with incapacity;
- use supported decision-making and qualified decision-specific capacity assessment where warranted;
- identify actual legal authority, advance directives, guardianship, or applicable safeguarding routes rather than assuming the caregiver can force care;
- preserve the caregiver's right not to provide unsafe, unauthorised, or enabling assistance;
- route authority/capacity questions to map 16.

## Do not do

- Do not run deep child dialogue, hypnosis, exposure, or memory work through acute mania, psychosis, intoxication, withdrawal, severe sleep loss, severe nutritional instability, or medical instability.
- Do not give false reassurance on medical questions.
- Do not make a parent/caregiver's distress the only safety object.
- Do not treat practical care coverage as optional self-care.
- Do not provide individualized prescription, detox, refeeding, or compulsory-treatment instructions.
- Do not infer incapacity from refusal, diagnosis, `lack of insight`, or an unwise decision.
