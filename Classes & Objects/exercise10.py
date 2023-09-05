#Create a base class called Vehicle with a method start() that prints "Vehicles Started." Create a derived class called Car that inherits from vehicle and overrides the start() method to print "Car Started"

class Vehicle():
    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    def start(self):
        print("Car Started")

BMW = Car()

BMW.start()
