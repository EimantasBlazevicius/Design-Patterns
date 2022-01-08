class TransportInterface:
    def give_ride(self):
        pass


class Car(TransportInterface):
    def give_ride(self):
        print("Give ride by car")


class Bike(TransportInterface):
    def give_ride(self):
        print("Give ride by bike")

# ================= With Factory ================


class TransportFactory:
    @staticmethod
    def get_transport(type):
        if type == "car":
            return Car()
        if type == "bike":
            return Bike()
        assert 0, "Coudn't find transport "+ type


car = TransportFactory.get_transport("car")
car.give_ride()
