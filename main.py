from flask import Flask, request
from monitor import ProductMonitor
from notify import Notifier
from checkout import CheckoutHandler
import threading
import time

app = Flask(__name__)

# Define the product monitor and handlers
product_url = "https://www.target.com/p/pok-233-mon-trading-card-game-scarlet-38-violet-prismatic-evolutions-booster-bundle/-/A-93954446#lnk=sametab"
monitor_interval = 10  # Check every 10 seconds
monitor = ProductMonitor(product_url, monitor_interval)
notifier = Notifier()
checkout = CheckoutHandler()

# Background thread for monitoring
def monitor_product():
    print("Starting Restock Rover...")
    while True:
        if monitor.is_in_stock():
            print("Product is back in stock!")
            notifier.send_notification("Product is in stock! Starting checkout...")
            checkout.automate_checkout()
            break
        time.sleep(monitor_interval)

@app.route("/")
def home():
    return "Restock Rover is running!", 200

@app.route("/start-monitoring", methods=["POST"])
def start_monitoring():
    thread = threading.Thread(target=monitor_product)
    thread.start()
    return "Started monitoring for restock.", 200

if __name__ == "__main__":
    import os
    # Ensure the app listens on port 8080 as required by Cloud Run
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
