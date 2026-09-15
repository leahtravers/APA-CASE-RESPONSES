#!/usr/bin/env python3
"""V44 protected sealed-holdout entry point; source/output stay inside existing protected boundary."""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v44_task_rules import V44_BASE_RULES, V44_CLASS_RULES

apparatus.BASE_RULES = V44_BASE_RULES
apparatus.CLASS_RULES = V44_CLASS_RULES

_OriginalCommandAdapter = base.CommandAdapter

class V44CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 1500):
        super().__init__(command, timeout=timeout)

base.CommandAdapter = V44CommandAdapter

if __name__ == "__main__":
    base.main()
