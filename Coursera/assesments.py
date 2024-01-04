'''age1 = input("how old are you:?")
age2 = input("how old is your best friend:?")
x = int(age1)
y = int(age2)
print(str(x+y))
'''
"""def fruit_color(fruit):
    if fruit == 'apple':
        return 'red'
    elif fruit == 'banana':
        return 'yellow'
    elif fruit == 'pear':
        return 'green'
        
print(fruit_color('apple'))
"""

"""def traffic_report(light):
    if light == 'red':
        return 'stop'
    elif light == 'yellow':
        return 'slow'
    elif light == 'green':
        return 'go'
        
print(traffic_report('orange'))"""

"""def grade_report(grade):
    if grade >= 80:
        return "Excellent"
    elif grade >=50:
        return "Pass"

check=grade_report(40)
print(check)"""


def collect_vowels(s):
    '''(str) -> str
    Collect a number of vowels in S.
    '''
    vowels = ''
    for char in s:
        if char in 'aeiouAEIOU':
            vowels = vowels + char
    return vowels


def count_vowels(s):
    num_vowels = 0
    for char in s:
        if char in 'aeiouAEIOU':
            num_vowels = num_vowels + 1
    return num_vowels


collect = collect_vowels("BRB")
check = count_vowels("Happy Birthday..!")
print(check, collect)
