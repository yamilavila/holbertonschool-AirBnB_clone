#!/usr/bin/python3
""" console contains the enery point of the command interpreter """
import cmd
import shlex
from models import classes
from models import storage


class HBNBCommand(cmd.Cmd):

    prompt = "(hbdb) "

    """This first 3 are the basic commands for the interpreter"""

    def emptyline(self):
        """ when user pres <ENTER> nothing is executed  """
        pass

    def do_EOF(self, arg):
        """ End of file.. Ends program \n"""
        return True

    def do_quit(self, arg):
        """ Quit command to exit the program\n """
        return True



if __name__ == "__main__":
    HBNBCommand().cmdloop()
