class String(object):
    def __get__(self, obj, objtype):
        print("String __get__ called for", obj)
        return self.val

    def __set__(self, obj, val):
        print("String __set__ called for", obj)
        if type(val) is not str: 
            raise TypeError("value must be a string")   
        self.val = val


class Number(object):
    def __get__(self, obj, objtype):
        print("Number __get__ called for", obj)
        return self.val

    def __set__(self, obj, val):
        print("Number __set__ called for", obj)
        if type(val) is not int: 
            raise TypeError("value must be a number")
        self.val = val

class Person(object):
     name = String()
     age = Number()


p = Person()
p.name = "Sam" 
print p.name

p.age = 30
print p.age

p1 = Person()
print p1.name
#print Person.name






