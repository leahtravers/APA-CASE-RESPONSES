#!/usr/bin/env python3
"""Compatibility entry point for V36 calibration after harness isolation.

Historical pre-correction V36 adapter content remains preserved in Git history and
workflow run 34939188598. Forward V36 execution delegates to the additive
contract-isolated successor while retaining the existing recovery directory name
expected by the workflow evidence-preservation step.
"""
from pathlib import Path

import v36_contract_isolated_openai_agents_adapter as isolated

isolated.recovery.RECOVERY_DIR = Path("researcher_inventory/runtime/v36_session_recovery")


if __name__ == "__main__":
    raise SystemExit(isolated.main())
