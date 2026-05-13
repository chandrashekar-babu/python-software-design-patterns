def cache(fn):
    cached_output = {}

    def wrapper(*args):
        if args not in cached_output:
            ret = fn(*args)
            cached_output[args] = ret
        return cached_output[args]
    return wrapper



from functools import lru_cache

@lru_cache(maxsize=10)
def square(x):
    from time import sleep
    sleep(2)
    return x*x


print(square(2))
print(square(3))
print(square(5))

print(square(2))
print(square(2))
print(square(3))
print(square(5))
print(square(3))
print(square(5))
print(square(3))
print(square(5))
