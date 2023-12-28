import math 

def area(base, height):
    return base * height / 2


def greater(one, two):
    return one > two


def even_bigger(x):
    return (2*x) ** x


def bigger(x):
    return x ** x


def add(number1, number2):
    '''Add two values'''
    print(number1 + number2)


def convert_to_celcius(fahrenheit):
    '''
    Return the number of celcius degrees equivalent to fahrenheit degrees,
    '''
    return (fahrenheit - 32) * 5/9


def convert_to_fahrenheit(celcius):
    '''
    Return the number of fahrenheit degree equivalent to celcius degree.
    '''
    return (celcius * 9/5) + 32


def perimeter(side1, side2, side3):
    '''
    (number1, number2, number3) -> Number
    Return the perimeter of a triangle with sides of length.
    side1, side2, side3.
    '''
    return side1 + side2 + side3

def semiperimeter(area1, area2, area3):
    '''
    (side1, side2, side3) -> Number
    Return the semiperimeter of a triange with side of length side1, side2, side3.
    '''
    return perimeter(side1, side2, side3) / 2

def convert_to_minutes(num_hours):
    """
    (int) -> int
    Return the number of Minutes.
    """
    result = num_hours * 60
    return result

def convert_to_seconds(num_hours):
    """
    (int) -> int
    Return the number of Seconds.
    """
    return convert_to_minutes(num_hours) * 60

def area_hero(side1, side2, side3):
    ''' (number, number, number) -> float
    Return the area of a triangle with sides of length side1, side2, side3.
    >>> area_hero(3, 4, 5)
    6.0
    >>> area_hero(10.5, 6, 9.3)
    27.731
    '''
    semi = semiperimeter(side1, side2, side3)
    area = math.sqrt(semi * (semi - side1) * (semi - side2) * (semi - side3))
    return area




