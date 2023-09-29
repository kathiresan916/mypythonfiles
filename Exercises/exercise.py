# Calculate area of Triange.

a = int(input("Enter A Value: "))
b = int(input("Enter B Value: "))
c = int(input("Enter C Value: "))

sum_of_triange = (a+b+c) / 2

area = (sum_of_triange*(sum_of_triange-a) *
        (sum_of_triange-b)*(sum_of_triange-c)) ** 0.5

print("Sum of Triange Value is: ", area)
