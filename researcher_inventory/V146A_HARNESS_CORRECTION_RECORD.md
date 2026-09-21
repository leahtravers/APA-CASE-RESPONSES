# Researcher Inventory V146A Harness Correction Record

Status: `ACTIVE HARNESS SUCCESSOR FOR V146 CALIBRATION — SEMANTIC CONTRACT UNCHANGED`  
Date: 2026-09-21  
Semantic contract retained: `researcher_inventory/AGENT_CONTRACT_V146.md` / `RI-CONTRACT-V146`  
Harness predecessor: retained V126A per-class request topology through `inventory_apparatus.py`  
Harness successor: `researcher_inventory/v146a_relation_first_harness.py`  
Authority: Leah's standing Researcher Inventory calibration instruction

## 1. Evidence gate

GitHub Actions run `35652026270` completed `FAILURE` under V146. Before model calibration it directly verified both Leah-approved workbook copies byte-for-byte and required no repair:

- Case 2 SHA-256: `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- Case 6 SHA-256: `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`

All 24 retained deterministic apparatus/harness tests passed. The failed attempt remains preserved at `calibration_history/researcher_inventory/35652026270-A1/`.

## 2. Harness defect

V146 changed the durable construction topology to:

`represented frames -> one source-native relation ledger -> functional primitive slots -> identity reconciliation -> frozen primitives -> compounds`

The inherited apparatus did not implement that topology. `inventory_apparatus.py` still submitted seven independent `_extract_class` requests concurrently through `ThreadPoolExecutor`. Each request invoked the model adapter independently and returned only one primitive class. Only after those independent semantic passes completed did code combine classes and ask separately for compounds.

The retained V126A request envelope correctly removed contradictory legacy semantic directives, but it did not change this per-class runtime topology. Existing tests verified request subordination and deterministic mechanics, not the whole-source V146 construction topology.

This is a harness/runtime defect, not a basis for another semantic-contract amendment.

## 3. V146A correction

V146A replaces only the semantic request topology used for V146 calibration. The successor harness:

1. sends the complete source to the saved V146 worker once;
2. requires the worker, under V146 alone, to execute the full relation-first construction order internally;
3. receives all seven primitive classes and compound membership together in one JSON response;
4. validates source-derived primitive fields mechanically against the source;
5. performs same-class alias/coreference merge and deterministic ordering;
6. assigns canonical apparatus IDs only after primitive validation;
7. maps compound members from returned `(class, canonical_key)` pairs to code-owned IDs;
8. rejects unknown, ambiguous, or sub-two-member compound references; and
9. preserves deterministic `_Q`, compound ordering, SQL shaping, evaluator comparison, retry, persistence, and candidate-only behavior.

The worker still receives no archetype rows, expected counts, evaluator findings, scored predecessor outputs, canonical gold extracts, case-specific hidden corrections, or holdout material.

## 4. Retained controls

V146A does not change any V146 semantic admission, typing, lexical-preservation, relation, frame, primitive, or compound rule; V66/V88A evaluator alignment; immutable workbook verification; candidate-only storage; failure-history preservation; saved-agent bootstrap; sealed holdout isolation; repeated Case 2/Case 6 pass requirements; one-shot holdout; fresh-agent clean-room certification; or the prohibition on Oval Office promotion, APA-ID minting, and APA database/fabric mutation.

## 5. Forward-control boundary

The V126A contract-subordinate prompt principle remains retained. The inherited **parallel per-class semantic extraction topology** is `PARTIALLY SUPERSEDED FOR V146 FORWARD CALIBRATION — 2026-09-21` by V146A. Predecessor files remain unchanged as historical evidence. `RI-CONTRACT-V146` remains the controlling semantic contract and is not superseded by this harness correction.

## 6. Evaluation rule after correction

The next V146A run must first pass deterministic harness tests and immutable workbook verification. Only model behavior observed under the corrected V146A topology may be used to determine whether V146 itself still has a generalizable semantic defect. A remaining mismatch may justify a later durable semantic successor only if the evidence is cross-case/generalizable and not explainable by harness mechanics.

## 7. Holdout state

The sealed Case 5 holdout remains closed. No Case 5 source, answer, score, or derivative example was used to create this correction.
