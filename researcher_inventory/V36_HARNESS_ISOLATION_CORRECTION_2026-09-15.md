# Researcher Inventory V36 Harness-Isolation Correction

Status: `ACTIVE HARNESS CORRECTION — V36 SEMANTICS UNCHANGED`
Date: 2026-09-15
Authority: Leah’s standing Researcher Inventory calibration directive
Registrar: `APA-EXEC-RI-CALIBRATION-V36-HARNESS-20260915T0813Z-0001`
Semantic contract: `researcher_inventory/AGENT_CONTRACT_V36.md`
Triggering diagnostic run: `34939188598`
Promotion authority: NONE

## 1. Finding

Run `34939188598` is preserved as a failed calibration attempt, but it does not cleanly isolate the semantic effect of V36.

The saved agent was correctly bootstrapped from `AGENT_CONTRACT_V36.md`. However, the runtime request path also forwarded `rules` and `class_rule` from `inventory_apparatus.py`. Those fields contain independent semantic selection/grain instructions inherited from the apparatus layer. `v36_openai_agents_adapter.py` then added another V36-specific semantic attention layer.

Accordingly, the worker received multiple semantic instruction layers. The hidden evaluator’s unit/compound failures remain valid evidence about the produced output, but they cannot yet prove that V36 itself requires semantic revision.

Classification: `TEST-HARNESS / PROMPT-PATH CONTAMINATION`.

## 2. Corrective successor

Forward V36 calibration uses:

`researcher_inventory/v36_contract_isolated_openai_agents_adapter.py`

The successor adapter:

- preserves task, requested class, response schema, source, frozen units, candidate/research metadata, and mechanical validator corrections;
- excludes apparatus `rules` and `class_rule` from worker-visible requests;
- treats the installed durable V36 contract as the sole semantic selection/grain authority;
- limits adapter text to procedural execution, response-shape, isolation, and mechanical retry requirements;
- preserves uncertain-session recovery behavior;
- does not expose archetypes, evaluator findings, expected counts, scored prior outputs, Case 5, or holdout output.

## 3. Retained history

Retained unchanged:

- `AGENT_CONTRACT_V36.md`;
- `v36_openai_agents_adapter.py` as the predecessor adapter used by run `34939188598`;
- run `34939188598` and all of its calibration history;
- immutable Case 2 and Case 6 archetype hashes;
- hidden evaluator logic;
- one-shot Case 5 and clean-room certification gates;
- candidate-only/no-promotion/no-APA-ID boundaries.

No prior failure is deleted or relabeled as a pass.

## 4. Forward test rule

A new Case 2/Case 6 calibration run must test unchanged V36 through the harness-isolated adapter before any semantic V37 successor is justified from the V36 failure pattern.

If the clean V36 run still fails, only cross-case, generalizable worker-behavior evidence from that clean run may support a semantic successor. Harness defects remain separately classified.

Sealed Case 5 remains `NOT DEPLOYED` until repeated archetype passes occur under the same finalized semantic contract.