#!/usr/bin/env python3
"""V149 calibration entry point with V149A inventory-coordinate harness.

The semantic change is controlled only by RI-CONTRACT-V149 and V149A's subordinate
operation selector. The 2400-second CommandAdapter bound is the separately documented
V149A harness-timeout correction and has no semantic effect.
"""
from researcher_inventory import v66_calibration_runner as v66
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v66_harness_correction import install_field_aware_alignment
from researcher_inventory.v88a_harness_alignment_correction import install_editor_shorthand_alignment
from researcher_inventory.v126a_task_rules import V126A_BASE_RULES, V126A_CLASS_RULES
from researcher_inventory.v149a_coordinate_harness import V149AInventoryCoordinateApparatus

apparatus.BASE_RULES = V126A_BASE_RULES
apparatus.CLASS_RULES = V126A_CLASS_RULES
base = v66.base
base.InventoryApparatus = V149AInventoryCoordinateApparatus
install_field_aware_alignment(base)
install_editor_shorthand_alignment(base)

_OriginalCommandAdapter = base.CommandAdapter

class V149AHarnessCommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 2400):
        super().__init__(command, timeout=timeout)

base.CommandAdapter = V149AHarnessCommandAdapter

if __name__ == "__main__":
    base.main()
