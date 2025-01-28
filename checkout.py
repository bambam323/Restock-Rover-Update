from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class CheckoutHandler:
    def __init__(self):
        # Path to chromedriver.exe
        self.chromedriver_path = "C:\\Users\\amber\\OneDrive\\Desktop\\chromedriver-win64\\chromedriver.exe"

    def setup_driver(self):
        """Sets up the Selenium WebDriver with Chrome."""
        service = Service(self.chromedriver_path)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in headless mode (optional)
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    def automate_checkout(self, product_url, login_url, shipping_address):
        """Automates the login and checkout process."""
        driver = self.setup_driver()
        try:
            # Log in
            print("Logging in...")
            driver.get(login_url)
            time.sleep(2)  # Allow page to load
            driver.find_element(By.ID, "login_username_field").send_keys("your_username")
            driver.find_element(By.ID, "login_password_field").send_keys("your_password")
            driver.find_element(By.ID, "login_submit_button").click()

            # Add product to cart
            print("Adding product to cart...")
            driver.get(product_url)
            time.sleep(2)  # Allow page to load
            driver.find_element(By.ID, "add_to_cart_button").click()
            time.sleep(1)
            driver.find_element(By.ID, "proceed_to_checkout_button").click()

            # Enter payment and shipping details
            print("Entering payment and shipping details...")
            driver.find_element(By.ID, "card_number_field").send_keys("your_card_number")
            driver.find_element(By.ID, "name_on_card_field").send_keys("Your Name")
            driver.find_element(By.ID, "expiry_date_field").send_keys("12/25")
            driver.find_element(By.ID, "cvv_field").send_keys("123")
            driver.find_element(By.ID, "shipping_address_field").send_keys(shipping_address)
            driver.find_element(By.ID, "place_order_button").click()

            print("Checkout completed successfully!")
        except Exception as e:
            print("An error occurred during checkout: {e}")
        finally:
            driver.quit()
