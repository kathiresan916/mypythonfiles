import math

def perimeter(side1, side2, side3):
    '''
    (number1, number2, number3) -> Number
    Return the perimeter of a triangle with sides of length.
    side1, side2, side3.
    '''
    return side1 + side2 + side3


def semiperimeter(side1, side2, side3):
    '''
    (side1, side2, side3) -> Number
    Return the semiperimeter of a triange with side of length side1, side2, side3.
    '''
    return perimeter(side1, side2, side3) / 2


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

