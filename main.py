import tkinter as tk
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

    root = tk.Tk()
    app = MainWindow(root, event_bus, order_agent, payment_agent, inventory_agent, shipping_agent)
    root.mainloop()
