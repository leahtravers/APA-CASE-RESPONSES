# V139 CALIBRATION CORRECTION RECORD

Status: `PROSPECTIVE SEMANTIC SUCCESSOR — CALIBRATION ONLY`  
Date: 2026-09-21  
Predecessor contract: `RI-CONTRACT-V138`  
Successor contract: `RI-CONTRACT-V139`  
Authority: Leah's standing Researcher Inventory calibration instruction  
Executive Registrar record: `APA-EXEC-2026-09-21-CASES-RI-V139-CAL-0001`

## Evidence reviewed

Latest completed calibration workflow before this correction:

- GitHub Actions run: `35597301001`
- Workflow: `Researcher Inventory Apparatus Verification`
- Head run commit: `ebd6c2b6c578a87ad70b7b8ab8b87446584e632e`
- Preserved-history commit: `df7b2ae519e99b7b69437ade1e9caa58c3b51639`
- Result: `FAILURE`
- Model: `gpt-5.6-sol`
- Contract: `RI-CONTRACT-V138`
- V138 contract SHA-256 reported by the run: `8f10c064f186cd4ce19af948b0f0b9a365198582d6199d6f855a26292c47cba3`
- Complete attempt preserved at: `calibration_history/researcher_inventory/35597301001-A1/`

For comparison, the immediately preceding V137 calibration attempt was run `35593385693` and is preserved under `calibration_history/researcher_inventory/35593385693-A1/`.

## Immutable archetype gate

Before semantic calibration, the V138 workflow directly hashed the repository workbook bytes and returned `VERIFIED`, with no repair required:

- `Case_2_Lightweight_Researcher_Inventory.xlsx` = `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- `Case_6_Lightweight_Researcher_Inventory_v2_with_Verbs_and_Locators.xlsx` = `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`

These remain immutable Leah-approved gold-standard archetypes. No archetype repair or semantic change is authorized or required.

## Harness determination

All 24 retained deterministic apparatus and prompt-harness tests passed before model calibration. The retained V126A contract-subordinate request envelope, V66 field alignment, V88A editor-shorthand alignment, and session-recovery mechanics showed no deterministic defect in V138.

Classification: `AGENT / DURABLE SEMANTIC CONTRACT DEFECT`, not `TEST-HARNESS DEFECT`.

No harness rule changes in V139.

## Generalized V138 failure pattern

V138 changed extraction from seven independent class passes to a shared representation ledger. The run shows that this architectural move made the **population admitted to the ledger itself too broad**. Treating every materially represented assertion/configuration as a precursor to extraction substitutes proposition completeness for lightweight Researcher Inventory selection.

The defect generalized across both approved archetypes:

1. **Assertion-to-row leakage:** source propositions that were genuinely represented but not independent worksheet coordinates survived because ledger admission treated representation as the principal floor.
2. **Surface-form typing leakage:** spatial-, temporal-, descriptive-, noun-, and verb-looking material could still become rows because an assertion/configuration supplied a plausible ledger role even when the source did not stage that span as the relevant class-native research coordinate.
3. **Structural under-resolution remains:** unnamed participant/occurrence positions and source-organized frames can still be missed when the model focuses on proposition content rather than the case's research-coordinate skeleton.
4. **Predicate overproduction remains dominant:** complete but non-inventory clause predicates, copular/support/reporting relations, and subordinate proposition relations can all look like valid ledger relations, producing a relation census rather than the archetypal relation spine.
5. **Referent/characterization instability remains:** some low-salience source-treated referents and source-applied handles are missed while other grammatically reifiable content/modifiers are admitted.
6. **Compound overproduction follows automatically:** one packet per materially represented assertion/configuration remains much broader than the gold-standard compound pattern, while missing primitives still cause missing bindings.

The comparative result did not justify another harness correction. V138 materially regressed Case 2 relative to V137 and did not resolve the broad Case 6 failure pattern. The error is the semantic selection architecture itself.

## V139 correction

`RI-CONTRACT-V139` replaces exhaustive representation-ledger projection with a **researcher-coordinate backbone**.

The successor keeps global source reading and cross-class reconciliation but adds these durable rules:

1. a represented assertion/proposition is not itself an admission criterion;
2. primitive membership requires an independently addressable class-native research role at lightweight worksheet grain;
3. lexical/grammatical form never establishes membership by itself;
4. lawful unnamed PLACE/TIME coordinates are structural exceptions derived from distinct staged positions/frames, not lexical tokens;
5. overlapping spans are typed by exact represented role, allowing a content referent and a larger orientation relation only when both roles are independently staged;
6. VERB extraction follows an admitted operative relation spine rather than all represented predicates;
7. compounds follow research-significant bindings among frozen coordinates rather than the set of all represented propositions;
8. a structural floor audit and anti-census ceiling audit operate against the researcher-coordinate backbone rather than a proposition ledger.

The correction is case-independent. It does not expose any gold row, expected count, evaluator finding, canonical archetype extract, or hidden case-specific answer to the worker.

## Historical integrity

V138 remains preserved with its contract, runtime wrapper, pipeline, correction record, workflow-run evidence, and complete failed attempt. V139 is prospective only. No predecessor output, failure, contract, or training history is deleted or rewritten.

The only existing forward-control file to be changed is `.github/workflows/researcher-inventory-contract-test.yml`, whose active pointers move prospectively from V138 to V139. Git history preserves its predecessor state.

## Holdout state

The sealed Case 5 holdout was not opened, fetched, or exposed in forming this correction. V139 must first pass Case 2 and Case 6 repeatedly under the same finalized contract and saved-agent lineage before the existing one-shot holdout gate may open. No correction may be made from sealed holdout output.