#!/usr/bin/python3
""" console contains the enery point of the command interpreter """
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
