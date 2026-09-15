#!/usr/bin/env python3
"""V42 calibration entry point using research-bearing frame/binding admission."""
from researcher_inventory import v34_calibration_runner as v34
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v42_task_rules import V42_BASE_RULES, V42_CLASS_RULES

apparatus.BASE_RULES = V42_BASE_RULES
apparatus.CLASS_RULES = V42_CLASS_RULES

if __name__ == "__main__":
    v34.base.main()
