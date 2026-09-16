#!/usr/bin/env python3
"""V49 calibration entry point using research-role resolution."""
from researcher_inventory import v34_calibration_runner as v34
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v49_task_rules import V49_BASE_RULES, V49_CLASS_RULES

apparatus.BASE_RULES = V49_BASE_RULES
apparatus.CLASS_RULES = V49_CLASS_RULES

if __name__ == "__main__":
    v34.base.main()
