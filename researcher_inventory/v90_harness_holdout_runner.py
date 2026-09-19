#!/usr/bin/env python3
"""V90 sealed-holdout entry point retaining proven harness corrections.

The workflow is the only authority that may invoke this after repeated archetype passes.
This module never exposes sealed source or holdout output to calibration instructions.
"""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v66_harness_correction import V66HarnessInventoryApparatus
from researcher_inventory.v90_task_rules import V90_BASE_RULES, V90_CLASS_RULES

apparatus.BASE_RULES = V90_BASE_RULES
apparatus.CLASS_RULES = V90_CLASS_RULES
base.InventoryApparatus = V66HarnessInventoryApparatus

_OriginalCommandAdapter = base.CommandAdapter
class V90HarnessCommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 2400):
        super().__init__(command, timeout=timeout)
base.CommandAdapter = V90HarnessCommandAdapter

if __name__ == "__main__":
    base.main()
