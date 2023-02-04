class State:
    def pay(self):
        pass

    def ship(self):
        pass

    def deliver(self):
        pass


class Order:
    def __init__(self):
        self.UNPAID = UnpaidState(self)
        self.PAID = Paid(self)
        self.SHIPPED = ShippedState(self)
        self.DELIVERED = DeliveredState(self)
        self.state = self.UNPAID

    def set_state(self, state: State):
        self.state = state

    def pay(self):
        self.state.pay()

    def ship(self):
        self.state.ship()

    def deliver(self):
        self.state.deliver()


class UnpaidState(State):
    def __init__(self, context):
        self.context = context

    def pay(self):
        self.context.set_state(self.context.PAID)
        print("Payment accepted")

    def ship(self):
        print('Pay first')

    def deliver(self):
        print('Pay first')


class Paid(State):
    def __init__(self, context):
        self.context = context

    def pay(self):
        print("This is done already, Ship now")

    def ship(self):
        self.context.set_state(self.context.SHIPPED)
        print('Your order is Shipped now')

    def deliver(self):
        print('Send the order first')


class ShippedState(State):
    def __init__(self, context):
        self.context = context

    def pay(self):
        print('Shoould already be at your place')

    def ship(self):
        print('Shoould already be at your place')

    def deliver(self):
        self.context.set_state(self.context.DELIVERED)
        print('Delivered now')


class DeliveredState(State):
    def __init__(self, context):
        self.context = context

    def pay(self):
        print('Already delivered nothing to do')

    def ship(self):
        print('Already delivered nothing to do')

    def deliver(self):
        print('Already delivered nothing to do')


if __name__ == "__main__":
    order = Order()
    print(order.state)
    order.pay()
    order.deliver()

