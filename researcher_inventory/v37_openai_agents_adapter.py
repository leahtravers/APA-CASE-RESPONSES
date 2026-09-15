#!/usr/bin/env python3
"""Compatibility entry point for V37 contract-isolated calibration."""
from pathlib import Path

import v37_contract_isolated_openai_agents_adapter as isolated

isolated.recovery.RECOVERY_DIR = Path("researcher_inventory/runtime/v37_session_recovery")


if __name__ == "__main__":
    raise SystemExit(isolated.main())
