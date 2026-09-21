#!/usr/bin/env python3
"""V146A sealed-holdout entry point retaining the existing one-shot isolation gate.

This module does not read the sealed source itself. It only installs the same corrected
whole-source harness that calibration must have already passed before the holdout runner
can become reachable under the pipeline gate.
"""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v126a_task_rules import V126A_BASE_RULES, V126A_CLASS_RULES
from researcher_inventory.v146a_relation_first_harness import V146ARelationFirstHarnessInventoryApparatus

apparatus.BASE_RULES = V126A_BASE_RULES
apparatus.CLASS_RULES = V126A_CLASS_RULES
base.InventoryApparatus = V146ARelationFirstHarnessInventoryApparatus

_OriginalCommandAdapter = base.CommandAdapter

class V146AHarnessCommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 2400):
        super().__init__(command, timeout=timeout)

base.CommandAdapter = V146AHarnessCommandAdapter

if __name__ == "__main__":
    base.main()
