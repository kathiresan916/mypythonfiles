#Calculate sum of Numbers 1 to 50:

total_sum = 0
a=int(input("Enter a number:"))
for i in range(1, a+1):
    total_sum = total_sum + i
    print(total_sum)