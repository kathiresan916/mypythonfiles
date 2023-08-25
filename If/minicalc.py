#Excercise: 6
a=int(input("Enter a value:"))
b=int(input("Enter b Value:"))

add=a+b
sub=a-b
mul=a*b
div=a/b

operation=input("add/sub/mul/div :")

if(operation=="add"):
    print("Your Addition is:", add)
elif(operation=="sub"):  
    print("Your Subtraction is:", sub)
elif(operation=="mul"):
    print("Your Multiply is:", mul)
else:
    print("Your Division is:", div)
