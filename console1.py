#!/usr/bin/env python3
"""
This module is the console for the
AirBnB clone project.
"""
import cmd
import re
from models.base_model import BaseModel
from models.__init__ import storage

# create global variables for use in and outside
# all classes and functions

classes = ["BaseModel"]


class HBNBCommand(cmd.Cmd):
    """This is the console class where
    all console functions are defined."""
    prompt = "(Hbnb) "

    def do_EOF(self, line):
        """
        This defines the End of Line Function
        That ends the running program
        """
        print("")
        return True

    def emptyline(self):
        """
        This ensures that emptyline does nothing
        """
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def args_parse(self, args):
        """parse args to use and check if present and in classes"""
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("args\n")
            print("** class doesn't exist **")
        else:
            arglist = [arg for arg in args.split()]
            return arglist

    def do_create(self, args):
        """Creates an instance of BaseModel"""
        pargs = self.args_parse(args)
        if pargs:
            new_ins = HBNBCommand.pargs[0]()
            print(new_ins.id)
            storage.save()


if __name__ == '__main__':
    # This command runs the console.py terminal
    HBNBCommand().cmdloop()
