#!/usr/bin/env python3
"""V118 semantic calibration runner with retained evaluator corrections.

This wrapper changes only the worker-facing semantic task rules. The hidden evaluator,
alignment corrections, and calibration isolation mechanics remain inherited from the
proven predecessor harness family.
"""
from researcher_inventory import v66_calibration_runner as v66
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v66_harness_correction import V66HarnessInventoryApparatus, install_field_aware_alignment
from researcher_inventory.v88a_harness_alignment_correction import install_editor_shorthand_alignment
from researcher_inventory.v118_task_rules import V118_BASE_RULES, V118_CLASS_RULES

apparatus.BASE_RULES = V118_BASE_RULES
apparatus.CLASS_RULES = V118_CLASS_RULES
base = v66.base
base.InventoryApparatus = V66HarnessInventoryApparatus
install_field_aware_alignment(base)
install_editor_shorthand_alignment(base)

if __name__ == "__main__":
    base.main()
