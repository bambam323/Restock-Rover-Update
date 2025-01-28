from monitor import ProductMonitor
from notify import Notifier
from checkout import CheckoutHandler

def main():
    product_url = "https://www.target.com/p/pok-233-mon-trading-card-game-scarlet-38-violet-prismatic-evolutions-booster-bundle/-/A-93954446#lnk=sametab"
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
