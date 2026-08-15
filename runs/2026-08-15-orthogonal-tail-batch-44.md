# Orthogonal Tail Batch 44 — Embedded Face-Saving / Reporting-Bias Diagnostics

Date: 2026-08-15

## Trigger

Owner proposal:

> Embed diagnostic questions in the commune-member survey, including basic questions whose expected response pattern/variance can help estimate how much respondents are face-saving.

## Outcome

**No Creative Tail survivor.**

The component methods are established in survey methodology and psychometrics: social-desirability scales, overclaiming/foil items, randomized response, list experiments, direct-vs-indirect questioning, criterion validation, mode experiments, vignette framing, response-consistency diagnostics, and paradata.

However, the target application yields a strong **embedded reporting-bias calibration battery** for federation communal research.

Key correction to the initial idea:

> **Do not infer face-saving mainly from low variance on ordinary questions.** A commune may genuinely be homogeneous. Prefer diagnostics with known truth, randomized comparison conditions, or independent anchors.

---

# B44-01 — Use a multi-diagnostic reporting-pressure profile, not an individual lie score

The research center should estimate a **community/sample-level reporting-pressure profile** using several independent indicators.

Do not label individuals as dishonest from one scale or battery score.

The profile should affect:
- uncertainty;
- survey mode;
- need for indirect questioning;
- triangulation requirements;
- whether raw self-report can be compared across communities.

It should **not** mechanically subtract points from happiness/safety outcomes.

---

# Candidate diagnostics and literature disposition

## T144-01 — Improbable-virtue / social-desirability items

Use a small validated social-desirability battery containing socially approved but implausibly perfect self-descriptions.

Source precedent: Marlowe–Crowne social-desirability scale (Crowne & Marlowe, 1960) and later impression-management measures.

**Verdict: KNOWN / PRACTICAL.**

Use only as one diagnostic because high scores can reflect genuine internalized norms/cultural response style as well as strategic self-presentation.

## T144-02 — Overclaiming foils with objectively nonexistent items

Ask respondents to rate familiarity/knowledge across real and invented neutral items. Because foil truth is known (`nonexistent`), false familiarity can estimate a response-bias/self-enhancement tendency independent of actual knowledge.

Source precedent: Paulhus et al. (2003) Over-Claiming Technique; 20% of items were nonexistent and signal-detection methods separated accuracy from response bias. The method retained diagnostic value even in instructed `fake good` conditions.

**Verdict: KNOWN / PRACTICAL.**

Critical limit: overclaiming measures a general self-enhancement/claiming style, not specifically willingness to protect one's commune.

## T144-03 — Direct-versus-indirect sensitive-question split

Randomize sensitive items between:
- ordinary direct question;
- list experiment / item-count or other validated indirect method.

Group-level discrepancy estimates **disclosure sensitivity** for that topic.

Source precedent: list experiments and randomized-response methods. A 2020 double-list study in Senegal/Burkina Faso found materially different prevalence estimates for condom use and intimate-partner violence than direct/polling-style measurement, with double lists reducing standard errors relative to simple lists.

**Verdict: KNOWN / STRONGLY PRACTICAL.**

Requires adequate sample size; often federation-wide rather than one commune.

## T144-04 — Privacy-mode elasticity experiment

Randomly vary credible privacy conditions for equivalent items, e.g.:
- standard confidential survey;
- stronger independent/anonymized custody;
- interviewer vs self-administered where appropriate.

Difference in answers is a **privacy/disclosure elasticity**, not proof that either mode is perfectly true.

**Verdict: KNOWN / PRACTICAL.**

## T144-05 — Ingroup-label mirror vignettes

Randomly show otherwise identical hypothetical cases framed as occurring:
- in `your community`;
- in `another community` / unlabeled community.

Compare severity/blame/reportability/process-trigger judgments.

A systematic leniency toward the ingroup indicates identity-sensitive evaluation of the same facts.

Nearest neighbors: ingroup favoritism, indirect/projective questioning, identity-label vignette experiments.

**Verdict: REJECT NOVELTY / PRACTICAL.**

Important confound: `your community` framing can legitimately import contextual knowledge. Keep facts explicit and interpret the differential as identity/context sensitivity, not automatically dishonesty.

## T144-06 — Independent-record truth anchors

With consent and ethical safeguards, include low-stakes factual questions for which an independent record exists.

Examples might include:
- meeting attendance;
- hours worked/credited;
- number of formal reviews/appeals used;
- dates of specific procedural events.

Compare self-report error on neutral versus reputation-relevant anchors.

**Verdict: KNOWN criterion-validation logic / PRACTICAL.**

Do not use leadership-controlled records as unquestioned ground truth.

## T144-07 — Self versus `people here` indirect questions

Ask both:
- `How often do you experience X?`
- `How common do you think X is among people here?`

Nearest neighbor: indirect/projective questioning.

**Verdict: KNOWN / WEAK DIAGNOSTIC.**

The difference can reflect perceived norms or projection rather than concealed self-report, so do not treat peer estimate as hidden truth.

## T144-08 — Reverse-coded / repeated consistency items

Use semantically equivalent or reversed items separated in the survey.

**Verdict: KNOWN / QUALITY CONTROL ONLY.**

A strategic face-saving respondent can answer consistently, so this detects inconsistency/acquiescence more than impression management.

## T144-09 — Response-time / paradata anomaly indicators

Use optional survey paradata to identify unusually fast, repeated, or hesitation patterns.

