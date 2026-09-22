#!/usr/bin/env python3
"""V151 calibration entry point with V151A class-function-complete harness.

The semantic authority is RI-CONTRACT-V151. The harness retains the established
whole-source request, deterministic alignment, and timeout behavior without adding
gold/evaluator/holdout guidance.
"""
from researcher_inventory import v66_calibration_runner as v66
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v66_harness_correction import install_field_aware_alignment
from researcher_inventory.v88a_harness_alignment_correction import install_editor_shorthand_alignment
from researcher_inventory.v126a_task_rules import V126A_BASE_RULES, V126A_CLASS_RULES
from researcher_inventory.v151a_class_function_harness import V151AClassFunctionCompleteApparatus

apparatus.BASE_RULES = V126A_BASE_RULES
apparatus.CLASS_RULES = V126A_CLASS_RULES
base = v66.base
base.InventoryApparatus = V151AClassFunctionCompleteApparatus
install_field_aware_alignment(base)
install_editor_shorthand_alignment(base)

_OriginalCommandAdapter = base.CommandAdapter

class V151AHarnessCommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 2400):
        super().__init__(command, timeout=timeout)

base.CommandAdapter = V151AHarnessCommandAdapter

if __name__ == "__main__":
    base.main()
