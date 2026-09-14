#!/usr/bin/env python3
"""V32 calibration entry point.

V32 changes worker-visible research-coordinate selection, class-boundary, and
relation-package guidance only. Hidden evaluator alignment, immutable workbook
gates, gold/pass criteria, holdout gates, and command timeout remain unchanged.
"""
from __future__ import annotations

from researcher_inventory import v20_calibration_runner as v20
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v32_task_rules import V32_BASE_RULES, V32_CLASS_RULES

apparatus.BASE_RULES = V32_BASE_RULES
apparatus.CLASS_RULES = V32_CLASS_RULES

base = v20.base
_OriginalCommandAdapter = base.CommandAdapter


class V32CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 1500):
        super().__init__(command, timeout=timeout)


base.CommandAdapter = V32CommandAdapter

if __name__ == "__main__":
    base.main()
