#Create a class called Calculator. Create 2 variables a and b. Create a functions called add, sub, mul, div all functions should take 2 variables as parameter. Pass  the a and b value through object():

class Calculator:
    def __init__ (self, a, b):
        self.a = a
        self.b = b
    
    def add (self):
        return self.a + self.b
    
    def sub (self):
        return self.a - self.b
    
    def mul (self):
        return self.a * self.b
    
    def div (self):
        if self.b!=0:
            return self.a / self.b
        else:
            return "Cannot Divided by Zero"

a = int (input("Enter A Value: "))
b = int (input("Enter B Value: "))

calc=Calculator(a, b)

addition_result = calc.add()
subtraction_result = calc.sub()
multiplication_result = calc.mul()
division_result = calc.div()

print("Addition Result is:", addition_result)
print("Subtraction Result is: ", subtraction_result)
print("Multiplication Result is: ", multiplication_result)
print("Division Result is: ", division_result)