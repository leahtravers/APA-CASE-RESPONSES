#!/usr/bin/env python3
"""V50 protected sealed-holdout entry point; source/output remain inside existing protected boundary."""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v50_task_rules import V50_BASE_RULES, V50_CLASS_RULES

apparatus.BASE_RULES = V50_BASE_RULES
apparatus.CLASS_RULES = V50_CLASS_RULES

_OriginalCommandAdapter = base.CommandAdapter

class V50CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 1500):
        super().__init__(command, timeout=timeout)

base.CommandAdapter = V50CommandAdapter

if __name__ == "__main__":
    base.main()
