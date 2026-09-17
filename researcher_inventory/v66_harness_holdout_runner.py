#!/usr/bin/env python3
"""V66 sealed-holdout entry point using the V66 harness-only compound correction.

This module is inert until the existing repeated-archetype gate succeeds. It does
not expose sealed source/output and does not alter the durable V66 worker contract.
"""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v66_harness_correction import V66HarnessInventoryApparatus
from researcher_inventory.v66_task_rules import V66_BASE_RULES, V66_CLASS_RULES

apparatus.BASE_RULES = V66_BASE_RULES
apparatus.CLASS_RULES = V66_CLASS_RULES
base.InventoryApparatus = V66HarnessInventoryApparatus

_OriginalCommandAdapter = base.CommandAdapter


class V66HarnessCommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 1500):
        super().__init__(command, timeout=timeout)


base.CommandAdapter = V66HarnessCommandAdapter

if __name__ == "__main__":
    base.main()
