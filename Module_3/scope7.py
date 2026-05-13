a = 100

def innerfn():
    print("In innerfn: a =", a) # a is accesed via enlosing scope.


def testfn(innerfn):
    a = 200
    innerfn() 

testfn(innerfn)
print("In main: a =", a)