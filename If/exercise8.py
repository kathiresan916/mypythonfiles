grade=int(input("Enter Your Score:"))
if (grade < 0 or grade>100):
    print("Please Enter Valid Score within 0 to 100")
elif grade <=35:
    print("Your Grade is F")
elif grade <=60:
    print("Your Grade is B")
elif grade <=90:
    print("your Grade is A")
else:
    print("Your Grade is A+")
