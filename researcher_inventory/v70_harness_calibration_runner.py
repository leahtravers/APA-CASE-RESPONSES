#!/usr/bin/env python3
"""V70 semantic calibration runner retaining the V66 field-aware evaluator correction."""
from researcher_inventory import v66_calibration_runner as v66
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v66_harness_correction import V66HarnessInventoryApparatus, install_field_aware_alignment
from researcher_inventory.v70_task_rules import V70_BASE_RULES, V70_CLASS_RULES

apparatus.BASE_RULES = V70_BASE_RULES
apparatus.CLASS_RULES = V70_CLASS_RULES
base = v66.base
base.InventoryApparatus = V66HarnessInventoryApparatus
install_field_aware_alignment(base)

if __name__ == "__main__":
    base.main()
