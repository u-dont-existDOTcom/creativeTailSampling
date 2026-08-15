# Branching-Process Covariate Schema for C005

Updated: 2026-08-15
Purpose: reusable coding schema for testing whether *how* a community fissions predicts daughter viability/reproduction, rather than treating parent→daughter counts as structure-free events.

## Unit of observation

One **fission/branching event** linking:
- parent community;
- daughter community;
- date/period;
- subsequent daughter outcomes.

Where one event creates more than one new unit, record each daughter and a shared `fission_event_id`.

## Identification fields

- `fission_event_id`
- `parent_id`
- `daughter_id`
- `movement_or_branch`
- `country_region`
- `fission_date`
- `source_ids`
- `source_confidence`

## Parent state before fission

- `parent_population_pre`
- `parent_households_pre`
- `parent_age_years`
- `parent_land_area`
- `parent_debt_load`
- `parent_liquidity_reserve`
- `parent_primary_economic_model`
- `parent_recent_conflict_flag`
- `parent_leadership_transition_flag`
- `parent_prior_daughters_count`

## Trigger for fission

Code one or more:
- `population_capacity`
- `labor_position_scarcity`
- `land/resource_constraint`
- `governance_manageability`
- `ideological_conflict`
- `economic_opportunity`
- `planned_reproductive_norm`
- `external_pressure`
- `other`

Add:
- `trigger_notes`
- `trigger_source_confidence`

## Member partition mechanism

- `partition_mode`
  - `lot_based`
  - `mutual_consent`
  - `volunteer_group`
  - `leadership_assignment`
  - `member_self_selection`
  - `hybrid`
  - `unknown`
- `composition_fixed_before_destination_known` — yes/no/partial/unknown
- `destination_assignment_mode`
  - `lot`
  - `negotiated`
  - `preassigned`
  - `voluntary`
  - `unknown`
- `families_kept_intact`
- `care_units_protected`
- `preference_swaps_allowed_after_partition`
- `minority_dissent_recorded`
- `partition_notes`

## Composition balance

For parent and daughter where observable:

- `daughter_population_initial`
- `daughter_households_initial`
- `daughter_share_of_parent_population`
- `leadership_experience_balance`
- `farm_business_skill_balance`
- `maintenance_trade_balance`
- `childcare_care_capacity_balance`
- `age_structure_balance`
- `health_support_balance`
- `social_family_network_balance`

Each balance variable should specify whether it is:
- directly measured;
- source-described qualitatively;
- researcher-coded;
- unknown.

## Asset / functional-capacity split

- `asset_book_value_parent_post`
- `asset_book_value_daughter_initial`
- `asset_value_adjustment_used`
- `land_quality_balance`
- `infrastructure_maturity_balance`
- `market_access_balance`
- `debt_balance`
- `productive_equipment_balance`
- `housing_capacity_balance`
- `water_food_security_balance`
- `functional_capacity_notes`

Do not treat equal book value as equal productive capacity.

## Transitional support / subsidy

- `parent_to_daughter_goods_support`
- `parent_to_daughter_cash_support`
- `parent_to_daughter_labor_support`
- `parent_to_daughter_management_mentoring`
- `shared_procurement_markets`
- `shared_religious_governance_support`
- `support_duration_months`
- `support_sunset_defined`
- `support_notes`

This interacts with C017: supported survival is not the same estimand as unaided robustness.

## Immediate outcomes

- `daughter_survives_1y`
- `daughter_survives_5y`
- `major_conflict_5y`
- `member_return_to_parent_count`
- `member_transfer_elsewhere_count`
- `financial_distress_5y`
- `leadership_failure_5y`
- `merger_or_reabsorption_5y`

Use explicit missing values rather than zero when data are unavailable.

## Reproductive outcomes

- `daughter_first_fission_date`
- `daughter_time_to_first_fission_years`
- `daughter_total_daughters_at_cutoff`
- `granddaughter_count_at_cutoff`
- `observation_cutoff_date`
- `exposure_years`

These feed C005 metrics.

## Human outcomes where ethically/empirically available

- `adult_retention`
- `leaver_wellbeing`
- `child_health_education_continuity`
- `exit_usability`
- `reported_autonomy`
- `relationship_family_disruption`

Do not pretend missing human-outcome data are zero harm.

## Candidate hypotheses

### H1 — Destination-blind composition
Holding context as well as possible, fissions in which two viable groups are fixed before mother/daughter destination is known may show less factional sorting and fewer immediate post-fission composition failures.

### H2 — Pure self-selection
Self-selected/volunteer partition may improve preference satisfaction while increasing skill/age/ideological imbalance unless strong viability constraints are imposed.

### H3 — Lot as anti-status manipulation
The lot's plausible effect is not mystical randomness; it may reduce strategic manipulation of group composition around the more desirable incumbent site.

### H4 — Transitional support
Support should improve early daughter survival but can confound inference about intrinsic replicability if not measured.

### H5 — Functional capacity beats asset equality
Productive/function-capacity balance may predict daughter success better than nominal asset-value equality.

## Analysis cautions

- Hutterite Leuts differ on many dimensions; lot-vs-consent comparisons are heavily confounded.
- branching practice may change over historical periods within the same branch;
- failed/aborted planned daughter colonies may be missing from genealogies;
- exposure time matters;
- daughter viability and member welfare are different outcomes;
- random/lot allocation does not establish consent or fairness by itself;
- family/care protection can constrain achievable balance.

## Data priority

1. Code the existing Hutterite lineage events if source-level branching details can be attached reliably.
2. Search for other communal movements with documented parent→daughter partition mechanisms.
3. Prefer within-movement/time comparisons over naive cross-movement regressions.
4. Do not infer causal benefit from current aggregate branch reproduction rates alone.
