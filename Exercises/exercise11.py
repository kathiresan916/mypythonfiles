"""Find & Allocate Even Numbers"""


def find_even(numbers):
    """Fillter Even Numbers"""
    return [num for num in numbers if num % 2 == 0]


user_input = input("Enter Values: ")
try:
    filter_numbers = [int(num) for num in user_input.split()]
    result = find_even(filter_numbers)
    print(f"Unsorted Result: {result} | Sorted Result: {sorted(result)}")
except ValueError:
    print("Please enter Valid Integers")
