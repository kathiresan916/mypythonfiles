"""Dictionaries"""

user_input = input("Enter Number: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}
OUTPUT = ""
for ch in user_input:
    OUTPUT += digits_mapping.get(ch, "!") + " "
print(OUTPUT)
