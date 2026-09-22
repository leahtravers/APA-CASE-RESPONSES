#!/usr/bin/env bash
set -euo pipefail

# V155 changes durable semantic instructions only. The retained V154 pipeline mechanics
# are transformed mechanically so history labels, recovery custody, status text, and
# compile checks use the V155 identity without duplicating or semantically modifying
# the proven calibration/holdout topology.
tmp="$(mktemp)"
trap 'rm -f "$tmp"' EXIT
sed \
  -e 's/V154/V155/g' \
  -e 's/v154/v155/g' \
  -e 's/V155_STRUCTURAL_LATTICE_PLUS_MINIMAL_RELATION_NUCLEUS/V155_REPRESENTED_ROLE_ADMISSION_BEFORE_SPAN/g' \
  -e 's/V155 durable structural-lattice\/minimal-relation-nucleus contract/V155 durable represented-role-admission-before-span contract/g' \
  researcher_inventory/v154_pipeline.sh > "$tmp"

bash "$tmp"
