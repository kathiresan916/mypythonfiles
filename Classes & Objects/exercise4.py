#Create a class called Teacher. Create a variable = name and register number using constructor. Create a function called display which should the name and register number of the teacher. Create T1 and T2 object and pass the name and reg no value through object. 

class Teacher:
    def __init__(self, name, reg_no):
        self.name = name
        self.reg_no = reg_no

    def display(self):
        print("Name:", self.name)
        print("Register Number:", self.reg_no)

t1=Teacher("Kathiresan", "001")
t2=Teacher("Selvaraj", "002") 

t1.display()
t2.display()


#If you type (Display) variable you need to include "Object.display"
#otherwise  no issues. 

""" the follwoing without using display variable ex:

class Teacher:
    def __init__(self, name, reg_no):
        self.name = name
        self.reg_no = reg_no

t1=Teacher("Kathiresan", "001")
t2=Teacher("Selvaraj", "002") 

print("Name: ", t1.name, "|" "Register Number: ", t1.reg_no)
print("Name: ", t2.name, "|" "Regisger Number: ", t2.reg_no)


"""
