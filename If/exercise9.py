def is_palindrome(s):
    s=s.lower().replace("","")
    return s==s[::-1]
word=input("Enter your Word:")
if is_palindrome(word):
    print(word, "is Palindrome")
else:
    print(word, "is Not Palindrome")
    