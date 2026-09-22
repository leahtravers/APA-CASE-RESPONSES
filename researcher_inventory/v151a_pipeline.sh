#!/usr/bin/env bash
set -euo pipefail

HISTORY_DIR="calibration_history/researcher_inventory/${GITHUB_RUN_ID}-A${GITHUB_RUN_ATTEMPT}"
PRESERVED=0

preserve_history() {
  local rc=$?
  if [ "$PRESERVED" -eq 1 ]; then return "$rc"; fi
  PRESERVED=1
  mkdir -p "$HISTORY_DIR"
  test ! -f researcher_inventory/runtime/archetype_integrity.json || cp researcher_inventory/runtime/archetype_integrity.json "$HISTORY_DIR/archetype_integrity.json"
  test ! -f researcher_inventory/runtime/training_history.ndjson || cp researcher_inventory/runtime/training_history.ndjson "$HISTORY_DIR/training_history.ndjson"
  test ! -f researcher_inventory/runtime/test_results.json || cp researcher_inventory/runtime/test_results.json "$HISTORY_DIR/test_results.json"
  test ! -d researcher_inventory/runtime/v151_session_recovery || cp -R researcher_inventory/runtime/v151_session_recovery "$HISTORY_DIR/v151_session_recovery"
  test ! -f "$RI_CONTRACT_FILE" || cp "$RI_CONTRACT_FILE" "$HISTORY_DIR/iteration_contract.md"
  python - <<'PY' > "$HISTORY_DIR/run_manifest.json"
import json,os
print(json.dumps({
  'workflow_run_id':os.environ.get('GITHUB_RUN_ID'),
  'workflow_run_attempt':os.environ.get('GITHUB_RUN_ATTEMPT'),
  'commit_sha':os.environ.get('GITHUB_SHA'),
  'contract_version':os.environ.get('CONTRACT_VERSION'),
  'contract_file':os.environ.get('RI_CONTRACT_FILE'),
  'model':os.environ.get('OPENAI_MODEL'),
  'event':os.environ.get('GITHUB_EVENT_NAME'),
  'evidence_policy':'calibration-only; sealed holdout source/output deliberately excluded',
  'semantic_contract':'V151_CLASS_FUNCTION_COMPLETE_SOURCE_OCCURRENCES',
  'harness_successor':'V151A_ONE_TURN_CLASS_FUNCTION_COMPLETE_TOPOLOGY',
  'harness_corrections':'V66_FIELD_ALIGNMENT + V88A_EDITOR_SHORTHAND_ALIGNMENT + V92_SAME_SESSION_TRANSIENT_RECOVERY + V126A_CONTRACT_SUBORDINATE_REQUEST_ENVELOPE + V146A_ONE_TURN_TOPOLOGY + V149A_COMPLETE_ATOM_NORMALIZATION + V151A_SEMANTIC_NEUTRAL_TASK_ROUTING + OUTER_TIMEOUT_2400'
},sort_keys=True,indent=2))
PY
  python - <<'PY' > "$HISTORY_DIR/holdout_stage_state.json"
import json
from pathlib import Path
r=Path('researcher_inventory/runtime')
out={
  'sealed_source_committed':False,
  'holdout_output_committed':False,
  'calibrated_lineage_holdout_attempted':(r/'calibrated_lineage_holdout_result.json').exists() or (r/'holdout_result.json').exists(),
  'clean_room_agent_created':(r/'retired_calibration_agent_id.txt').exists() and (r/'extractor_agent_id.txt').exists()
}
if (r/'calibrated_lineage_holdout_result.json').exists(): out['calibrated_lineage_holdout_pass']=bool(json.loads((r/'calibrated_lineage_holdout_result.json').read_text()).get('pass'))
if (r/'retired_calibration_agent_id.txt').exists() and (r/'holdout_result.json').exists(): out['latest_holdout_pass']=bool(json.loads((r/'holdout_result.json').read_text()).get('pass'))
print(json.dumps(out,sort_keys=True,indent=2))
PY
  git add "$HISTORY_DIR" researcher_inventory/status 2>/dev/null || true
  if ! git diff --cached --quiet; then
    git commit -m "training-history: preserve researcher inventory V151 run ${GITHUB_RUN_ID} attempt ${GITHUB_RUN_ATTEMPT} [skip ci]"
    git pull --rebase origin main
    git push origin main
  fi
  return "$rc"
}
trap preserve_history EXIT

mkdir -p researcher_inventory/runtime researcher_inventory/status
python -m researcher_inventory.verify_archetypes

