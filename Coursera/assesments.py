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

'''
def collect_vowels(s):
    
   
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
'''

'''
def common_chars(s1, s2):
    res = ''
    if ch in s2:
        for ch in s1:
            res = res + ch
    return res


check = common_chars('abb', 'ab')
print(check)
'''
'''
num = 6
while num > 0:
    num = num - 2
    print(num)
'''
'''
s = 'xyz'
i = 0
while i < len(s) and not (s[i] in 'aeiouAEIOU'):
    print(s[i])
    i = i + 1
'''

s = 'xyz'
for char in s:
    if not (char in 'aeiouAEIOU'):
        print(char)
