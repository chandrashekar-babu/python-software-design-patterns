# Traditional singleton (module-level)
class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connect()
        return cls._instance
    
    def connect(self):
        print("Connecting to database...")

# With metaclass - more elegant and reusable
class SingletonMeta(type):
    """Metaclass that enforces singleton pattern"""
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self):
        self.connect()
    
    def connect(self):
        print("Connecting to database...")
        self.connection = "DB_CONNECTION"

class Configuration(metaclass=SingletonMeta):
    def __init__(self):
        self.settings = {}
    
    def set(self, key, value):
        self.settings[key] = value
    
    def get(self, key):
        return self.settings.get(key)

# Usage
db1 = DatabaseConnection()  # Prints: Connecting to database...
db2 = DatabaseConnection()  # No print - returns existing instance
print(db1 is db2)  # True

config1 = Configuration()
config2 = Configuration()
config1.set('debug', True)
print(config2.get('debug'))  # True - same instance