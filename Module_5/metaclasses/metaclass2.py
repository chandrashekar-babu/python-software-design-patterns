def vehicle(name, bases, attrs):
    class_object = type.__new__(type, name, bases, attrs)
    class_object.color = "Red"
    return class_object

class Car:
    __metaclass__ = vehicle

class Bike:
    __metaclass__ = vehicle

c = Car()
b = Bike()

print c
print b

print c.color
print b.color

