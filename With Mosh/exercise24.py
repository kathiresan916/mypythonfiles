#Number to String: using Dictionary method

type_phone_number = input("Enter Phone Number: ")

dic = {
    "1" : "One", 
    "2" : "Two",
    "3" : "Three", 
    "4" : "Four", 
    "5" : "Five",
    "6" : "Six", 
    "7" : "Seven", 
    "8" : "Eight", 
    "9" : "Nine", 
    "0" : "Zero"
}

user_input = ""

for number in type_phone_number:
    user_input += dic.get(number, "!") + " "
print(user_input)