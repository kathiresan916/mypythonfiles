Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def count_vowels(s):
...     num_vowels = 0
...     for char in s:
...         if char in 'aeiouAEIOU':
...             num_vowels = num_vowels + 1
