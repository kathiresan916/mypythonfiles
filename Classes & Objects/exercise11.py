#Create a base class called Employee with properties name and salary. Create  a derived class called Manager that inherits from Employee and adds a property department. Write a method in Manager to display the name, salary, and department of the manager. 

class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, project):
        super().__init__(name, salary)
        self.project=project
    
    def display(self):
        print("Name is:", self.name, "Salary is:", self.salary, "Project is:", self.project)

kathir=Manager("Kathiresan Selvaraj", "32,500", "NAB")
kathir.display()
