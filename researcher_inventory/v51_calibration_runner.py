#!/usr/bin/env python3
"""V51 calibration entry point using role-bearing proposition resolution."""
from researcher_inventory import v34_calibration_runner as v34
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v51_task_rules import V51_BASE_RULES, V51_CLASS_RULES

apparatus.BASE_RULES = V51_BASE_RULES
apparatus.CLASS_RULES = V51_CLASS_RULES

if __name__ == "__main__":
    v34.base.main()
