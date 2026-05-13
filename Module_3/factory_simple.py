
def testfn(): 
    def foo(): # Inner-function
        print("foo() invoked...")
    return foo

def create(budget):
    if budget < 1000:
        def toy():
            print("this is a toy...")
        return toy
    elif budget < 10000:
        def basic_phone():
            print("this is a basic phone...")
        return basic_phone
    elif budget < 100000:
        def bike():
            print("this is a bike...")
        return bike

a = create(70000)
a()

