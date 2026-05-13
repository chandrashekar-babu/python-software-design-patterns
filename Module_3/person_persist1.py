class Person(object):
    def __init__(self, name):
        import shelve
        self.__dict__['_store'] = shelve.open("people.dat")
        self.__dict__['_store'].setdefault(name, {"name" : name})
        self.__dict__['_name'] = name

    @staticmethod
    def _check(attr, store):
        if attr not in store:
            raise AttributeError, "invalid attribute - " + attr

    def __getattr__(self, attr):
        self._check(attr, self.__dict__['_store'][self.__dict__['_name']])
        return self.__dict__['_store'][self.__dict__['_name']][attr]

    def __setattr__(self, attr, value):
        info = self.__dict__['_store'][self.__dict__['_name']]
        info[attr] = value
        self.__dict__['_store'][self.__dict__['_name']] = info
        self.__dict__['_store'].sync()

    def __del__(self):
        self.__dict__['_store'].close()

        


