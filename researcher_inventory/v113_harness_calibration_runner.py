#!/usr/bin/env python3
"""V113 semantic calibration runner with retained evaluator corrections."""
from researcher_inventory import v66_calibration_runner as v66
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v66_harness_correction import V66HarnessInventoryApparatus, install_field_aware_alignment
from researcher_inventory.v88a_harness_alignment_correction import install_editor_shorthand_alignment
from researcher_inventory.v113_task_rules import V113_BASE_RULES, V113_CLASS_RULES

apparatus.BASE_RULES = V113_BASE_RULES
apparatus.CLASS_RULES = V113_CLASS_RULES
base = v66.base
base.InventoryApparatus = V66HarnessInventoryApparatus
install_field_aware_alignment(base)
install_editor_shorthand_alignment(base)

if __name__ == "__main__":
    base.main()
