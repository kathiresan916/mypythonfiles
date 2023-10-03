"""To Find Max number in the Given Values"""


def max_number(number):
    """Find Max Number"""
    return max(number)


find_max = [int(x)
            for x in input("Enter Number Separated by Spaces: ").split()]
result = max_number(find_max)
print(result)
