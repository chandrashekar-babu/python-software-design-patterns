a = 100

def testfn():
    a = 200
    def innerfn():
        print("In innerfn: a =", a) # a is accesed via enlosing scope.
    innerfn()

testfn()
print("In main: a =", a)