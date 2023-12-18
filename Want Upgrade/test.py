# Class & Objects:

class Car:
    def start_engine(self):
        print("Car Started")


class ElectricCar(Car):
    def charge_battery(self):
        print("Battery Charging")


my_car = ElectricCar()
my_car.start_engine()
