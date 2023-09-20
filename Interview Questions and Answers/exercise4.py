#Print the sum of the current number and the previous number:

print("Printing current and previous number sum in a range(10)")
previous_num = 0

for i  in range (1,11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, "Sum: ", x_sum)
    previous_num = i
