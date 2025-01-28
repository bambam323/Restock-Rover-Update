from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from cryptography.fernet import Fernet
import time

class CheckoutHandler:
    def __init__(self):
        # Secure encryption key (store this securely)
        key = Fernet.generate_key()
        self.cipher_suite = Fernet(key)

        # Encrypted credentials (replace these with your actual encrypted values)
        self.encrypted_username = self.cipher_suite.encrypt(b"your_username")
        self.encrypted_password = self.cipher_suite.encrypt(b"your_password")
        self.encrypted_card_number = self.cipher_suite.encrypt(b"your_card_number")

    def decrypt_data(self, encrypted_data):
        return self.cipher_suite.decrypt(encrypted_data).decode('utf-8')

    def setup_driver(self):
        options = Options()
        options.add_argument('--headless')  # Run in headless mode
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        service = Service("path_to_chromedriver")  # Replace with the correct path to your chromedriver
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    def login(self, driver, url):
        username = self.decrypt_data(self.encrypted_username)
        password = self.decrypt_data(self.encrypted_password)
        
        driver.get(url)
        time.sleep(2)  # Allow page to load
        driver.find_element(By.ID, "login_username_field").send_keys(username)
        driver.find_element(By.ID, "login_password_field").send_keys(password)
        driver.find_element(By.ID, "login_submit_button").click()

    def add_to_cart_and_checkout(self, driver, product_url):
        driver.get(product_url)
        time.sleep(2)  # Allow page to load
        driver.find_element(By.ID, "add_to_cart_button").click()
        time.sleep(1)
        driver.find_element(By.ID, "proceed_to_checkout_button").click()

    def enter_payment_and_shipping(self, driver, shipping_address):
        card_number = self.decrypt_data(self.encrypted_card_number)
        
        driver.find_element(By.ID, "card_number_field").send_keys(card_number)
        driver.find_element(By.ID, "name_on_card_field").send_keys("Your Name")
        driver.find_element(By.ID, "expiry_date_field").send_keys("12/25")
        driver.find_element(By.ID, "cvv_field").send_keys("123")
        driver.find_element(By.ID, "shipping_address_field").send_keys(shipping_address)
        driver.find_element(By.ID, "place_order_button").click()

    def automate_checkout(self, product_url, login_url, shipping_address):
        driver = self.setup_driver()
        try:
            print("Logging in...")
            self.login(driver, login_url)

            print("Adding product to cart and proceeding to checkout...")
            self.add_to_cart_and_checkout(driver, product_url)

            print("Entering payment and shipping details...")
            self.enter_payment_and_shipping(driver, shipping_address)

            print("Checkout completed successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            driver.quit()
