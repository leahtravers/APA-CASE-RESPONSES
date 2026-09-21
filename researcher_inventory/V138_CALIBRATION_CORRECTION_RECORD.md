# V138 CALIBRATION CORRECTION RECORD

Status: `PROSPECTIVE SEMANTIC SUCCESSOR — CALIBRATION ONLY`
Date: 2026-09-21
Predecessor contract: `RI-CONTRACT-V137`
Successor contract: `RI-CONTRACT-V138`
Authority: Leah's standing Researcher Inventory calibration instruction

## Evidence reviewed

Latest completed calibration workflow before this correction:

- GitHub Actions run: `35593385693`
- Workflow: `Researcher Inventory Apparatus Verification`
- Result: `FAILURE`
- Model: `gpt-5.6-sol`
- Contract: `RI-CONTRACT-V137`
- V137 contract SHA-256 reported by the run: `a653749a4d4a07b7459b49e302647124e671a8d0bdc1f2f9cfd3dbdc75f6eb3d`
- Complete attempt preserved at: `calibration_history/researcher_inventory/35593385693-A1/`
- Preservation/base commit: `f1319f89d5253f73693ffdbc80cbc509b93280bc`

## Immutable archetype gate

Before semantic calibration the workflow directly hashed the repository workbook bytes and returned `VERIFIED`, with no repair required:

- `Case_2_Lightweight_Researcher_Inventory.xlsx` = `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- `Case_6_Lightweight_Researcher_Inventory_v2_with_Verbs_and_Locators.xlsx` = `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`

These remain immutable Leah-approved gold-standard archetypes.

## Harness determination

All 24 retained deterministic apparatus and prompt-harness tests passed before model calibration. The V126A contract-subordinate request envelope, V66 field alignment, V88A editor-shorthand alignment, and session-recovery mechanics showed no deterministic defect in V137.

Classification: `AGENT / DURABLE SEMANTIC CONTRACT DEFECT`, not `TEST-HARNESS DEFECT`.

No harness rule changes in V138.

## Generalized V137 failure pattern

V137 tightened primitive admission around `distinct represented jobs`, but still instructed the worker to run a complete raw-source pass for every primitive class. That construction architecture left seven separate opportunities to re-parse wording without a shared representation model.

The paired-archetype failures generalized into the same durable families:

1. **Independent class harvesting / census leakage:** lexical or grammatical candidates could survive because each class restarted from raw wording rather than from a single source representation.
2. **Structural-coordinate omission:** unnamed occurrence/participant/referent positions and episode frames could be missed because their role emerges from the source's represented configuration rather than an explicit class-looking token.
3. **Predicate fragmentation:** one represented relation could be split into control/support/modal/aspectual/infinitival/embedded pieces even when those pieces jointly form one worksheet-grain relation identity.
4. **Referent/characterization instability:** source-treated content and characterization roles could be inconsistently retained because they were assessed outside the assertion/configuration in which the source staged them.
5. **Compound cascade:** primitive fragmentation/overproduction generated excessive packets while primitive omission removed source bindings.

The failure is not case-specific and justifies a prospective durable-contract successor.

## V138 correction

`RI-CONTRACT-V138` requires a **representation-ledger projection** architecture:

1. read the whole source;
2. form one source-order internal ledger of materially represented assertions/configurations and structural frames;
3. freeze that ledger;
4. project all seven primitive classes from the roles those source-staged items play in the same ledger;
5. use a complete minimal predicate kernel that preserves one relation identity rather than grammatical fragments;
6. perform floor review against ledger coverage and ceiling review against lexical/grammar leakage;
7. freeze primitives;
8. build compounds only for materially distinct frozen-ledger assertions/configurations, never recursive/transitive closure.

PLACE/TIME are structural positions/frames used by represented material, not spatial/temporal word inventories. PERSON/OBJECT/LABEL/LOCATOR likewise require class-native roles in the shared ledger. Exact lexical and posture preservation remains mandatory.

No hidden archetype semantics, row counts, evaluator feedback, scored outputs, or holdout material enter the durable worker instructions.

## Historical integrity

V137 remains preserved with its full run evidence. V138 is prospective only. No prior contract, output, failure, or score is deleted or rewritten.

Executive Registrar record: `APA-EXEC-2026-09-21-CASES-RI-V138-CAL-0002`. Its predecessor `...0001` was abandoned before authorization/submission after an inaccurate version-evidence label in stage 1; that predecessor remains preserved without operational effect.

## Holdout state

The sealed Case 5 holdout was not opened, fetched, or exposed for this correction. V138 must first pass Case 2 and Case 6 repeatedly under the same finalized contract and saved-agent lineage before the existing one-shot holdout gate may open. No correction may be made from sealed holdout output.
