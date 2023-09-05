#Create a base class called Person with a constructor that takes a name as a parameter. Create a derived class called Student that inherits from Person and has a constructor that takes a parameter called grade. Write a method in Student to display the name and

class Person():
    def __init__(self, name):
        self.name=name
        """print("Names is: Kathiresan Selvaraj")"""

class Student(Person):
    def __init__ (self, name, grade):
        super().__init__(name)
        self.grade=grade
        """print("Grade is: Destintion")"""

    def display(self):
        print(self.name, self.grade)
    
kathir=Student("Kathir", "A")
kathir.display()

