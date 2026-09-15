#!/usr/bin/env python3
"""V38 sealed-holdout entry point.

Delegates to the protected holdout harness and applies the same neutral V38 task
rules used in calibration. This module does not print or persist sealed holdout
source/content outside the existing protected runtime boundary.
"""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v38_task_rules import V38_BASE_RULES, V38_CLASS_RULES

apparatus.BASE_RULES = V38_BASE_RULES
apparatus.CLASS_RULES = V38_CLASS_RULES

_OriginalCommandAdapter = base.CommandAdapter


class V38CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 1500):
        super().__init__(command, timeout=timeout)


base.CommandAdapter = V38CommandAdapter

if __name__ == "__main__":
    base.main()
