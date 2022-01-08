# == abstract ride classes
class DeluxeInterface:
    def give_deluxe_ride(self):
        pass


class PremiumInterface:
    def give_premium_ride(self):
        pass


# == concrete ride classes
class CarDeluxRide(DeluxeInterface):
    def give_deluxe_ride(self):
        print("Delux car ride")


class BikeDeluxRide(DeluxeInterface):
    def give_deluxe_ride(self):
        print("Delux bike ride")


class CarPremiumRide(PremiumInterface):
    def give_premium_ride(self):
        print("Premium car ride")


class BikePremiumRide(PremiumInterface):
    def give_premium_ride(self):
        print("Premium bike ride")


# == abstract Ride Factory
class RideFactoryInterface:
    def get_ride(self, category): pass


# == concrete Ride Factory
class Car(RideFactoryInterface):
    @staticmethod
    def get_ride(category):
        if category == "premium":
            return CarPremiumRide()
        if category == "delux":
            return CarDeluxRide()
        assert 0, "Couldn't find car " + category


class Bike(RideFactoryInterface):
    @staticmethod
    def get_ride(category):
        if category == "premium":
            return BikePremiumRide()
        if category == "delux":
            return BikeDeluxRide()
        assert 0, "Couldn't find Bike " + category


class TransportFactory:
    @staticmethod
    def get_transport(type, category):
        if type == "car":
            return Car().get_ride(category)
        if type == "bike":
            return Bike().get_ride(category)


car = TransportFactory.get_transport(type="car", category="premium")
car.give_premium_ride()
