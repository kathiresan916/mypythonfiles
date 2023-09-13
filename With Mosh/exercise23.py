#Dictionary types exercises:

"""
Output:
Phone Number: 1234
One Two Three Four
"""
type_phone = input("Enter Phone Number: ")

dic = {
    "1": "One",
    "2": "Tow",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight", 
    "9": "Nine",
    "0": "Zero"
}
output = ""
for number in type_phone:
    output += dic.get(number, "!") + " "
print(output)




