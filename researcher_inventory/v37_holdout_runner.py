#!/usr/bin/env python3
"""V37 sealed-holdout entry point.

Delegates to the protected holdout harness and applies the same neutral V37 task
rules used in calibration. This module does not print or persist sealed holdout
source/content outside the existing protected runtime boundary.
"""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v37_task_rules import V37_BASE_RULES, V37_CLASS_RULES

apparatus.BASE_RULES = V37_BASE_RULES
apparatus.CLASS_RULES = V37_CLASS_RULES

_OriginalCommandAdapter = base.CommandAdapter


class V37CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 1500):
        super().__init__(command, timeout=timeout)


base.CommandAdapter = V37CommandAdapter

if __name__ == "__main__":
    base.main()
