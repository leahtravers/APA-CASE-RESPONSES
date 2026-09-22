from __future__ import annotations

import unittest
from unittest import mock

from researcher_inventory import v156_openai_agents_adapter as v156


class V156ResultRetrievalTests(unittest.TestCase):
    def test_collects_final_answer_from_later_page(self):
        calls: list[str] = []

        def fake_request(path: str, method: str = "GET", body=None):
            calls.append(path)
            if "after=item-100" in path:
                return {
                    "data": [{
                        "id": "item-101",
                        "type": "message",
                        "role": "assistant",
                        "status": "completed",
                        "phase": "final_answer",
                        "content": [{"type": "output_text", "text": "{\"ok\": true}"}],
                    }],
                    "has_more": False,
                    "last_id": "item-101",
                }
            return {
                "data": [{"id": "item-100", "type": "trace"}],
                "has_more": True,
                "last_id": "item-100",
            }

        with mock.patch.object(v156.recovery, "request", side_effect=fake_request):
            answers = v156._collect_final_answers("sess-test")

        self.assertEqual(answers, ['{"ok": true}'])
        self.assertEqual(len(calls), 2)
        self.assertIn("after=item-100", calls[1])

    def test_initial_absence_rereads_same_session(self):
        item_reads = 0
        session_reads = 0

        def fake_request(path: str, method: str = "GET", body=None):
            nonlocal item_reads, session_reads
            if "/items?" in path:
                item_reads += 1
                if item_reads == 1:
                    return {"data": [], "has_more": False}
                return {
                    "data": [{
                        "id": "final-1",
                        "type": "message",
                        "role": "assistant",
                        "status": "completed",
                        "phase": "final_answer",
                        "content": [{"type": "output_text", "text": "{\"value\": 1}"}],
                    }],
                    "has_more": False,
                }
            if path == "/agents/sessions/sess-same":
                session_reads += 1
                return {"id": "sess-same", "status": "idle"}
            raise AssertionError(path)

        with mock.patch.object(v156.recovery, "request", side_effect=fake_request), \
             mock.patch.object(v156.time, "sleep", return_value=None):
            value = v156._paged_final_answer("sess-same")

        self.assertEqual(value, '{"value": 1}')
        self.assertEqual(item_reads, 2)
        self.assertEqual(session_reads, 1)


if __name__ == "__main__":
    unittest.main()
