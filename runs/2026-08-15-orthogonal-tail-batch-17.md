# Orthogonal Tail Batch 17 — Applicant Thickness, Hutterite Cross-Branch Reproduction, and Governance Testing

Date: 2026-08-15

## Goals

1. adversarially narrow C009 cohort-composition admission after the user noted applicant scarcity;
2. perform the first comparative C005 test using FEEFHS Lehrerleut and Dariusleut parent-colony tables;
3. generate >=12 orthogonal cross-domain transfers and promote only candidates that survive common-sense and nearest-neighbor screens.

---

# A. C009 adversarial refinement — candidate-pool thickness

## User objection / scope correction

C009 is potentially useful, but mature communes may rarely have many simultaneous applicants. Founding groups are more likely to have a meaningful pool, and founding groups may already think intuitively about complementary couples, households, skills, and subgroups.

This is a real scope constraint, not a minor implementation detail.

## Target-domain screen

Intentional-community guidance and listings remain predominantly sequential/probationary:

- Foundation for Intentional Community membership-process material describes recruitment, cultivation, orientation, integration and standing membership teams, but not explicit candidate-set optimization.
- ICmatch membership guidance describes milestones such as committee approval and trial periods for a potential member.
- multiple FIC directory entries describe one-applicant-at-a-time visit / trial / vote processes.

Near precedents:

- Ottawa Cohousing explicitly uses intake information for **matchmaking**, constructs potential groups, and brings selected people together into an “Affinity Group.” This is a forming-community case and therefore supports the user’s prediction that cohort thinking is more natural at formation.
- Sovereign Tree says that if several qualified applicants emerge, it may introduce them so they can voluntarily collaborate; again this is a forming/small-site context, not a mature-community cohort-admission system.

Sources:

- https://www.ic.org/designing-a-community-membership-process/
- https://icmatch.org/guidelines-for-intentional-community-agreements/membership-selection-process/
- https://www.ottawacohousing.ca/our-process
- https://www.ottawacohousing.ca/forming-groups
- https://www.ic.org/directory/sovereign-tree/

## Result

C009 survives only in a narrower form:

> **When the applicant market is thick enough that several plausible people/households overlap in time, and applicant interaction effects are material, individual sequential acceptance can destroy better reachable cohort configurations.**

Do not infer that mature communes should routinely delay admission to create artificial batches. Batching has costs:

- vacancies remain unfilled;
- applicants may accept alternatives while waiting;
- longer uncertainty burdens applicants;
- cohort selection can become a cover for discrimination or clique engineering;
- predicting human interaction effects can be noisy.

The operative decision is therefore itself dynamic: **batch only when expected composition value exceeds waiting/attrition cost.** This is a standard matching-market thickness tradeoff and is not a separate creative-tail discovery.

Practical niche:

- founding;
- daughter-community seeding;
- new-site opening;
- deliberate expansion waves;
- several simultaneous vacancies;
- rare periods when a mature community genuinely has multiple viable applicants at once.

Verdict: **C009 survives, narrowed.**

---

# B. C005 comparative empirical test — Lehrerleut and Dariusleut

## Sources

FEEFHS republishes Hostetler-derived flat-file tables with `Year Founded`, `Colony Name`, and `Parent Colony` fields:

- Lehrerleut, 65 colonies as of 1973: https://feefhs.org/erg/hutterites-lehrerleut-colonies-1973
- Dariusleut, 87 colonies as of 1973: https://feefhs.org/erg/hutterites-dariusleut-colonies-1973

The tables give a parent-child genealogy rather than only aggregate colony counts.

## Cohort definition

To reduce right-censoring, use post-migration colonies founded **1918-1953 inclusive**, giving at least 20 years of potential daughter production before the 1973 observation cutoff.

`K` = number of listed daughter colonies founded through 1973.

Data snapshot:

- `data/hutterite_feefhs_1973_mature_cohorts.csv`
- `analysis/hutterite_feefhs_reproduction_metrics.py`

### Source normalization

