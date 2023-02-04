class Order:

    def __init__(self):
        self.items = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, price):
        self.items.append(name)
        self.prices.append(price)

    def total_price(self):
        return sum(self.prices)

    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        else:
            print(f"Unknown payment type: {payment_type}")


order = Order()
order.add_item("Item 1", 70)
order.add_item("Item 2", 140)
order.add_item("Item 3", 35)

print(order.total_price())
order.pay("debit", "0372846")
