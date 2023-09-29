"""Convert Kimometers to Miles"""

kilometer = float(input("Enter Kilometer: "))

CONV_FAC = 0.621371

miles = kilometer * CONV_FAC

print(f'{kilometer:.2f} kilometers is equal to {miles:.2f} miles')
