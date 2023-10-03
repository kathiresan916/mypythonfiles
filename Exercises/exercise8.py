"""Check the word is Palindrome"""


def is_palindrome(palindrome_check):
    """Check Palindrome"""
    return palindrome_check == palindrome_check[::-1]


check = is_palindrome(input("Enter String: "))
print(check)
