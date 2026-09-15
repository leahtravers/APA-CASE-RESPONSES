#!/usr/bin/env python3
"""V35 calibration entry point.

V35 replaces the oscillating global admission gate with class-native positive
capture followed by narrow negative pruning, while retaining the V34 evaluator
isolation/alignment correction and immutable archetype gates.
"""
from researcher_inventory import v34_calibration_runner as v34
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v35_task_rules import V35_BASE_RULES, V35_CLASS_RULES

apparatus.BASE_RULES = V35_BASE_RULES
apparatus.CLASS_RULES = V35_CLASS_RULES

if __name__ == "__main__":
    v34.base.main()
