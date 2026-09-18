# V82 Harness Durability Correction — Workflow Attempt Preservation

Status: `BOUNDED HARNESS / EVIDENCE-PRESERVATION CORRECTION`  
Date: 2026-09-18  
Authority: Leah's standing Researcher Inventory calibration instruction  
Semantic contract: `RI-CONTRACT-V82` unchanged by this correction  
Executive Registrar record: `APA-EXEC-2026-09-18-CASES-RI-V82-CAL-0001`

## Defect class

`TEST-HARNESS / EVIDENCE-DURABILITY DEFECT`

The live workflow previously wrote durable run evidence under:

`calibration_history/researcher_inventory/${GITHUB_RUN_ID}`

GitHub workflow re-runs preserve the same `GITHUB_RUN_ID` while incrementing `GITHUB_RUN_ATTEMPT`. A later attempt could therefore replace the visible branch copy of files from an earlier attempt inside the same directory even though Git history still retained prior commits.

That is inconsistent with the standing requirement to preserve every attempt and failure as directly inspectable training history wherever possible.

## Correction

Prospectively, durable history uses:

`calibration_history/researcher_inventory/${GITHUB_RUN_ID}-A${GITHUB_RUN_ATTEMPT}`

Each GitHub Actions attempt therefore receives a distinct create/update namespace at the workflow-history level.

## Boundaries

This correction does not change:

- worker instructions or Researcher Inventory semantics;
- archetype workbooks or canonical extracts;
- evaluator alignment/scoring logic;
- the sealed holdout source or gate;
- transport/session behavior;
- candidate status;
- promotion/APA-ID/database prohibitions.

All predecessor history remains intact. No prior directory is deleted or rewritten.
