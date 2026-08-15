# Creative Tail Sampling

Durable workspace for the Creative Tail Sampling method and its findings.

The purpose of this repository is to prevent high-value exploratory reasoning from being lost in chat history and to make the method resumable from a canonical checkpoint.

## Canonical files

- [`PROTOCOL.md`](PROTOCOL.md) — the current Creative Tail Sampling protocol.
- [`FINDINGS.md`](FINDINGS.md) — findings, rejected candidates, and current hypotheses.
- [`STATE.md`](STATE.md) — exact current frontier and resume instructions.

## Operating rule

For future sessions, load these files before continuing. New substantive findings should be committed here as they are reached rather than left only in conversation history.

## Epistemic labels

- **SURVIVED** — passed the current novelty/coherence/consequence gates; still a hypothesis unless independently established.
- **PROMISING** — worth developing, but not yet through all gates.
- **REJECTED** — failed because it was obvious, incoherent, unrealistic, merely a renamed known concept, or otherwise did not meet the protocol.
- **RECOVERED** — reconstructed from surviving conversation context after an accidental deletion; wording may not be verbatim.

This repository separates *creative discovery* from *empirical verification*. Tail sampling is used to generate and develop propositions; evidence review is a later stage when required.
