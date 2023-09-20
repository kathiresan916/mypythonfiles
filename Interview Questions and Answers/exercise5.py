#Print characters from a string that are present at even index number.


str = input("Eneter Word: ")
print("Oringinal String is ", str)
result = len(str)
print("Printing Only Even Chars ")
for i in range(0, result -1, 2):
    print("Index[", i, "]", str[i])