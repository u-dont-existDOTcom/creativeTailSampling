# Creative Tail Sampling

Durable workspace for the Creative Tail Sampling method and its findings.

The purpose of this repository is to prevent high-value exploratory reasoning from being lost in chat history and to make the method resumable from a canonical checkpoint.

## Canonical files

- [`PROTOCOL.md`](PROTOCOL.md) — the current Creative Tail Sampling protocol.
- [`FINDINGS.md`](FINDINGS.md) — compact canonical index of findings, provisional ideas, and the rejection frontier.
- [`MODEL.md`](MODEL.md) — explicit structural model, variables, feedback loops, falsifiers, and discriminating predictions.
- [`STATE.md`](STATE.md) — exact current frontier and resume instructions.
- [`runs/`](runs/) — immutable detailed tail-batch audits and recovered snapshots, including rejected candidates and why they failed.

## Operating rule

For future sessions, load `PROTOCOL.md`, `FINDINGS.md`, `MODEL.md`, and `STATE.md` before continuing. New substantive findings should be committed here as they are reached rather than left only in conversation history.

Every substantive tail batch should be saved under `runs/`, after which only genuine survivors are promoted into `FINDINGS.md`.

## Epistemic labels

- **SURVIVED** — passed the current novelty/coherence/consequence gates; still a hypothesis unless independently established.
- **PROMISING** — worth developing, but not yet through all gates.
- **REJECTED** — failed because it was obvious, incoherent, unrealistic, merely a renamed known concept, or otherwise did not meet the protocol.
- **RECOVERED** — reconstructed from surviving conversation context after an accidental deletion; wording may not be verbatim.

This repository separates *creative discovery* from *empirical verification*. Tail sampling is used to generate and develop propositions; evidence review is a later stage when required.
