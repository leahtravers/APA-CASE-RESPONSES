#!/usr/bin/env python3
"""V72 sealed-holdout entry point retaining the V66 harness-only corrections."""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v66_harness_correction import V66HarnessInventoryApparatus
from researcher_inventory.v72_task_rules import V72_BASE_RULES, V72_CLASS_RULES

apparatus.BASE_RULES = V72_BASE_RULES
apparatus.CLASS_RULES = V72_CLASS_RULES
base.InventoryApparatus = V66HarnessInventoryApparatus

_OriginalCommandAdapter = base.CommandAdapter
class V72HarnessCommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 1500):
        super().__init__(command, timeout=timeout)
base.CommandAdapter = V72HarnessCommandAdapter

if __name__ == "__main__":
    base.main()
