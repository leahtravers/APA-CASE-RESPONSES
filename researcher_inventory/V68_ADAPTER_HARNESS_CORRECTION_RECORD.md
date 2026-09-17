# V68 Adapter Harness Correction Record

Status: `BOUNDED HARNESS / TRANSPORT CORRECTION`  
Date: 2026-09-17  
Authority: Leah's standing Researcher Inventory calibration instruction

## Triggering attempt

Workflow run `35215377518` preserved the first V68 attempt. Immutable workbook verification and deterministic apparatus tests passed, but calibration failed before any candidate output because `v68_openai_agents_adapter.py` imported `researcher_inventory.v60_openai_agents_adapter` while being executed as a file path from inside the package directory. Python therefore could not resolve the package root and raised `ModuleNotFoundError: No module named 'researcher_inventory'`.

## Classification

`TEST-HARNESS / ADAPTER ROUTING DEFECT`.

This failure provides no evidence about V68 worker semantics. Do not revise `RI-CONTRACT-V68` from this attempt.

## Correction

Restore the proven V67 adapter loading pattern: import sibling `v60_openai_agents_adapter` directly, bind `prior.base.CONTRACT_VERSION` to V68, and point the proven recovery implementation to `runtime/v68_session_recovery`.

The failed adapter file remains reconstructable through Git history and run `35215377518`; the run's failure evidence remains preserved in calibration history.
