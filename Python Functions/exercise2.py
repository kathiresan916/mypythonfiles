#Find even or odd using Functions:

def even_odd(a):
    if a%2==0:
        return "Even."
    else:
        return "Odd."
    
a=int(input("Enter Number: "))

result=even_odd(a)

print("You're Entered Number is,", result)