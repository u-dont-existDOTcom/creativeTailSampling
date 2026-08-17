# Verification — inner-child therapy protocol Batch 004

Date: 2026-08-17
Branch: `agent/inner-child-therapy-protocol-mermaid-20260817`
Base: `7cb7ad8f75fdb3a423157a94c8c23ba78712031c`

## Verification target

Verify the durable protocol checkpoint after map-first architecture, Batch-004 Tail generation/adjudication, Exa research, two Parallel hostile reviews, practical protocol hardening and checkpoint synchronization.

## Live branch clone

The working branch was freshly cloned from GitHub into an isolated local verification directory before these checks. Verification was performed against that clone rather than against remembered chat text.

## Required control-surface presence

Verified present:

- canonical `THERAPY-PROTOCOL-OVERVIEW.md`;
- nine focused Mermaid maps;
- protocol state;
- protocol-gap ledger;
- article→protocol crosswalk;
- candidate-status ledger;
- evidence ledger;
- Batch-004 candidate CSV;
- Batch-004 source fingerprint;
- Batch-004 run record;
- Exa/Parallel retrieval evidence records;
- dedicated fresh-conversation handoff.

## Mermaid static checks

Automated static checks required:

- exactly 10 visual-control files = canonical overview + 9 maps;
- exactly one fenced `mermaid` block in each visual-control file;
- each Mermaid block declares `flowchart` or `graph`;
- canonical overview links all nine numbered drill-down maps;
- required companion control artifacts exist.

Result: **PASS**.

## Mermaid parser/render verification

Every Mermaid block from the canonical overview and all nine drill-downs was extracted to an individual `.mmd` file and rendered using `@mermaid-js/mermaid-cli`.

Result: **PASS — all 10 graphs rendered successfully.**

This verifies Mermaid syntax/renderability at this checkpoint. It does not by itself validate clinical logic.

## Parallel Task state

Rechecked both Batch-004 Parallel runs after completion:

- `trun_201682d6febd4300b59f13e08a55ce07` — no-arrears hostile review — completed; result persisted.
- `trun_201682d6febd430086d514bfd8db3648` — internal-jurisdiction hostile review — completed; result persisted.

No Batch-004 Parallel run remains live.

## Stale-state checks

Checkpoint state/handoff were rewritten so they no longer instruct a future worker to poll the already-completed internal-jurisdiction task.

The canonical inner-child state records only the correct base SHA:

`7cb7ad8f75fdb3a423157a94c8c23ba78712031c`

## Topology-level conclusions verified against artifacts

The current architecture visibly contains:

- longitudinal bot safety / operation-permission routing before therapeutic operation selection;
- operation-specific capacity/readiness rather than a global stabilization identity;
- Nurturer / Protector / Guide function × context assessment;
- parentification history separated from current overfunctioning/function imbalance;
- contestable/as-if parts formulation;
- optional-introspection consent and no automatic guard retry debt;
- thin adult-led interface rather than formal internal constitution;
- prediction-based trust and explicit broken-promise repair;
- no-arrears with external-accountability and therapeutic-dose boundaries;
- ordinary positive child-adult relationship outside crisis;
- identity/differentiation safety against default isolation;
- source provenance separated from confidence/meaning;
- owner-locked depth ≠ integration distinction;
- integration-load / restored-capacity gate without fixed waiting interval;
- external-helper concentration risk review without nonlinear novelty claim;
- outcome/adverse-effect fault localization;
- multi-turn vulnerability-amplifying-loop audit;
- missing-information gates.

## Evidence-scope verification

The evidence ledger explicitly warns that:

- the full Mermaid topology is a **research-stage synthesis**, not a validated unified treatment;
- individual components have different levels of direct, adjacent or safety-support evidence;
- current chatbot-safety studies justify architectural safeguards but do not establish that a future deployment of this protocol is safe;
- the owner's broader reparenting thesis remains an explicit challengeable thesis rather than settled universal evidence.

## Strict Tail verification

Candidate and run ledgers agree:

- **zero Batch 002–004 strict Tail survivors**;
- no-arrears remains practical but novelty-rejected;
- internal constitution remains novelty-rejected and practically replaced by a thinner interface;
- general function/mode matching is known prior art;
- parentification/function imbalance has known roots and corrected terminology;
- longitudinal bot-safety architecture has strong current prior art and is a practical safety addition, not a novelty claim.

## Remaining unresolved frontier

The checkpoint correctly leaves these unresolved rather than pretending completion:

1. qualitative restored-capacity recognition before deliberate depth re-entry;
2. comparative utility of the N/P/G intervention-mismatch heuristic versus simpler formulation;
3. non-pathologizing current-function markers for possible parentification-linked overfunctioning;
4. transition-specific mandatory fields and explicit `unknown` behavior in a future implementation;
5. comparative value of the thin role interface versus a simpler adult-led formulation;
6. real-world validation of longitudinal bot safety, including privacy/retention, false-positive escalation, gradual-risk misses and actionable external-support paths.

## Verification conclusion

**PASS for repository persistence, required map topology, Mermaid syntax/renderability, provider-result persistence and checkpoint synchronization.**

Clinical efficacy/safety of the unified therapy protocol is deliberately **not** claimed by this verification.
