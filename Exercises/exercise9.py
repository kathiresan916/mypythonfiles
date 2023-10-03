"""Find and Count Vowels"""


def count_vowel(check_vowel):
    """Find Vowel"""
    vowel = "aeiouAEIOU"
    return sum(1 for char in check_vowel if char in vowel)


result = count_vowel(input("Enter a String: "))
print(result)
