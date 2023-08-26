age=int(input("Enter your Age:"))
if age<=11:
    print("Your age is:", age, "and you're Child")
elif age>=12 and age<=18:
    print("Your age is:", age, "and you're a Teenager")
elif age>=19 and age<=50:
    print("You're age is:", age, "and you're a Adult")
else:
    print("Your age is:", age, "and you're a Senior")