a = [100, 200]

def testfn():
    print("In testfn: a =", a)
    a[0] = 200 # This is not variable assignment, but a mutation of the list object that 'a' references

print("Before testfn: a =", a)
testfn()
print("After testfn: a =", a)
