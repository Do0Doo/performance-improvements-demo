import unittest

from perf_demo.analytics import normalize_label, summarize_products


class AnalyticsTests(unittest.TestCase):
    def test_normalize_label_is_stable(self):
        self.assertEqual(normalize_label("  Mobile Apps  "), "mobile apps")
        self.assertEqual(normalize_label("mobile apps"), "mobile apps")

    def test_summarize_products_aggregates_by_category(self):
        products = [
            {"category": " Mobile Apps ", "units": 12},
            {"category": "mobile apps", "units": 3},
            {"category": "Analytics", "units": 7},
            {"category": "analytics", "units": 5},
        ]

        self.assertEqual(
            summarize_products(products),
            {"analytics": 12, "mobile apps": 15},
        )


if __name__ == "__main__":
    unittest.main()
