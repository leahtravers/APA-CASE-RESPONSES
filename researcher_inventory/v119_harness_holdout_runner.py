#!/usr/bin/env python3
"""V119 sealed-holdout entry point retaining proven evaluator/isolation controls.

Workflow invocation remains gated on repeated Case 2 + Case 6 passes under one
finalized V119 contract and saved-agent lineage. This module never exposes sealed
source or holdout output to calibration instructions.
"""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v66_harness_correction import V66HarnessInventoryApparatus
from researcher_inventory.v119_task_rules import V119_BASE_RULES, V119_CLASS_RULES

apparatus.BASE_RULES = V119_BASE_RULES
apparatus.CLASS_RULES = V119_CLASS_RULES
base.InventoryApparatus = V66HarnessInventoryApparatus

_OriginalCommandAdapter = base.CommandAdapter

class V119HarnessCommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 2400):
        super().__init__(command, timeout=timeout)

base.CommandAdapter = V119HarnessCommandAdapter

if __name__ == "__main__":
    base.main()
