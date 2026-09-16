#!/usr/bin/env python3
"""V58 calibration entry point using the preserved hidden evaluator with relation-anchored task rules."""
from researcher_inventory import v52_calibration_runner as v52
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v58_task_rules import V58_BASE_RULES, V58_CLASS_RULES

apparatus.BASE_RULES = V58_BASE_RULES
apparatus.CLASS_RULES = V58_CLASS_RULES

if __name__ == "__main__":
    v52.v34.base.main()
