def vehicle(name, bases, attrs):
    print "vehicle called with name =", name 
    #print name, ", bases =", bases, ", attrs =", attrs
    if name == "Car":
        class FourWheeler: pass
        return FourWheeler
    elif name == "Bike":
        class TwoWheeler: pass
        return TwoWheeler
    else:
        class Vehicle: pass
        return Vehicle

class Car:
    pass

class SUV(Car):
    __metaclass__ = vehicle
    name = "dssddsf"


#class Bike:
#    __metaclass__ = vehicle


s = SUV()

