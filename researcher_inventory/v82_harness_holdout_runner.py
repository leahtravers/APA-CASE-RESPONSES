#!/usr/bin/env python3
"""V82 sealed-holdout entry point retaining V66 harness corrections. Prepared only; workflow gates execution after repeated archetype passes."""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v66_harness_correction import V66HarnessInventoryApparatus
from researcher_inventory.v82_task_rules import V82_BASE_RULES, V82_CLASS_RULES

apparatus.BASE_RULES = V82_BASE_RULES
apparatus.CLASS_RULES = V82_CLASS_RULES
base.InventoryApparatus = V66HarnessInventoryApparatus

_OriginalCommandAdapter = base.CommandAdapter
class V82HarnessCommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 1500):
        super().__init__(command, timeout=timeout)
base.CommandAdapter = V82HarnessCommandAdapter

if __name__ == "__main__":
    base.main()
