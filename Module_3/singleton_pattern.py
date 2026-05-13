class SingleTon:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance



def singleton_old(target):
    def create_single_instance(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = cls.__base__.__new__(cls, *args, **kwargs)
            if hasattr(cls, "__init__"):
                cls.__init__(cls.instance, *args, **kwargs)
                delattr(cls, "__init__")
        return cls.instance

    target.__new__ = create_single_instance
    return target

def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class World:
    def __init__(self):
        print("A world is being created...")


w1 = World()
w2 = World()
print(w1)