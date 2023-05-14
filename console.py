#!/usr/bin/env python3
"""
This module is the console for the
AirBnB clone project.
"""
import cmd
import json
import shlex

from models.base_model import BaseModel
from models import storage


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
        pass

    def do_quit(self, line):
        """Calling this function quits the console"""
        return True
    def do_create(self, arg):
        """creates an instance of the class Basemodel and
        saves it as a Json file"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesnt exit **")
    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id.
        Usage: show <class name> <id>"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
        obj_key = args[0] + "." + args[1]
        objects = storage.all()
        if obj_key not in objects:
            print("** no instance found **")
            return
        print(objects[obj_key])

    def do_destroy(self, arg):
        """Deletes an instance based on the clas name and id
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exit **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = args[0] + "." + args[1]
        objects = storage.all()
        if obj_key not in objects:
            print("** no instance found **")
            return
        del objects[obj_key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name.
        Usage: all or all <class name>"""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        elif arg in storage.classes:
            print([str(obj) for obj in objects.values()
                   if type(obj).__name__ == arg])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Usage: update <class name> <id> <attribute value>"""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) ++ 3:
            print("** value missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        obj = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3]

        # check if attr_value is a string with spaces
        if len(args) > 4:
            attr_value = " ".join(args[3:])
            if '"' not in attr_value:
                print("** value missing **")
                return
            attr_value = attr_value.strip('"')

        # Check if attr_name is a value attribute for this object
        if hasattr(obj, attr_name):
            attr_value = type(getattr(obj, attr_name))(attr_value)
            setattr(obj, attr_name, attr_value)
            obj.save()
        else:
            print("** no instance found **")





if __name__ == '__main__':
    HBNBCommand().cmdloop()
