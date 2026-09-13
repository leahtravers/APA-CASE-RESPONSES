#!/usr/bin/env python3
"""V18 sealed-holdout entry point.

Delegates to the sealed holdout harness and applies the same neutral V18 task rules
used in calibration. This module does not read or emit holdout content itself.
"""
from researcher_inventory import holdout_runner as base
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v18_task_rules import V18_BASE_RULES, V18_CLASS_RULES

apparatus.BASE_RULES = V18_BASE_RULES
apparatus.CLASS_RULES = V18_CLASS_RULES

_OriginalCommandAdapter = base.CommandAdapter


class V18CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 480):
        super().__init__(command, timeout=timeout)


base.CommandAdapter = V18CommandAdapter


if __name__ == "__main__":
    base.main()
