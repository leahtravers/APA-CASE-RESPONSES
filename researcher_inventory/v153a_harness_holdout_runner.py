#!/usr/bin/env python3
"""V153A sealed-holdout entry point retaining the existing one-shot isolation gate.

This module does not read the sealed source itself. It installs the same V153A
whole-source harness used by calibration; pipeline eligibility controls reachability.
"""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v126a_task_rules import V126A_BASE_RULES, V126A_CLASS_RULES
from researcher_inventory.v153a_role_complete_harness import V153ARoleCompleteInventoryApparatus

apparatus.BASE_RULES = V126A_BASE_RULES
apparatus.CLASS_RULES = V126A_CLASS_RULES
base.InventoryApparatus = V153ARoleCompleteInventoryApparatus

_OriginalCommandAdapter = base.CommandAdapter

class V153AHarnessCommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 2400):
        super().__init__(command, timeout=timeout)

base.CommandAdapter = V153AHarnessCommandAdapter

if __name__ == "__main__":
    base.main()
