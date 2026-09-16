#!/usr/bin/env python3
"""V60 protected sealed-holdout entry point; source/output remain inside the existing protected boundary."""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v60_task_rules import V60_BASE_RULES, V60_CLASS_RULES

apparatus.BASE_RULES = V60_BASE_RULES
apparatus.CLASS_RULES = V60_CLASS_RULES

_OriginalCommandAdapter = base.CommandAdapter
class V60CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 1500):
        super().__init__(command, timeout=timeout)
base.CommandAdapter = V60CommandAdapter

if __name__ == "__main__":
    base.main()
