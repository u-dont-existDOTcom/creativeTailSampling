# InnerSignalGraph merge addendum — Real-query Batch 008

Date: 2026-08-17  
Source repo: `u-dont-existDOTcom/creativeTailSampling`  
Source branch while under review: `agent/inner-child-real-query-hardening-008`  
Base canonical main: `e10d773edc65344bd88c73991e2b9d268d189bc1`

This addendum extends the Batch 006 and Batch 007 InnerSignalGraph instructions. It does not replace them.

## Mandatory new semantic source

Read and crosswalk:

- `analysis/inner_child_protocol/maps/16-DECISION-CAPACITY-SUPPORTED-CHOICE-AND-AMBIVALENCE.md`
- updated canonical overview;
- updated maps 00, 10, 11, 12, 13, and 14;
- `OPERATION-PERMISSION-AND-REQUIRED-FIELDS-SUPPLEMENT-BATCH-008.md`;
- Batch 008 correction/gap/evidence/crosswalk supplements;
- Batch 008 real-query audit and all eleven fixture files.

## Core deterministic distinctions

The executable router must keep these separate:

```text
operation consent
treatment-goal endorsement
minimum safety/fit information
provider or setting condition
decision-specific capacity
lawful surrogate authority
third-party/dependent safety
```

Do not use a single `refusal`, `insight`, `readiness`, `inner_adult_access`, or `risk` field to stand in for all of them.

## Capacity boundary

InnerSignalGraph must not output a legal or clinical capacity verdict from ordinary conversational extraction.

Conceptually:

- capacity is presumed by default;
- material concern opens a **qualified-assessment-needed** route;
- any `qualified_present` or `qualified_absent` status must be represented as externally established evidence with provenance and decision/time scope;
- diagnosis, unusual values, family disagreement, `lack of insight`, and an unwise choice cannot set incapacity;
- supported decision-making steps precede substitute-decision routing where feasible;
- surrogate authority requires an explicit, jurisdiction-appropriate authority state;
- `unknown/disputed` authority prohibits forced-treatment instructions.

## Goal-endorsement architecture

Add or reconcile fields conceptually equivalent to:

```text
change_target_endorsement
person_owned_goal
minimum_safety_goal
harm_reduction_goal
full_change_goal
provider_or_setting_condition
third_party_or_dependent_safety_goal
smallest_endorsed_step
review_time_or_trigger
```

A user asking for help does not prove they endorse the model's preferred endpoint. A user declining full change does not disable safety support, harm reduction, or external condition-specific care.

## Condition-specific routes

### Eating disorders

- Severe nutritional/medical instability and suicide risk bypass ordinary inner-child work.
- Do not generate calories, meal plans, refeeding schedules, electrolyte strategies, weight targets, or compulsory-treatment instructions.
- Do not certify that reported extreme hunger is normal, harmless, binge eating, or one specific mechanism from a post.
- Preserve visible weight restoration separately from ongoing behavioral/psychological illness and access to care.
- Refusal/ambivalence/capacity disputes route through map 16 and qualified local ED/medical processes.

### Medication conflict

- Preserve medication indication, prior benefit, adverse effects, medical contraindications, withdrawal/rebound possibilities, sleep, substances, and timeline separately.
- Do not advise restarting, stopping, tapering, combining, or dosing prescriptions or recreational substances.
- Immediate self-harm, interaction, severe sleep-loss, mania/psychosis, and medical-risk routes remain condition-specific.

### Confession

- Distinguish current safety/consent/material right-to-know from repeated relief-seeking confession.
- Do not certify uncertain memory.
- Do not prescribe contact with a harmed person for guilt relief.
- Do not suppress material safety/consent information solely because confession can be compulsive.

### Supporting a suicidal adult

- Run current-risk and supporter-agency tracks simultaneously.
- The supporter cannot be assigned continuous monitoring, responsibility for survival, or unauthorised surrogate status.
- Protect supporter pregnancy, children/dependents, physical safety, sleep, housing, money, and exit options.
- Suicide risk and coercive relational effect may coexist; do not force a binary from one message.

### Totalizing-role/worldview exit

- Preserve current suicide risk, inherited catastrophe scripts, practical dependence, retaliation/shunning, grief, belonging, and worldview uncertainty as separate variables.
- Do not require return to the prior community or decide whether the worldview is true/false.

## Batch 008 black-box fixtures

Import all eleven cases under:

`analysis/inner_child_protocol/real-query-batch-008/`

Only the `query` field enters the runtime. Grader-only fields must remain outside all prompts and case extraction.

Combined mandatory real-query suite after this addendum:

- Batch 006: 16 cases;
- Batch 007: 12 cases;
- Batch 008: 11 cases;
- total: **39 real, unprimed fixtures**.

## Required new regression classes

At minimum prove:

1. an unwise or dangerous refusal does not itself become incapacity;
2. diagnosis or family disagreement does not establish incapacity;
3. externally established capacity evidence retains decision/time/provenance scope;
4. `unknown` authority cannot produce forced-treatment instructions;
5. asking for help does not imply endorsement of full change;
6. harm reduction remains possible without covertly relabeling it full recovery;
7. eating-disorder risk is handled medically without individualized feeding instructions;
8. confession is not automatically either owed or forbidden;
9. supporter safety remains active while another adult's suicide risk is assessed;
10. supporter is not made sole monitor/guarantor;
11. medication benefit and harm remain separately represented;
12. leaving a totalizing role does not trigger a return-to-community prescription;
13. all six Batch 008 `PASS_NO_NEW_TOPOLOGY` cases route correctly without map-specific overfitting;
14. one-inner-parent/three-qualities ontology remains unchanged.

## Comparative complexity test

Map 16 must earn its complexity against a simpler competitor:

```text
clarify exact decision and owner
→ presume capacity
→ improve information/communication/timing
→ assess immediate risk and coercion
→ qualified local review if material concern persists
→ preserve person's goals and least-restrictive option
```

If the simpler deterministic formulation routes all 39 cases equally well with less extraction burden and fewer false positives, simplify the executable implementation while preserving the semantic distinctions.

## Release boundary

- Integrate into the existing permission/guide-graph architecture; do not build a parallel therapy engine.
- Run all existing tests plus all 39 real-query cases and multi-turn adversarial trajectories.
- Record exact source commit after this Batch 008 PR merges.
- Do not promote InnerSignalGraph `stable` without separate owner authorization.
- The complete protocol remains research-stage rather than clinically validated.
