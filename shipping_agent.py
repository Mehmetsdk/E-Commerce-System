# ShippingAgent (Teslimat Ajansı)
class ShippingAgent:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def ship_order(self, order_id):
        print(f"Shipping Order {order_id}")
