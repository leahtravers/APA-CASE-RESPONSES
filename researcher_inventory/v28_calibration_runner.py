#!/usr/bin/env python3
"""V28 calibration entry point.

V28 changes worker-visible durable/task rules and increases only the version-specific
command timeout needed to avoid misclassifying a still-running Agent session as a
semantic failure. Hidden evaluator alignment and gold/pass criteria remain unchanged.
"""
from __future__ import annotations

from researcher_inventory import v20_calibration_runner as v20
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v28_task_rules import V28_BASE_RULES, V28_CLASS_RULES

apparatus.BASE_RULES = V28_BASE_RULES
apparatus.CLASS_RULES = V28_CLASS_RULES

base = v20.base
_OriginalCommandAdapter = base.CommandAdapter


class V28CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 1500):
        super().__init__(command, timeout=timeout)


base.CommandAdapter = V28CommandAdapter

if __name__ == "__main__":
    base.main()
