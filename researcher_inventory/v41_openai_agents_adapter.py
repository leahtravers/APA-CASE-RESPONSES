#!/usr/bin/env python3
"""Compatibility entry point for V41 contract-isolated calibration."""
from pathlib import Path

import v41_contract_isolated_openai_agents_adapter as isolated

isolated.recovery.RECOVERY_DIR = Path("researcher_inventory/runtime/v41_session_recovery")

if __name__ == "__main__":
    raise SystemExit(isolated.main())
