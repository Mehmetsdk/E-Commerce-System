    # InventoryAgent (Stok Ajansı)
class InventoryAgent:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def check_inventory(self, order_id, product_id, quantity):
        print(f"Checking inventory for Order {order_id}, Product {product_id}, Quantity {quantity}")
        in_stock = True  # For simplicity, stock is always available
        if in_stock:
            self.event_bus.emit("inventory_check_passed", {"order_id": order_id, "product_id": product_id})
        else:
            self.event_bus.emit("inventory_check_failed", {"order_id": order_id, "product_id": product_id})
