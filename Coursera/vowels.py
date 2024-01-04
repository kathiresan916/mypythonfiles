Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def count_vowels(s):
...     '''
...     char -> int
...     Count a number of vowels in s.
...     >>> count_vowels = "Happy Birthday.!"
...     3
...     >>> count_vowels = "BBB"
...     0
...     '''
...     count_vowels = 0
...     for char in s:
...         if s in 'aeiouAEIOU':
...             count_vowels = count_vowels + 1print(
...                 
SyntaxError: invalid decimal literal
>>> def count_vowels(s):
...     '''
...     char -> int
...     Count a number of vowels in s.
...     >>> count_vowels = "Happy Birthday.!"
...     3
...     >>> count_vowels = "BBB"
...     0
...     '''
...     count_vowels = 0
...     for char in s:
...         if s in 'aeiouAEIOU':
...             count_vowels = count_vowels + 1
...             print(count_vowels)
