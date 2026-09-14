#!/usr/bin/env python3
"""V26 calibration entry point.

V26 changes worker-visible durable/task rules only. Hidden evaluation remains the
existing evaluator-alignment layer unchanged. Gold rows and pass criteria are not
modified.
"""
from __future__ import annotations

from researcher_inventory import v20_calibration_runner as v20
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v26_task_rules import V26_BASE_RULES, V26_CLASS_RULES

apparatus.BASE_RULES = V26_BASE_RULES
apparatus.CLASS_RULES = V26_CLASS_RULES

base = v20.base

if __name__ == "__main__":
    base.main()
