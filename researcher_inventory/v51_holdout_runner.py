#!/usr/bin/env python3
"""V51 protected sealed-holdout entry point; source/output remain inside existing protected boundary."""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v51_task_rules import V51_BASE_RULES, V51_CLASS_RULES

apparatus.BASE_RULES = V51_BASE_RULES
apparatus.CLASS_RULES = V51_CLASS_RULES

_OriginalCommandAdapter = base.CommandAdapter

class V51CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 1500):
        super().__init__(command, timeout=timeout)

base.CommandAdapter = V51CommandAdapter

if __name__ == "__main__":
    base.main()
