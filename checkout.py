import requests

class CheckoutHandler:
    def __init__(self):
        self.user_credentials = {"username": "user", "password": "pass"}
        self.payment_details = {"card_number": "1111-2222-3333-4444", "expiry": "01/25", "cvv": "123"}
        self.checkout_url = "https://example.com/checkout"

    def automate_checkout(self):
        try:
            login_response = requests.post("https://example.com/login", data=self.user_credentials)
            if login_response.status_code == 200:
                print("Logged in successfully.")

            checkout_response = requests.post(self.checkout_url, data=self.payment_details)
            if checkout_response.status_code == 200:
                print("Checkout completed successfully!")
            else:
                print("Failed to complete checkout.")
        except Exception as e:
            print("Checkout error: {e}")
