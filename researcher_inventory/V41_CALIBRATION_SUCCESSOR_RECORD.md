# V41 Researcher Inventory Calibration Successor Record

Status: `CALIBRATION SUCCESSOR — CANDIDATE ENVIRONMENT ONLY`
Date: 2026-09-15
Predecessor: `RI-CONTRACT-V40`
Successor: `RI-CONTRACT-V41`
Evidence run: `34987375876`

## Behavioral basis

The V40 Case 2 calibration attempt passed the immutable archetype hash gate and deterministic apparatus checks, then failed hidden archetype evaluation. The pattern was not one local miss: the worker omitted multiple source-presented coordinates across PLACE, TIME, PERSON, OBJECT, LABEL, VERB, and LOCATOR while also admitting a smaller set of wrong or over-split candidates. Compound differences then cascaded from the incorrect unit ledger.

The general defect is therefore the V40 semantic admission threshold, not an archetype-storage or hash problem. Requiring a unit to fill a sufficiently distinct/indispensable binding role still suppresses source-presented coordinates that are nested, dependent, local, one-use, possessive/relational, or already contained in a broader binding.

V41 prospectively replaces that threshold with a source-coordinate-ledger plus linkage test. Worker-visible V41 instructions contain no gold rows, expected counts, case-specific evaluator findings, scored outputs, or holdout information.

## Separate Case 6 runtime finding

The V40 Case 6 attempt did not reach semantic evaluation. LABEL extraction exhausted retries after the model returned a `researcher_short_tag` containing wording not present in the exact coordinate/cue. The apparatus has a deterministic short-tag source-token guard and a deterministic unit test requiring synonym/non-source tag rejection. The durable contract likewise requires source-near tags and prohibits analyst/synonym wording.

Accordingly this V40 stop is preserved as a mechanical/worker-format failure, not as Case 6 semantic-resolution evidence and not as justification for weakening the validator. V41 makes the existing tag-token rule explicit in worker-visible durable instructions so the calibration can execute cleanly without changing hidden evaluator semantics.

## Retained controls

- V40 and run `34987375876` remain historical evidence.
- Case 2 and Case 6 archetype workbooks remain immutable and must pass their presidential SHA-256 gate before every use.
- Hidden evaluator findings never enter worker prompts.
- Calibration remains candidate-only.
- Sealed Case 5 remains closed until repeated Case 2 and Case 6 passes under one finalized successor contract.
- Holdout and clean-room one-shot rules remain unchanged.
- No Oval Office promotion and no APA-ID minting.
