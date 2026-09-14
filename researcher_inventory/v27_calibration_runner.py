#!/usr/bin/env python3
"""V27 calibration entry point.

V27 changes worker-visible durable/task rules only. Hidden evaluation remains the
existing evaluator-alignment layer unchanged. Gold rows and pass criteria are not
modified.
"""
from __future__ import annotations

from researcher_inventory import v20_calibration_runner as v20
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v27_task_rules import V27_BASE_RULES, V27_CLASS_RULES

apparatus.BASE_RULES = V27_BASE_RULES
apparatus.CLASS_RULES = V27_CLASS_RULES

base = v20.base

if __name__ == "__main__":
    base.main()
