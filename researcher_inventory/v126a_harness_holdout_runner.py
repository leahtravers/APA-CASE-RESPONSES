#!/usr/bin/env python3
"""V126A sealed-holdout entry point retaining the existing one-shot isolation gate."""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v126a_harness_prompt_correction import V126AHarnessInventoryApparatus
from researcher_inventory.v126a_task_rules import V126A_BASE_RULES, V126A_CLASS_RULES

apparatus.BASE_RULES = V126A_BASE_RULES
apparatus.CLASS_RULES = V126A_CLASS_RULES
base.InventoryApparatus = V126AHarnessInventoryApparatus

_OriginalCommandAdapter = base.CommandAdapter

class V126AHarnessCommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 2400):
        super().__init__(command, timeout=timeout)

base.CommandAdapter = V126AHarnessCommandAdapter

if __name__ == "__main__":
    base.main()
