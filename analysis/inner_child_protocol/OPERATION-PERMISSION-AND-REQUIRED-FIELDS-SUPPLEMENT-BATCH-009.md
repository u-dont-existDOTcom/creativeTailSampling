# Operation-permission and required-fields supplement — Batch 009

Date: 2026-08-18

## New cross-cutting fields

```text
required_external_resource
resource_access_status:
  reachable_now
  reachable_later
  waitlisted
  unaffordable
  ineligible
  geographically_unavailable
  unsafe_to_access
  blocked_by_guardian_or_authority
  unknown
access_barrier
access_attempts_known
fallback_action
fallback_limit
unmet_external_need
retry_or_advocacy_trigger
handoff_state:
  suggested
  reachable
  attempted
  response_received
  bridged
  unavailable
  failed
  unknown
```

## Permission consequence

When an operation requires an external resource or condition that is unavailable:

1. the required operation does not become permitted merely because the bot can describe it;
2. the bot may select only a bounded fallback whose prerequisites are present;
3. the fallback must state its limits;
4. the original external need remains active;
5. internal coping cannot mark the external need resolved;
6. repeated referral to the same inaccessible route is prohibited unless access conditions changed.

## Unknown semantics

`resource_access_status = unknown` requires one of:

- verify access;
- ask the minimum missing question;
- choose a fallback that does not assume availability;
- preserve the need without claiming a handoff.

## Saturation policy

No additional conceptual fields should be added from anecdotal cases unless an executable failure demonstrates that existing fields cannot represent the necessary distinction.
