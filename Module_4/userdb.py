class User:
    def __init__(self, name, password, fullname, sep=":"):
        self.name = name
        self.password = password
        self.fullname = fullname
        self.sep = sep

    def __getitem__(self, attr):
        if attr in ('name', 'password', 'fullname'):
            return getattr(self, attr)
        else:
            raise KeyError(f"Invalid attribute '{attr}' for User")
        
    def __setitem__(self, attr, value):
        if attr in ('name', 'password', 'fullname'):
            setattr(self, attr, value)
        else:
            raise KeyError(f"Invalid attribute '{attr}' for User")
        
    def __str__(self):
        return f"{{'name': '{self.name}', 'password': '{self.password}', 'fullname': '{self.fullname}'}}"
    
    def __repr__(self):
        return f"User(name='{self.name}', password='{self.password}', fullname='{self.fullname}')"

    def raw(self):
        return f"{self.name}{self.sep}{self.password}{self.sep}{self.fullname}"


class UserDB:
    def __init__(self, filename, sep=":"):
        self.filename = filename
        self.sep = sep
        self.users = {}
    
    def _load(self):
        with open(self.filename) as f:
            for line in f:
                name, password, fullname = line.strip().split(self.sep)
                self.users[name] = User(name, password, fullname, sep=self.sep)

    def _save(self):
        with open(self.filename, "w") as f:
            for user in self.users.values():
                f.write(user.raw() + "\n")

    def __getitem__(self, name):
        if not self.users:
            self._load()
        return self.users[name]

    def __setitem__(self, name, user):
        if type(user) not in (dict, User):
            raise ValueError("User must be a dict or User instance.")
        
        if not self.users:
            self._load()

        if isinstance(user, dict):
            user = User(**user, sep=self.sep)
        self.users[name] = user

        self._save()

    def __delitem__(self, name):
        if not self.users:
            self._load()
        del self.users[name]
        self._save()

    def authenticate(self, name, password):
        if not self.users:
            self._load()
        user = self.users.get(name)
        if user and user.password == password:
            return True
        return False
