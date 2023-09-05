#Create a base class called Shape with a method area() that returns 0. Create a derived class called Rectangle that inherits from Shape and overrides area() method to calculate and return the area of a rectangle. 

class Shape():
    def area(self):
        return 0

class Rectangle(Shape):
    def area(self):
        l=10
        w=20
        return l*w
    
shape1 = Shape()
shape2 = Rectangle()

print(shape1.area())
print(shape2.area())
