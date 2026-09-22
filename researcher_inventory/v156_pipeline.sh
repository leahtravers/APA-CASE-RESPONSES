#!/usr/bin/env bash
set -euo pipefail

# V156 changes durable semantic instructions and adds one semantically-neutral result
# retrieval correction. The retained V153A whole-source topology, evaluator, immutable
# archetype gate, attempt preservation, holdout isolation, and clean-room certification
# remain unchanged.
tmp="$(mktemp)"
trap 'rm -f "$tmp"' EXIT
sed \
  -e 's/V154/V156/g' \
  -e 's/v154/v156/g' \
  -e 's/V156_STRUCTURAL_LATTICE_PLUS_MINIMAL_RELATION_NUCLEUS/V156_RESEARCHER_HANDLE_RELATION_PHRASE_GRAIN/g' \
  -e 's/V156 durable structural-lattice\/minimal-relation-nucleus contract/V156 durable researcher-handle relation-phrase-grain contract/g' \
  -e 's/researcher_inventory.tests.test_v153a_role_complete_harness -v/researcher_inventory.tests.test_v153a_role_complete_harness researcher_inventory.tests.test_v156_result_retrieval -v/' \
  -e 's/V153A_NEUTRAL_TASK_SELECTOR + OUTER_TIMEOUT_2400/V153A_NEUTRAL_TASK_SELECTOR + V156_PAGINATED_SAME_SESSION_FINAL_ANSWER_RECOVERY + OUTER_TIMEOUT_2400/g' \
  researcher_inventory/v154_pipeline.sh > "$tmp"

bash "$tmp"