The Dariusleut table contains two distinct historical `Beadle, South Dakota` episodes, 1905-1918 and 1920-1935. Raley (1918) descends from the earlier episode, whereas Felger (1926) and King Ranch (1935) descend from the 1920 episode. The mature-cohort `K` for the 1920 Beadle node is therefore 2 rather than 3.

Several minor Lehrerleut spelling variants in parent fields were normalized to the corresponding listed colony name (`O. K.` / `O. K. Colony`, `Macillan` / `McMillan`, `New Elm Spring` / `New Elmspring`, and missing comma in `Big Bend Alberta`).

## Results

### Lehrerleut mature cohort

- parents `n = 29`
- listed daughters = 53
- mean `K = 1.828`
- median `K = 1`
- population variance `= 1.453`
- variance/mean `= 0.795`
- `P(K=0) = 3.45%`
- top 10% of parents account for `24.53%` of daughters
- maximum `K = 5`

### Dariusleut mature cohort

- parents `n = 33`
- listed daughters = 60
- mean `K = 1.818`
- median `K = 2`
- population variance `= 0.694`
- variance/mean `= 0.382`
- `P(K=0) = 0%`
- top 10% of parents account for `20.0%` of daughters
- maximum `K = 3`

## Interpretation

This substantially strengthens the Hutterite result.

The earlier Manitoba reconstruction could in principle have been an unusually reproducible Schmiedeleut/Manitoba sublineage. Instead, two other Hutterite branch tables show the same qualitative signature under a standardized 20+ year observation window:

- almost every mature parent reproduces at least once;
- the median parent is reproductively successful;
- variance is not strongly overdispersed relative to the mean;
- the top decile does not dominate daughter production;
- there are no giant reproductive jackpots in these cohorts.

The Dariusleut result is especially striking: every 1918-1953 cohort node has at least one listed daughter by 1973, subject to the source and node-identity caveats below.

### Caveats

- These are historical source tables, not a modern research dataset built for reproductive-demography analysis.
- Colony moves, extinction/re-establishment, and reused names can complicate node identity.
- The 1973 cutoff omits later offspring.
- The analysis counts listed colony fissions/descendants, not independent de-novo starts.
- Differences in branch subsidy, land availability, demographic growth, and fission norms remain to be measured.
- The Manitoba current-era reconstruction has a much longer follow-up than these standardized 20+ year cohorts, so absolute mean K should not be compared naïvely across datasets.

## C005 update

C005 is now less a warning about a hypothetical superstar trap and more a **positive discriminator** identifying what is unusual about the best current reproduction exemplar:

> Successful Hutterite community reproduction appears broadly distributed across ordinary mature parent communities and across multiple branches, not driven by a small set of extraordinary founders or flagship colonies.

That suggests a strong movement-design criterion: **make reproduction boring.** A replicable community system should make daughter formation an ordinary lifecycle event for the median competent community, rather than an exceptional achievement by unusually charismatic or capable founders.

This phrase is operational shorthand, not a claim of academic novelty.

---

# C. Orthogonal candidate batch

Sixteen plain candidates were generated before selection.

## T117-01 — Applicant batching should depend on market thickness

Plain claim: cohort-aware admission only helps if enough plausible candidates overlap; waiting for a thicker pool has vacancy and attrition costs.

Nearest neighbor: matching-market thickness / waiting tradeoffs.

Verdict: **USEFUL REFINEMENT OF C009; NOT NEW.**

## T117-02 — Governance fault injection

Plain claim: a community should sometimes deliberately simulate or safely induce the temporary unavailability of a key person, permission, account, service, or infrastructure component to discover hidden dependencies before a real failure.

Source-domain mechanism: chaos engineering, fault injection, continuity exercises.

Nearest-neighbor target search:

- intentional-community material discusses founder syndrome, succession, role sharing, and governance redesign;
- generic nonprofit/business-continuity practice includes key-person-unavailable tabletop exercises;
- FEMA continuity exercise kits explicitly test essential-function continuity under personnel/facility/system disruption;
- no close intentional-community precedent was found for **systematic governance/dependency fault injection** as a recurring design practice.

Sources:

