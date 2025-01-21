import tkinter as tk
from random import randint

class MainWindow:
    def __init__(self, root, event_bus, order_agent, payment_agent, inventory_agent, shipping_agent):
        self.root = root
        self.event_bus = event_bus
        self.order_agent = order_agent
        self.payment_agent = payment_agent
        self.inventory_agent = inventory_agent
        self.shipping_agent = shipping_agent

        self.event_bus.subscribe("order_created", self.on_order_created)
        self.event_bus.subscribe("payment_successful", self.on_payment_successful)
        self.event_bus.subscribe("inventory_check_passed", self.on_inventory_check_passed)
        self.event_bus.subscribe("inventory_check_failed", self.on_inventory_check_failed)

        self.label = tk.Label(root, text="E-commerce System", font=("Arial", 16))
        self.label.pack()

        self.create_order_button = tk.Button(root, text="Create Order", command=self.create_order)
        self.create_order_button.pack()

        self.payment_button = tk.Button(root, text="Process Payment", command=self.process_payment, state=tk.DISABLED)
        self.payment_button.pack()

        self.ship_button = tk.Button(root, text="Ship Order", command=self.ship_order, state=tk.DISABLED)
        self.ship_button.pack()

        self.order_status_label = tk.Label(root, text="Order Status: Waiting...", font=("Arial", 12))
        self.order_status_label.pack()

        self.current_order = None  # Keeps track of the current order

    def create_order(self):
        order_id = randint(1000, 9999)
        customer = f"Customer {randint(1, 5)}"
        self.order_agent.create_order(order_id, customer)
        self.current_order = {"order_id": order_id, "customer": customer}
        self.order_status_label.config(text=f"Order Status: Created for {customer}")
        self.payment_button.config(state=tk.NORMAL)

    def process_payment(self):
        if self.current_order:
            order_id = self.current_order["order_id"]
            amount = randint(100, 500)
            self.payment_agent.process_payment(order_id, amount)
            self.order_status_label.config(text=f"Order Status: Payment Processed for Order {order_id}")
            self.inventory_agent.check_inventory(order_id, randint(1, 3), 1)
            self.ship_button.config(state=tk.NORMAL)

    def ship_order(self):
        if self.current_order:
            order_id = self.current_order["order_id"]
            self.shipping_agent.ship_order(order_id)
            self.order_status_label.config(text=f"Order Status: Shipped Order {order_id}")
            self.ship_button.config(state=tk.DISABLED)

    def on_order_created(self, data):
        print(f"Order Created: {data['order_id']} for {data['customer']}")

    def on_payment_successful(self, data):
        print(f"Payment Successful for Order {data['order_id']}")

    def on_inventory_check_passed(self, data):
        print(f"Inventory check passed for Order {data['order_id']}")

    def on_inventory_check_failed(self, data):
        print(f"Inventory check failed for Order {data['order_id']}")
