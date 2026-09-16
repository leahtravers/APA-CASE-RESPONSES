#!/usr/bin/env python3
"""V47 calibration entry point using selectable-semantic-atom admission."""
from researcher_inventory import v34_calibration_runner as v34
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v47_task_rules import V47_BASE_RULES, V47_CLASS_RULES

apparatus.BASE_RULES = V47_BASE_RULES
apparatus.CLASS_RULES = V47_CLASS_RULES

if __name__ == "__main__":
    v34.base.main()
