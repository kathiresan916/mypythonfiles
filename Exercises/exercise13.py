"""Factorization Found"""


def is_factorization(number):
    """Found Factorization"""
    factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1
    return factors


check_factor = int(input("Enter a Number: "))
result = is_factorization(check_factor)
print(result)
