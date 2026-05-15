def admin_methods(obj, attr):
    def add(name, dept):
        print("Adding user: name = {0}, dept = {1}".format(name, dept))

    def remove(name):
        print("Deleting user: name =", name)

    def logout():
        del obj.name
        print("Logged out!")

    if attr == 'add':
        return add
    elif attr == 'remove':
        return remove
    elif attr == 'logout':
        return logout
    else:
        raise AttributeError("invalid attribute " + attr)


def guest_methods(obj, attr):
    def login(name, password):
        print("Logging in as {0} with password {1}".format(name, password))
        obj.name = name
        obj.password = password

    if attr == 'login':
        return login
    else:
        raise AttributeError("invalid attribute " + attr)


def user_methods(obj, attr):
    def logout():
        del obj.name
        print("Logged out!")

    if attr == 'logout':
        return logout
    else:
        raise AttributeError("invalid attribute " + attr)

class User:

    def __getattr__(self, attr):
        if 'name' not in self.__dict__:
            return guest_methods(self, attr)
        elif self.__dict__['name'] == 'root':
            return admin_methods(self, attr)
        else:
            return user_methods(self, attr)

    def __dir__(self):
        if 'name' not in self.__dict__:
            return ['login']
        elif self.__dict__['name'] == 'root':
            return ['add', 'remove', 'logout']
        else:
            return ['logout']
















