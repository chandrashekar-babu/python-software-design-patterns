color = "white"

class Car:
    color = "red" # Car.color = "red"
    def __init__(self):
        color = "blue" # local variable, not an instance attribute
        self.color = "green" # instance attribute, shadows class attribute

    def drive(self):
        print("Color of the car is", color)
        print(Car.color) # Accessing class attribute using class name
        print(self.color) # Accessing instance attribute using self


c = Car()
c.drive()
