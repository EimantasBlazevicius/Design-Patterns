
class Order:
    UNPAID = 0
    PAID = 1
    SHIPPED = 2
    DELIVERED = 3

    def __init__(self):
        self.state = self.UNPAID

    def pay(self):
        if self.state == self.UNPAID:
            self.state = self.PAID
            print('Payed :), Good job')
        elif self.state == self.PAID:
            print('already Payed')
        elif self.state == self.SHIPPED:
            print('already paid and shipped')
        elif self.state == self.DELIVERED:
            print('you already paid and delivered')

    def ship(self):
        if self.state == self.UNPAID:
            print('Cant ship, UNPAID')
        elif self.state == self.PAID:
            self.state = self.SHIPPED
            print('Your order is sent')
        elif self.state == self.SHIPPED:
            print('Already shipped, wait for it')
        elif self.state == self.DELIVERED:
            print('Can not ship delivered product again')

    def deliver(self):
        if self.state == self.UNPAID:
            print('Long path ahead - Pay first')
        elif self.state == self.PAID:
            print('Wait for the shipping')
        elif self.state == self.SHIPPED:
            self.state = self.DELIVERED
            print('You order is delivered now')
        elif self.state == self.DELIVERED:
            print('Already Delivered')


if __name__ == "__main__":
    order = Order()
    print(order.state)
    order.pay()

