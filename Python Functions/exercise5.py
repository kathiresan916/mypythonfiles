#Using Return Statment, user inputs valid or invalid:

set_username="Kathiresan"
set_password="12345"

def validate():
    if (set_username) == username and set_password == password:
        return True
    else:
        return False
  
username = input("Enter Username:")
password = input("Enter Password:")

result=validate()

print("You've Entered Username & Password is:", result)

