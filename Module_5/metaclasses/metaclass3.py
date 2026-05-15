def vehicle(name, bases, attrs):
    class Vehicle(type):
        def __init__(self, name):
            print "Created", self.name

        def buy(self):
            print "Bought", self.name
            
    return type.__new__(Vehicle, name, bases, attrs)

class Car:
    __metaclass__ = vehicle

class Bike:
    __metaclass__ = vehicle

c = Car()
b = Bike()

print c
print b


