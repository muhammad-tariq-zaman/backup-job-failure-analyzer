import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import analyze


def row(j, r):
    return {"job": j, "date": "2026-11-01", "result": r}


class TestBackupFailures(unittest.TestCase):
    def test_rate_computed(self):
        per_job, _ = analyze([row("Nightly", "failed"), row("Nightly", "success")])
        self.assertEqual(per_job[0][1], 0.5)

    def test_highest_first(self):
        per_job, _ = analyze([row("A", "success"), row("B", "failed")])
        self.assertEqual(per_job[0][0], "B")

    def test_overall_rate(self):
        _, overall = analyze([row("A", "failed"), row("A", "success"),
                              row("B", "success"), row("B", "success")])
        self.assertEqual(overall, 0.25)

    def test_empty(self):
        self.assertEqual(analyze([]), ([], 0.0))
