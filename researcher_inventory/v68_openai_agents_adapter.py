#!/usr/bin/env python3
"""V68 OpenAI Agents adapter: reuse proven transport/session machinery with V68 contract binding."""
import os

from researcher_inventory import v60_openai_agents_adapter as prior

os.environ.setdefault("CONTRACT_VERSION", "RI-CONTRACT-V68")
os.environ.setdefault("RI_CONTRACT_FILE", "researcher_inventory/AGENT_CONTRACT_V68.md")
os.environ.setdefault("RI_SESSION_RECOVERY_DIR", "researcher_inventory/runtime/v68_session_recovery")

if __name__ == "__main__":
    prior.main()
