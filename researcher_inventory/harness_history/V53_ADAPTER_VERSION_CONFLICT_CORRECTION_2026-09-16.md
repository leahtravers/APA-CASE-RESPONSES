# Researcher Inventory V53 Harness Version-Conflict Correction

Status: `IN-SCOPE BOUNDED CORRECTION / GAP CLOSURE`  
Date: 2026-09-16  
Authority: Leah's standing Researcher Inventory calibration instruction  
Registrar filing: `APA-EXEC-2026-09-16-CASES-RI-V53-HARNESS-0001`

## Predecessor defect

The durable worker contract `researcher_inventory/AGENT_CONTRACT_V53.md` was installed correctly by `session_bootstrap.py`, but the active command path used:

- predecessor V53 adapter blob `c5c61e34cef6b3984c0a0eb6ccda440a172c5c01`;
- V52 base adapter blob `6e4bef03f98a33fd6f5cff204903e0e7e69d963b`.

The V53 wrapper delegated its execution to that V52 base. The base's initial and adjudication prompts explicitly instructed the worker to act under an "installed durable V52 contract." During a V53 run, that is a harness-level contract-version conflict.

Latest affected preserved workflow run: `35082043482`. Earlier V53 run `35077906779` used the same defective path. Those attempts and findings remain historical evidence, but they are not clean evidence for another durable semantic-contract revision until V53 is rerun without the version-conflicting harness instruction.

## Corrective successor

Additive successor: `researcher_inventory/v53_openai_agents_adapter_v2.py`.

The successor:

- reads the active `CONTRACT_VERSION` supplied by the workflow;
- removes apparatus `rules` and `class_rule` prose before the worker request, preserving the installed durable contract as sole semantic authority;
- keeps only mechanical schema/retry/adjudication instructions in the harness;
- preserves gold/evaluator/holdout isolation;
- retains the same provider/session recovery machinery and the same two-session provisional/adjudication pattern;
- does not alter `AGENT_CONTRACT_V53.md`.

## Forward-control boundary

For new V53 calibration beginning after this correction, route the workflow to `v53_openai_agents_adapter_v2.py`. The predecessor V53 adapter remains preserved and is not deleted or rewritten.

A future durable contract successor requires clean post-correction evidence demonstrating a generalizable semantic requirement. The existence of the harness correction itself does not authorize V54.

## Holdout boundary

No sealed Case 5 source or output was consulted to identify or repair this harness defect. The sealed holdout remains closed until the repeated paired-archetype gate succeeds under one finalized durable contract.
