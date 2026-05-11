class CommandDispatch:
    def __init__(self):
        self.dispatch = {}

    def for_command(self, command_name):
        def decorator(fn):
            self.dispatch[command_name] = fn      
        return decorator

    def invalid(self, fn):
        self._invalid_fn = fn

    def input(self, fn):
        self._input_fn = fn

    def run(self):
        while True:
            args = self._input_fn()
            if not args:
                continue
            command = args[0]
            self.dispatch.get(command, self._invalid_fn)(*args)
    