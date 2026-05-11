class CommandDispatch:
    def __init__(self):
        self.commands = {}

    def for_command(self, command):
        def decorator(func):
            self.commands[command] = func
        return decorator

    def invalid(self, func):
        self.invalid_fn = func

    def input(self, func):
        self.input_fn = func

    def run(self):
        while True:
            args = self.input_fn()
            comm = args[0]
            self.commands.get(comm, self.invalid_fn)(*args)

