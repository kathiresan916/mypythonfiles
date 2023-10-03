"""Count Occurances"""


def count_occurances(numbers):
    """Find Occurances"""
    occurances = {}
    for number in numbers:
        occurances[number] = occurances.get(number, 0) + 1
    return occurances


user_input = input("Enter a Values: ")
find_occurances = [int(num) for num in user_input.split()]

result = count_occurances(find_occurances)
print(result)
