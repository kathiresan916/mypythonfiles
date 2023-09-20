#Print characters from a string that are present at even index number.

#method 2:

word = input("Enter Word: ")
print("Original word ", word)

x=list(word)

for i in x[0::2]:
    print(i)
