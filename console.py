#!/usr/bin/python3
"""This module provides us with a console
which allows us to easily interact with
our development environment.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """this class contains the entry point of the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """The command 'quit' exit the program"""
        return(True)

    def do_EOF(self, args):
        """Handle the signal EOF"""
        print("")
        return(True)

    def emptyline(self):
        """Does not perform any action"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
