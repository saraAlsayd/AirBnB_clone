#!/usr/bin/python3
"""create a program that contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
    file = None

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        exit()

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        exit()

    def emptyline(self):
        """Doesn't execute anything\n"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
