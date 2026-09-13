#!/usr/bin/env python3
"""V14 calibration entry point.

V14 changes the durable worker grain and bounded adapter only. The validated
semantic-alignment evaluator remains unchanged. No archetype, evaluator, prior
score, or holdout material is supplied to the worker.
"""
from researcher_inventory import v12_calibration_runner as v12


if __name__ == "__main__":
    v12.base.main()
