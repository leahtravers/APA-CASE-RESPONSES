#!/usr/bin/env python3
"""V36 calibration entry point.

V36 restores sparse event-map coordinate admission after V35 over-enumeration,
while retaining V34 evaluator-order isolation, immutable archetype gates, and
candidate-only boundaries.
"""
from researcher_inventory import v34_calibration_runner as v34
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v36_task_rules import V36_BASE_RULES, V36_CLASS_RULES

apparatus.BASE_RULES = V36_BASE_RULES
apparatus.CLASS_RULES = V36_CLASS_RULES

if __name__ == "__main__":
    v34.base.main()
