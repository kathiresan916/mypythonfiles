def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
try:
    age = int(input("Enter your age: "))
    checked_age = check_age(age)
    print("Your age is:", checked_age)
except ValueError as e:
    print("Error:", e)