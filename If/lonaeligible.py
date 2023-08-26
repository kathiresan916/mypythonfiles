salary=int(input("Enter your Salary:"))
age=int(input("Enter your Age:"))

if(salary>=20000 or age<=25):
    loan=int(input("Required Loan Amount: "))
    if(loan>=50000):
        print("You're eligible Loan Amount is 50000")
    else:
        print("You're Eligible for Loan")
    
else:
    print("You're not eligible for Loan")