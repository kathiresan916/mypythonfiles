#Number to String:

user_input = input("Enter Number: ")

dic = {
    "1" : "One", 
    "2" : "Two",
    "3" : "Three", 
    "4" : "Four", 
    "5" : "Five", 
    "6" : "Six", 
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nione", 
    "0" : "Zero"
}

output = ""

for number in user_input:
    output += dic.get(number, "Space!") + " "
print(output)