# InnerSignalGraph merge addendum — Real-query saturation Batch 009

Date: 2026-08-18  
Creative Tail source main before this batch: `c24fef6f3700fe3795d81edfcc6aba38ff685898`  
Batch branch: `agent/inner-child-real-query-saturation-009`

This addendum supplements the Batch 006–008 merge instructions.

## Required runtime change

Do **not** create map 17 or a parallel referral engine.

Implement a deterministic cross-cutting external-resource state in the existing permission/guide-graph architecture.

Minimum semantics:

```text
required_external_resource
resource_access_status
access_barrier
fallback_action
fallback_limit
unmet_external_need
retry_or_advocacy_trigger
handoff_state
```

Required behavior:

- distinguish `resource suggested` from `resource reachable`;
- distinguish `reachable` from `contact attempted`, `response received`, and `bridge/handoff`;
- represent unavailable, unaffordable, waitlisted, ineligible, unsafe, or guardian-blocked routes;
- stop repeating the same inaccessible referral;
- select the smallest reachable harm-reduction substitute;
- state that substitute's limits;
- preserve the original unmet external need in longitudinal state;
- do not convert access failure into noncompliance, resistance, poor motivation, or inner-parent deficit;
- do not claim contact or handoff the runtime did not perform.

## New black-box fixtures

Import `RQ9-01` through `RQ9-10`.

The model receives only the `query` field. Route, result, defect, and assertions are grader-only.

Total real-query fixture count after this batch:

```text
Batch 006: 16
Batch 007: 12
Batch 008: 11
Batch 009: 10
TOTAL: 49
```

## Saturation rule

Batch 009 is the final open-ended Mermaid architecture batch.

After the resource-unavailable patch:

- 10/10 cases fit maps 00–16;
- no map 17 is justified;
- future cases should be regression fixtures unless executable tests, qualified review, or real adverse-event evidence reveal a genuinely unrepresentable structural rule.

## Required tests

At minimum prove:

1. unavailable food/housing/medical care is not routed as motivation failure;
2. insurance coverage is not assumed to mean affordability;
3. a repeated unavailable referral is rejected;
4. a fallback states its limitations;
5. improved coping does not close an unmet external need;
6. `unknown` access does not become `reachable`;
7. minor/guardian access barriers remain explicit;
8. the bot does not fabricate local service availability or claim contact;
9. all 49 real-query fixtures pass at the expected operation level;
10. existing A001/H001 and longitudinal-safety tests do not regress.

## Comparative simplification

Continue testing maps 15 and 16 against simpler deterministic alternatives. The Batch 009 patch itself should remain a small cross-cutting state machine, not a new topical map.

## Boundary

No article edit. No clinical validation claim. No `stable` promotion without separate owner authorization.
