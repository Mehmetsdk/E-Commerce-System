
Building a Modular E-Commerce System with Python and Tkinter
In today’s world of complex systems and microservices, designing software with modularity in mind is essential. In this blog, we’ll walk through building a simple, modular e-commerce system using Python, Tkinter for the UI, and a custom-built event bus for managing communication between components.

This system showcases fundamental software engineering principles like event-driven architecture and separation of concerns, making it an ideal project for beginners and enthusiasts.

The Goal
We’ll create an e-commerce system that allows users to:

Create orders.
Process payments.
Check inventory.
Ship orders.
Each component will function independently, communicating through an event bus. The interface will be powered by Tkinter, Python’s built-in GUI library.

The Modular Design
Our application is divided into the following classes:

EventBus: Manages communication between different parts of the system.
OrderAgent: Handles order creation.
PaymentAgent: Processes payments.
InventoryAgent: Verifies product availability.
ShippingAgent: Manages order shipping.
MainWindow: Provides the user interface.
Each class resides in its own Python file, ensuring modularity and ease of maintenance.

The Code
1. EventBus: The Communication Hub
The EventBus class allows components to subscribe to and emit events, decoupling their functionality.

python
Kopyala
Düzenle
# event_bus.py
class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, handler):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(handler)

    def emit(self, event_type, data):
        if event_type in self.subscribers:
            for handler in self.subscribers[event_type]:
                handler(data)
                
2. Agents: Handling Business Logic
Each agent focuses on one specific task:

OrderAgent creates orders and emits an event.
PaymentAgent processes payments and notifies success.
InventoryAgent checks stock and emits the result.
ShippingAgent handles shipping once all prior steps are completed.
Here’s the code for OrderAgent:

python
Kopyala
Düzenle
# order_agent.py
class OrderAgent:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def create_order(self, order_id, customer):
        print(f"Order {order_id} for {customer} created.")
        self.event_bus.emit("order_created", {"order_id": order_id, "customer": customer})
        
The other agents follow a similar pattern. Each one performs its task and communicates the result via the EventBus.

3. MainWindow: The User Interface
Using Tkinter, we’ll create a simple interface with buttons for each step of the process.

python
Kopyala
Düzenle
# main_window.py
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
        
Running the Application
The main.py file ties everything together and starts the application:

python
Kopyala
Düzenle
# main.py
from tkinter import Tk
from event_bus import EventBus
from order_agent import OrderAgent
from payment_agent import PaymentAgent
from inventory_agent import InventoryAgent
from shipping_agent import ShippingAgent
from main_window import MainWindow

if __name__ == "__main__":
    event_bus = EventBus()
    order_agent = OrderAgent(event_bus)
    payment_agent = PaymentAgent(event_bus)
    inventory_agent = InventoryAgent(event_bus)
    shipping_agent = ShippingAgent(event_bus)

    root = Tk()
    app = MainWindow(root, event_bus, order_agent, payment_agent, inventory_agent, shipping_agent)
    root.mainloop()
    
Benefits of This Architecture
Scalability: New features or agents can be added without altering existing code.
Reusability: Each class is self-contained and can be reused in other projects.
Testability: Components can be tested independently.
Conclusion
This project demonstrates how you can design a modular system in Python using an event-driven architecture. While the example is simplified, the principles here can be extended to build more robust and scalable applications.

If you’d like to explore the full code, check out the GitHub repository here (insert link to your repository).

v
