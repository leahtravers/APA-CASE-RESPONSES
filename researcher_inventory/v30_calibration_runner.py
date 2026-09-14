#!/usr/bin/env python3
"""V30 calibration entry point.

V30 changes worker-visible durable/task grain only. Hidden evaluator alignment,
gold/pass criteria, holdout gates, and V29's longer command timeout remain unchanged.
"""
from __future__ import annotations

from researcher_inventory import v20_calibration_runner as v20
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v30_task_rules import V30_BASE_RULES, V30_CLASS_RULES

apparatus.BASE_RULES = V30_BASE_RULES
apparatus.CLASS_RULES = V30_CLASS_RULES

base = v20.base
_OriginalCommandAdapter = base.CommandAdapter


class V30CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 1500):
        super().__init__(command, timeout=timeout)


base.CommandAdapter = V30CommandAdapter

if __name__ == "__main__":
    base.main()
