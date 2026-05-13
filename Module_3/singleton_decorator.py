def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self, host):
        self.host = host
        print(f"Connecting to database at {host}")

if __name__ == "__main__":
    db1 = DatabaseConnection("localhost")
    db2 = DatabaseConnection("localhost")
    print(db1 is db2)  # This should print True, confirming both are the same instance
    print(id(db1), id(db2))  # This should print the same id for both instances
    