# OrderAgent (Sipariş Ajansı)
class OrderAgent:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def create_order(self, order_id, customer):
        print(f"Order {order_id} for {customer} created.")
        self.event_bus.emit("order_created", {"order_id": order_id, "customer": customer})
