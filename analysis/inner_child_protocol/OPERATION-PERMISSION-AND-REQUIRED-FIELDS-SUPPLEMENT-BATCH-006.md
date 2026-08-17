# Operation-permission and required-fields supplement — Batch 006

Date: 2026-08-17  
Status: conceptual runtime contract for reconciliation with the existing O0–O10 architecture

## Entry fields

- `request_actor`: self / supporter / caregiver / minor-or-dependent / mixed / unknown
- `beneficiary_present`: yes / no / unknown
- `original_concern_pending`
- `primary_problem_class`
- `inner_child_role`: primary / adjunctive / deferred / irrelevant-to-next-action / unknown

## Current-reality fields

- immediate danger and basic-needs status;
- communication surveillance;
- current relational conduct and disputed facts;
- medical/physical burden, sleep, medication, intoxication/withdrawal, and change from baseline;
- dependent safety and sober/capable care coverage;
- structural load and resources;
- decision impact, reversibility, third-party rights, bodily autonomy, and actual obligations;
- problem-portfolio dependencies and selected bottleneck.

## Consent / helper fields

- `scope_of_no`: content / modality / intensity / timing / helper / all engagement / unknown;
- frame accepted / uncertain / rejected;
- frame impact and revised/withdrawn status;
- optional exploration versus minimum safety/fit disclosure versus treatment-goal authority versus provider conditions;
- support recipient qualification, capability, limits, backup, and concentration risk.

## Epistemic record

Each salient experiential claim keeps four independent dimensions:

```text
source_class
factual_confidence
personal_meaning
action_authority
```

Confidence or meaning cannot rewrite source class. High personal meaning does not automatically authorize irreversible action.

## Outcome / longitudinal fields

- benefit, harm/deterioration, functioning, treatment burden, external burden/cost;
- repeated reassurance relief duration, repetition, escalation, and burden;
- handoff relevant / private-reachable / attempted / response / bridge-complete;
- safe-enough-to-resume and original-concern restoration;
- changed failure hypothesis before identical retry.

## Unknown semantics

`unknown` constrains only operations that require the missing fact. It does not globally disable low-demand support. The runtime may collect the field, choose an operation that does not consume it, or defer/escalate. It may not infer it from tone.
