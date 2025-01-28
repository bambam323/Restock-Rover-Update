import unittest
from monitor import ProductMonitor

class TestProductMonitor(unittest.TestCase):
    def setUp(self):
        self.product_url = "https://example.com/product"
        self.monitor = ProductMonitor(self.product_url, 10)

    def test_is_in_stock(self):
        # Mock the response from the website to simulate in-stock
        self.monitor._fetch_product_page = lambda: "<html><body>In Stock</body></html>"
        self.assertTrue(self.monitor.is_in_stock(), "Product should be in stock")

    def test_is_not_in_stock(self):
        # Mock the response from the website to simulate out-of-stock
        self.monitor._fetch_product_page = lambda: "<html><body>Out of Stock</body></html>"
        self.assertFalse(self.monitor.is_in_stock(), "Product should not be in stock")

if __name__ == "__main__":
    unittest.main()
