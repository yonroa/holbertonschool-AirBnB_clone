#!/usr/bin/python3
"""This module provides us with a console
which allows us to easily interact with
our development environment.
"""

import cmd
import datetime
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import shlex
import re


class HBNBCommand(cmd.Cmd):
    """this class contains the entry point of the command interpreter"""
    prompt = "(hbnb) "
    classes = ['BaseModel', 'User', 'City',
               'Place', 'Review', 'State', 'Amenity']

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

    def do_create(self, line):
        """
        Creates a new instance and saves it

        Ex: (hbnb) create BaseModel
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(line)()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """
        Prints the string representation of an
        instance based on the class name and id

        Ex: (hbnb) show BaseModel 1234-1234-1234
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            command = line.split(" ")
            if command[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(command) < 2:
                print("** instance id missing **")
            else:
                key = f"{command[0]}.{command[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id

        Ex: (hbnb) destroy BaseModel 1234-1234-1234
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            command = line.split(" ")
            if command[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(command) < 2:
                print("** instance id missing **")
            else:
                key = f"{command[0]}.{command[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based or not on the class name

        Ex: (hbnb) all BaseModel or (hbnb) all
        """
        if line == "":
            obj = [str(obj) for key, obj in storage.all().items()]
            print(obj)
        else:
            if line not in self.classes:
                print("** class doesn't exist **")
            else:
                obj = [str(obj) for key, obj in storage.all().items()
                       if type(obj).__name__ == line]
                print(obj)

    def do_update(self, line):
        """
        Updates an instance based on the class
        name and id by adding or updating attribute

        Usage: update <class name> <id> <attribute name> "<attribute value>"

        Ex: (hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        command = shlex.split(line)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** instance id missing **")
        else:
            key = f"{command[0]}.{command[1]}"
            data = storage.all().get(key)
            if data is None:
                print("** no instance found **")
            elif len(command) == 2:
                print("** attribute name missing **")
            elif len(command) == 3:
                print("** value missing **")
            else:
                command[3] = self.analyze(command[3])
                setattr(data, command[2], command[3])
                setattr(data, "updated_at", datetime.datetime.now())
                storage.save()

    def analyze(self, value):
        """
        Analyze the value and check if it
        need to be converted to int or float
        """
        if value.isdigit():
            return int(value)
        if value.replace(".", "", 1).isdigit():
            return float(value)
        return value

    def default(self, line):
        """
        If the command is not recognized, check
        if the syntax is: <class name>.<method name> or not,
        if the class name and the method name exists will be executed
        """
        if "." in line:
            command = re.split(r"\.|\(|\)", line)

            if command[0] in self.classes:
                if command[1] == "show":
                    self.do_show(f"{command[0]} {command[2][1:-1]}")
                elif command[1] == "destroy":
                    self.do_destroy(f"{command[0]} {command[2][1:-1]}")
                elif command[1] == "count":
                    print(len(self.get_instances(command[0])))
                elif command[1] == "all":
                    print(self.get_instances(command[0]))

    def get_instances(self, object=""):
        """Gets the objects of the specified class"""
        instances = storage.all()

        if object:
            key = instances.keys()
            return [str(val) for key, val in instances.items()
                    if key.startswith(object)]
        return [str(val) for key, val in instances.items()]


if __name__ == '__main__':
    HBNBCommand().cmdloop()
