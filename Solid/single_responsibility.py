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


class PaymentProcessor:

    def pay_debit(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

    def pay_credit(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


order = Order()
order.add_item("Item 1", 70)
order.add_item("Item 2", 140)
order.add_item("Item 3", 35)

print(order.total_price())
processor = PaymentProcessor()
processor.pay_debit(order, "0372846")
