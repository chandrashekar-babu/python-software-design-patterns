from abc import ABC, abstractmethod

# 1. The Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

# 2. Concrete Command
class ProcessDataCommand(Command):
    def __init__(self, facade, source_type, path, strategy):
        self.facade = facade
        self.source_type = source_type
        self.path = path
        self.strategy = strategy

    def execute(self):
        # The command delegates the actual work to the Facade
        self.facade.process(self.source_type, self.path, self.strategy)

# 3. The Invoker (The "Manager")
class TaskManager:
    def __init__(self):
        self._history = []

    def run_task(self, command: Command):
        command.execute()
        self._history.append(command)

    def show_history(self):
        print(f"Total tasks executed: {len(self._history)}")