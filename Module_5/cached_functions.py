function_cache = {}

def cache(fn):
    return function_cache.setdefault(fn.__qualname__, fn)

@cache
def foo():
    print("this is definition of foo once...")

foo()

@cache
def foo():
    print("this is definition of foo twice...")


foo()




