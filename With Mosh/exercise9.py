'''If name is less then 3 characters long name must be at least 3 characters.
otherwise if it's more then 50 characters long name can be a maximum of 50 characters
otherwise, name looks good. '''


name = input("Enter your Name: ")

if len(name) <=3:
    print("Name must be at least 3 characters.")
elif len(name) >=50:
    print("Name can be maximum of 50 Characters")
else:
    print("Name looks good.")
