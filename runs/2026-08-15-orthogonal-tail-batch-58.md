# Orthogonal Tail Batch 58 — Collection-Scene Privacy / Shoulder-Surfing in Small Communes

Date: 2026-08-15

## Trigger

Owner correction:

> Even if the survey itself is nominally private, someone can simply walk in while a member is filling it out, glance at the paper/screen, or see what was written while the member gets up for a snack.

## Outcome

**No Creative Tail survivor.**

The root mechanisms are ordinary physical privacy, shoulder-surfing, unattended-device/document exposure, visual privacy and observational disclosure. The communal application is foundational because co-residence makes these events unusually plausible and can destroy confidence in all later confidentiality guarantees.

The privacy architecture must therefore add a fifth independent layer:

> **Collection-scene privacy: can another person observe the response while it is being created or before it enters the protected data path?**

---

# B58-L01 — Treat the physical collection scene as part of the privacy protocol

A cryptographically protected backend is irrelevant if another resident can read the answer over the respondent's shoulder before submission.

Audit:
- room privacy;
- shared devices;
- people walking through;
- unattended forms/screens;
- printer/scanner handling;
- saved browser state;
- notification previews;
- screen reflections/visibility;
- paper disposal.

## B58-L02 — Do not require completion in common spaces

Sensitive modules should not be designed for:
- dining halls;
- common offices;
- shared computer rooms;
- group meetings;
- supervised survey sessions.

Provide a genuinely private option.

## B58-L03 — Support pause-and-lock safely

Members may need to stop mid-survey.

Digital design should:
- hide answers when app/browser loses focus where practical;
- provide quick screen blank/lock;
- require reauthentication to resume sensitive modules;
- avoid showing previous answers on an obvious summary page;
- not leave plaintext drafts in shared browser history/autofill/local storage unnecessarily.

Do not make recovery so cumbersome that people abandon the survey.

## B58-L04 — Paper surveys need sealed custody from the moment of completion

If paper is unavoidable:
- fixed-choice response format where possible;
- opaque envelope immediately after completion;
- no completed form left unattended;
- no local leader collection/inspection;
- sealed batch transfer to independent custody;
- secure destruction after digitization where policy permits.

## B58-L05 — Shared-device mode needs special design

A shared tablet/laptop can leak through:
- browser back button;
- autofill/history;
- cached pages;
- screenshots;
- download folders;
- saved passwords;
- OS recent-items lists.

Use a kiosk/private mode designed for the threat model, not ordinary web browsing assumptions.

## B58-L06 — Minimize visible sensitive wording on screen

Someone glancing briefly should not be able to infer the respondent's answer from a large highlighted selection or summary.

Possible controls:
- neutral option layout;
- no persistent colored answer summary;
- quick advance after selection;
- privacy screen filter on shared hardware where useful.

Do not sacrifice accessibility/readability without testing.

## B58-L07 — Participation timing itself can expose the respondent

If only one member is absent from dinner for a `confidential interview`, privacy has already partly failed.

Use:
- broad completion windows;
- private remote/off-site options;
- ordinary-looking multipurpose research access;
- no local participation attendance sheet for sensitive modules.

## B58-L08 — The research center should not ask respondents to create dangerous local artifacts

Avoid requiring members to:
- write accusations in notebooks kept locally;
- save narratives to shared drives;
- print sensitive forms;
- email raw answers through community-controlled accounts.

Route sensitive data directly into independent/non-custodial systems.

## B58-L09 — Add collection-scene questions to the reporting-pressure battery

After sensitive modules ask, where appropriate:
- `Were you alone while answering?`
- `Could anyone see your screen/paper?`
- `Did anyone enter or interrupt you?`
- `Did you leave the form/screen unattended?`
- `Did anyone ask what you answered?`

Do not treat an affirmative answer as respondent fault; use it to qualify confidentiality and mode validity.

## B58-L10 — Offer a safe re-answer route after observed exposure

If a respondent believes someone saw their answers, allow them to:
- invalidate the prior submission if technically possible;
- retake privately;
- contact the independent research custodian;
- flag the record as potentially disclosure-affected.

Avoid maintaining two conflicting responses without version/provenance handling.

## B58-L11 — Do not expose who used the privacy-enhanced option

If only dissatisfied members choose the `private room` or `anonymous tablet`, using the privacy feature becomes a signal.

Make the private mode routine/available to everyone rather than an exceptional distress channel.

## B58-L12 — Shoulder-surfing risk interacts with face-saving

One observed or rumored privacy breach can change future behavior even for people whose responses were never actually seen.

Therefore track:
- privacy incidents;
- member confidence after incidents;
- survey-mode effects before/after incidents.

## B58-L13 — Collection privacy and response-fingerprint privacy are different

A person can complete the survey entirely alone yet later be identified from writing style/story (Batch 57).

Conversely, a perfectly non-identifying fixed-choice form can still be exposed by someone looking at the screen while it is filled out.

Both layers must pass.

## B58-L14 — Collection privacy can be the binding constraint in co-residential life

In ordinary population surveys, respondents often have natural private spaces. In tightly shared communal housing, privacy may be scarce by design.

Research protocols should therefore ask about **actual available private space** rather than assume it exists.

---

# Revised communal research privacy stack

1. **Participation privacy** — can locals tell who participated?
2. **Collection-scene privacy** — can anyone observe the answer while it is being created or left unattended? (Batch 58)
3. **Input confidentiality** — who can inspect raw submitted answers? (C024)
4. **Response-fingerprint privacy** — can handwriting, prose, voice or context identify the author? (Batch 57)
5. **Output/composition privacy** — can released aggregates reconstruct the answer? (C023)

A sensitive survey can solve four of these and still fail through the fifth.

---

## Disposition

No Creative Tail survivor.

Foundational practical rule:

> **Privacy starts before submission. In co-residential communities, design the physical/digital completion scene so a member can answer, pause, leave, and submit without another resident being able to glance at, recover, or infer the response.**
