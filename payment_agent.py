# PaymentAgent (Ödeme Ajansı)
class PaymentAgent:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def process_payment(self, order_id, amount):
        print(f"Processing payment for Order {order_id} with amount {amount}.")
        self.event_bus.emit("payment_successful", {"order_id": order_id, "amount": amount})