**Verdict: KNOWN / WEAK.**

Do not infer deception from response time; it is affected by literacy, device, disability, reflection and many other factors.

## T144-10 — `No ordinary human faults` ceiling sentinel

Embed a few statements where universal perfection is implausible, e.g. never being irritated, never concealing a mistake, always treating everyone fairly.

Nearest neighbor: social-desirability scales.

**Verdict: MERGE T144-01.**

Do not invent an unvalidated local scale and pretend population norms are known.

## T144-11 — Aggregate expected-variance compression

Compare community variance on neutral/basic traits with external-population variance and treat unusually low variance as face-saving.

**Verdict: REJECT AS PRIMARY METHOD.**

A community is selected and may genuinely be homogeneous. External variance is not a valid truth benchmark without strong invariance/selection assumptions.

Useful only as a weak anomaly flag after other diagnostics.

## T144-12 — Randomized assurance wording

Randomize credible privacy reassurance / explanation of who can see the data.

**Verdict: KNOWN / PRACTICAL IF THE DIFFERENCE IN ACTUAL PRIVACY IS REAL OR THE EXPERIMENT IS ETHICALLY APPROVED.**

Do not falsely promise stronger anonymity than exists.

## T144-13 — Extended crosswise / randomized response diagnostic

Use privacy-preserving response designs that can also diagnose systematic response bias.

Source precedent: extended crosswise-model experiments explicitly allow detection of some systematic response bias; randomized response is established for sensitive attributes.

**Verdict: KNOWN / PRACTICAL WITH SAMPLE-SIZE AND COMPREHENSION LIMITS.**

## T144-14 — Known-truth `foil incident` recognition

Ask whether the respondent remembers a fabricated community event to detect willingness to affirm favorable/expected narratives.

**Verdict: REJECT / HIGH ETHICAL AND INTERPRETIVE RISK.**

A fictional local event can feel like researcher deception, confuse memory, and damage trust. Prefer neutral overclaiming foils unrelated to actual community history.

## T144-15 — Bogus pipeline

Create belief that deception can be physiologically detected.

Source precedent: Jones & Sigall (1971) bogus pipeline; later work identifies demand-characteristic limitations.

**Verdict: REJECT FOR ROUTINE COMMUNAL RESEARCH.**

Deceptive and ethically unattractive in precisely the high-control settings where trust matters.

## T144-16 — Longitudinal pre/post-exit disclosure differential

Compare the same person's responses while resident and after exit when follow-up is possible.

**Verdict: KNOWN / PRACTICAL RESEARCH CONTROL.**

A post-exit change can reflect reduced pressure, changed experience, grievance, new information or retrospective reinterpretation; it is not a truth oracle.

---

# Recommended embedded battery

## Tier A — Every sufficiently large communal survey

1. **4–8 validated social-desirability / improbable-virtue items** appropriate to language/culture;
2. **perceived disclosure-consequence items** from Batch 43;
3. **small set of repeated/reverse-coded quality items**;
4. **C022 measurement canaries** for locally interpreted outcome categories;
5. **current-vs-leaver status and cohort identifiers** for Batch 41 controls.

## Tier B — Federation-wide surveys where N is adequate

6. **randomized direct vs indirect sensitive-question experiment** for 1–3 critical constructs;
7. **privacy/mode randomization**;
8. **ingroup-label mirror vignettes**;
9. **neutral overclaiming foils**;
10. **independent-record validation subsample** where ethically feasible.

## Tier C — High-risk / methodological studies

11. randomized-response / extended-crosswise methods;
12. repeated longitudinal resident→leaver comparisons;
13. independent standardized interview/observation subsamples.

---

# What to compute

Do **not** compute `person X lies 37%`.

Compute sample/community-level diagnostics such as:

- social-desirability response distribution;
- foil false-positive / overclaiming bias;
- direct–indirect prevalence gap with CI;
- privacy-mode response shift;
- ingroup-vs-neutral vignette leniency;
- known-record self-report error distribution;
- perceived disclosure-risk distribution;
- resident-vs-leaver longitudinal change where available.

Call the combined output a **reporting-pressure profile**, not a correction factor.

Use it to classify the evidence environment, for example:

- low detected pressure / high privacy confidence;
- moderate mode-sensitive reporting;
- strong group-protective response pattern;
- high uncertainty / contradictory diagnostics.

Do not automatically rank communities on the profile; some communities may genuinely have stronger shared norms while others have weaker survey comprehension or different response styles.

---

# Important methodological warning

The user's initial `expected variance` intuition is useful only when the expected distribution is genuinely justified.

The strongest embedded diagnostics deliberately manufacture or know the benchmark:

- foil truth is known;
- random assignment creates comparable groups;
- external records create criterion anchors;
- identical vignettes hold observed facts fixed.

Those designs are much less dependent on assuming commune members `should` look like outsiders.

---

# Updated federation research-center gates

Batch 44 refines gate 6 rather than creating a new gate:

6. **Disclosure-incentive gate — Batches 43–44:**
   - do respondents have incentives/fears that can alter self-report?;
   - what embedded diagnostics indicate about the magnitude/direction of reporting pressure?;
   - do conclusions survive more private/indirect measurement modes?

---

## Disposition

No Creative Tail survivor.

Strong practical architecture:

> **Embed multiple reporting-bias diagnostics with known truth, randomized comparison, or independent anchors. Use their convergence to characterize the reporting environment; never infer face-saving from low ordinary variance alone and never turn the battery into an individual lie detector.**
