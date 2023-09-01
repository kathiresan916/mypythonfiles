#Create a function called add(), div(), mul() and sub():
a=int(input("Enter A Value:"))
b=int(input("Enter B Value:"))

def add():
    print("Addition:")
    print(a+b)
    
def sub():
    print("Subtraction:")
    print(a-b)
    
def mul():
    print("Multiplication:")
    print(a*b)
    
def div():
    print("Division:")
    print(a/b)
    

print("Additional Value is:", add())
print("subtraction Value is:", sub())
print("Multiplication Value is:", mul())
print("Division Value is:", div())
