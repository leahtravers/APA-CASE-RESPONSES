#!/usr/bin/env python3
"""V13 calibration entry point.

V13 changes worker contract/orchestration only. The evaluator-only semantic
alignment and non-consuming cross-class diagnostics remain the validated V12
harness behavior. No worker input, archetype, or holdout material is added here.
"""
from researcher_inventory import v12_calibration_runner as v12


if __name__ == "__main__":
    v12.base.main()
