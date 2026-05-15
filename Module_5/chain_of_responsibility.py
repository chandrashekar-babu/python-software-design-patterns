class ChainOfResponsibility:
    def __init__(self, data):
        self.data = data
        self.tasks = []

    def add(self, fn):
        self.tasks.append(fn)

    def run(self):
        for d in self.data:
            for t in self.tasks:
                print(f"Running {t.__qualname__} on {d}:", end=" ")
                r = t(*d)
                print(r)
            print("-" * 30)



