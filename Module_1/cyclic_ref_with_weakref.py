import weakref

class Person:
    def __del__(self):
        print("Person object is being destroyed")

class Car:
    def __del__(self):
        print("Car object is being destroyed")

if __name__ == "__main__":
    p = Person()
    c = Car()
    print("Created Person and Car objects")
    p.owns = weakref.ref(c)
    c.owner = weakref.ref(p)
    del c
    del p
    print("Deleted Person and Car objects")
    
