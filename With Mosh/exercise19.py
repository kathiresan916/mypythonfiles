#Find the largest number in the List. Using loop statements. 

largest_numbers = [ 545, 6545, 564, 6565, 2154]

max = largest_numbers[0]

for number in largest_numbers:
    if number > max:
        max = number
print(max)
