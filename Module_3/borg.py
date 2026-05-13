class World:
    __shared = { }

    def __init__(self):
        self.__dict__ = World.__shared

w1 = World()
w2 = World()

print w1
print w2

w1.population = 10000000000
print w1.population
print w2.population

