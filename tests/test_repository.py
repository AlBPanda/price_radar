import unittest
from src.db import get_connection, init_db
from src.repository import ProductRepository


class TestProductRepository(unittest.TestCase):
    def setUp(self):
        self.conn = get_connection(":memory:")
        init_db(self.conn)
        self.repo = ProductRepository(self.conn)

    def tearDown(self):
        self.conn.close()

    def test_add_and_get_product(self):
        product = self.repo.add_product("Kablosuz Kulaklık", "https://example.com/kulaklik", 1500.0)
        self.assertIsNotNone(product.id)
        self.assertEqual(product.name, "Kablosuz Kulaklık")

        fetched = self.repo.get_product(product.id)
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.name, "Kablosuz Kulaklık")
        self.assertEqual(fetched.target_price, 1500.0)

    def test_list_products(self):
        self.repo.add_product("Ürün 1", "https://example.com/1")
        self.repo.add_product("Ürün 2", "https://example.com/2")
        products = self.repo.list_products()
        self.assertEqual(len(products), 2)

    def test_add_and_get_price_history(self):
        prod = self.repo.add_product("Akıllı Saat", "https://example.com/saat")
        self.repo.add_price_snapshot(prod.id, 2500.0, "TRY", True)
        self.repo.add_price_snapshot(prod.id, 2350.0, "TRY", True)

        history = self.repo.get_price_history(prod.id)
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0].price, 2350.0)
        self.assertEqual(history[1].price, 2500.0)


if __name__ == "__main__":
    unittest.main()
