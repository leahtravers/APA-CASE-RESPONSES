#!/usr/bin/env python3
"""V48 calibration entry point using class-native research-coordinate admission."""
from researcher_inventory import v34_calibration_runner as v34
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v48_task_rules import V48_BASE_RULES, V48_CLASS_RULES

apparatus.BASE_RULES = V48_BASE_RULES
apparatus.CLASS_RULES = V48_CLASS_RULES

if __name__ == "__main__":
    v34.base.main()
