# Creative Tail Sampling

Durable workspace for the Creative Tail Sampling method and its findings.

The purpose of this repository is to prevent high-value exploratory reasoning from being lost in chat history and to make the method resumable from a canonical checkpoint.

## Canonical files

- [`PROTOCOL.md`](PROTOCOL.md) — the current Creative Tail Sampling protocol.
- [`FINDINGS.md`](FINDINGS.md) — compact canonical index of findings, provisional ideas, and the rejection frontier.
- [`MODEL.md`](MODEL.md) — explicit structural model, variables, feedback loops, falsifiers, and discriminating predictions.
- [`STATE.md`](STATE.md) — exact current frontier and resume instructions.
- [`runs/`](runs/) — immutable detailed tail-batch audits and recovered snapshots, including rejected candidates and why they failed.

## Active inner-child / reparenting therapy-protocol workspace

The inner-child project now has a protocol-first operational architecture intended for eventual therapy-bot use. For that lane, after resolving current GitHub heads, read:

1. [`analysis/inner_child_protocol/STATE.md`](analysis/inner_child_protocol/STATE.md)
2. **[`analysis/inner_child_protocol/THERAPY-PROTOCOL-OVERVIEW.md`](analysis/inner_child_protocol/THERAPY-PROTOCOL-OVERVIEW.md)** — canonical therapy Mermaid control surface
3. the focused drill-down maps under [`analysis/inner_child_protocol/maps/`](analysis/inner_child_protocol/maps/)
4. [`analysis/inner_child_protocol/ARTICLE-PROTOCOL-CROSSWALK.md`](analysis/inner_child_protocol/ARTICLE-PROTOCOL-CROSSWALK.md)
5. [`analysis/inner_child_protocol/PROTOCOL-GAP-LEDGER.md`](analysis/inner_child_protocol/PROTOCOL-GAP-LEDGER.md)
6. [`analysis/inner_child_protocol/CANDIDATE-STATUS-LEDGER.md`](analysis/inner_child_protocol/CANDIDATE-STATUS-LEDGER.md)
7. [`analysis/inner_child_protocol/EVIDENCE-LEDGER.md`](analysis/inner_child_protocol/EVIDENCE-LEDGER.md)

Dedicated recovery packet:

- [`docs/INNER-CHILD-THERAPY-PROTOCOL-FRESH-CONVERSATION-HANDOFF.md`](docs/INNER-CHILD-THERAPY-PROTOCOL-FRESH-CONVERSATION-HANDOFF.md)

For this lane, Mermaid maps are living operational control surfaces, not article outlines. Material protocol changes must update the map topology in the same change. The article remains a separate explanatory artifact and should not be silently edited from protocol research.

## Operating rule

For future sessions, load `PROTOCOL.md`, `FINDINGS.md`, `MODEL.md`, and `STATE.md` before continuing. New substantive findings should be committed here as they are reached rather than left only in conversation history.

Every substantive tail batch should be saved under `runs/`, after which only genuine survivors are promoted into `FINDINGS.md`.

## Epistemic labels

- **SURVIVED** — passed the current novelty/coherence/consequence gates; still a hypothesis unless independently established.
- **PROMISING** — worth developing, but not yet through all gates.
- **REJECTED** — failed because it was obvious, incoherent, unrealistic, merely a renamed known concept, or otherwise did not meet the protocol.
- **RECOVERED** — reconstructed from surviving conversation context after an accidental deletion; wording may not be verbatim.

This repository separates *creative discovery* from *empirical verification*. Tail sampling is used to generate and develop propositions; evidence review is a later stage when required.
