#!/usr/bin/env python3
<<<<<<< HEAD
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



=======


""" AirBnB Console """

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ Class HBNB to read command """
    prompt = '(hbnb) '
    __chk_117 = 0

    def emptyline(self):
        """Pass if no command is given"""
        pass

    def precmd(self, line):
        """ Edit given command to allow second type of input"""
        if not sys.stdin.isatty():
            print()
        if '.' in line:
            HBNBCommand.__chk_117 = 1
            line = line.replace('.', ' ').replace('(', ' ').replace(')', ' ')
            cmd_argv = line.split()
            cmd_argv[0], cmd_argv[1] = cmd_argv[1], cmd_argv[0]
            line = " ".join(cmd_argv)
        return cmd.Cmd.precmd(self, line)

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        print()
        return True

    def do_create(self, arg):
        "Create an instance if the Model exists"
        if not arg:
            print("** class name missing **")
            return None
        try:
            my_model = eval(arg + "()")
            my_model.save()
            print(my_model.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, arg):
        "Print dict of a instance in base of it's ID"
        cmd_argv = arg.split()
        if not cmd_argv:
            print("** class name missing **")
            return None
        try:
            eval(cmd_argv[0])
        except Exception:
            print("** class doesn't exist **")
            return None

        all_objs = storage.all()
        if len(cmd_argv) < 2:
            print("** instance id missing **")
            return None

        cmd_argv[1] = cmd_argv[1].replace("\"", "")
        key = cmd_argv[0] + '.' + cmd_argv[1]

        if all_objs.get(key, False):
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_all(self, arg):
        "Print all the instances saved in file.json"
        cmd_argv = arg.split()

        if cmd_argv:
            try:
                eval(cmd_argv[0])
            except Exception:
                print("** class doesn't exist **")
                return None

        all_objs = storage.all()
        print_list = []
        len_objs = len(all_objs)
        for key, value in all_objs.items():
            if not cmd_argv:
                if HBNBCommand.__chk_117 == 0:
                    print_list.append("\"" + str(value) + "\"")
                else:
                    print_list.append(str(value))
            else:
                check = key.split('.')
                if cmd_argv[0] == check[0]:
                    if HBNBCommand.__chk_117 == 0:
                        print_list.append("\"" + str(value) + "\"")
                    else:
                        print_list.append(str(value))
        print("[", end="")
        print(", ".join(print_list), end="")
        print("]")

    def do_destroy(self, arg):
        """Deletes an instance based on it's ID and save the changes\n \
        Usage: destroy <class name> <id>"""

        cmd_argv = arg.split()
        if not cmd_argv:
            print("** class name missing **")
            return None
        try:
            eval(cmd_argv[0])
        except Exception:
            print("** class doesn't exist **")
            return None

        all_objs = storage.all()

        if len(cmd_argv) < 2:
            print("** instance id missing **")
            return None

        cmd_argv[1] = cmd_argv[1].replace("\"", "")
        key = cmd_argv[0] + '.' + cmd_argv[1]

        if all_objs.get(key, False):
            all_objs.pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, arg):
        "Usage: update <class name> <id> <attribute name> <attribute value>"
        cmd_argv = []
        part2_argv = []
        is_dict = 0
        if "\"" in arg:
            if "," in arg:
                if "{" in arg:
                    is_dict = 1
                    part1_argv = arg.split(",")[0].split()
                    for i in part1_argv:
                        cmd_argv.append(i.replace("\"", ""))
                    part2_argv = arg.replace("}", "").split("{")[1].split(", ")
                    for i in part2_argv:
                        for j in i.split(": "):
                            cmd_argv.append(j.replace("\"", "")
                                            .replace('\'', ""))
                else:
                    arg_key = arg.replace(",", "")
                    part1_argv = arg_key.split()
                    for i in part1_argv[:2]:
                        cmd_argv.append(i.replace("\"", ""))
                    part2_argv = arg.split(", ")[1:]
                    for i in part2_argv:
                        cmd_argv.append(i.replace("\"", ""))
            else:
                part1_argv = arg.split("\"")[0]
                for i in part1_argv.split():
                    cmd_argv.append(i)
                part2_argv = arg.split("\"")[1:]
                for i in part2_argv:
                    if i != " " and i != "":
                        cmd_argv.append(i.replace("\"", ""))

        else:
            part1_argv = arg.split()
            for i in range(len(part1_argv)):
                if i == 4:
                    break
                cmd_argv.append(part1_argv[i])

        if (len(cmd_argv) == 0):
            print("** class name missing **")
            return None

        try:
            eval(cmd_argv[0])
        except Exception:
            print("** class doesn't exist **")
            return None

        if len(cmd_argv) < 2:
            print("** instance id missing **")
            return None

        all_objs = storage.all()

        key = cmd_argv[0] + '.' + cmd_argv[1]
        if all_objs.get(key, False):
            if (len(cmd_argv) >= 3):
                if (len(cmd_argv) % 2) == 0:
                    for i in range(2, len(cmd_argv), 2):
                        attr = cmd_argv[i]
                        type_att = getattr(all_objs[key], cmd_argv[i], "")
                        try:
                            cast_val = type(type_att)(cmd_argv[i + 1])
                        except Exception:
                            cast_val = type_att
                        setattr(all_objs[key], cmd_argv[i], cast_val)
                        all_objs[key].save()
                        if is_dict == 0:
                            break
                else:
                    print("** value missing **")
            else:
                print("** attribute name missing **")
        else:
            print("** no instance found **")

    def do_count(self, arg):
        "Usage: count <class name> or <class name>.count()"
        cmd_argv = arg.split()

        if cmd_argv:
            try:
                eval(cmd_argv[0])
            except Exception:
                print("** class doesn't exist **")
                return None

        all_objs = storage.all()
        count = 0

        for key, value in all_objs.items():
            if not cmd_argv:
                count += 1
            else:
                check = key.split('.')
                if cmd_argv[0] == check[0]:
                    count += 1
        print(count)
>>>>>>> 0f16c540970cf192e47c17428f054accdd127911


if __name__ == '__main__':
    HBNBCommand().cmdloop()
