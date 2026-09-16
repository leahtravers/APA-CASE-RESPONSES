#!/usr/bin/env python3
"""V56 protected sealed-holdout entry point; source/output remain inside the existing protected boundary."""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v56_task_rules import V56_BASE_RULES, V56_CLASS_RULES

apparatus.BASE_RULES = V56_BASE_RULES
apparatus.CLASS_RULES = V56_CLASS_RULES

_OriginalCommandAdapter = base.CommandAdapter
class V56CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 1500):
        super().__init__(command, timeout=timeout)
base.CommandAdapter = V56CommandAdapter

if __name__ == "__main__":
    base.main()
