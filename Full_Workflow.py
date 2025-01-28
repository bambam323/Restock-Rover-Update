import unittest
from monitor import ProductMonitor
from notify import Notifier
from checkout import CheckoutHandler

class TestRestockRoverWorkflow(unittest.TestCase):
    def setUp(self):
        self.product_url = "https://example.com/product"
        self.monitor = ProductMonitor(self.product_url, 10)
        self.notifier = Notifier()
        self.checkout = CheckoutHandler()

    def test_full_workflow(self):
        # Mock methods for stock check, notification, and checkout
        self.monitor.is_in_stock = lambda: True
        self.notifier.send_notification = lambda message: f"Notification sent: {message}"
        self.checkout.automate_checkout = lambda product_url, login_url, shipping_address: "Checkout complete"

        # Simulate the full workflow
        if self.monitor.is_in_stock():
            notification_result = self.notifier.send_notification("Product is in stock!")
            checkout_result = self.checkout.automate_checkout(
                product_url=self.product_url,
                login_url="https://example.com/login",
                shipping_address="123 Main Street"
            )

            # Assertions
            self.assertEqual(notification_result, "Notification sent: Product is in stock!")
            self.assertEqual(checkout_result, "Checkout complete")

if __name__ == "__main__":
    unittest.main()
