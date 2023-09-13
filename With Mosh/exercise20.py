#Find largest number in the List. 

lar_number = [54, 5454, 54545, 565, 989, 844]

max = lar_number[0]

for number in lar_number:
    if number > max:
        max = number
print(max)
