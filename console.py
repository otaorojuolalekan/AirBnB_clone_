#!/usr/bin/env python3
"""
This module is the console for the
AirBnB clone project.
"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
