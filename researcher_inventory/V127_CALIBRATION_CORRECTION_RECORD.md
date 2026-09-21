# Researcher Inventory V127 Calibration Correction Record

Status: `PROSPECTIVE SUCCESSOR CORRECTION — CALIBRATION ONLY`  
Date: 2026-09-20  
Predecessor contract: `RI-CONTRACT-V126`  
Successor contract: `RI-CONTRACT-V127`  
Authority: Leah's standing Researcher Inventory calibration instruction  
Registrar: `APA-EXEC-2026-09-20-CASES-RI-V127-CAL-0001`

## Predecessor evidence

Workflow run `35547233935` executed V126 through the active V126A contract-subordinate request harness from commit `8d01ac9684e170b4aac180095db189f94329bd6b`. The run verified both immutable Leah-approved archetype workbooks at their required SHA-256 values, passed all 24 deterministic apparatus/harness tests before model execution, failed the paired Case 2 / Case 6 semantic comparison, preserved its complete candidate/training evidence under `calibration_history/researcher_inventory/35547233935-A1`, and committed that history at `770ca06a558444b90de30f90b8250d3b83584560`.

The holdout and clean-room stages were not reached.

## Independent harness check

Before revising the durable contract, the saved-agent boot path was checked separately.

`researcher_inventory/session_bootstrap.py` reads the exact `RI_CONTRACT_FILE`, computes its SHA-256, prepends only the bounded semantic-worker boot prefix, and performs a new `POST /agents` on every invocation. It writes the returned new agent ID to runtime state. `v126a_pipeline.sh` calls that bootstrap after clearing the run's transient result state and before archetype execution. It calls bootstrap again only after a successful calibrated-lineage holdout to create the clean-room agent.

Therefore the failed V126A run was not caused by reuse of a saved agent booted from an older durable contract. Together with the passed immutable-hash gate and passed 24 deterministic tests, no independent prompt-composition, stale-agent, evaluator, alignment, serialization, isolation, preservation, or holdout-gating defect is established for run `35547233935`.

## Defect classification

`WORKER-SEMANTIC / CONTRACT-GENERALIZATION DEFECT`

## Generalizable V126 defect

V126 correctly moved frame reconstruction ahead of lexical admission, but it still described several coordinate families through one broad `distinct binding role` test. The paired clean failure shows three source-general ambiguities remain:

1. **support node versus orientation relation** — explicit spatial/temporal wording was still sometimes emitted as PLACE/TIME when its actual job was a positional, recurrence, contextual, path, or other orienting relation; meanwhile differentiated local where/when frame nodes were under-reconstructed;
2. **scene evidence versus incidental scenery** — source-named concrete/sensory details that jointly establish a represented scene, condition, or contrast were pruned when they were not separately acted upon, even though they function as researcher-selectable OBJECT evidence;
3. **semantic relation versus grammatical predicate** — common copular, auxiliary, discourse, and lexical predicates were still over-admitted as independent VERB/LABEL coordinates after nodes were selected, while some reified content/state wording was mis-typed from surface grammar or spatial imagery.

These errors occur across materially different archetype sources and can be corrected without exposing any hidden answer, expected count, or case-specific example.

## V127 correction

V127 replaces the single broad role test with an explicit **binding-ledger projection**:

1. build the internal source-local binding ledger first;
2. assign every binding to its best source-established PLACE and TIME support identities before lexical extraction;
3. treat PLACE/TIME as frame-support nodes and LOCATOR as an orienting relation, including temporal orientation where appropriate;
4. project PERSON, OBJECT, and LABEL nodes before projecting VERB/LOCATOR relations;
5. admit source-named scene-defining evidence as OBJECT when those details instantiate the represented scene/condition/contrast, even if one-use and not separately acted upon;
6. admit VERB only when the operative relation itself remains necessary after the participating nodes/states/supports are known;
7. distinguish LABEL predication, OBJECT content/reification, LOCATOR orientation, and PLACE/TIME support by represented job rather than lexical shape;
8. perform support-node, scene-evidence, relation-austerity, and type-inversion audits before primitive freeze;
9. build compounds as the frozen projection of the already identified binding ledger.

## What is retained unchanged

V127 retains:

- the seven primitive classes;
- exact lexical preservation and source-span rules;
- class-local identity/coreference and canonical-ID ownership by code;
- immutable Case 2 / Case 6 workbook verification;
- V66 field-aware evaluator correction;
- V88A editor-shorthand alignment correction;
- V92 same-session transient recovery behavior;
- the V126A contract-subordinate request/compound harness correction;
- durable preservation of every attempt/failure;
- candidate-only / no-promotion / no-APA-ID boundaries;
- the diagnostic + repeated paired archetype gate;
- the single calibrated-lineage Case 5 holdout gate;
- retirement of the calibrated lineage after a successful first holdout;
- the brand-new saved-agent clean-room Case 5 certification gate.

## Isolation boundary

The V127 worker receives none of the Case 2 or Case 6 gold rows, expected counts, evaluator findings, scored predecessor outputs, canonical gold extracts, case-specific corrections/examples, sealed Case 5 material, or holdout output. This correction record is administrative evidence and is not supplied to the worker. The worker receives only the complete source, finalized V127 durable contract, contract-subordinate request envelope, response schema, and ordinary runtime metadata.

## Holdout boundary

Case 5 remains sealed and unattempted in this lineage. V127 must first pass one paired diagnostic and both required repeated paired verification batches under the same finalized V127 contract and saved-agent lineage. Only then may that lineage access Case 5 exactly once. If it passes, that agent is retired and a brand-new saved agent bootstrapped only from finalized V127 instructions must pass the sealed holdout in a fresh session for certification.

## Historical integrity

V126, V126A, every earlier contract/harness correction, every workflow run, candidate, finding, recovery artifact, and preserved failure remain intact. V127 controls only prospective calibration after the workflow is explicitly routed to it.
