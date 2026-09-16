#!/usr/bin/env python3
"""V50 calibration entry point using class-native coverage-without-atomization resolution."""
from researcher_inventory import v34_calibration_runner as v34
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v50_task_rules import V50_BASE_RULES, V50_CLASS_RULES

apparatus.BASE_RULES = V50_BASE_RULES
apparatus.CLASS_RULES = V50_CLASS_RULES

if __name__ == "__main__":
    v34.base.main()
