#Create a class called Animal with a method sound() that prints "Animal Makes a Sound." Create a derived class called dog that inherits from Animal and overrides the sound() method to print "Dog Barks". Create another derived class called Bird that inherits from Animal and override the sound() method to print "Birds Sing"

class Animal():
    def sound(self):
        print("Animal Makes Sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

class Bird(Animal):
    def sound(self):
        print("Birds Sing")

jack=Dog()
vellachi=Bird()
animal1=Animal()

animal1.sound()
jack.sound()
vellachi.sound()

"""This is my first Program without any help from google & chatGPT"""

"""Awesome Kathir, Keep it up..!"""