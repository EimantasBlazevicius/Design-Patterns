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


class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self):
        pass


class AuthorizeSMS(Authorizer):
    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f"Eyy, doing verification stuff of on your code {code}")
        self.authorized = True

    def is_authorized(self):
        return self.authorized


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: Authorizer):
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order):
        if self.authorizer.is_authorized() is not True:
            print('Not Authorized to do stuff')

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


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email, authorizer: Authorizer):
        self.email = email
        self.authorizer = authorizer

    def pay(self, order):
        if self.authorizer.is_authorized() is not True:
            print('Not Authorized to do stuff')

        print("Processing paypal payment type")
        print(f"Verifying email: {self.email}")
        order.status = "paid"


def main():
    order = Order()
    order.add_item("Item 1", 70)
    order.add_item("Item 2", 140)
    order.add_item("Item 3", 35)

    print(order.total_price())
    authorizer = AuthorizeSMS()
    authorizer.verify_code(546164616)
    processor = PaypalPaymentProcessor("eima.blaz@gmail.com", authorizer)
    processor.pay(order)
    if order.status == "paid":
        print("Payment was a great success!!")


if __name__ == "__main__":
    main()
