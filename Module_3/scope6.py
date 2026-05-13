a = 100

def testfn():
    a = 200
    def innerfn():
        print("In innerfn: a =", a) # a is accesed via enlosing scope.
    return innerfn

inner_function = testfn()
inner_function()
print("In main: a =", a)