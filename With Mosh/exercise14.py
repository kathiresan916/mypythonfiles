#Print Series:

"""
output:
*****
**
*****
**
**
"""

numbers = [1, 2, 3, 4, 5]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += '*'
    print(output)