Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
courses = 3
courses != 3
False
courses == 3.0
True
3 >= courses
True
3 = courses
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
cents = 34
cents < 10 or cents > 100
False
not cents * 2 > 34
False
not cents < 12
True
not not cents >= 35
False
dollars = 18
cents = 53
not dollars == 18 or not cents == 53
False
dollars == 10 or not cents != 53
True
not dollars < 10 and cents > 15
True
not (dollars < cents and dollars > 0)
False
3 <= x < 10
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    3 <= x < 10
NameError: name 'x' is not defined
x >= 3 and x > 10
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    x >= 3 and x > 10
NameError: name 'x' is not defined
x = 5
x >=3 and x > 10
False
not (3 <= x and x < 10)
False
3 <= x and x < 10
True
3 <= x or x < 10
True
eggs = 12
if eggs % 12 == 0:
    return False
SyntaxError: incomplete input
age1 = input("How Old are you?: ")
How Old are you?: 12
age2 = input("How old your friend?:")
How old your friend?:13
print(str(int(age1 + age2)))
1213
x = int(age1)
y = int(age2)
print(str(x + y))
25
print(int(age1) + int(age2))
25
print(int(age1 + age2))
1213
import math
factorial = 8
dir help
SyntaxError: incomplete input
dir help math
SyntaxError: invalid syntax
help dir
SyntaxError: incomplete input
import math
factorial_of_8 = math.factorial(8)
print(factorial_of_8)
40320
def traffic_report(light):
    if light == 'red':
        return 'stop'
    elif light == 'yellow':
        return 'slow'
    elif light == 'green':
        return 'go'

    
print(traffic_report('yellow'))
slow
def fruit_color(fruit):
    if fruit == 'apple':
        return 'red'
    elif fruit == 'banana':
        return 'yellow'
    elif fruit == 'pear':
        return 'green'

    
print(fruit_color('peach'))
None
def weather_report(temp):
    if temp >= 20:
        return 'warm enough for ice cream'
    elif temp >= 0:
        return 'above freezing'

    
print(weather_report(30))
warm enough for ice cream
print(weather_report(-5))
None
print(weather_report(20))
warm enough for ice cream
print(weather_report(10))
above freezing
grade1 = 0.00
grade2 = 100.0
total = 0
grade_count = 0
if grade1 >= 50:
    total = total + grade1
    grade_count = grade_count + 1
else:
    total = tatal + grade2
    grade_count = grade_count + 1

    
Traceback (most recent call last):
  File "<pyshell#82>", line 5, in <module>
    total = tatal + grade2
NameError: name 'tatal' is not defined. Did you mean: 'total'?
grade1 = 0.00
grade2 = 100.0
total = 0
grade_count = 0
if grade1 >= 50:
    total = total + grade1
    grade_count = grade_count + 1
else:
    total = total + grade2
    grade_count = grade_count + 1
    
SyntaxError: multiple statements found while compiling a single statement





grade1 = 0.0
grade2 = 100.0
total = 0
grade_count = 0
if grade1 >= 50:
    total = total + grade1
    grade_count = grade_count + 1
else:
    total = total + grade2
    grade_count = grade_count + 1
if grade_count > 0:
    
SyntaxError: invalid syntax
grade1 = 0.0
grade2 = 100.0
total = 0
grade_count = 0
SyntaxError: multiple statements found while compiling a single statement
if grade1 >= 50 and grade2 >= 50:
    total = grade1 + grade2
    grade_count = 2

    
if grade_count >0:
    print(total / grade_count)
else:
    print(0.0)

0.0
if grade1 >= 50:
    total = total + grade1
    grade_count = grade_count + 1
if grade2 >= 50:
    
SyntaxError: invalid syntax
instructors = 2
instructors < 2 or instructors > 4
False
instructors < 0 or instructors > 1
True
not instructos < 1
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    not instructos < 1
NameError: name 'instructos' is not defined. Did you mean: 'instructors'?
not instructors < 1
True
instructors == 2 and instructors < 2
False
dollars = 18
cents = 53
not dollars == 18 or not cents == 53
False
not (dollars < cents and dollars > 0)
False
not dollars < 10 and cents > 15
True
(not dollars == 18) or cents == 53
True
import math
ceiling_result = math.ceil(84.2)
print(ceiling_result)
85
'mile' in 'smiles'
True
'I' in 'smiles'
False
'smiles' in 'smiles'
True
'limes' in 'smiles'
False
len("hello World!")
12
s = 'Call Me Maybe'
s[12]
'e'
s[13]
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    s[13]
IndexError: string index out of range
s[-0]
'C'
>>> s[-1]
'e'
>>> len(s)
13
>>> s[-10:-13]
''
>>> s = 'Call Me Maybe'
>>> s[-09:]
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> s[-9:]
' Me Maybe'
>>> s[-9:-13]
''
>>> s[-10:]
'l Me Maybe'
>>> s[-13:-10]
'Cal'
>>> s[-13:-9]
'Call'
>>> s[-9:-13]
''
>>> s = 'Call Me Maybe'
>>> s[-5:] = 'Perhaps'
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    s[-5:] = 'Perhaps'
TypeError: 'str' object does not support item assignment
>>> s = s[:-5] + 'Perhaps'
>>> s
'Call Me Perhaps'
>>> s = s[0:-5] + 'Perhaps'
>>> s
'Call Me PePerhaps'
>>> s = s - s[-5:] + 'Perhaps'
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    s = s - s[-5:] + 'Perhaps'
TypeError: unsupported operand type(s) for -: 'str' and 'str'
