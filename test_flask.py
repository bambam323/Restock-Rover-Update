import unittest
from main import app

class TestFlaskRoutes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_route(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Restock Rover is running!")

    def test_start_monitoring_route(self):
        response = self.client.post("/start-monitoring")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Started monitoring for restock.")

if __name__ == "__main__":
    unittest.main()
