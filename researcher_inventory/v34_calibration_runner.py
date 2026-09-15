#!/usr/bin/env python3
"""V34 calibration entry point.

V34 restores the research-coordinate admission gate after V33 over-enumeration,
while retaining evaluator isolation, immutable workbook gates, and candidate-only
boundaries.
"""
from __future__ import annotations

from researcher_inventory import v33_calibration_runner as v33
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v34_task_rules import V34_BASE_RULES, V34_CLASS_RULES

apparatus.BASE_RULES = V34_BASE_RULES
apparatus.CLASS_RULES = V34_CLASS_RULES

base = v33.base

if __name__ == "__main__":
    base.main()
