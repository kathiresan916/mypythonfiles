#Count Vowels:
'''
a=input("Enter Word: ")

for i in range(len(a)):
    if a[i] in "aeiouAEIOU":
        print(a[i],end="")

'''

a=input("Enter a String: ")
char_count=0

for char in a:
    if char in "aeiouAEIOU":
        char_count=char_count+1
print("Number of Vowels is: ", char_count)
        