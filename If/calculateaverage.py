#Excercise:9

a=int(input("Enter Score for Tamil: "))
b=int(input("Enter Score for English: "))
c=int(input("Enter Score for Maths: "))
d=int(input("Enter Score for Science: "))
e=int(input("Enter Score for Social: "))

f=(a+b+c+d+e)
print("Your Total score is:", f)

average=(f/5)
print("You're Average is:", average)

if (average >=35):
    print("You're Good")
else:
    print("Please focus on your studies")