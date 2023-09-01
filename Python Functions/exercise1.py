#Create a function called add(), div(), mul() and sub():

def add(a,b):
    print("Addition:")
    return a+b

def sub(a,b):
    print("Subtraction:")
    return a-b

def mul(a,b):
    print("Multiplication:")
    return a*b
      
def div(a,b):
    print("Division:")
    if b==0:
        return "Cannot divide by zero"
    return a/b

a=int(input("Enter A Value: "))
b=int(input("Enter B Value: "))

print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))
