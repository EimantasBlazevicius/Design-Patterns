from abc import ABC, abstractmethod


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


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class PaymentProcessorSMS(PaymentProcessor):

    @abstractmethod
    def auth_sms(self, code):
        pass


class DebitPaymentProcessor(PaymentProcessorSMS):
    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False

    def auth_sms(self, code):
        print(f"verifying SMS code {code}")
        self.verified = True

    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessorSMS):
    def __init__(self, email):
        self.email = email
        self.verified = False

    def auth_sms(self, code):
        print(f"verifying SMS code {code}")
        self.verified = True

    def pay(self, order):
        print("Processing paypal payment type")
        print(f"Verifying email: {self.email}")
        order.status = "paid"


order = Order()
order.add_item("Item 1", 70)
order.add_item("Item 2", 140)
order.add_item("Item 3", 35)

print(order.total_price())
processor = PaypalPaymentProcessor("eima.blaz@gmail.com")
processor.auth_sms(8943164681)
processor.pay(order)
if order.status == "paid":
    print("Payment was a great success!!")
