#!/usr/bin/env python3
"""V44 calibration entry point using canonical binding-role admission."""
from researcher_inventory import v34_calibration_runner as v34
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v44_task_rules import V44_BASE_RULES, V44_CLASS_RULES

apparatus.BASE_RULES = V44_BASE_RULES
apparatus.CLASS_RULES = V44_CLASS_RULES

if __name__ == "__main__":
    v34.base.main()
