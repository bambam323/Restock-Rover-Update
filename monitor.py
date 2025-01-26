import requests
from bs4 import BeautifulSoup
import time

class ProductMonitor:
    def __init__(self, url, interval):
        self.url = url
        self.interval = interval

    def is_in_stock(self):
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            stock_element = soup.find("div", {"id": "stock-status"})
            if stock_element and "In Stock" in stock_element.text:
                return True
            time.sleep(self.interval)
        except Exception as e:
            print(f"Error checking stock: {e}")
        return False
