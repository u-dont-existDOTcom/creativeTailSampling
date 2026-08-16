# Retrieval Ensemble Round 001 — Routine Adjudication

Date: 2026-08-16
Branch: `agent/exa-parallel-retrieval-ensemble`
Manifest SHA-256: `6bdbe5e0b75c9f1f0779f0084513d901372d084b9131e3ab6a567636c2fec40c`
Status: routine Exa + Parallel Search pass complete; Parallel Task escalation pending

## Purpose

Retrospectively test whether independent Exa and Parallel retrieval improve Creative Tail Sampling's external novelty-collision gate. The benchmark freezes 14 historical candidates and four provider-independent query families before retrieval. Evaluator metadata (`known_collision_family`, `expected_action`, historical notes) is never exposed to either provider.

Routine raw evidence is stored under:

`analysis/retrieval_ensemble/results/round-001/raw/`

## Historical reject/narrow set

The primary benchmark positive set contains eight historical cases whose correct disposition was already known before this benchmark: three rejects and five narrowings.

### R001 — Multiplex relational unbundling — expected REJECT

**Exa: correct reject.** Retrieved direct community-resilience work explicitly centered on multiplex/multilevel networks and the familiar multiplex/social-capital neighborhood.

**Parallel: correct reject.** Independently retrieved the same general target neighborhood.

Disposition: both providers catch the false novelty.

### R002 — Generic propagule fidelity — expected REJECT

**Exa: correct reject.** Retrieved organizational replication/template/franchise and transmission-fidelity precedents sufficient to collapse the proposition into established reproduction/fidelity mechanisms.

**Parallel: miss.** Routine queries were pulled toward literal offspring/genetic language rather than organizational/cultural replication.

Disposition: Exa-only correct catch.

### R003 — Ordinary exit liquidity — expected REJECT

**Exa: correct reject.** Retrieved substantive/meaningful exit-right literature, including work on realistic exit and explicit communal exit-fund proposals.

**Parallel: miss under conservative scoring.** It retrieved some formal-versus-substantive freedom/portability material but not a sufficiently direct community/outside-option precedent to justify the historical rejection by itself.

Disposition: Exa-only correct catch.

### N003 — Asset-gated cultural mutation — expected NARROW

**Exa: correct narrow.** Retrieved institutional-evolution, capital lock-in/inheritance, founder/resource-dependence and selection neighborhoods. These consume the broad `assets matter` root while leaving the narrower residual: capitalization can pre-select which institutional variants become viable competitors before competitive performance is observed.

**Parallel: miss.** Queries were repeatedly diverted by literal `variant` / genetics / investment-brand polysemy.

Disposition: Exa-only correct narrowing.

### N011 — Shadow governance — expected NARROW

**Exa: correct narrow.** Retrieved experimentalist governance, sandbox/pilot traditions, and parallel assessment/divergence mechanisms. These consume generic piloting/parallel governance without fully containing the narrow same-real-case incumbent-vs-proposed-process execution residual.

**Parallel: correct narrow.** Its source-domain lane found prior parallel governance structures used for institutional experimentation/change.

Disposition: both providers correctly identify the familiar root and leave a narrower residual.

### N013 — Federated reciprocal clearing after exploration — expected NARROW

**Exa: correct narrow.** Retrieved strong matching-market precedents combining preference discovery/interviews with a later clearing stage; notably, admissions mechanisms where local programs retain admission authority while a clearing process coordinates offers. This closely matches the source-domain structure and leaves only the community-specific post-exploration/local-authority residual.

**Parallel: miss.** Queries latched onto behavioral `commitment` literature rather than matching markets.

Disposition: Exa-only correct narrowing.

### N018 — Replicated-governance tombstones — expected NARROW

**Exa: correct narrow.** Retrieved tombstone/deprecation/supersession and lifecycle-governance mechanisms that consume the broad `remember retired failure patterns` root while leaving the institutional replication-channel residual.

