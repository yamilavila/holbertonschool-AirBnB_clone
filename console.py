#!/usr/bin/python3
""" console contains the enery point of the command interpreter """
import cmd
import shlex
from models import classes
from models import storage


class HBNBCommand(cmd.Cmd):

    prompt = '(hbdb) '
    
    """This first 3 are the basic commands for the interpreter"""

    def emptyline(self):
        """ when user pres <ENTER> nothing is executed  """
        pass

    def do_EOF(self, command):
        """ End of file.. Ends program """
        return True

    def do_quit(self, command):
        """ Quit command to exit the program """
        self.close()
        quit()

    def help_quit(self):
        print('\n'.join(['Quit command to exit the program\n']))

    def close(self):
        if self.string:
            self.string.close()
            self.string = None

   
    def do_count(self, command):
        """count the instance of a class"""
        ctr = 0
        if command not in classes:
            print("**class name missing**")
        for key in storage.all.keys():
            if comand in key:
                cnt += 1
        print(ctr)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
