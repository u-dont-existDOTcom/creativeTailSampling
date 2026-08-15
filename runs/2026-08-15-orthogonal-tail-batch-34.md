# Orthogonal Tail Batch 34 — Scrutiny-Conditioned Evidence and Self-Confirming Suspicion

Date: 2026-08-15

## Outcome

One narrow provisional cross-domain survivor:

- **C021 — Scrutiny-conditioned evidence accounting**

The source mechanisms are established: predictive-policing feedback loops, selective labels, scrutiny/label bias, observational bias, and intervention-surveillance bias. The surviving target transfer is an intentional-community evidence rule:

> **When suspicion changes how intensely a person is observed, evidence generated after that change must carry the observation/monitoring regime with it; raw discovered-incident counts cannot be treated as independent confirmation of the suspicion that caused the extra scrutiny.**

This does not prohibit targeted monitoring after a credible safety concern. It changes how monitoring-generated evidence is interpreted.

---

# A. Mechanism

## Feedback loop

1. Person A attracts an initial allegation/suspicion.
2. A is watched, questioned, documented, restricted, or reviewed more intensely than other members.
3. Greater observation produces more **discoverable** incidents, especially low-level/ambiguous conduct that would often go unrecorded for others.
4. The larger incident count is treated as corroboration that A is unusually dangerous/problematic.
5. Monitoring intensifies further.
6. Members receiving less scrutiny appear comparatively safer partly because their comparable conduct is less observable.

The evidence stream is therefore endogenous to the monitoring decision.

## Important asymmetries

The bias can run in more than one direction:

- more observation can increase detected incidents;
- restrictions/monitoring can suppress opportunities for harmful conduct, making the monitored person look safer than they would be without restrictions;
- observation itself can provoke/reactively change behavior;
- some independent reports arise regardless of targeted monitoring and should be distinguished from monitoring-discovered events.

Therefore the correction is not simply `divide incidents by hours watched`. The system needs provenance/context.

---

# B. Source-domain collision boundary

## Predictive policing

Ensign et al. formally model runaway feedback where discovered crime drives deployment, deployment produces more discovered crime, and the process repeatedly returns attention to the same locations independent of true underlying crime rate.

## Selective labels

Lakkaraju et al. show that observed outcome labels can be a non-random result of earlier human decisions. Standard evaluation on the observed subset can be biased because unchosen/unobserved cases lack labels.

Clinical deployment research similarly shows that deployed decision rules can change which labels are observed and thereby distort later performance monitoring.

## Scrutiny/surveillance bias

Financial-misconduct work explicitly models scrutiny bias under uneven regulatory attention. Child-welfare research has examined **intervention surveillance bias**, where intervention/service exposure changes the likelihood of later maltreatment reports. Observer-label studies likewise show that labels can influence some observational judgments.

These source mechanisms are established and not claimed as new.

## Target-domain search

Intentional-community sources discuss:

- screening;
- community monitoring/sanctions;
- surveillance/disciplinary power;
- concerns about safety and harmful members;
- observation during provisional membership;

but the targeted search did not locate a close intentional-community protocol that systematically distinguishes **reported vs scrutiny-discovered conduct**, records monitoring exposure/regime, and prevents suspicion-triggered observation from becoming self-validating evidence.

**C021 survives only as this target-domain operational transfer.**

---

# C. Operational architecture

## 1. Record evidence provenance

For consequential conduct evidence, distinguish at least:

- independently reported incident;
- routine observation available for comparable members/roles;
- event discovered during suspicion-triggered monitoring;
- event discovered because of a restriction/check/search that others do not face;
- retrospective interpretation of already-existing records;
- self-report/admission;
- external source.

Do not collapse these into one undifferentiated incident count.

## 2. Record the observation regime

Where targeted scrutiny is material and lawful/ethical, record:

- why it began;
- start/end/review time;
- what changed relative to ordinary observation;
- who receives/controls the records;
- whether restrictions changed opportunities for the conduct;
- whether monitoring itself plausibly altered behavior.

## 3. Separate trigger evidence from monitoring-generated evidence

The original trigger should remain identifiable.

When later evidence arises because the trigger caused special scrutiny, do not present it as though it were a statistically independent sample from the same observation process that applied before suspicion.

This does **not** mean later evidence is false or irrelevant.

## 4. Compare like with like when using rates

If ordinary comparable conduct is counted for everyone, compare rates under similar observation opportunities/exposure where feasible.

Do not infer that Person A is uniquely problematic merely because A has six documented minor events and others have zero when only A was intensively observed.

## 5. Preserve severity

A severe independently meaningful event does not become unimportant because observation intensity was high.

Exposure correction is mainly about inference from **frequency/pattern/count** and low-level discovered behavior, not erasing direct evidence of serious harm.

## 6. Independent review of escalation

When monitoring-generated evidence is being used to justify still more monitoring/restriction, require a review point that asks:

- would this evidence have been observable under ordinary conditions?;
- how much is independent of the original allegation?;
- did restrictions suppress or provoke relevant opportunities?;
- are comparable members observed similarly?;
- has the case crossed from safety monitoring into generalized surveillance?

## 7. Avoid random suspicion as the correction

C016's random-audit logic can be useful for **process auditing** across communities or records. It should not become random personal surveillance merely to create a control group.

