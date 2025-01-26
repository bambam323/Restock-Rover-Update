from app.monitor import ProductMonitor
from app.notify import Notifier
from app.checkout import CheckoutHandler

def main():
    product_url = "https://example.com/product"
    monitor_interval = 10  # Check every 10 seconds

    monitor = ProductMonitor(product_url, monitor_interval)
    notifier = Notifier()
    checkout = CheckoutHandler()

    print("Starting Restock Rover...")

    while True:
        if monitor.is_in_stock():
            print("Product is back in stock!")
            notifier.send_notification("Product is in stock! Starting checkout...")
            checkout.automate_checkout()
            break

if __name__ == "__main__":
    main()
