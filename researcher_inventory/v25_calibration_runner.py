#!/usr/bin/env python3
"""V25 calibration entry point.

V25 changes worker-visible durable/task rules only. Hidden evaluation remains the
V20 evaluator-alignment layer unchanged. Gold rows and pass criteria are not
modified.
"""
from __future__ import annotations

from researcher_inventory import v20_calibration_runner as v20
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v25_task_rules import V25_BASE_RULES, V25_CLASS_RULES

apparatus.BASE_RULES = V25_BASE_RULES
apparatus.CLASS_RULES = V25_CLASS_RULES

base = v20.base

if __name__ == "__main__":
    base.main()