Safer comparators can include:

- existing routine records under standard observation;
- standardized role-specific checks applied to everyone with that authority;
- independent reports;
- historical base rates with explicit limitations;
- bounded procedural audits rather than personal monitoring.

## 8. Keep rights independent of inferred risk

Even a correctly inferred elevated risk does not eliminate notice, reply, recusal, proportionality, direct bypass rights, review, privacy limits, or child/survivor rights.

C021 is an evidence-quality control, not a complete safety process.

---

# D. Distinctive predictions

If scrutiny feedback matters inside communities:

- members who receive more suspicion-triggered observation will show higher counts of low-level documented conduct even after controlling imperfectly for underlying behavior;
- raw documentation counts will partly measure observation intensity;
- some cases will show apparent escalating evidence with weak growth in independent reports;
- after monitoring begins, the mix of evidence will shift from independent reports toward monitoring-discovered events;
- reviewers who can see observation-regime metadata should reach different confidence judgments from reviewers shown only raw incident totals;
- policies that standardize role-based monitoring for sensitive powers should reduce some person-specific scrutiny bias without requiring universal surveillance.

---

# E. Falsifiers / demotion conditions

Demote C021 if:

- close intentional-community/cohousing/communal safeguarding practice already systematically tracks monitoring exposure and conditions conduct inference on it;
- real community cases show monitoring intensity contributes negligibly to documented evidence differences;
- the added provenance burden is too high to change decisions in practice;
- routine independent reporting dominates the relevant safety evidence so strongly that scrutiny-generated detection rarely matters.

---

# F. Candidate audit

At least sixteen candidates were screened.

## T134-01 — Suspicion causes more observation, producing more incidents
**Verdict:** SOURCE MECHANISM KNOWN; target transfer forms C021.

## T134-02 — Raw incident counts require observation-exposure denominator
**Verdict:** MERGE INTO C021; simple rates may still be insufficient because monitoring changes behavior/opportunity.

## T134-03 — Separate reported from discovered incidents
**Verdict:** MERGE INTO C021. Predictive-policing source literature explicitly distinguishes these streams.

## T134-04 — Trigger evidence vs derivative evidence
**Verdict:** MERGE. Related to Batch 26 dependency provenance but here the dependency is the observation process itself.

## T134-05 — Randomly monitor everyone for unbiased comparison
**Verdict:** REJECT as a general communal recommendation; privacy/safety cost unacceptable and unnecessary.

## T134-06 — Standardize sensitive-role checks
Apply the same financial/childcare/records/security controls to everyone holding the same sensitive role rather than targeting checks solely by reputation.

**Verdict:** PRACTICAL / KNOWN; role-based control/least privilege.

## T134-07 — Severe-event exemption from exposure normalization
**Verdict:** PRACTICAL constraint; MERGE into C021.

## T134-08 — Monitoring can suppress the outcome
**Verdict:** KNOWN intervention/observation effect; important C021 caveat.

## T134-09 — Monitoring can provoke/reactively change behavior
**Verdict:** KNOWN observer/reactivity effect; important caveat.

## T134-10 — Documentation intensity as a confounder
**Verdict:** KNOWN measurement/surveillance bias; target application useful.

## T134-11 — Independent escalation review
**Verdict:** PRACTICAL; existing due-process principle, C021-specific question set is useful.

## T134-12 — Suspicion score trained on prior suspected cases
**Verdict:** REJECT as too algorithm-specific and close to predictive-policing bias.

## T134-13 — Lack of incidents among unmonitored members is unlabeled, not zero risk
**Verdict:** MERGE into C021; selective-label principle.

## T134-14 — Role-based monitoring creates comparable observation processes
**Verdict:** PRACTICAL / KNOWN; safer than person-random surveillance.

## T134-15 — Monitoring-regime versioning
**Verdict:** PRACTICAL provenance; merge.

## T134-16 — Scrutiny-aware retrospective audits
Re-evaluate old high-incident cases after reconstructing how observation intensity changed.

**Verdict:** PRACTICAL; potentially useful but source mechanism known.

---

# G. Practical lessons to mirror into communities

1. raw documented conduct counts partly reflect how intensively someone was observed;
2. distinguish independently reported incidents from scrutiny-discovered incidents;
3. record when/why observation intensity changed in consequential cases;
4. do not treat evidence produced by suspicion-triggered monitoring as independent corroboration of the trigger without qualification;
5. lack of observed incidents among less-monitored people is not equivalent to evidence of zero risk;
6. use comparable role-based checks for sensitive powers where possible instead of reputation-driven surveillance;
7. preserve severe event evidence without mechanically normalizing it away;
8. at escalation review, explicitly ask how much evidence would have existed under ordinary observation;
9. account for restrictions that suppress opportunities and observation that changes behavior;
10. do not solve surveillance bias by randomly surveilling ordinary members;
11. keep direct rights/due process separate from the evidence-quality calculation;
12. for research, treat monitoring intensity/observation regime as a confounder/exposure variable.

## Method lesson

A community's evidence system can change the data-generating process it later treats as evidence. The crucial cross-domain transfer is not `bias exists`; it is to preserve the **observation regime as part of the evidence provenance** so suspicion cannot silently become its own measuring instrument.
