#!/usr/bin/env bash
set -euo pipefail

# V157 is a semantically-neutral harness successor for the unchanged V156 durable
# contract. It retains the V153A one-turn whole-source topology and all V156 semantic
# instructions, but reconciles the actual root-turn lifecycle before accepting output.
generated="$(mktemp)"
tmp="$(mktemp)"
trap 'rm -f "$generated" "$tmp"' EXIT

# First materialize exactly the V156 pipeline successor from its V154 predecessor.
sed \
  -e 's/V154/V156/g' \
  -e 's/v154/v156/g' \
  -e 's/V156_STRUCTURAL_LATTICE_PLUS_MINIMAL_RELATION_NUCLEUS/V156_RESEARCHER_HANDLE_RELATION_PHRASE_GRAIN/g' \
  -e 's/V156 durable structural-lattice\/minimal-relation-nucleus contract/V156 durable researcher-handle relation-phrase-grain contract/g' \
  -e 's/researcher_inventory.tests.test_v153a_role_complete_harness -v/researcher_inventory.tests.test_v153a_role_complete_harness researcher_inventory.tests.test_v156_result_retrieval -v/' \
  -e 's/V153A_NEUTRAL_TASK_SELECTOR + OUTER_TIMEOUT_2400/V153A_NEUTRAL_TASK_SELECTOR + V156_PAGINATED_SAME_SESSION_FINAL_ANSWER_RECOVERY + OUTER_TIMEOUT_2400/g' \
  researcher_inventory/v154_pipeline.sh > "$generated"

# Then change only harness/runtime custody, deterministic coverage, and executable
# adapter routing. Contract version, contract file, evaluator, prompts, and semantic
# labels remain V156.
sed \
  -e 's#researcher_inventory/runtime/v156_session_recovery#researcher_inventory/runtime/v157_session_recovery#g' \
  -e 's#researcher_inventory/v156_openai_agents_adapter.py#researcher_inventory/v157_openai_agents_adapter.py#g' \
  -e 's/researcher_inventory.tests.test_v156_result_retrieval -v/researcher_inventory.tests.test_v156_result_retrieval researcher_inventory.tests.test_v157_turn_aware_result_retrieval -v/' \
  -e 's/V156_PAGINATED_SAME_SESSION_FINAL_ANSWER_RECOVERY + OUTER_TIMEOUT_2400/V156_PAGINATED_SAME_SESSION_FINAL_ANSWER_RECOVERY + V157_TURN_AWARE_ROOT_TURN_RECONCILIATION + OUTER_TIMEOUT_2400/g' \
  -e 's/preserve researcher inventory V156 run/preserve researcher inventory V156 semantic - V157 harness run/g' \
  "$generated" > "$tmp"

bash "$tmp"
