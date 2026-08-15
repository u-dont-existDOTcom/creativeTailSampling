# Orthogonal Tail Batch 23 — Performative Rescue Forecasts and Strategic Resource Reporting

Date: 2026-08-15

## Outcome

One narrow provisional cross-domain survivor:

- **C017 — Intervention-aware evaluation of rescue-triggering community forecasts**

C016 verifiably unpredictable audit sampling also survives the scheduled target-domain attack.

Most other candidates collapsed into established performative-prediction, anticipatory-action, insurance, bailout/soft-budget, voluntary-disclosure, triage, causal-inference, or mechanism-design ideas.

---

# A. C016 target-domain attack

Searches covered cooperative federation audits, credit-union audit sampling, participatory guarantee systems, NGO/public-sector sampling, and quality-assurance systems.

## Result

Close target practices exist for:

- random account/item sampling in credit unions;
- statistical/random operational audits;
- participatory guarantee systems with random farm/site inspection;
- risk-based and random audit mixes.

No close cooperative/intentional-community target implementation was found that combines all three C016 properties:

1. eligible universe frozen/committed **before** the future random seed is knowable;
2. sample derived from unpredictable randomness not controlled by federation leadership/auditee;
3. deterministic selection replayable/verifiable afterward.

NIST explicitly documents public-randomness-beacon use for auditable random sampling. This remains a strong source-domain precedent rather than target-domain collision.

**Disposition: C016 survives provisionally.**

---

# B. C017 — Intervention-aware evaluation of rescue-triggering community forecasts

## Plain proposition

If a community's forecast/report of its own future failure helps determine whether a federation intervenes, the intervention can change the very outcome later used to judge whether the forecast was accurate.

Therefore:

> **Do not score a pre-rescue risk forecast against the observed post-rescue outcome as though no intervention occurred.**

A successful rescue can make a truthful warning look retrospectively false.

## Minimal example

1. Community A reports an 80% chance of insolvency within six months without help.
2. The federation uses this warning to release emergency liquidity, send experienced members, renegotiate debt, or otherwise intervene.
3. Community A survives.
4. A naïve review records `predicted failure; no failure occurred` and concludes A exaggerated risk.
5. Future communities learn that a successful preventive intervention damages the forecaster's credibility.
6. Honest early warnings are chilled, or communities delay until distress becomes impossible to prevent.

The central evaluation error is **conditioning the forecast score on an outcome produced under a different intervention regime from the one the forecast described**.

## Source-domain collision boundary

The causal logic itself is strongly established and therefore not claimed as new.

### Performative prediction

Perdomo et al. (ICML 2020) formalized the setting in which predictions support decisions and thereby change the distribution/outcome being predicted.

Later work makes the evaluation/incentive issue even sharper:

- conditional-forecast/proper-scoring work shows classical proper scoring rules can fail in performative settings;
- causal/performativity work studies how to identify effects when deployed predictions steer outcomes;
- medical `prediction under intervention` methods explicitly evaluate counterfactual prediction performance because ordinary observed-outcome scoring is invalid when treatment changes outcomes;
- clinical early-warning literature recognizes a `treatment paradox`: correctly identified high-risk patients receive treatment that prevents the event and can make the prediction appear wrong.

So C017 is **not** a new prediction theory.

## Target-domain screen

Humanitarian anticipatory-action systems already:

- use forecasts/triggers to release aid before disasters;
- separately evaluate trigger performance and intervention impacts;
- use randomized/quasi-experimental designs where feasible to estimate what anticipatory assistance changed;
- explicitly distinguish trigger model design from downstream action effectiveness.

This is an important near precedent.

However, the screened material did not reveal a close intentional-community/cooperative mutual-aid architecture where **communities themselves submit risk forecasts that may trigger federation rescue and later have those forecasts evaluated with intervention-aware/counterfactual scoring**.

Therefore only the target transfer survives.

## Narrow target use case

C017 matters if a community federation or internal research center asks communities to periodically report something like:

- probability of insolvency/default;
- probability of membership collapse or inability to meet labor/care obligations;
- probability of food/water/housing shortfall;
- probability that a governance/safety system will fail without outside help;
- expected need for founder replacement, temporary staffing, emergency liquidity, mediation, or other movement support.

If those forecasts can cause preventive action, observed outcomes become intervention-contaminated labels.

## Operational architecture

### 1. Forecast the correct estimand

Record explicitly whether the report means:

- risk **without additional federation intervention**;
- risk under current support only;
- risk under a specified intervention package;
- probability that a defined trigger/threshold will be crossed.

Do not let `80% risk` float without an intervention regime.

### 2. Freeze the forecast before the rescue decision

Timestamp the forecast, evidence state, uncertainty interval, and assumed support level before the new intervention is chosen.

This prevents later narrative rewriting in either direction.

### 3. Separate two evaluations

**Forecast evaluation:** Was the pre-intervention risk estimate reasonable for the counterfactual regime it described?

