#!/usr/bin/env python3
"""V15 calibration entry point.

Evaluator behavior remains the validated V12 semantic-alignment evaluator.
V15 restores the independent stateless verification pass. The longer adapter
budget is a harness-only correction for the known V13 subprocess timeout; it
changes no worker instructions, archetype, scoring rule, or holdout content.
"""
from researcher_inventory import v12_calibration_runner as v12


base = v12.base
_OriginalCommandAdapter = base.CommandAdapter


class V15CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 420):
        super().__init__(command, timeout=timeout)


base.CommandAdapter = V15CommandAdapter


if __name__ == "__main__":
    base.main()
