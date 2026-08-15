# Orthogonal Tail Batch 57 — Structural Non-Anonymity in Small Communes

Date: 2026-08-15

## Trigger

Owner correction:

> In small communes there may effectively be no true survey anonymity. Other members can identify respondents from handwriting, phrasing, way of speaking, unique stories, or simply knowing who participated.

## Outcome

**No Creative Tail survivor.**

The root mechanisms are established:
- deductive disclosure / internal confidentiality in small connected communities;
- quasi-identifier re-identification;
- stylometric authorship attribution;
- qualitative research confidentiality limitations;
- handwriting/voice/behavioral identifiers.

The practical consequence is foundational enough to revise the communal research architecture:

> **For sensitive research in small communes, assume local re-identification is possible unless the data path makes it impossible for local actors to ever see person-level expressive responses. Do not promise anonymity merely because names are absent.**

---

# Source-domain boundary

Research ethics literature on small connected communities explicitly warns that participants can be identified through combinations of contextual details even when names are removed (`deductive disclosure` / `internal confidentiality`).

Survey/research ethics guidance likewise warns that small populations and combinations of demographic fields can identify people.

Stylometry research demonstrates that nominally anonymous text can be attributed to an author based on writing style. Modern authorship-attribution systems treat lexical, syntactic and stylistic features as identifying signals.

Open-text fields therefore create a qualitatively different privacy risk from fixed-choice data.

**Disposition: root theory known; no novelty promotion.**

---

# Practical architecture

## B57-L01 — Stop calling sensitive small-commune surveys anonymous by default

Use precise terms:
- `confidential`;
- `non-custodial` where C024 applies;
- `locally unlinkable by design` only if technically true;
- `aggregate-only output` where appropriate.

If re-identification cannot reasonably be excluded, consent materials should say so.

## B57-L02 — Treat expressive response channels as identifying

For sensitive topics, assume these may identify the respondent:
- handwriting;
- free-text prose;
- spelling/grammar;
- characteristic phrases;
- voice/audio;
- unique anecdotes;
- highly specific chronology;
- device/account metadata;
- completion timestamp;
- unusual demographic combinations.

## B57-L03 — Prefer structured fixed-choice items for routine sensitive measurement

Where the research question allows, use:
- categorical choices;
- bounded numerical scales;
- randomized/indirect response methods;
- standardized vignettes;
- encrypted/secure aggregation.

This reduces stylistic fingerprinting compared with open narrative responses.

## B57-L04 — Do not collect handwriting for sensitive routine surveys

Paper forms can be identifiable through handwriting and physical handling.

If paper is necessary for accessibility:
- use machine-readable fixed-choice marks rather than freehand prose;
- physically mix forms before custody;
- ensure local leadership cannot inspect completed forms;
- transfer them directly to independent research custody.

## B57-L05 — Open-text responses need a different privacy regime

When qualitative detail is genuinely necessary:
- collect it through independent external researchers;
- keep raw text/audio inaccessible to local leaders and ordinary federation staff;
- treat raw narrative as identifiable/confidential microdata;
- publish only carefully transformed/synthesized content when safe;
- obtain separate consent for verbatim quotation.

## B57-L06 — Verbatim quotes should be presumed locally attributable

In a small commune, another member may recognize:
- phrase choice;
- story;
- event;
- worldview;
- role-specific knowledge.

Prefer semantic summaries or pooled thematic reporting for sensitive material unless the participant explicitly accepts attribution risk.

## B57-L07 — Paraphrasing reduces but does not eliminate identification risk

A transformed quote can still identify through unique facts/context.

Before publication ask:
- could an insider infer the speaker from the event?
- does the quote reveal a unique role/relationship?
- does combination with other published data isolate the person?

Connect to C023 cumulative release review.

## B57-L08 — Separate participation privacy from answer privacy

Even if answers are protected, people may know who participated because:
- they saw someone filling the survey;
- the participant disappeared for an interview;
- devices/rooms are shared;
- leaders distribute survey links individually.

Research design should reduce both where possible:
- private universal access windows;
- off-site/mobile completion;
- no local attendance list for optional sensitive modules;
- independent participant contact.

## B57-L09 — Randomize or blur timing metadata where feasible

Do not expose exact completion timestamps to local/community analysts when they can be linked to observed behavior.

Batch/group transmission can reduce timing inference.

## B57-L10 — Avoid unnecessary demographic cross-tabs

In an eight-person commune, `female + parent + age 42–50 + treasurer` may equal one known individual.

Collect only needed demographics, and publish at broader pooled scopes.

## B57-L11 — C024 becomes more important for closed-ended sensitive data

Non-custodial secure aggregation can make fixed-choice sensitive responses useful at federation scale without local or central plaintext custody.

It cannot protect open-ended narratives from stylometric/contextual identification if those narratives are ever exposed.

## B57-L12 — Qualitative insight may require honest confidentiality rather than fake anonymity

Some questions cannot be answered well without narrative context.

The ethical solution can be:
- explicit confidentiality limits;
- independent custody;
- restricted researcher access;
- no local raw-data disclosure;
- publication with aggressive deductive-disclosure review.

Do not destroy the research question merely to retain the word `anonymous`.

## B57-L13 — Use outsider coding before local/federation access

For sensitive narrative material, an independent research team can convert raw responses into:
- coded categories;
- themes;
- standardized incident descriptors;
- aggregate counts.

The commune/federation can receive the coded layer without raw expressive text when sufficient.

Coder access remains a confidentiality relationship and needs governance.

## B57-L14 — Automated text rewriting is not a guaranteed anonymizer

Stylometric obfuscation/rephrasing research exists, but semantic details can still identify the person and transformations can distort meaning.

Do not promise anonymity because an LLM paraphrased the text.

## B57-L15 — Privacy confidence must be measured under the actual design

Batch 43/44 should ask not merely `is this survey anonymous?` but:
- `could other members recognize your phrasing/story?`;
- `could anyone see when/how you completed it?`;
- `do you believe local leadership can access raw responses?`;
- `would you answer differently if no person ever saw your raw text?`.

## B57-L16 — Local re-identification risk should determine the allowed response format

Possible policy:

### Very small N / high sensitivity
- no local open-text publication;
- closed-ended secure aggregation;
- qualitative interview only under independent confidential custody;
- federation-pooled output.

### Larger N / lower sensitivity
- carefully reviewed open text may be possible;
- still apply deductive-disclosure and C023 composition checks.

---

# Architectural revision

The communal research privacy stack now needs four distinct concepts:

1. **Participation privacy:** can locals tell who participated?
2. **Input confidentiality:** who can inspect raw answers? (C024)
3. **Response fingerprint privacy:** can the answer itself identify the author? (Batch 57)
4. **Output/composition privacy:** can aggregate publications reconstruct a person's answer? (C023)

A system can solve any three and still fail on the fourth.

---

## Disposition

No Creative Tail survivor.

Foundational practical rule:

> **In very small communes, assume expressive responses are identifiable to insiders. Use fixed-choice/non-custodial aggregate methods for routine sensitive measurement, reserve qualitative material for independently custodied confidential research, and never promise anonymity merely because names were removed.**
