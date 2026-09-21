#!/usr/bin/env bash
set -euo pipefail

# Additive V147 successor: preserve the proven V146 pipeline controls while replacing
# only semantic-contract/harness-specific call sites in a temporary execution copy.
python - <<'PY'
from pathlib import Path
src = Path('researcher_inventory/v146_pipeline.sh').read_text(encoding='utf-8')
src = src.replace('v146_session_recovery', 'v147_session_recovery')
src = src.replace(
    'researcher_inventory.tests.test_v126a_prompt_harness -v',
    'researcher_inventory.tests.test_v126a_prompt_harness researcher_inventory.tests.test_v146a_relation_first_harness researcher_inventory.tests.test_v147a_hybrid_harness -v',
)
src = src.replace(
    'researcher_inventory/v146_openai_agents_adapter.py',
    'researcher_inventory/v147a_task_rules.py researcher_inventory/v147a_hybrid_harness.py researcher_inventory/v147a_harness_calibration_runner.py researcher_inventory/v147a_harness_holdout_runner.py researcher_inventory/v147_openai_agents_adapter.py',
)
src = src.replace(
    "'semantic_contract':'V146_RELATION_FIRST_FUNCTIONAL_SLOT_DERIVATION'",
    "'semantic_contract':'V147_FRAME_SCAFFOLD_BOUNDED_RELATION_HYBRID'",
)
src = src.replace(
    "'harness_successor':'V126A_CONTRACT_SUBORDINATE_REQUEST_ENVELOPE_RETAINED'",
    "'harness_successor':'V147A_WHOLE_SOURCE_SCAFFOLD_BOUNDED_RELATION_TOPOLOGY'",
)
src = src.replace(
    "'harness_corrections':'V66_FIELD_ALIGNMENT + V88A_EDITOR_SHORTHAND_ALIGNMENT + V92_SAME_SESSION_TRANSIENT_RECOVERY + V126A_CONTRACT_SUBORDINATE_REQUEST_ENVELOPE'",
    "'harness_corrections':'V66_FIELD_ALIGNMENT + V88A_EDITOR_SHORTHAND_ALIGNMENT + V92_SAME_SESSION_TRANSIENT_RECOVERY + V126A_CONTRACT_SUBORDINATE_REQUEST_ENVELOPE + V146A_ONE_TURN_TOPOLOGY + V147A_SCAFFOLD_BOUNDED_SELECTOR'",
)
src = src.replace('researcher_inventory.v126a_harness_calibration_runner', 'researcher_inventory.v147a_harness_calibration_runner')
src = src.replace('researcher_inventory.v126a_harness_holdout_runner', 'researcher_inventory.v147a_harness_holdout_runner')
src = src.replace('V146 CONTRACT / V126A CONTRACT-SUBORDINATE HARNESS', 'V147 CONTRACT / V147A WHOLE-SOURCE HYBRID HARNESS')
src = src.replace('V146 CONTRACT / V126A HARNESS', 'V147 CONTRACT / V147A HARNESS')
src = src.replace(
    'V146 durable relation-first functional-slot contract with the retained V126A contract-subordinate runtime prompt harness',
    'V147 durable scaffold-first / bounded-relation contract with the V147A whole-source hybrid harness',
)
src = src.replace(
    'executed through the retained V126A contract-subordinate runtime prompt harness',
    'executed through the V147A whole-source hybrid harness',
)
Path('/tmp/v147a_pipeline_runtime.sh').write_text(src, encoding='utf-8')
PY

bash /tmp/v147a_pipeline_runtime.sh