**Intervention evaluation:** Did the federation action reduce the feared outcome, at what cost and with what adverse effects?

Do not collapse these into `did the predicted bad thing happen?`

### 4. Prefer intervention-invariant or counterfactual evidence when possible

Possible approaches, depending on scale/data/ethics:

- exogenous hazard/input indicators not themselves changed by the rescue;
- matched or untreated comparable communities/cases;
- historical natural experiments;
- causal models adjusted for intervention assignment;
- prediction-under-intervention methods;
- staggered/randomized intervention only where ethical and practically appropriate;
- independent expert/model forecasts made from the same pre-rescue information.

No one method is universally valid.

### 5. Do not punish a prevented event as a false alarm

The retrospective category should distinguish at least:

- forecast appears poor even after accounting for intervention;
- event did not occur and intervention plausibly prevented it;
- event did not occur but intervention probably made little difference;
- counterfactual remains unresolved.

### 6. Preserve honest uncertainty

A community should not need to claim near-certainty to qualify for help. Record probabilities/ranges and calibration over many forecasts rather than judging one difficult case as `right` or `wrong` whenever possible.

## Distinctive predictions

If a federation naïvely scores intervention-triggering self-forecasts against post-intervention outcomes, it should create one or more pathologies:

- underreporting/late reporting to avoid later accusations of exaggeration;
- strategic overstatement if aid rewards distress and forecast credibility is not penalized;
- distorted calibration statistics because high-risk cases receive more effective intervention;
- retrospective belief that fragile systems were safe because the safety net worked;
- confusion between good forecasting and good rescue policy.

An intervention-aware evaluation architecture should reduce the first and fourth distortions without requiring the federation to accept every self-report at face value.

## Relation to C005 / community reproducibility

C017 yields an important research warning:

> A well-supported community lineage can look intrinsically robust when federation interventions systematically prevent high-risk communities from failing.

This is a direct treatment/soft-budget confounding problem, **not** a separate Creative Tail discovery.

When comparing community designs, record rescue/subsidy exposure so survival/reproduction is not mistaken for unaided robustness.

## Falsifiers / demotion conditions

Demote C017 if:

- mutual-aid/cooperative federations already use substantially this intervention-aware counterfactual scoring of member communities' own risk forecasts;
- community self-forecasting proves too noisy/strategic to improve allocation compared with external indicators;
- the federation cannot obtain enough cases to evaluate calibration or counterfactual performance meaningfully;
- intervention assignment is so endogenous and heterogeneous that the evaluation architecture produces more false precision than useful learning.

## Critical limits

- counterfactuals are not observed facts;
- rescue may be targeted precisely to the highest-risk cases, producing strong confounding;
- communities can strategically report risk to obtain resources;
- forecast accuracy is not the same thing as deserving aid;
- using “counterfactual risk” can create opaque expert/model authority;
- a community that made itself unnecessarily fragile should not be rewarded merely because its forecast was accurate;
- the architecture must separately evaluate preventability, responsibility, need, rights, and system design rather than turning forecast calibration into a moral score.

## Disposition

**SURVIVES as C017 — provisional cross-domain operational transfer.**

Claim only the communal mutual-aid application. Performative prediction, treatment paradoxes, counterfactual forecast evaluation, and anticipatory-action impact evaluation are established source/adjacent-domain ideas.

---

# C. Remaining Batch 23 candidates

At least sixteen plain candidates were generated before selection.

## T123-02 — Rescue makes fragile designs look intrinsically robust

Plain claim: repeated federation rescue can keep fragile communities alive, causing retrospective survival comparisons to misclassify supported fragility as robust design.

Nearest neighbors: treatment paradox/confounding, bailout/soft-budget constraints, zombie firms, selection under subsidy.

Verdict: **REJECT AS NOVEL; KEEP PRACTICAL/RESEARCH-CONTROL.**

Operational lesson: record subsidy/rescue exposure and distinguish supported survival from autonomous robustness.

---

## T123-03 — Soft-budget community reproduction

Plain claim: if communities expect federation rescue, local decisions may rationally take more risk or delay adaptation.

Nearest neighbors: soft budget constraint and moral hazard.

Verdict: **REJECT.**

---

## T123-04 — Aid triggers based on hard-to-manipulate exogenous indicators

Plain claim: use rainfall, market prices, external debt events, or other exogenous indices where suitable rather than only self-reported distress.

Nearest neighbors: parametric/index insurance and forecast-based financing.

Verdict: **REJECT AS NOVEL; PRACTICAL.**

Caveat: index basis risk can deny help to genuinely needy communities whose local conditions diverge from the trigger.

---

## T123-05 — Separate forecast quality from intervention efficacy

Plain claim: do not call a forecast good/bad based solely on final outcome when intervention followed it; score forecast and rescue separately.

Verdict: **MERGE INTO C017.**

---

## T123-06 — Score the no-rescue estimand, not the observed post-rescue outcome

