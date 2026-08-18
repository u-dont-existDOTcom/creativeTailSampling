# Operation-permission and required-fields supplement — Batch 008

Date: 2026-08-17

These are conceptual requirements for the existing operation-permission architecture. InnerSignalGraph should reconcile them with O0–O10 rather than create a parallel engine.

## New recognition fields

### Decision, authority, and capacity

```text
decision_subject
decision_owner
decision_deadline
decision_impact
current_capacity_status: presumed | qualified_present | qualified_absent | fluctuating | disputed | unknown
capacity_concern_basis
support_steps_attempted
communication_or_access_need
undue_influence_or_coercion
advance_directive_or_known_wishes
lawful_decision_maker_status: self | authorised_surrogate | disputed | unknown | not_applicable
least_restrictive_option
review_time_or_trigger
```

Rules:

- default `current_capacity_status` is `presumed`, not `unknown/incapable`;
- only qualified external assessment may set `qualified_present` or `qualified_absent` where capacity is material;
- `diagnosis`, `unwise_choice`, `lack_of_insight`, `family_disagreement`, and `caregiver_burden` are not capacity values;
- capacity is attached to `decision_subject` and current time, not to the person globally;
- `lawful_decision_maker_status` must be explicit before any surrogate-action route;
- if authority is `unknown`, the bot may support, clarify, and reduce reversible risk but may not direct forced treatment or substitute consent.

### Goal endorsement and ambivalence

```text
change_target_endorsement: endorsed | mixed | not_endorsed | unknown
person_owned_goal
minimum_safety_goal
harm_reduction_goal
full_change_goal
provider_or_setting_condition
third_party_or_dependent_safety_goal
feared_loss_from_change
smallest_endorsed_step
review_time_or_trigger
```

Rules:

- do not infer `endorsed` merely because the person asks for help;
- do not infer `not_endorsed` from fear, inconsistency, or one refusal;
- minimum safety and third-party safety may constrain available operations without silently replacing the person's longer-term goal;
- repeated motivational dialogue after a clear informed refusal can become coercive and should not be the default fallback;
- harm reduction remains available when full change is not endorsed unless condition-specific risk/provider limits make the requested operation unavailable.

### Confession and disclosure

```text
actual_event_status: confirmed | uncertain | intrusive_feared | disputed | unknown
current_other_person_risk
material_consent_or_right_to_know
concrete_repair_possible
already_disclosed_in_substance
confession_relief_duration
confession_repetition_or_escalation
qualified_disclosure_review_needed
```

Rules:

- `material_consent_or_right_to_know = present` routes to qualified ethical/clinical/legal review where needed;
- `actual_event_status = uncertain` and repetitive relief-seeking prohibit historical certification and immediate confession prescription;
- do not ask for unnecessary graphic or intimate detail to classify the route;
- direct contact with a harmed person remains unavailable when it would be unsafe, unwanted, unlawful, evidence-damaging, or primarily for guilt relief.

### Supporter safety and limits

```text
supporter_physical_safety
supporter_pregnancy_or_medical_vulnerability
supporter_sleep_and_function
supporter_financial_or_housing_dependence
dependent_present
supporter_can_leave_or_disengage
sole_monitor_expectation
emergency_threshold_defined
handoff_attempted
handoff_response
```

Rules:

- a supporter operation is unavailable if it requires the supporter to remain in danger, surrender bodily autonomy, or guarantee another adult's survival;
- `sole_monitor_expectation = yes` triggers authority-concentration repair and backup planning;
- risk escalation and supporter disengagement can both be appropriate; do not make them mutually exclusive;
- the absent person's inner states, diagnosis, and capacity remain unformulated unless qualified evidence is available.

### Eating-disorder and medication conflict

```text
nutritional_or_refeeding_risk
current_medical_monitoring
current_suicide_risk
restriction_or_compensatory_pattern
recovery_target_endorsement
medication_indication
medication_prior_benefit
medication_adverse_effect
medication_or_substance_timeline
prescriber_reachable
interaction_or_withdrawal_risk
```

Rules:

- severe nutritional/medical risk makes ordinary inward depth operations unavailable;
- the bot must not create individualized calorie, meal, refeeding, electrolyte, prescription, taper, combination, or recreational-substance instructions;
- prior benefit and adverse effect must be stored separately;
- same-day medical/prescriber/pharmacist escalation depends on current risk, not on whether the user agrees with a diagnosis.

## Operation consequences

### Low-demand support remains possible

When capacity, authority, or full-goal endorsement is unresolved, the bot may still:

- listen and summarize using the person's language;
- clarify the exact decision and present concern;
- provide bounded factual information with uncertainty;
- support communication access;
- identify immediate reversible safety actions;
- help prepare questions for qualified clinicians/legal support;
- identify the smallest endorsed harm-reduction step;
- protect supporter/dependent safety;
- preserve the original concern for later return.

### Operations unavailable without additional fields

Do not permit:

- forced-treatment planning;
- surrogate consent;
- declaration of legal or clinical incapacity;
- individualized ED refeeding/meal prescription;
- prescription or withdrawal dosing;
- direct confession/contact with a harmed person;
- major irreversible decisions based on uncertain memories or unusual beliefs;
- deep child dialogue, hypnosis, or suggestive memory work during severe medical/nutritional instability, intoxication/withdrawal, acute mania/psychosis, or material capacity uncertainty.

## Runtime status

These fields are **REQUIRED CONCEPTUAL INPUTS** for the new routes. Exact schema shape, extraction burden, stale-state policy, and O0–O10 mapping remain an InnerSignalGraph implementation task.
