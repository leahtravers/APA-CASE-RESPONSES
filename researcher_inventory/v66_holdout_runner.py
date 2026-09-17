#!/usr/bin/env python3
"""V66 protected sealed-holdout entry point.

This module is inert during calibration. The workflow may invoke it only after
repeated Case 2/Case 6 passes under finalized V66. Sealed source/output remain
inside the existing protected holdout boundary.
"""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v66_task_rules import V66_BASE_RULES, V66_CLASS_RULES

apparatus.BASE_RULES = V66_BASE_RULES
apparatus.CLASS_RULES = V66_CLASS_RULES

_OriginalCommandAdapter = base.CommandAdapter
class V66CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 1500):
        super().__init__(command, timeout=timeout)
base.CommandAdapter = V66CommandAdapter

if __name__ == "__main__":
    base.main()
