#!/usr/bin/env python3
"""V57 calibration entry point using the preserved hidden evaluator with class-native completeness rules."""
from researcher_inventory import v52_calibration_runner as v52
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v57_task_rules import V57_BASE_RULES, V57_CLASS_RULES

apparatus.BASE_RULES = V57_BASE_RULES
apparatus.CLASS_RULES = V57_CLASS_RULES

if __name__ == "__main__":
    v52.v34.base.main()
