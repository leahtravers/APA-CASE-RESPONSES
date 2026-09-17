#!/usr/bin/env python3
"""V69 sealed-holdout entry point retaining the V66 harness-only corrections."""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v66_harness_correction import V66HarnessInventoryApparatus
from researcher_inventory.v69_task_rules import V69_BASE_RULES, V69_CLASS_RULES

apparatus.BASE_RULES = V69_BASE_RULES
apparatus.CLASS_RULES = V69_CLASS_RULES
base.InventoryApparatus = V66HarnessInventoryApparatus

_OriginalCommandAdapter = base.CommandAdapter
class V69HarnessCommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 1500):
        super().__init__(command, timeout=timeout)
base.CommandAdapter = V69HarnessCommandAdapter

if __name__ == "__main__":
    base.main()
