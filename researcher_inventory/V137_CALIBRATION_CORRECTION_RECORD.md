# V137 CALIBRATION CORRECTION RECORD

Status: `PROSPECTIVE SEMANTIC SUCCESSOR — CALIBRATION ONLY`
Date: 2026-09-21
Predecessor contract: `RI-CONTRACT-V136`
Successor contract: `RI-CONTRACT-V137`
Authority: Leah's standing Researcher Inventory calibration instruction

## Evidence reviewed

Latest completed calibration workflow before this correction:

- GitHub Actions run: `35590164740`
- Workflow: `Researcher Inventory Apparatus Verification`
- Head before preserved-history commit: `3ea794d43cfa82726304630cbf631cbe6f1d705e`
- Result: `FAILURE`
- Model: `gpt-5.6-sol`
- Contract: `RI-CONTRACT-V136`
- Contract SHA-256 reported by the run: `a713a93d33c555154fc0e17806e4225e70b48c66d8f7e062cd272a250cc0e27c`

The run preserved its complete attempt under `calibration_history/researcher_inventory/35590164740-A1/` and pushed that history to main in commit `830e2bd0e5bd2087c42529d24fa49efe808d2473`.

## Immutable archetype gate

Before semantic calibration, the workflow directly hashed the repository workbook bytes and returned `VERIFIED`, with no repairs:

- `Case_2_Lightweight_Researcher_Inventory.xlsx` = `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- `Case_6_Lightweight_Researcher_Inventory_v2_with_Verbs_and_Locators.xlsx` = `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`

These remain immutable gold-standard archetypes.

## Harness determination

All 24 retained deterministic apparatus and prompt-harness tests passed before model calibration. The retained V126A contract-subordinate request envelope, V66 field alignment, V88A editor-shorthand alignment, and session-recovery mechanics therefore showed no deterministic defect in this run.

Classification: `AGENT / DURABLE SEMANTIC CONTRACT DEFECT`, not `TEST-HARNESS DEFECT`.

No harness rule is changed by V137.

## Generalized V136 failure pattern

V136 improved the balance between sparse graphing and lexical census, but its phrase `researcher-selectable source coordinate` remained too permissive. The model could treat almost any locally meaningful wording as selectable merely because it was source-established, while also omitting low-salience coordinates whose importance came from their represented worksheet job rather than lexical salience.

Across both approved archetypes the failures generalized into the same families:

1. **Surface-form typing:** spatial-looking or descriptive wording was sometimes typed by lexical appearance rather than its represented job.
2. **Episode/position under-resolution:** unnamed occurrence positions and source-organized episode frames were omitted because they lacked explicit place/time nouns.
3. **Referent under-resolution:** low-salience concrete and abstract source-treated things were omitted when they nonetheless participated as distinct referents/content.
4. **Characterization instability:** ordinary modifiers were over-admitted while some questioned, rejected, corrected, or relation-bearing characterizations were omitted.
5. **Predicate census:** auxiliaries/support/copulas and subordinate verb tokens were over-admitted while some complete modal/state relation kernels were omitted.
6. **Locator instability:** merely spatial-sounding wording was over-admitted while some actual orientation/context relations were omitted.
7. **Lexical normalization:** at least one source-native expression was normalized to a synonym, violating the literal lock.
8. **Compound explosion and omission:** primitive over/under-resolution cascaded into both excessive assertion packets and missing source bindings.

These are durable, case-independent rule failures. They justify a prospective contract successor.

## V137 correction

`RI-CONTRACT-V137` replaces the permissive selectability test with a four-part **distinct represented job** gate:

- source establishment;
- class-native representation job;
- independent addressability at lightweight worksheet grain;
- natural-grain identity/deduplication.

It then supplies tighter class boundaries, a strict literal/posture lock, explicit floor and ceiling audits, and a selective compound-admission test. The target is neither maximum lexical density nor global-necessity sparsity.

## Historical integrity

V136 remains preserved with its complete run evidence. V137 is prospective only. No prior output, score, failure, or contract text is deleted or rewritten.

## Holdout state

The sealed Case 5 holdout was not opened or exposed for this correction. V137 must first pass the approved Case 2 and Case 6 archetypes repeatedly under the same finalized contract and saved-agent lineage before the one-shot holdout gate can open.
