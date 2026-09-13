#!/usr/bin/env python3
"""V19 calibration entry point.

Uses the existing hidden evaluator while versioning only worker-visible neutral task
rules and subprocess timeout. No archetype/evaluator/holdout material is exposed to
the worker.
"""
from researcher_inventory import v12_calibration_runner as v12
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v19_task_rules import V19_BASE_RULES, V19_CLASS_RULES

apparatus.BASE_RULES = V19_BASE_RULES
apparatus.CLASS_RULES = V19_CLASS_RULES

base = v12.base
_OriginalCommandAdapter = base.CommandAdapter


class V19CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 480):
        super().__init__(command, timeout=timeout)


base.CommandAdapter = V19CommandAdapter


if __name__ == "__main__":
    base.main()
