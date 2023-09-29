# Swap two variables.

# Method: 1

x = int(input("Enter X Value: "))
y = int(input("Enter Y Value: "))

temp = x
x = y
y = temp

print("The Value of 'X' after swapping: {}" .format(x))
print("The Value of 'Y' after swapping: {}" .format(y))
