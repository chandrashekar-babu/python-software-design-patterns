# %load https://tinyurl.com/pyshell-deco-ex
"""
Exercise:
     Implement the command_dispatch module with class CommandDispatch
     such that the following example program that implements a
     rudimentary command-line shell works.
"""

from command_dispatch import CommandDispatch


shell = CommandDispatch()

@shell.for_command("list")
def list_directory(*args):
    from os import listdir
    if len(args) < 2:
        args += ".",
    for path in args[1:]:
        print("{}:".format(path))
        print("\n".join(listdir(path)))

@shell.for_command("whoami")
def show_user(*args):
    from getpass import getuser
    print(getuser())

@shell.for_command("date")
def print_date(*args):
    from time import ctime
    print(ctime())

@shell.for_command("pwd")
def show_curr_dir(*args):
    import os
    print(os.getcwd())

@shell.for_command("exit")
def exit_shell(*args):
    exit(0)

@shell.for_command("hostname")
def show_hostname(*args):
    from os import uname
    print(uname().nodename)

@shell.invalid
def invalid_command(*args):
    print("Invalid command - ", args[0])


@shell.for_command("cd")
def change_directory(*args):
    import os
    os.chdir(args[1])

@shell.input
def get_input():
    import rlcompleter
    return input("PyShell> ").split()

if __name__ == '__main__':
    shell.run()

