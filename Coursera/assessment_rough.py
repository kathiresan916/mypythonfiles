'''
def for_version(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0 and not found_even:
            total = total + num
        else:
            found_even = True

    return total


print(for_version(10))


numbers = [1, 4, 3]
# numbers.reverse() True
# reversed(numbers) False
numbers = reversed(numbers)
print(numbers)[3, 4, 1]


veggies = ['carrot', 'broccoli', 'potato', 'asparagus']
veggies.insert(veggies.index('broccoli'), 'celery')
print(veggies)

a = [1, 2, 3]
b = a
# MISSING CODE HERE
# b[-2] = 'A' True
# a[1] = 'A' True
# a = [1, 'A', 3]
# b = [1, 'A', 3] True
b[1] = 'AB'
a[1] = a[1][0] True
print(a, b)


a = [1, 2, 3]
b = [1, 2, 3]
# b[1] = 'AB' a[1] = a[1][0] False
# a = [1, 'A', 3] b = [1, 'A', 3] True
# b[-2] = 'A' False
# a[1] = 'A' False
print(a, b)



def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1


values = [1, 2, 3]
print(increment_items(values, 2))
print(values)

values = []
for num in range(3, 10, 3):
    values.append(num)
print(values) True

values = []
for num in range(1, 4):
    values.append(num * 3)
print(values) True

values = []
for num in range(3, 9, 3):
    values.append(num)
print(values) False

values = []
for num in range(1, 3):
    values.append(num * 3)
print(values) False


for num in range(3, 8, 20):  # 3,23,8 - True / 3,19,8 - False / 3, 20, 8 - True / 3, 20,8 - False
    print(num)


start = 524
end = 10508
current_num = start
sum_while = 0

while current_num <= end:
    if current_num % 2 == 0:
        sum_while += current_num
    current_num += 1

print("Sum using while loop:", sum_while)


def for_version(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0 and not found_even:
            total = total + num
        else:
            found_even = True
 
    return total 




    while playlist.count(song) > 3:
        playlist.pop(song)
    
        while playlist.count(song) > 3:
        playlist.remove(song)



fruits = ['banana', 'apple', 'pear', 'peach']
fruits.insert(fruits.index('pear'), 'watermelon')
print(fruits)



def mystery(s):
    i = 0
    result = ''

    while not s[i].isdigit():
        result = result + s[i]
        i = i + 1

    return result


call = mystery('abc123')  # executed('123') & ('123abc') .
print(call)             # error ('abc')


# Define the range
start = 1523
end = 10503

# Initialize the sum
sum_of_odd_numbers = 0

# Iterate through the range and add odd numbers to the sum
for num in range(start, end + 1):
    if num % 2 != 0:  # Check if the number is odd
        sum_of_odd_numbers += num

# Print the result
print("Sum of odd numbers:", sum_of_odd_numbers)


numbers = [1, 4, 3]
# numbers.reverse() True
# reversed(numbers) False
# numbers = reverse(numbers) False
numbers = numbers.reverse()
print(numbers)[1, 4, 3]


fruits = ['banana', 'apple', 'pear', 'peach']
fruits.insert(fruits.index('pear'), 'watermelon')
print(fruits)



def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1


values = [1, 2, 3]
print(increment_items(values, 2))
print(values)


fruits = ['banana', 'apple', 'pear', 'peach']
fruits.insert(fruits.index('pear'), 'watermelon')
print(fruits)



def example(L):
    """ (list) -> list
    """
    i = 0
    result = []
    while i < len(L):
        result.append(L[i])
        i = i + 3
    return result


# Define the range
start = 1523
end = 10503

# Initialize the sum
sum_of_odd_numbers = 0

# Iterate through the range and add odd numbers to the sum
for num in range(start, end + 1):
    if num % 2 != 0:  # Check if the number is odd
        sum_of_odd_numbers += num

# Print the result
print("Sum of odd numbers:", sum_of_odd_numbers)


fruits = ['banana', 'apple', 'pear', 'peach']
fruits.insert(fruits.index('pear'), 'watermelon')
print(fruits)

Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'a' in ['mom', 'dad']
False
len('mom') in [1,2,3]
True
int('3') in [len('a'), len('b'), len('abc')]
True
len([1,2,3]) == len(['a', 'b', 'c'])
True
'3' in [1, 2, 3]
False
[1, 2, 3] in len('mom')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    [1, 2, 3] in len('mom')
TypeError: argument of type 'int' is not iterable
'''
