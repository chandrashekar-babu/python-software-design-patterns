from chain_of_actions import ChainOfActions


chain = ChainOfActions()

@chain.test
def add_test(x, y):
    return x + y

@chain.test
def mul_test(x, y):
    return x * y


dataset = [(10, 20), (4.5, 6.7), ("55", 78), (None, False)]
chain.add_data(dataset)
chain.run()

