#Create a class called student. Create a variable = name and register number using constructor. Create a function called display which should display the name and register number of the student. 

class Student:
    def __init__(self):
        self.name = ""
        self.register_number= ""

    def display(self):
        print("Name:", self.name)
        print("Register Number:", self.register_number)

register1=Student()
register2=Student()

register1.name="Kathiresan"
register1.register_number="001"

register2.name="Selvaraj"
register2.register_number="002"

register1.display()
register2.display()





