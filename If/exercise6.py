year=int(input("Please Enter the Year:"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,"is leap year")
else:
    print(year,"is non-leap year")