# Creative Tail Sampling — Canonical Findings Index

Updated: 2026-08-15

This file distinguishes **actual survivors** from useful-but-familiar material. A user familiarity veto or strong historical/literature compression overrides earlier promotion.

## Current result

### No accepted grand social-theory finding yet

The multiplex/relational-unbundling branch failed the novelty gate. It is preserved in run history and `MODEL.md` as historical/applied material only.

## Surviving cross-domain connections

### C001 — Active normative edge-case search

**Status:** SURVIVING CROSS-DOMAIN CONNECTION; not claimed as academically unprecedented.

**Target:** intentional-community values, membership fit, governance calibration, cultural replication.

**Source:** active learning / preference elicitation + software regression testing.

Instead of maximizing agreement on abstract values, adaptively select concrete cases where members' currently plausible interpretations are most likely to diverge.

Architecture:

1. collect independent baseline judgments before discussion;
2. infer where latent interpretations differ;
3. choose the next case expected to reduce uncertainty most;
4. separate measurement from later deliberation/socialization;
5. resolve disagreements that materially affect design;
6. preserve the highest-information resolved cases as a versioned **constitutional regression suite**;
7. rerun them after membership/rule changes to expose semantic drift;
8. replicate/randomize some cases to detect sequence sensitivity rather than assuming fixed preferences.

The moral-preference-elicitation literature gives an important caveat: active querying can perform badly when moral judgments are unstable, sequence-sensitive, noisy, or poorly represented by the assumed model. Therefore C001 is a diagnostic procedure, not a claim that a group has one fixed latent utility function.

Demote if a target-domain precedent is found using substantially the same adaptive case-selection + regression-suite architecture.

Audit: `runs/2026-08-15-orthogonal-tail-batch-04.md` and Batch 06 revisit.

### C003 — Asset-gated cultural mutation

**Status:** SURVIVING CROSS-DOMAIN CONNECTION; current strongest reproduction-specific candidate.

**Target:** community movements that want both reproduction and institutional learning/variation.

**Source connection:** evolutionary variation/selection + organizational property/fission architecture.

The property rules governing a split can control the movement's **effective cultural mutation rate**.

Distinguish:

- **sanctioned reproduction** — parent/movement-recognized daughter branches inherit substantial accumulated resources;
- **unsanctioned cultural forks** — dissenting branches attempt a materially different norm/governance model.

If sanctioned daughters inherit land/capital/resources while dissenting forks must leave with little or none, a movement can reproduce rapidly while exploring very little institutional design space.

The key consequence is **selection blindness**:

> Observed community evolution is not selection among all plausible designs. It is selection among designs that the incumbent reproduction architecture allowed to become sufficiently capitalized competitors.

Therefore apparent long-run stability of a community form is weaker evidence of its superiority when property rules heavily pre-filter which alternatives can become viable experiments.

Empirical anchor: Hutterite daughter-colony formation explicitly divides colony assets between parent and daughter, while Hutterite legal cases describe members leaving/being expelled without claims to colony property. This is not a criticism of Hutterite practice; it exposes the structural distinction between demographic branching and culturally divergent branching.

Distinctive predictions:

- movements with greater branch-level capital portability should generate more viable institutional variation, controlling for ideological disagreement;
- high ordinary daughter-formation rates need not imply high institutional experimentation rates;
- property/legal architecture should predict which kinds of forks survive independently of the substantive quality of their ideas.

Possible design consequence: if a movement wants bounded experimentation, it could precommit a **fork-capital/seed protocol** based on process and viability criteria rather than doctrinal approval. This remains a mechanism-design hypothesis because automatic portability can also incentivize strategic fission/asset stripping.

Demote if existing scholarship is found that already treats branch asset portability explicitly as a control on cultural/institutional variation rather than merely documenting property disputes after schism.

Audit: `runs/2026-08-15-orthogonal-tail-batch-06.md`.

### C004 — Governance commutativity

**Status:** SURVIVING CROSS-DOMAIN CONNECTION; current strongest distributed-systems transfer.

**Target:** federations/networks of semi-autonomous daughter communities.

**Source:** distributed systems / scalable software, where operations that commute can proceed without unnecessary serialization/conflict.

For two local governance actions A and B, ask:

> If A then B and B then A produce materially equivalent shared movement state, why must those decisions share a central coordination bottleneck?

If their effects do **not** commute—e.g. competing claims on one shared asset, incompatible movement-wide commitments, or mutually exclusive assignments—some ordering/coordination is genuinely necessary.

