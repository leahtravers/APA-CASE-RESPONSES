#!/usr/bin/env python3
"""V23 sealed-holdout entry point.

Delegates to the existing sealed holdout harness and applies the same neutral V23
task rules used in calibration. This module does not read, print, or persist sealed
holdout source/content outside the existing protected runtime boundary.
"""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v23_task_rules import V23_BASE_RULES, V23_CLASS_RULES

apparatus.BASE_RULES = V23_BASE_RULES
apparatus.CLASS_RULES = V23_CLASS_RULES

_OriginalCommandAdapter = base.CommandAdapter


class V23CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 480):
        super().__init__(command, timeout=timeout)


base.CommandAdapter = V23CommandAdapter


if __name__ == "__main__":
    base.main()
