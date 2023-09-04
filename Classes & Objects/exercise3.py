#Create a class called fruit. Create a variable called using __init__ method. Create a object called apple "Pass the color variable as a parameter through object"

class fruits:
    def __init__ (self, col):
        self.color=col

apple=fruits("Red")
print(apple.color)
        