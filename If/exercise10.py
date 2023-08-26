print("Temprature Convertor:")
print("Choice 1: Celcius to Fahrenheit")
print("Choice 2: Fahrenheit to Celcius")

choice=int(input("Enter your Choice 1/2:"))

if choice==1:
    celsius=float(input("Enter your Tempreature in Celsius: "))
    fahrenheit=(celsius *9/5) +32
    print("Tempreature in Fahrenheit:", fahrenheit)
elif choice==2:
    fahrenheit=float(input("Enter your Tempreature in Fahrenheit: "))
    celsius=(fahrenheit-32) *5/9
    print("Tempreature in Celsius:", celsius)
else:
    print("Please enter valid Choice")