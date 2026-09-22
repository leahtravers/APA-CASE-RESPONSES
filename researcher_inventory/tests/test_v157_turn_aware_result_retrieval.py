from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest import mock

# Runtime adapters intentionally use script-local absolute imports because the workflow
# executes them as `python researcher_inventory/<version>_openai_agents_adapter.py`.
RI_ROOT = Path(__file__).resolve().parents[1]
if str(RI_ROOT) not in sys.path:
    sys.path.insert(0, str(RI_ROOT))

import v157_openai_agents_adapter as v157


class V157TurnAwareResultRetrievalTests(unittest.TestCase):
    def setUp(self):
        v157._BOUND_ROOT_TURNS.clear()

    def test_failed_root_turn_is_runtime_failure_not_idle_success(self):
        calls: list[str] = []

        def fake_request(path: str, method: str = "GET", body=None):
            calls.append(path)
            if "/turns?" in path:
                return {
                    "data": [{
                        "id": "turn-failed",
                        "session_id": "sess-failed",
                        "subagent_id": None,
                        "status": "failed",
                        "error": {"code": "runtime_error", "message": "bounded failure"},
                    }]
                }
            raise AssertionError(path)

        with mock.patch.object(v157.recovery, "request", side_effect=fake_request):
            with self.assertRaisesRegex(RuntimeError, "turn terminal status failed"):
                v157._turn_aware_final_answer("sess-failed")

        self.assertTrue(any("/turns?" in path for path in calls))
        self.assertFalse(any("/items?" in path for path in calls))

    def test_completed_turn_collects_exact_turn_final_answer_from_later_page(self):
        calls: list[str] = []

        def fake_request(path: str, method: str = "GET", body=None):
            calls.append(path)
            if "/turns?" in path:
                return {
                    "data": [{
                        "id": "turn-1",
                        "session_id": "sess-1",
                        "subagent_id": None,
                        "status": "completed",
                    }]
                }
            if "after=item-100" in path:
                return {
                    "data": [
                        {
                            "id": "other-final",
                            "turn_id": "turn-other",
                            "type": "message",
                            "role": "assistant",
                            "status": "completed",
                            "phase": "final_answer",
                            "content": [{"type": "output_text", "text": "ignore"}],
                        },
                        {
                            "id": "item-101",
                            "turn_id": "turn-1",
                            "type": "message",
                            "role": "assistant",
                            "status": "completed",
                            "phase": "final_answer",
                            "content": [{"type": "output_text", "text": "{\"ok\": true}"}],
                        },
                    ],
                    "has_more": False,
                    "last_id": "item-101",
                }
            if "/items?" in path:
                return {
                    "data": [{"id": "item-100", "turn_id": "turn-1", "type": "trace"}],
                    "has_more": True,
                    "last_id": "item-100",
                }
            raise AssertionError(path)

        with mock.patch.object(v157.recovery, "request", side_effect=fake_request):
            value = v157._turn_aware_final_answer("sess-1")

        self.assertEqual(value, '{"ok": true}')
        self.assertEqual(sum("/items?" in path for path in calls), 2)
        self.assertIn("after=item-100", calls[-1])

    def test_nonterminal_root_turn_is_polled_until_same_turn_completes(self):
        turn_reads = 0

        def fake_request(path: str, method: str = "GET", body=None):
            nonlocal turn_reads
            if "/turns?" in path:
                turn_reads += 1
                return {
                    "data": [{
                        "id": "turn-same",
                        "session_id": "sess-same",
                        "subagent_id": None,
                        "status": "in_progress",
                    }]
                }
            if path.endswith("/turns/turn-same"):
                turn_reads += 1
                return {
                    "id": "turn-same",
                    "session_id": "sess-same",
                    "subagent_id": None,
                    "status": "completed",
                }
            if "/items?" in path:
                return {
                    "data": [{
                        "id": "final-same",
                        "turn_id": "turn-same",
                        "type": "message",
                        "role": "assistant",
                        "status": "completed",
                        "phase": "final_answer",
                        "content": [{"type": "output_text", "text": "{\"value\": 1}"}],
                    }],
                    "has_more": False,
                }
            raise AssertionError(path)

        with mock.patch.object(v157.recovery, "request", side_effect=fake_request), \
             mock.patch.object(v157.time, "sleep", return_value=None):
            value = v157._turn_aware_final_answer("sess-same")

        self.assertEqual(value, '{"value": 1}')
        self.assertEqual(v157._BOUND_ROOT_TURNS["sess-same"], "turn-same")
        self.assertEqual(turn_reads, 2)

    def test_completed_turn_with_delayed_item_visibility_rereads_same_turn(self):
        item_reads = 0
        direct_turn_reads = 0

        def fake_request(path: str, method: str = "GET", body=None):
            nonlocal item_reads, direct_turn_reads
            if "/turns?" in path:
                return {
                    "data": [{
                        "id": "turn-delay",
                        "session_id": "sess-delay",
                        "subagent_id": None,
                        "status": "completed",
                    }]
                }
            if path.endswith("/turns/turn-delay"):
                direct_turn_reads += 1
                return {
                    "id": "turn-delay",
                    "session_id": "sess-delay",
                    "subagent_id": None,
                    "status": "completed",
                }
            if "/items?" in path:
                item_reads += 1
                if item_reads == 1:
                    return {"data": [], "has_more": False}
                return {
                    "data": [{
                        "id": "final-delay",
                        "turn_id": "turn-delay",
                        "type": "message",
                        "role": "assistant",
                        "status": "completed",
                        "phase": "final_answer",
                        "content": [{"type": "output_text", "text": "{\"ready\": true}"}],
                    }],
                    "has_more": False,
                }
            raise AssertionError(path)

        with mock.patch.object(v157.recovery, "request", side_effect=fake_request), \
             mock.patch.object(v157.time, "sleep", return_value=None):
            value = v157._turn_aware_final_answer("sess-delay")

        self.assertEqual(value, '{"ready": true}')
        self.assertEqual(item_reads, 2)
        self.assertEqual(direct_turn_reads, 1)
        self.assertEqual(v157._BOUND_ROOT_TURNS["sess-delay"], "turn-delay")


if __name__ == "__main__":
    unittest.main()
