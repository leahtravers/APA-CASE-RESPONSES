#!/usr/bin/env python3
"""V33 calibration entry point.

V33 corrects unit-resolution versus compound-construction semantics while keeping
hidden evaluation, immutable workbook gates, holdout gates, and candidate-only
boundaries unchanged.
"""
from __future__ import annotations

from researcher_inventory import v20_calibration_runner as v20
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v33_task_rules import V33_BASE_RULES, V33_CLASS_RULES

apparatus.BASE_RULES = V33_BASE_RULES
apparatus.CLASS_RULES = V33_CLASS_RULES

base = v20.base
_OriginalCommandAdapter = base.CommandAdapter


class V33CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 1500):
        super().__init__(command, timeout=timeout)


base.CommandAdapter = V33CommandAdapter

if __name__ == "__main__":
    base.main()