This differs from generic subsidiarity because it creates both a diagnostic and a design objective:

> **Do not only decentralize decisions that already happen to be independent. Redesign shared state so more decisions become commutative.**

Possible architectural moves:

- partition one shared discretionary budget into bounded local budgets;
- use distinct local resource/land namespaces where possible;
- keep the movement-wide promise/interface minimal while local practices vary;
- use append-only shared records where overwriting is unnecessary;
- predefine resource ceilings/interfaces so local actions remain compatible.

Hypothesis: federation coordination burden may depend more on the **density of non-commuting decision pairs** than on raw community/member count.

Distinctive predictions:

- coordination overhead should track cross-community state conflicts better than raw federation size;
- simple delegation without reducing shared-state conflict should generate more disputes than redesigns that make local actions order-independent;
- federations with more separable decision domains should scale with less central-governance growth.

Polycentric-governance literature already covers autonomous decision centers, overlap, interdependence, subsidiarity, and coordination. The targeted search did not locate an explicit use of operation commutativity/order-independence as the criterion or design objective. Therefore this remains a cross-domain connection, not a new governance theorem.

Demote if an equivalent criterion is found under different governance vocabulary or if non-commutativity adds no explanatory value beyond standard interdependence/resource-overlap measures.

Audit: `runs/2026-08-15-orthogonal-tail-batch-06.md`.

## Demoted applied hypotheses

### D001 — Flagship founder trap / founder-export externality

Previously C002. **Demoted after literature attack.**

The application to intentional communities may still be useful: attractive parents can retain experienced potential founders, while the wider movement benefits from their departure. But employee-spinout research already analyzes parent loss of human capital, high-ability founder retention/deterrence, and parent consequences of spinouts; classical social-movement theory also analyzes organizational maintenance versus movement goals. The transfer is not currently far enough from those literatures.

### D002 — Multi-parent daughter recombination

Useful possibility, but still too close to cross-pollination, diverse founder experience, and cultural recombination.

### D003 — Developmental-sequence replication

Useful possibility, but still too close to tacit knowledge, organizational lifecycle, sequencing, and path dependence.

## Known / derivative community material — DO NOT REPROMOTE AS NOVEL

- specialization/commodification/alienation of social relations;
- thick-vs-thin ties, embeddedness, social capital, multiplex-resource exchange;
- specialization making people replaceable;
- planned community fission / propagule reproduction;
- packet reproduction through experienced member splits;
- cultural-transmission complexity/fidelity thresholds;
- germline/reproductive specialization;
- source/sink institutional dynamics;
- network modularity/fission;
- cultural compression through repeated transmission;
- recruitment-composition effects;
- ordinary collective forkability/scission;
- generic migration/diversity tradeoffs;
- ordinary property disputes after schism;
- key-person risk, stress inoculation, conflict queues;
- local retention being an incomplete movement metric;
- generic organizational lifecycle/sequencing;
- generic stress testing/chaos drills;
- redundant encoding of values without a stronger consequence.

## Earlier provisional branches

### E001 — Epistemic firebreaks

Independent observation/deliberation before communication can reduce correlated error. Too close to wisdom-of-crowds / information-cascade theory.

### E002 — Whole-package ratification

Component-wise collective choices can assemble a package that still deserves whole-package ratification. Too close to known social-choice problems.

## Protocol lessons

### M001 — Formalization is not novelty

A familiar root idea does not become a tail discovery because downstream mechanisms receive technical names.

### M002 — User familiarity veto dominates model confidence

If the intended expert user immediately compresses the candidate to common sense or known theory, record the collision and move outward.

### M003 — Nearest-neighbor literature attack before promotion

Candidate survivors require explicit search for conceptual ancestors. This prevents obvious retrieval failures; it does not prove originality.

### M004 — Cross-domain transfer can count, same-domain rediscovery cannot

A known source-domain mechanism can survive if its target transfer is nonstandard and yields distinctive predictions/design rules.

### M005 — Empty batches are successful

Prefer 'nothing survived' over weak promotion.

## Provenance

- recovered pre-deletion state: `runs/2026-08-15-recovered-pre-deletion-findings.md`
- multiplex batches 01–03: historical exploration, later vetoed
- user veto: `runs/2026-08-15-user-veto-multiplex-branch.md`
- orthogonal batch 04: `runs/2026-08-15-orthogonal-tail-batch-04.md`
- reproduction batch 05: `runs/2026-08-15-reproduction-tail-batch-05.md`
- orthogonal batch 06: `runs/2026-08-15-orthogonal-tail-batch-06.md`
