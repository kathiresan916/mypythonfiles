"""Prime number or not"""


def is_prime(number):
    """Enter number is Prime or Not"""
    if number <= 1:
        return "Entered Number is Not a Prime Number"
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return "Entered Number is Not a Prime Number"
        return "Entered Numer is a Prime Number"


check_prime = int(input("Enter a Number: "))
RESULT = is_prime(check_prime)
print(RESULT)
