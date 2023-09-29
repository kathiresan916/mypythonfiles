# Quadratic Equation

import cmath

a = int(input("Enter A Value: "))
b = int(input("Enter B Value: "))
c = int(input("Enter C Value: "))

sum_of_quadratic = (b**2) - (4*a*c)  # Calculate the discrinment

solution_1 = (-b-cmath.sqrt(sum_of_quadratic))/(2*a)
solution_2 = (-b+cmath.sqrt(sum_of_quadratic))/(2*a)

print('The Solution are {0} and {1}' .format(solution_1, solution_2))
