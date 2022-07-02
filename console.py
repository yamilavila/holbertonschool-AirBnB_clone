#!/usr/bin/python3
""" console contains the enery point of the command interpreter """
import cmd
from types import new_class
from models import classes
from models import storage


class HBNBCommand(cmd.Cmd):

    prompt = '(hbdb) '

    def do_quit(self, command):
        """ Quit command to exit the program """
        return True

    def do_EOE(self, command):
        """ End of file.. Ends program """
        print()
        return True

    def emptyline(self):
        """ when user pres <ENTER> nothing is executed  """
        pass

    def do_create(self, command):
        if command is None:
            print("** class name missing **")
        elif command == "BaseModel":
            n_class = classes[command]()
            print(n_class.id)
            storage.new(n_class)
            storage.save()
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
