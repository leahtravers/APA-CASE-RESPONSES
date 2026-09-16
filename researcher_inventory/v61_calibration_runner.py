#!/usr/bin/env python3
"""V61 calibration entry point using the preserved hidden evaluator and class-projection task rules."""
from researcher_inventory import v52_calibration_runner as v52
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v61_task_rules import V61_BASE_RULES, V61_CLASS_RULES

apparatus.BASE_RULES = V61_BASE_RULES
apparatus.CLASS_RULES = V61_CLASS_RULES

if __name__ == "__main__":
    v52.v34.base.main()
