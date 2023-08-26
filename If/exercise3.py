'''

a=int(input("Enter A Value:"))
b=int(input("Enter B Value:"))
c=int(input("Enter C Value:"))
numbers=[a,b,c]
sorted_numbers=sorted(numbers)
print(sorted_numbers)

'''

a=int(input("Enter A Value:"))
b=int(input("Enter B Value:"))
c=int(input("Enter C Value:"))

if a<=b and a<=c:
    smallest=a
    if b<=c:
        middle=b
        largest=c
    else:
        middle=c
        largest=b
elif b<=a and b<=c:
    smallest=b
    if a<=c:
        middle=a
        largest=c
    else:
        middle=c
        largest=a
else:
    smallest=c
    if a<=b:
        middle=a
        largest=b
    else:
        middle=b
        largest=a
print("Ascending order values are:", smallest, middle, largest)