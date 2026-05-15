class User:
    import shelve
    user_store = shelve.open('user_store.db', writeback=True)

    def __init__(self, name):
        self.__dict__['_user_info'] = self.user_store
        self.__dict__['_user_info'].setdefault(name, {"name" : name})
        self.__dict__['_name'] = name

    def __getattr__(self, item):
        return self.__dict__['_user_info'][self.__dict__['_name']][item]
    
    def __setattr__(self, key, value):
        rec = self.__dict__['_user_info'][self.__dict__['_name']]
        rec[key] = value
        self.__dict__['_user_info'][self.__dict__['_name']] = rec
        self.__dict__['_user_info'].sync()
    
    def __str__(self):
        return f"User({self.__dict__['_user_info'][self.__dict__['_name']]})"


if __name__ == "__main__":
    u1 = User("alice")
    u1.age = 30
    u1.location = "Wonderland"
    print(u1)
    