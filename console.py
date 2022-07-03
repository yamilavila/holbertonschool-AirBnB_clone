#!/usr/bin/python3
""" console contains the enery point of the command interpreter """
import cmd
import shlex
from types import new_class
from models import classes
from models import storage


class HBNBCommand(cmd.Cmd):

    prompt = '(hbdb) '

    """This is a static method for keys & arguments for one place validation"""
    @staticmethod
    def key_for_command(command):
        new_command = command.split()
        count = len(new_command)
        key = None
        tmp_val = None
        if not command:
            print("** class name missing ** ")
        elif new_command[0] not in classes:
            print("** class doesn`t exist **")
        elif count < 2:
            print("** instance id missing **")
        else:
            new_command[1] = new_command[1].strip('",')
            tmp_val = '.'.join(new_command[0:2])
            if tmp_val not in storage.all():
                print("** no instance found **")
            else:
                key = tmp_value
        return key

    """This first 3 are the basic commands for the interpreter"""
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
        """Creates a new instance of BaseModel, saves it (in the JSON file) & prints id"""
        if command is None:
            print("** class name missing **")
        elif command == "BaseModel":
            n_class = classes[command]()
            print(n_class.id)
            storage.new(n_class)
            storage.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, command):
        """Prints the string representation of an instance based on the name & id"""
        key = HBNBCommand.val_get_key(command)
        if key:
            print(storage.all()[key])

    def destroy(self, command):
        """Deletes an instance based on the class name and id"""
        key = HBNBCommand.val_get_key(command)
        if key:
            del storage.all()[key]
            storage.save()

    def do_all(self, command):
        """Prints all string representation of all instances based or not on the class name"""
        arguments = command.split()
        if not arguments:
            for a in storage.all().values():
                print(a)
        elif arguments[0] in classes:
            for b, c in storage.all().items():
                if b[0: b.index('.')] == arguments[0]:
                    print(c)
        else:
            print("** class doesn`t exist **")

    def do_update(self, command):
        """Updates the arguments"""



if __name__ == '__main__':
    HBNBCommand().cmdloop()
