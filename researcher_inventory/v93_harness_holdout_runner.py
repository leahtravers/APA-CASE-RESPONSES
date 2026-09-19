#!/usr/bin/env python3
"""V93 sealed-holdout entry point retaining proven evaluator and isolation controls.

Workflow invocation remains forbidden until repeated Case 2 + Case 6 passes under
one finalized V93 contract and saved-agent lineage. This module does not expose
sealed source or holdout output to calibration instructions.
"""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v66_harness_correction import V66HarnessInventoryApparatus
from researcher_inventory.v93_task_rules import V93_BASE_RULES, V93_CLASS_RULES

apparatus.BASE_RULES = V93_BASE_RULES
apparatus.CLASS_RULES = V93_CLASS_RULES
base.InventoryApparatus = V66HarnessInventoryApparatus

_OriginalCommandAdapter = base.CommandAdapter

class V93HarnessCommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 2400):
        super().__init__(command, timeout=timeout)

base.CommandAdapter = V93HarnessCommandAdapter

if __name__ == "__main__":
    base.main()
