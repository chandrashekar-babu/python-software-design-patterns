a = 100

def testfn():
    global a
    print("In testfn: a =", a)
    a = 200

print("Before testfn: a =", a)
testfn()
print("After testfn: a =", a)
