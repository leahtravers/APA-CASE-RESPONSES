#!/usr/bin/env python3
"""V150 calibration entry point with V150A promoted-coordinate harness.

The semantic change is controlled only by RI-CONTRACT-V150 and V150A's subordinate
operation selector. The 2400-second CommandAdapter bound is retained harness/runtime
infrastructure and has no semantic effect.
"""
from researcher_inventory import v66_calibration_runner as v66
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v66_harness_correction import install_field_aware_alignment
from researcher_inventory.v88a_harness_alignment_correction import install_editor_shorthand_alignment
from researcher_inventory.v126a_task_rules import V126A_BASE_RULES, V126A_CLASS_RULES
from researcher_inventory.v150a_promoted_coordinate_harness import V150APromotedCoordinateApparatus

apparatus.BASE_RULES = V126A_BASE_RULES
apparatus.CLASS_RULES = V126A_CLASS_RULES
base = v66.base
base.InventoryApparatus = V150APromotedCoordinateApparatus
install_field_aware_alignment(base)
install_editor_shorthand_alignment(base)

_OriginalCommandAdapter = base.CommandAdapter

class V150AHarnessCommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 2400):
        super().__init__(command, timeout=timeout)

base.CommandAdapter = V150AHarnessCommandAdapter

if __name__ == "__main__":
    base.main()
