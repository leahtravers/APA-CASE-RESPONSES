# Researcher Inventory V156 Harness Correction Record

Status: `HARNESS CORRECTION — SEMANTICALLY NEUTRAL`  
Date: 2026-09-22  
Authority: Leah's standing Researcher Inventory calibration instruction  
Related failed run: `35707571998`  
Semantic contract successor: `RI-CONTRACT-V156`

## 1. Defect demonstrated

The V155 Case 6 calibration attempt ended in a runtime/session-retrieval failure rather than an evaluator semantic failure.

Observed evidence:

- immutable archetype verification passed;
- deterministic apparatus/harness tests passed;
- the Case 6 adapter failed with `RuntimeError: no final answer`;
- the recovery trace records three separate extraction session creations with no completed result record;
- the shared `final_answer()` implementation reads only one `/items` page (`limit=100`);
- `no final answer` is not classified as a transient result-read condition by the V92 recovery layer;
- after that exception, the inherited V55 wrapper deletes local recovery state, so outer apparatus retry may create a replacement semantic session.

This violates the recovery principle: reconcile the existing attempt before starting another.

## 2. Correction

V156 adds a semantically neutral result-retrieval shim that:

1. reads all available session-item pages in ascending order;
2. searches every page for completed assistant `final_answer` output;
3. when the session is terminal-success/idle but final-answer visibility is temporarily absent, waits and rereads the **same session** for a bounded interval;
4. if the result remains unavailable after that bounded interval, raises a timeout-class condition so the existing V92 same-session recovery logic preserves/reconciles the session instead of treating absence as an immediate semantic failure; and
5. never changes the worker prompt, semantic contract, source, archetype evaluator, primitive normalization, compound normalization, or holdout gates.

## 3. No semantic feedback injection

This correction does not supply the worker with:

- archetype rows;
- expected counts;
- evaluator findings;
- prior scored output;
- holdout source/output;
- case-specific semantic corrections.

It changes transport/result visibility only.

## 4. Verification requirement

A deterministic unit test must prove at minimum:

- a final answer on a later paginated item page is retrieved without creating a new session; and
- an initially absent final answer is reread on the same session before failure/recovery classification.

The next calibration workflow must preserve any failure and must not infer Case 6 semantic behavior unless a semantic candidate is actually returned and adjudicated.

## 5. Historical integrity

No V155 or earlier adapter is rewritten. V156 uses a new adapter and new recovery directory. Prior V155 runtime traces remain preserved.
