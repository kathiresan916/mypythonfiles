#Remove duplicate in lists:

numbers = [2, 5, 8, 6, 5, 8, 2]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)