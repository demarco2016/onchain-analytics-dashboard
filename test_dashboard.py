#!/usr/bin/env python3
"""Basic tests for analytics dashboard."""

import unittest
from dashboard import get_network_metrics, get_historical_trends

class TestDashboard(unittest.TestCase):
    def test_network_metrics(self):
        metrics = get_network_metrics("ethereum")
        self.assertIn("network", metrics)
        self.assertIn("source", metrics)

    def test_historical_trends(self):
        trends = get_historical_trends(3)
        self.assertEqual(len(trends), 3)

if __name__ == "__main__":
    unittest.main()
