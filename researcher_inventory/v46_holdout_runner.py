#!/usr/bin/env python3
"""V46 protected sealed-holdout entry point; source/output remain inside existing protected boundary."""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v46_task_rules import V46_BASE_RULES, V46_CLASS_RULES

apparatus.BASE_RULES = V46_BASE_RULES
apparatus.CLASS_RULES = V46_CLASS_RULES

_OriginalCommandAdapter = base.CommandAdapter

class V46CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 1500):
        super().__init__(command, timeout=timeout)

base.CommandAdapter = V46CommandAdapter

if __name__ == "__main__":
    base.main()
