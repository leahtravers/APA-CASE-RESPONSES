#!/usr/bin/env python3
"""V36 sealed-holdout entry point.

Delegates to the protected holdout harness and applies the same neutral V36 task
rules used in calibration. This module does not print or persist sealed holdout
source/content outside the existing protected runtime boundary.
"""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v36_task_rules import V36_BASE_RULES, V36_CLASS_RULES

apparatus.BASE_RULES = V36_BASE_RULES
apparatus.CLASS_RULES = V36_CLASS_RULES

_OriginalCommandAdapter = base.CommandAdapter


class V36CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 1500):
        super().__init__(command, timeout=timeout)


base.CommandAdapter = V36CommandAdapter

if __name__ == "__main__":
    base.main()
