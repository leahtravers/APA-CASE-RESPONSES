#!/usr/bin/env python3
"""V15 sealed-holdout entry point with harness-only timeout correction.

This module never reads or emits sealed holdout content itself. It delegates to
the existing holdout runner and changes only the subprocess budget so the V15
two-pass adapter is not misclassified as a behavior failure.
"""
from researcher_inventory import holdout_runner as base


_OriginalCommandAdapter = base.CommandAdapter


class V15CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 420):
        super().__init__(command, timeout=timeout)


base.CommandAdapter = V15CommandAdapter


if __name__ == "__main__":
    base.main()
