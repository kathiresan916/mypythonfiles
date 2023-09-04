#Create a class called Laptop and create a following varaiables and funtions: Variables: Price, Processor, Ram. Object: HP, DELL, LENOVO

"""
class Laptop():
    price=""
    processor=""
    ram=""

    def HP(self):
        self.price=1000
        self.processor="Intel Core i7"
        self.ram="16GB"
    
    def DELL(self):
        self.price=2000
        self.processor="Intel Core i7"
        self.ram="16GB"

    def LENOVO(self):
        self.price=3000
        self.processor="Intel Core i7"
        self.ram="16GB"

HP=Laptop()
DELL=Laptop()
LENOVO=Laptop()

print(HP.price, HP.processor, HP.ram)
print(DELL.price, DELL.processor, DELL.ram)
print(LENOVO.price, LENOVO.processor, LENOVO.ram)

"""


class Laptop:
    def __init__(self, price, processor, ram):
        self.price = price
        self.processor = processor
        self.ram = ram
        
#Create instance for HP, DELL and Lenovo devices

HP = Laptop(1000, "Intel Core i7", "16GB")
DELL = Laptop(2000, "Intel Core i7", "16GB")
LENOVO = Laptop(3000, "Intel Core i7", "16GB")

print("HP:", HP.price, HP.processor, HP.ram)
print("DELL:", DELL.price, DELL.processor, DELL.ram)
print("Lenovo:", LENOVO.price, LENOVO.processor, LENOVO.ram)