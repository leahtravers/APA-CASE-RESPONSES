#!/usr/bin/env python3
"""V19 sealed-holdout entry point.

Delegates to the sealed holdout harness and applies the same neutral V19 task rules
used in calibration. This module does not read, print, or persist sealed holdout
source/content outside the existing protected runtime boundary.
"""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v19_task_rules import V19_BASE_RULES, V19_CLASS_RULES

apparatus.BASE_RULES = V19_BASE_RULES
apparatus.CLASS_RULES = V19_CLASS_RULES

_OriginalCommandAdapter = base.CommandAdapter


class V19CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 480):
        super().__init__(command, timeout=timeout)


base.CommandAdapter = V19CommandAdapter


if __name__ == "__main__":
    base.main()
