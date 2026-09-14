#!/usr/bin/env python3
"""V29 calibration entry point.

V29 changes only worker-visible durable/task grain. Hidden evaluator alignment and
gold/pass criteria remain unchanged. V28's longer command timeout is retained.
"""
from __future__ import annotations

from researcher_inventory import v20_calibration_runner as v20
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v29_task_rules import V29_BASE_RULES, V29_CLASS_RULES

apparatus.BASE_RULES = V29_BASE_RULES
apparatus.CLASS_RULES = V29_CLASS_RULES

base = v20.base
_OriginalCommandAdapter = base.CommandAdapter


class V29CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 1500):
        super().__init__(command, timeout=timeout)


base.CommandAdapter = V29CommandAdapter

if __name__ == "__main__":
    base.main()