**Parallel: borderline.** It found generic software deprecation and governance-failure/lifecycle material, enough to recognize that deprecation itself is not novel, but did not retrieve a strong tombstone-plus-replication-channel structural analogue. Primary scoring treats this as a miss; sensitivity scoring credits it as a narrowing catch.

Disposition: Exa correct; Parallel borderline.

### N026 — Adulthood option grant — expected NARROW

**Exa: correct narrow.** Retrieved same-domain born-into-community/adult-consent/meaningful-exit literature, Amish/rumspringa discussion, and explicit communal exit-fund proposals. These consume non-inherited membership, usable exit and transition support while leaving the timing/symmetry residual: portable launch resources are available *before* adult opt-in rather than only after joining and later exiting.

**Parallel: miss.** Results were dominated by generic transition-to-adulthood and portability polysemy.

Disposition: Exa-only correct narrowing.

## Routine primary metrics

Conservative scoring:

| Condition | Correct historical catches | Catch rate |
|---|---:|---:|
| Exa | 8 / 8 | 100% |
| Parallel Search | 2 / 8 | 25% |
| Exa + Parallel union | 8 / 8 | 100% |

Sensitivity analysis crediting Parallel's N018 result as sufficient root-plus-residual evidence:

- Parallel Search: 3 / 8 = 37.5%.

### Incremental recall

- Ensemble incremental recall over Exa: **0 / 8**.
- Exa supplied at least five clear correct catches that Parallel missed.
- No historical positive was rescued by Parallel after Exa failed.

This means the routine benchmark strongly supports **Exa as a mandatory external semantic collision lane**. It does **not yet support mandatory Parallel Search on every candidate**. Parallel's failure mode was systematic: short keyword queries often locked onto lexical/polysemous neighbors instead of structural conceptual neighbors.

## Current-survivor / cross-domain stress tests

These cases were *not* scored as false positives merely because a provider found a neighbor. The question is whether new retrieval materially changes the present novelty judgment.

### C015 / X015 — Governance rights-liveness verification

**Routine result: materially narrowed.** Exa found:

- social-choice/voting work explicitly formalizing **safety and liveness**;
- formal verification of voting schemes;
- DAO/governance work where quorum, participation, certification, execution and veto determine whether decisions can become effective;
- real governance rules coupling recusal, quorum and deadline exigency;
- formal delegation/revocation models and rights-structure literature.

The broad claim that governance rights should be examined with safety/liveness concepts is therefore not a novel transfer. A possible residual remains:

> systematic reachable-state / model-checking of an entire governance-rights architecture for bounded liveness across interacting recusal, vacancy, quorum, deadline, delegation and noncooperation states.

Parallel routine Search largely missed this neighborhood.

Status after routine retrieval: **NARROW / deep-research boundary case**.

### C001 / S001 — Active normative edge-case search

Exa found constitutional hard-case traditions, analogical/case-oriented reasoning, incompletely theorized agreements, independent-method triangulation and cross-domain borrowing. It did not retrieve a clear established method containing the full compound architecture:

1. actively choose high-information edge cases to discriminate plausible value/constitutional interpretations;
2. collect independent answers before deliberation;
3. preserve resolved cases as a regression-test corpus.

Parallel routine Search found generic constitutional-interpretation material but no stronger match.

Status after routine retrieval: **SURVIVES routine attack / deep-research confirmation warranted**.

### C005 / S005 — Reproductive-variance / superstar-reproduction trap

Exa retrieved the exact source-domain demographic theory: means such as `R0` conceal zero inflation, variance, skew and long-tail reproductive success, including work involving Hutterites. Parallel found similar biological/genetic material.

This establishes that the distribution-not-mean mechanism is old, as already acknowledged. Routine retrieval did not establish the target transfer:

