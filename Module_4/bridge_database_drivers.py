from abc import ABC, abstractmethod

# 1. The Implementation (The "Engine")
class DatabaseDriver(ABC):
    @abstractmethod
    def connect_to(self, host: str): pass
    @abstractmethod
    def execute_query(self, query: str): pass

class MySQLDriver(DatabaseDriver):
    def connect_to(self, host): print(f"Connecting to MySQL at {host}...")
    def execute_query(self, query): print(f"Running SQL: {query}")

class MongoDriver(DatabaseDriver):
    def connect_to(self, host): print(f"Connecting to MongoDB at {host}...")
    def execute_query(self, query): print(f"Running NoSQL: {query}")

# 2. The Abstraction (The "App Logic")
class DataManager:
    def __init__(self, driver: DatabaseDriver):
        self.driver = driver # The Bridge

    def save_user(self, name: str):
        self.driver.connect_to("localhost")
        self.driver.execute_query(f"INSERT INTO users VALUES ('{name}')")

# 3. Execution
# We can swap the entire backend without changing the DataManager logic
sql_app = DataManager(MySQLDriver())
sql_app.save_user("Alice")

nosql_app = DataManager(MongoDriver())
nosql_app.save_user("Bob")