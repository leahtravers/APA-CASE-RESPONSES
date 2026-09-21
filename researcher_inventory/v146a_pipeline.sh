#!/usr/bin/env bash
set -euo pipefail

# Additive harness-routing successor. Preserve the V146 pipeline body and transform only
# the harness-specific call sites in a temporary execution copy.
python - <<'PY'
from pathlib import Path
src = Path('researcher_inventory/v146_pipeline.sh').read_text(encoding='utf-8')
src = src.replace(
    'researcher_inventory.tests.test_v126a_prompt_harness -v',
    'researcher_inventory.tests.test_v126a_prompt_harness researcher_inventory.tests.test_v146a_relation_first_harness -v',
)
src = src.replace(
    'researcher_inventory/v146_openai_agents_adapter.py',
    'researcher_inventory/v146a_task_rules.py researcher_inventory/v146a_relation_first_harness.py researcher_inventory/v146a_harness_calibration_runner.py researcher_inventory/v146a_harness_holdout_runner.py researcher_inventory/v146_openai_agents_adapter.py',
)
src = src.replace(
    "'harness_successor':'V126A_CONTRACT_SUBORDINATE_REQUEST_ENVELOPE_RETAINED'",
    "'harness_successor':'V146A_ONE_TURN_WHOLE_SOURCE_RELATION_FIRST_TOPOLOGY'",
)
src = src.replace(
    "'harness_corrections':'V66_FIELD_ALIGNMENT + V88A_EDITOR_SHORTHAND_ALIGNMENT + V92_SAME_SESSION_TRANSIENT_RECOVERY + V126A_CONTRACT_SUBORDINATE_REQUEST_ENVELOPE'",
    "'harness_corrections':'V66_FIELD_ALIGNMENT + V88A_EDITOR_SHORTHAND_ALIGNMENT + V92_SAME_SESSION_TRANSIENT_RECOVERY + V126A_CONTRACT_SUBORDINATE_REQUEST_ENVELOPE + V146A_WHOLE_SOURCE_RELATION_FIRST_TOPOLOGY'",
)
src = src.replace('researcher_inventory.v126a_harness_calibration_runner', 'researcher_inventory.v146a_harness_calibration_runner')
src = src.replace('researcher_inventory.v126a_harness_holdout_runner', 'researcher_inventory.v146a_harness_holdout_runner')
src = src.replace('V146 CONTRACT / V126A CONTRACT-SUBORDINATE HARNESS', 'V146 CONTRACT / V146A WHOLE-SOURCE RELATION-FIRST HARNESS')
src = src.replace('V146 CONTRACT / V126A HARNESS', 'V146 CONTRACT / V146A HARNESS')
src = src.replace(
    'V146 durable relation-first functional-slot contract with the retained V126A contract-subordinate runtime prompt harness',
    'V146 durable relation-first functional-slot contract with the V146A whole-source relation-first runtime harness',
)
src = src.replace(
    'executed through the retained V126A contract-subordinate runtime prompt harness',
    'executed through the V146A whole-source relation-first runtime harness',
)
Path('/tmp/v146a_pipeline_runtime.sh').write_text(src, encoding='utf-8')
PY

bash /tmp/v146a_pipeline_runtime.sh
