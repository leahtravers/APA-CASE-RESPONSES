#!/usr/bin/env python3
"""V43 protected sealed-holdout entry point; source/output stay inside existing protected boundary."""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v43_task_rules import V43_BASE_RULES, V43_CLASS_RULES

apparatus.BASE_RULES = V43_BASE_RULES
apparatus.CLASS_RULES = V43_CLASS_RULES

_OriginalCommandAdapter = base.CommandAdapter

class V43CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 1500):
        super().__init__(command, timeout=timeout)

base.CommandAdapter = V43CommandAdapter

if __name__ == "__main__":
    base.main()
