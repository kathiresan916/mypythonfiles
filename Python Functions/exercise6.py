#GEt Input from user for a and b. Function called add() which should return the sum of a and b. Any multiply that sum with c. 

def add(a,b):
    return a+b

a=int(input("Enter A Value:"))
b=int(input("Enter B Value:"))
c=int(input("Enter C Value:"))

result=add(a,b)

print("Sum of (a+b)*c is:", result*c)