- https://preptoolkit.fema.gov/web/em-toolkits/continuity-of-essential-functions
- https://www.readyrating.org/resource-center/training-and-exercises/business-continuity-exercise-plan-template
- https://principlesofchaos.org/
- https://icmatch.org/guidelines-for-intentional-community-agreements/governance-of-intentional-community/roles-of-your-core-founders-group/

Derived practice:

1. map a critical function/dependency;
2. define a bounded, reversible failure injection;
3. predict what should happen;
4. temporarily remove the dependency or tabletop the exact loss;
5. observe who actually has knowledge, authority, credentials, relationships and fallback capacity;
6. record unanticipated coupling;
7. repair the architecture;
8. rerun later.

Candidate injections:

- founder unavailable for one governance cycle;
- treasurer unavailable and normal banking approver inaccessible;
- internet/phone unavailable;
- one vehicle or supplier unavailable;
- membership records inaccessible;
- usual meeting facilitator absent;
- key childcare/care organizer unavailable;
- outside professional or government contact unavailable.

Safety constraint: never inject failures whose realistic downside to health, children, legal rights, housing security, essential medication, or other necessities is material. Use tabletop/sandbox simulation for high-stakes functions.

Distinctive prediction: communities that repeatedly test **actual dependency loss** should discover more hidden single points of failure than communities that only document succession/backups, even when both possess similarly complete written plans.

Verdict: **SURVIVES as C010, provisional cross-domain operational transfer.**

## T117-03 — Shadow governance before live governance

Plain claim: before transferring real authority to a substantially new governance process, run it nonbinding in parallel on the same decisions and compare what it would have done with the incumbent process.

Source-domain mechanism: shadow mode / parallel-run deployment in software, policy engines, and enterprise-system migration.

Target-domain nearest neighbors:

- Cambridge Cohousing reports implementing Dynamic Governance for a six-month **live trial**;
- Cherry Hill Cohousing and Dancing Rabbit describe adopting new governance systems;
- target searches found trials/pilots, but no close intentional-community example in which the proposed governance body/rule makes **parallel nonbinding decisions on the same live cases** before receiving authority.

Sources:

- https://www.ic.org/directory/cambridge-cohousing/
- https://web.cohousing.com/governance/
- https://www.ic.org/radical-governance-changes-in-two-north-american-ecovillages/
- source-domain parallel/shadow concept: Microsoft/AWS/software policy-engine practice.

Minimal protocol:

1. define exactly which decisions the new process would govern;
2. keep the incumbent process authoritative;
3. give the shadow process the same admissible information, without letting it affect the live outcome;
4. record its decision, reasoning, time/cost, dissent, recusal and evidence requirements;
5. compare divergence cases rather than average agreement;
6. ask which differences are improvements, regressions, or artifacts;
7. only then choose live trial, revision, or rejection.

Why this differs from an ordinary pilot: a live pilot changes the people affected and creates real path dependence; shadow mode can reveal decision differences before imposing them.

Limits:

- participants may behave differently when decisions are nonbinding;
- running two processes costs time;
- confidentiality must not be doubled unnecessarily;
- personal disciplinary/safety cases may be inappropriate for experimental duplicate review;
- shadow agreement does not prove live legitimacy.

Distinctive prediction: shadow runs will identify high-impact divergence cases before live implementation that ordinary constitutional discussion misses, particularly where two procedures sound similar abstractly but allocate agenda, evidence, veto, recusal or timing differently.

Verdict: **SURVIVES as C011, provisional cross-domain operational transfer.**

## T117-04 — Change cadence should be slower than feedback lag

Plain claim: repeated governance changes before earlier changes produce observable consequences can create oscillation/thrashing.

Nearest neighbors: policy feedback, organizational change fatigue, control-system delay.

Verdict: **REJECTED AS NOVEL; PRACTICALLY USEFUL.**

## T117-05 — Count evidence lineages, not endorsers

Plain claim: ten people repeating one originating rumor are not ten independent observations.

Nearest neighbors: source-independence analysis, data provenance, pseudoreplication, intelligence analysis.

Verdict: **REJECTED AS NOVEL; useful evidence-process lesson.**

