#!/usr/bin/env python3
"""V21 calibration entry point.

V21 changes worker-visible durable/task rules only. Hidden evaluation remains the
V20 evaluator-alignment layer unchanged: immutable gold rows and pass criteria are
not modified. This keeps worker-behavior correction separate from harness repair.
"""
from __future__ import annotations

from researcher_inventory import v20_calibration_runner as v20
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v21_task_rules import V21_BASE_RULES, V21_CLASS_RULES

# Override only the neutral worker task rules. Importing V20 above installs the
# evaluator-only alignment normalization already admitted by the V20 correction.
apparatus.BASE_RULES = V21_BASE_RULES
apparatus.CLASS_RULES = V21_CLASS_RULES

base = v20.base


if __name__ == "__main__":
    base.main()
