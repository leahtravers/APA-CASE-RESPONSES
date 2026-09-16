#!/usr/bin/env python3
"""V52 calibration entry point using source-coordinate coverage."""
from researcher_inventory import v34_calibration_runner as v34
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v52_task_rules import V52_BASE_RULES, V52_CLASS_RULES

apparatus.BASE_RULES = V52_BASE_RULES
apparatus.CLASS_RULES = V52_CLASS_RULES

if __name__ == "__main__":
    v34.base.main()