## T117-06 — Irreversibility should raise decision thresholds

Plain claim: under equal uncertainty, harder-to-reverse actions should require more evidence or favor reversible interim steps.

Nearest neighbors: real options, precautionary principle, reversible decision theory.

Verdict: **REJECTED.**

## T117-07 — Constitution as a sufficient statistic for founder history

Plain claim: if successors cannot make competent decisions without founder-specific historical knowledge, formal documentation has not captured enough state.

Nearest neighbors: tacit knowledge, organizational memory, succession documentation.

Verdict: **REJECTED.**

## T117-08 — Deliberately vary daughter implementations to detect accidental tradition

Plain claim: cloned daughters create correlated institutional errors; deliberate implementation variation can distinguish invariant principles from inherited accidents.

Nearest neighbors: policy experimentation, laboratories of democracy, evolutionary recombination.

Verdict: **REJECTED.**

## T117-09 — Preserve dissent as parity information

Plain claim: archived dissenting rationales can later diagnose whether a failure followed a previously identified model boundary.

Nearest neighbors: minority reports, dissent channels, premortems, red teaming.

Verdict: **REJECTED.**

## T117-10 — Network interference invalidates individual policy evaluation

Plain claim: a rule applied to one member changes outcomes for others, so individual treatment/outcome assumptions fail.

Nearest neighbor: causal inference under interference/network spillovers.

Verdict: **REJECTED AS NOVEL; RESEARCH CONTROL ONLY.**

## T117-11 — Current-member satisfaction can reverse policy evaluation

Plain claim: if a policy causes dissatisfied people to leave, surveying only remaining members can make the policy look better because the treatment changes who remains observable.

Nearest neighbors: survivorship/attrition bias, conditioning on post-treatment variables, principal stratification.

Verdict: **REJECTED AS NOVEL.** Already covered operationally by post-exit outcome requirements.

## T117-12 — Critical rights need graceful-degradation modes

Plain claim: communities should specify reduced-capability modes that preserve essential rights when normal governance fails.

Nearest neighbors: graceful degradation, business continuity, emergency governance.

Verdict: **REJECTED AS NOVEL; useful architecture.**

## T117-13 — Governance feedback oscillation

Plain claim: delayed effects plus rapid adjustment can cause alternating governance reforms rather than convergence.

Nearest neighbors: policy feedback, control systems, institutional-change repetition.

Verdict: **REJECTED.**

## T117-14 — Use reversible diagnostic interventions to distinguish hidden causes

Plain claim: when several latent causes produce the same observable symptom, small interventions can identify which cause is active before a major rule change.

Nearest neighbors: experimental design, control-system observability, causal diagnosis.

Verdict: **REJECTED AS GENERAL NOVELTY; potentially useful case method.**

## T117-15 — Separate source diversity from voter diversity

Plain claim: a diverse decision body can still rely on one evidence source, giving false epistemic redundancy.

Nearest neighbors: source independence, common-mode information failure.

Verdict: **REJECTED.**

## T117-16 — Exploration budget should vary over institutional life stage

Plain claim: founding systems should explore more; mature high-stakes systems should exploit more; daughter formation can reopen exploration.

Nearest neighbors: exploration/exploitation, organizational lifecycle, ambidexterity.

Verdict: **REJECTED.**

---

# Batch 17 promotions

## C010 — Governance fault injection

Provisional cross-domain transfer. Distinctive element is moving from **having a backup plan** to **testing the loss of the dependency** under bounded conditions and recording unanticipated coupling.

## C011 — Shadow governance

Provisional cross-domain transfer. Distinctive element is a **nonbinding parallel decision process on the same cases** before authority transfer, rather than an ordinary live pilot.

## C005 strengthened

The FEEFHS Lehrerleut and Dariusleut mature-cohort reconstructions strongly replicate the qualitative Manitoba result: Hutterite reproduction is unusually broadly distributed across ordinary parent communities.

## C009 narrowed

Cohort-aware admission is not a general replacement for sequential admission. Its practical value depends on candidate-pool thickness and material interaction effects.
