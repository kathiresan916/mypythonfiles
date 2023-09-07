#Simple Calculator

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if b!=0:
        return a / b
    else:
        return "Cannot divide by 0"

while True:
    print("Operations:")
    print("Enter 'add' for Addition")
    print("Enter 'sub' for Subtraction")
    print("Enter 'mul' for Multiplication")
    print("Enter 'div' for Division")
    print("Enter 'quit' to end the program")
    user_input = input(":")

    if user_input == "quit":
        break
    elif user_input in ("add", "sub", "mul", "div"):
        a=float(input("Enter First Value: "))
        b=float(input("Enter Second Value: "))

        if user_input == "add":
            print("Result:", add(a,b))
        elif user_input == "sub":
            print("Result:", sub(a,b))
        elif user_input == "mul":
            print("Result:", mul(a,b))
        elif user_input == "div":
            print("Result:", div(a,b))
    else:
        print("Invalid Input")
        




