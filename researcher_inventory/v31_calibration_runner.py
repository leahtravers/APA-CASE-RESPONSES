#!/usr/bin/env python3
"""V31 calibration entry point.

V31 changes only worker-visible durable/task grain and literal self-check guidance.
Hidden evaluator alignment, gold/pass criteria, holdout gates, and command timeout
remain unchanged.
"""
from __future__ import annotations

from researcher_inventory import v20_calibration_runner as v20
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v31_task_rules import V31_BASE_RULES, V31_CLASS_RULES

apparatus.BASE_RULES = V31_BASE_RULES
apparatus.CLASS_RULES = V31_CLASS_RULES

base = v20.base
_OriginalCommandAdapter = base.CommandAdapter


class V31CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 1500):
        super().__init__(command, timeout=timeout)


base.CommandAdapter = V31CommandAdapter

if __name__ == "__main__":
    base.main()
