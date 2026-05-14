"""
A simple user manager to manage users stored in a text file
(users.dat) in the following format:
   #username:password:fullname
   hansson:heine123:David Hansson
   larry:larry567:Larry Wall
   rossum:guido11:Guido Rossum
   steve:steve123:Steven Bourne
   korn:dk1122:David Korn

Provide the following functionality for usage:
(Make sure that your implementations passes all the below tests)

    >>> import userdb_mod as users

    >>> users.add("adrian", "ad123", "Adrian Smith")

    >>> users.add("adrian", "ad444", "Adrian Smith")
    Traceback (most recent call last):
    ...
    ValueError: user 'adrian' already exists in database

    >>> users.mod(name="adrian", password="welcome")

    >>> users.mod(name="john", password="john123")
    Traceback (most recent call last):
    ...
    ValueError: user 'john' does not exist in database

    >>> users.remove(name="adrian")

    >>> users.remove(name="adrian")
    Traceback (most recent call last):
    ...
    ValueError: user 'adrian' does not exist in database

    >>> users.add(name="john", password="john123", fullname="John Doe")

    >>> users.authenticate(name="john", password="john123")
    True

    >>> users.authenticate(name="john", password="welcome")
    False

    >>> users.authenticate(name="larry", password="welome")
    False

"""


def add(self, name, password, fullname):
    """
    Add a new user into the users database (file) in the
    form name:password:fullname

    The username (passed as 'name' parameter) must be unique.

    >>> import userdb_mod as users
    >>> users.add("ritchie", "dmr123", "Dennis Ritchie")
    >>> users.add("ritchie", "welcome", "Dennis M Ritchie")
    Traceback (most recent call last):
    ...
    ValueError: user 'ritchie' already exists in database
    """
    pass # TODO

def mod(self, name, password=None, fullname=None):
    """
    Changes user information in the users database.

    The username (passed as 'name' parameter) must exist.

    >>> import userdb_mod as users
    >>> users.mod("ritchie", fullname="Dennis M Ritchie")
    >>> users.mod("cutler", password="dave123")
    Traceback (most recent call last):
    ...
    ValueError: user 'cutler' does not exist in database. 
    """
    pass # TODO

def remove(self, name):
    """
    Removes a user record from the users database.

    The username (passed as 'name' parameter) must exist.

    >>> import userdb_mod as users
    >>> users.remove("ritchie")
    >>> users.remove("cutler")
    Traceback (most recent call last):
    ...
    ValueError: user 'cutler' does not exist in database. 
    """
    pass # TODO

def authenticate(self, name, password):
    """
    Authenticate a user from user database.

    Returns True if the user is authenticated, else returns False

    >>> import userdb_mod as users
    >>> users.add("ritchie", "dmr123", "Dennis Ritchie")

    >>> users.authenticate(name="ritchie", password="welcome")
    False

    >>> users.authenticate(name="ritchie", password="dmr123")
    True

    >>> users.authenticate(name="bourne", password="steve123")
    False

    """
    pass # TODO


if __name__ == '__main__':
    from doctest import testmod
    testmod()

