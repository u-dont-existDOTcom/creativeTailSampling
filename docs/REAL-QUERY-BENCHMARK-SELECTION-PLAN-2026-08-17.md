# Real-query benchmark selection plan — executed Batches 006–009

**Updated:** 2026-08-18  
**Original one-parent checkpoint:** `db591713a3feb0a1576943408ae356685c0034ec`  
**Pre-Batch-009 main:** `c24fef6f3700fe3795d81edfcc6aba38ff685898`  
**Status:** open-ended architecture benchmark complete

## Goal

Use real, naturally phrased therapy problems to expose missing protocol topology rather than merely produce different prose.

## Corpus constraints

A candidate enters the benchmark only when:

1. it is a real public first-person help-seeking/problem statement;
2. the original post, not comments or later advice, supplies the benchmark input;
3. usernames and incidental identifying details can be removed without changing the problem;
4. the paraphrase does not add target-framework language, diagnosis, or preferred solution;
5. source-provided diagnostic/causal priming is removed when it would tell the bot how to answer;
6. expected routes and prohibited behavior stay grader-only.

## Executed corpus

| Batch | Cases | Principal architecture result |
|---|---:|---|
| 006 | 16 | Actor/problem-class router; maps 10–14 |
| 007 | 12 | Capability/skill/scaffold map 15 |
| 008 | 11 | Decision-capacity/supported-choice map 16 |
| 009 | 10 | Resource-unavailable handoff correction; no new map |
| **Total** | **49** | Maps 00–16 |

## Batch 009 saturation result

Coverage included:

- lost time without DID/OSDD priming;
- hospice/culture/patient authority;
- unavailable food/resources;
- parenting harm and repair;
- reciprocal violence with dependent safety;
- abortion moral conflict and bodily autonomy;
- unaffordable recommended treatment;
- uncertain abuse memory;
- current minor abuse/placement uncertainty;
- guardian denial of diagnosed medical needs.

Initial result:

- 8/10 passed unchanged.
- 2/10 found one shared defect: correct external resource identified but genuinely unreachable.

Correction:

- no map 17;
- overview + maps 00 and 07 now represent resource access, barrier, unavailable handoff, bounded fallback, fallback limits, unresolved need, and retry/advocacy trigger.

Post-patch:

- 10/10 pass conceptually.
- architecture saturation criterion reached.

## Revised stopping rule

Stop open-ended anecdotal topology expansion.

A new real case should become a regression fixture unless at least one is true:

1. the executable runtime cannot represent the required safe action;
2. adversarial multi-turn testing exposes a new high-severity loop;
3. qualified clinical/legal/safeguarding review identifies a missing authority or duty;
4. a real adverse event demonstrates an unsafe fallback or dead end.

Emotional novelty, diagnosis novelty, and subject-matter novelty alone do not justify a map branch.

## Next benchmark mode

Future work is no longer broad source discovery. It is:

- run all 49 fixtures through InnerSignalGraph;
- compare expected first operation, questions, prohibited actions, fallback, and longitudinal persistence;
- test maps 15 and 16 against simpler deterministic alternatives;
- test unavailable-resource and false-handoff behavior;
- add newly found real cases only as regression fixtures unless structural failure is proven.

## Boundary

Conceptual saturation is not clinical validation.