git add researcher_inventory/tests/archetypes/Case_2_Lightweight_Researcher_Inventory.xlsx researcher_inventory/tests/archetypes/Case_6_Lightweight_Researcher_Inventory_v2_with_Verbs_and_Locators.xlsx
if ! git diff --cached --quiet; then
  git commit -m "tests: restore immutable researcher inventory archetypes [skip ci]"
  git pull --rebase origin main
  git push origin main
fi

python -m unittest researcher_inventory.tests.test_inventory_apparatus researcher_inventory.tests.test_v64_compound_order_harness researcher_inventory.tests.test_v66_harness_correction researcher_inventory.tests.test_v88a_harness_alignment researcher_inventory.tests.test_v126a_prompt_harness researcher_inventory.tests.test_v146a_relation_first_harness researcher_inventory.tests.test_v147a_hybrid_harness researcher_inventory.tests.test_v148a_class_complete_harness researcher_inventory.tests.test_v149a_coordinate_harness researcher_inventory.tests.test_v150a_promoted_coordinate_harness researcher_inventory.tests.test_v151a_class_function_harness -v
python -m py_compile researcher_inventory/v151a_class_function_harness.py researcher_inventory/v151a_harness_calibration_runner.py researcher_inventory/v151a_harness_holdout_runner.py researcher_inventory/v151_openai_agents_adapter.py

if [ -f researcher_inventory/status/CLEAN_ROOM_CERTIFIED.md ]; then
  echo "ALREADY CLEAN-ROOM CERTIFIED"
  exit 0
fi

python - <<'PY'
import json,sys
from pathlib import Path
root=Path('calibration_history/researcher_inventory')
attempts=[]
if root.exists():
  for p in sorted(root.glob('*/holdout_stage_state.json')):
    try: s=json.loads(p.read_text())
    except Exception: continue
    if s.get('calibrated_lineage_holdout_attempted'): attempts.append((p.parent.name,s))
if attempts:
  run_id,state=attempts[0]
  Path('researcher_inventory/status/HOLDOUT_CONSUMED_HOLD.md').write_text('# Researcher Inventory Sealed Holdout Hold\n\nThe sealed holdout has already been attempted in workflow history `%s`. Automatic reuse is prohibited. Preserve the prior result and do not reopen or expose the sealed source for calibration.\n' % run_id)
  print('SEALED HOLDOUT ALREADY CONSUMED — AUTOMATIC REUSE HELD')
  sys.exit(9)
PY

: > researcher_inventory/runtime/training_history.ndjson
rm -f researcher_inventory/runtime/test_results.json researcher_inventory/runtime/holdout_result.json researcher_inventory/runtime/calibrated_lineage_holdout_result.json researcher_inventory/runtime/retired_calibration_agent_id.txt
python researcher_inventory/session_bootstrap.py

echo '=== V151 CONTRACT / V151A CLASS-FUNCTION-COMPLETE HARNESS DIAGNOSTIC ARCHETYPE BATCH ==='
TEST_REPETITIONS=1 python -m researcher_inventory.v151a_harness_calibration_runner

echo '=== V151 CONTRACT / V151A HARNESS REPEATABILITY BATCH 1 ==='
TEST_REPETITIONS=2 python -m researcher_inventory.v151a_harness_calibration_runner

echo '=== V151 CONTRACT / V151A HARNESS REPEATABILITY BATCH 2 ==='
TEST_REPETITIONS=2 python -m researcher_inventory.v151a_harness_calibration_runner

cat > researcher_inventory/status/ARCHETYPE_CALIBRATED.md <<'EOF'
# Researcher Inventory Apparatus Archetype Calibration
V151 durable class-function-complete source-occurrence contract with the V151A whole-source harness passed the immutable Case 2/Case 6 SHA-256 gate, one diagnostic batch, and two repeated verification batches under the same finalized durable contract and saved-agent lineage. The worker had no archetype access.
EOF

python -m researcher_inventory.v151a_harness_holdout_runner
cp researcher_inventory/runtime/extractor_agent_id.txt researcher_inventory/runtime/retired_calibration_agent_id.txt
cp researcher_inventory/runtime/holdout_result.json researcher_inventory/runtime/calibrated_lineage_holdout_result.json

python researcher_inventory/session_bootstrap.py
python -m researcher_inventory.v151a_harness_holdout_runner

cat > researcher_inventory/status/CLEAN_ROOM_CERTIFIED.md <<'EOF'
# Researcher Inventory Apparatus Clean-Room Certification
The finalized V151 durable class-function-complete source-occurrence contract, executed through the V151A whole-source harness, passed immutable workbook verification and repeated hidden Case 2/Case 6 calibration under one saved-agent lineage. The calibrated lineage passed the sealed holdout exactly once and was retired. A brand-new saved agent bootstrapped only from finalized V151 durable instructions, with no prior session or holdout output, then passed the sealed holdout in a new session.
EOF

preserve_history
trap - EXIT