Verdict: **MERGE INTO C017.**

---

## T123-07 — Prevention-credit ledger

Plain claim: record credible avoided losses separately from observed losses so prevention is not treated as “nothing happened.”

Nearest neighbors: program impact evaluation, avoided-loss analysis, counterfactual prevention evaluation.

Verdict: **REJECT AS NOVEL; practical companion to C017.**

---

## T123-08 — Voluntary self-disclosure safe harbor

Plain claim: communities that promptly disclose their own control failure should receive some procedural/penalty protection to preserve incentives for honest reporting.

Nearest neighbors: regulatory leniency, voluntary-disclosure/self-reporting policies, safety reporting systems.

Verdict: **REJECT AS NOVEL; potentially useful with limits.**

Do not immunize intentional harm or let self-reporting erase restitution/rights.

---

## T123-09 — Rescue allocation by marginal benefit, not visible severity alone

Plain claim: scarce aid should consider how much intervention changes outcomes rather than only who currently looks worst.

Nearest neighbors: triage, cost-effectiveness, treatment-effect targeting.

Verdict: **REJECT.**

---

## T123-10 — Randomized/staggered borderline rescue for learning

Plain claim: when several ethically equivalent borderline interventions exist, limited randomization/staggering can improve causal learning.

Nearest neighbors: randomized trials, stepped-wedge designs, bandits.

Verdict: **REJECT AS NOVEL; high ethical threshold.**

---

## T123-11 — Experience-rated rescue contributions

Plain claim: communities generating repeated avoidable claims should pay more into a mutual-aid pool.

Nearest neighbors: insurance experience rating and moral-hazard pricing.

Verdict: **REJECT.** Can punish unlucky or structurally disadvantaged communities and create hiding incentives.

---

## T123-12 — Correlated-risk reserve sizing

Plain claim: federation reserves cannot be sized as if member-community shocks are independent because drought, recession, legal attacks, epidemics or supply failures can hit many simultaneously.

Nearest neighbors: catastrophe insurance, systemic-risk/common-shock modeling.

Verdict: **REJECT AS NOVEL; strongly practical.**

---

## T123-13 — First-come rescue funding creates a reporting race

Plain claim: a fixed mutual-aid pot distributed first-come can reward fast/strategic reporting rather than severity or marginal benefit.

Nearest neighbors: common-pool depletion, queueing/allocation mechanisms.

Verdict: **REJECT AS NOVEL.**

---

## T123-14 — Distress legibility investment

Plain claim: if aid depends on easily documented metrics, communities may invest in making distress legible to the federation rather than in preventing it.

Nearest neighbors: Goodhart/Campbell effects, bureaucratic legibility, grant/aid incentive design.

Verdict: **REJECT.**

---

## T123-15 — Independent forecast reference panel

Plain claim: pair community self-forecast with an external forecast from the same frozen information set to detect systematic optimism/pessimism.

Nearest neighbors: forecast ensembles, second opinions, independent risk assessment.

Verdict: **REJECT AS NOVEL; possible C017 implementation.**

---

## T123-16 — Rescue-budget allocation based on counterfactual avoided harm

Plain claim: rank interventions by expected avoided harm rather than predicted raw harm.

Nearest neighbors: treatment-effect targeting, expected value of intervention, cost-effectiveness.

Verdict: **REJECT.**

---

## T123-17 — Calibrate self-forecasts over repeated windows rather than one-shot blame

Plain claim: assess probabilistic risk reports across many cases/periods instead of calling each one true/false.

Nearest neighbors: probabilistic forecast calibration/proper scoring.

Verdict: **REJECT AS NOVEL; MERGE practical implementation into C017.**

---

# Batch 23 disposition

## Survivor

- **C017 — Intervention-aware evaluation of rescue-triggering community forecasts**

## Retained survivor

- **C016** survives cooperative/credit-union/participatory-audit target attack; ordinary random sampling is not the same as commit-before-randomness + replayable selection.

## Practical-but-known lessons to mirror into `communities`

1. never call a prevented outcome a false alarm without accounting for the intervention;
2. record intervention regime explicitly in risk forecasts;
3. freeze pre-rescue forecast/evidence before aid decisions;
4. separate forecast quality from intervention efficacy;
5. record rescue/subsidy exposure when comparing community survival/reproduction;
6. use exogenous/parametric triggers only where basis risk is acceptable;
7. consider carefully designed self-disclosure protections to preserve honest incident reporting;
8. size mutual-aid reserves for correlated/systemic shocks, not independent member risk;
9. avoid first-come depletion rules when a fixed rescue pool can face simultaneous needs.

## Method lesson

A target transfer can survive even when the causal mechanism is old if the operational error is specific and consequential. C017 is not “predictions influence outcomes”; it is the narrower communal mutual-aid rule:

> **Do not use the intervention-produced outcome as an unadjusted label for the forecast that triggered the intervention.**
