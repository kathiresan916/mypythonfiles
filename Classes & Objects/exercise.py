#Classes and Objects:

"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

p1 = Person("John", 30)
print(p1)
"""

class goa:
    name=""
    drink=""
    def party(self):
        print("Let's Party!")
    def beach(self):
        print("Enjoy the View of Beach!")

kathir = goa()
kiran = goa()
stephen = goa()
anish = goa()

kathir.name = "Kathir"
kiran.name = "Kiran"
stephen.name = "Stephen"
anish.name = "Anish Kumar"

kathir.drink ="No"
kiran.drink = "Yes"
stephen.drink = "No"
anish.drink = "Yes"

print(kathir.name, "Drink:", kathir.drink)
print(kiran.name, "Drint:", kiran.drink)
print(stephen.name, "Drink:", stephen.drink)
print(anish.name, "Drink:", anish.drink)

