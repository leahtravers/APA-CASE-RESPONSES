#!/usr/bin/env python3
"""V148 calibration entry point with V148A whole-source class-complete harness."""
from researcher_inventory import v66_calibration_runner as v66
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v66_harness_correction import install_field_aware_alignment
from researcher_inventory.v88a_harness_alignment_correction import install_editor_shorthand_alignment
from researcher_inventory.v126a_task_rules import V126A_BASE_RULES, V126A_CLASS_RULES
from researcher_inventory.v148a_class_complete_harness import V148AClassCompleteInventoryApparatus

apparatus.BASE_RULES = V126A_BASE_RULES
apparatus.CLASS_RULES = V126A_CLASS_RULES
base = v66.base
base.InventoryApparatus = V148AClassCompleteInventoryApparatus
install_field_aware_alignment(base)
install_editor_shorthand_alignment(base)

if __name__ == "__main__":
    base.main()
