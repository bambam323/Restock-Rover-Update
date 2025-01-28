import unittest
from notify import Notifier

class TestNotifier(unittest.TestCase):
    def setUp(self):
        self.notifier = Notifier()

    def test_send_notification(self):
        # Mock sending a notification
        self.notifier._send = lambda message: f"Sent: {message}"
        result = self.notifier.send_notification("Test message")
        self.assertEqual(result, "Sent: Test message", "Notification should be sent successfully")

if __name__ == "__main__":
    unittest.main()
