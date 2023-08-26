a=int(input("Enter Your Number:"))
if a<=1:
    print(a, "is not a Primer Number")
elif a==2 or a==3:
    print(a, "is a Prime Number")
elif a%2==0 or a%3==0:
    print(a, "is not a Prime number")
else:
    print(a, "is a Prime number")