class ChainOfActions:
    def __init__(self):
        self.tests = { }
        self.data = []

    def add_data(self, data):
        self.data = data

    def test(self, fn):
        self.tests[fn.__qualname__] = fn
        return fn

    def run(self):
        for d in self.data:
            print("*" * 40)
            for k, v in self.tests.items():
                print("Running test: {}{}".format(k, str(d)))
                try:
                    print(">>>> ", v(*d))
                except Exception as e:
                    print("FAILED!")
                else:
                    print("SUCCESS")
                print("-" * 40)




