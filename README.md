Understanding the Classes in Our Modular E-Commerce System
In our e-commerce application, each class is designed to handle a specific responsibility, following the Single Responsibility Principle. Let’s break them down, one by one, and explain their role in the system.

1. EventBus: The Backbone of Communication
The EventBus is the foundation of the event-driven architecture. It enables components to communicate without being directly dependent on each other.

Responsibilities
Allows components to subscribe to specific events.
Enables components to emit events, triggering all associated subscribers.
Code Explanation
python
Kopyala
Düzenle
class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, handler):
        if event_type not in self.subscribers:
            self.subscribers[event_type = []
        self.subscribers[event_type].append(handler)

    def emit(self, event_type, data):
        if event_type in self.subscribers:
            for handler in self.subscribers[event_type]:
                handler(data)
subscribe(event_type, handler): Registers a handler (callback function) to respond to a specific event type.
emit(event_type, data): Invokes all handlers for the given event type, passing along the data.
2. OrderAgent: Creating Orders
The OrderAgent is responsible for creating new orders and notifying the system when an order is created.

Responsibilities
Generate a new order with an ID and customer name.
Emit an order_created event to notify the rest of the system.
Code Explanation
python
Kopyala
Düzenle
class OrderAgent:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def create_order(self, order_id, customer):
        print(f"Order {order_id} for {customer} created.")
        self.event_bus.emit("order_created", {"order_id": order_id, "customer": customer})
create_order(order_id, customer): Simulates the creation of an order and uses the EventBus to notify other components.
3. PaymentAgent: Processing Payments
The PaymentAgent handles payment processing for orders. Once payment is successful, it emits a payment_successful event.

Responsibilities
Process payments for a given order.
Notify the system upon successful payment.
Code Explanation
python
Kopyala
Düzenle
class PaymentAgent:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def process_payment(self, order_id, amount):
        print(f"Processing payment for Order {order_id} with amount {amount}.")
        self.event_bus.emit("payment_successful", {"order_id": order_id, "amount": amount})
process_payment(order_id, amount): Simulates payment processing and triggers the payment_successful event.
4. InventoryAgent: Checking Stock
The InventoryAgent verifies if the required products are in stock. Depending on the result, it emits either an inventory_check_passed or inventory_check_failed event.

Responsibilities
Check inventory for specific products and quantities.
Emit events based on stock availability.
Code Explanation
python
Kopyala
Düzenle
class InventoryAgent:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def check_inventory(self, order_id, product_id, quantity):
        print(f"Checking inventory for Order {order_id}, Product {product_id}, Quantity {quantity}")
        in_stock = True  # Assume stock is always available
        if in_stock:
            self.event_bus.emit("inventory_check_passed", {"order_id": order_id, "product_id": product_id})
        else:
            self.event_bus.emit("inventory_check_failed", {"order_id": order_id, "product_id": product_id})
check_inventory(order_id, product_id, quantity): Checks stock and emits the appropriate event.
5. ShippingAgent: Shipping Orders
The ShippingAgent is responsible for shipping the order once all prior steps are completed.

Responsibilities
Ship the order when all requirements are met.
Code Explanation
python
Kopyala
Düzenle
class ShippingAgent:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def ship_order(self, order_id):
        print(f"Shipping Order {order_id}")
ship_order(order_id): Simulates the process of shipping an order.
6. MainWindow: The User Interface
The MainWindow class ties the system together with a simple graphical interface, allowing users to interact with the system.

Responsibilities
Display buttons for creating orders, processing payments, and shipping orders.
Update the UI to reflect the current order status.
React to events emitted by the agents.
Code Explanation
python
Kopyala
Düzenle
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

        self.setup_ui()
        self.current_order = None

        self.event_bus.subscribe("order_created", self.on_order_created)

    def setup_ui(self):
        self.label = tk.Label(self.root, text="E-commerce System", font=("Arial", 16))
        self.label.pack()

        self.create_order_button = tk.Button(self.root, text="Create Order", command=self.create_order)
        self.create_order_button.pack()

    def create_order(self):
        order_id = randint(1000, 9999)
        customer = f"Customer {randint(1, 5)}"
        self.order_agent.create_order(order_id, customer)

    def on_order_created(self, data):
        print(f"Order Created: {data['order_id']} for {data['customer']}")
setup_ui(): Sets up the Tkinter buttons and labels.
create_order(): Triggers the order creation process.
Conclusion
By splitting the responsibilities into separate classes:

Each component is self-contained and reusable.
Testing is simplified as each class can be tested independently.
The application is easy to maintain and extend.
