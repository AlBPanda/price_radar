import unittest
from datetime import datetime
from src.models import Product, PriceSnapshot, AlertRule


class TestModels(unittest.TestCase):
    def test_product_creation(self):
        product = Product(
            id=1,
            name="Mechanical Keyboard",
            url="https://example.com/item/1",
            target_price=120.0,
            created_at=datetime(2026, 1, 1, 12, 0)
        )
        self.assertEqual(product.name, "Mechanical Keyboard")
        self.assertEqual(product.target_price, 120.0)

    def test_price_snapshot_creation(self):
        now = datetime.now()
        snapshot = PriceSnapshot(
            id=1,
            product_id=1,
            price=99.99,
            currency="USD",
            in_stock=True,
            recorded_at=now
        )
        self.assertEqual(snapshot.price, 99.99)
        self.assertTrue(snapshot.in_stock)

    def test_alert_rule_default(self):
        rule = AlertRule(id=1, product_id=1, threshold_price=100.0)
        self.assertTrue(rule.notify_on_drop_only)


if __name__ == "__main__":
    unittest.main()