> judge intentional-community reproducibility by the parent-community → daughter-community offspring distribution, including zero-daughter probability, median, variance and concentration in superstar parent communities.

Status after routine retrieval: **SURVIVES as cross-domain communal-design transfer / deep-research confirmation warranted**.

### C006 / S006 — Descendant inflation / lineage-size sampling bias

Exa retrieved direct intentional-community work warning that `success` depends on the chosen unit/criterion and that commune persistence does not necessarily represent movement success. It also retrieved lineage/founder literature showing that inference from extant descendants omits extinct lines and that prolific lineages disproportionately shape present observations.

The exact commune-specific estimand rule is less directly established than the underlying source mechanism:

> state whether the estimand is a random founding attempt/root, lineage, extant community, resident, or future movement contribution.

Status after routine retrieval: **SURVIVES only as a narrow research-control transfer / deep-research boundary case**.

### C016 / X016 — Verifiably unpredictable federation audit sampling

**Routine result: DEMOTE from the strict originality ledger.** Exa retrieved RFC 3797, which already specifies essentially the complete mechanism:

- freeze/publish the eligible pool;
- publish/precommit the deterministic selection algorithm;
- use future public randomness unknown when the algorithm is fixed;
- use randomness outside the administrator's control;
- keep the pool immutable once published;
- make the realized selection publicly replayable/verifiable.

Parallel independently retrieved public-randomness-beacon material applying the same architecture explicitly to audit sampling: commit the record list first, use future public randomness, then regenerate the sample afterward.

Status after routine retrieval: **REJECT as a Creative Tail Sampling originality finding; preserve as a practical design rule.**

### C025 / X025 — Community resolution / living-will architecture

Routine retrieval found much stronger target adjacency than the prior bank-resolution attack:

- FEMA devolution planning for essential community services;
- continuity planning explicitly covering community-based organizations and nonprofits;
- transfer of essential functions to another organization during devolution;
- separate reconstitution planning for recovery of the original organization;
- essential records, personnel/family recovery, alternate providers and sustained operations.

Parallel also retrieved the known bank-resolution critical-function architecture.

The broad `preserve essential functions separately from normal organizational operation` root is therefore established in community/nonprofit continuity practice. What may remain distinct is specifically:

> preplanned **permanent communal dissolution/nonviability**, with member-portable obligations for housing, care, food, records, transport and other member-critical functions even when the commune itself is not recovered.

Status after routine retrieval: **NARROW / deep-research boundary case**.

## Routine architecture verdict

### Exa Search

**Strongly supported.** On the frozen historical positive set it recovered every known rejection/narrowing and repeatedly translated unusual wording into the correct intellectual neighborhood.

### Parallel Search

**Not yet supported as a mandatory routine lane.** It provided independent corroboration in some cases, but did not add historical-positive recall beyond Exa and showed a recurring lexical-polysemy failure mode. Keep it available until the survivor/deep-research analysis is complete; do not yet bake it into every future candidate gate.

### Parallel Task / deep research

Not yet tested. This is now the critical remaining question: can deeper Parallel research resolve boundary cases or discover credible precedents missed by Exa routine search?

## Escalation set

Use Parallel deep research on exactly five cases:

1. **C015** — determine whether whole-governance reachable-state/bounded-liveness verification is already established.
2. **C001** — search for the complete discriminating-edge-case + independent-pre-deliberation + regression-corpus architecture.
3. **C005** — search specifically for offspring-distribution evaluation of institutional/communal replication rather than biological reproduction.
4. **C006** — search for explicit size-biased/extant-lineage sampling controls in intentional-community / organizational-replication research.
5. **C025** — search for permanent nonprofit/communal dissolution plans that preserve member-critical functions through alternate providers without preserving/reconstituting the organization.

Do **not** spend deep-research calls on C016; it is already decisively demoted.

## Protocol status

Do not update the canonical external novelty gate yet. The final architecture decision waits for the Parallel Task escalation results.
