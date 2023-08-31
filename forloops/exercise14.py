#Print Pattern:
n=int(input("Enter your Choice: "))
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print()