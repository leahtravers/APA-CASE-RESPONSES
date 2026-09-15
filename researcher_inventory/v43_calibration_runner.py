#!/usr/bin/env python3
"""V43 calibration entry point using component-preserving binding reconstruction."""
from researcher_inventory import v34_calibration_runner as v34
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v43_task_rules import V43_BASE_RULES, V43_CLASS_RULES

apparatus.BASE_RULES = V43_BASE_RULES
apparatus.CLASS_RULES = V43_CLASS_RULES

if __name__ == "__main__":
    v34.base.main()
