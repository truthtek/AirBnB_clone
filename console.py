#!/usr/bin/python3
"""
Module containing the command interpreter for HBNB
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for HBNB
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def help_quit(self):
        """
        Print help message for quit command
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        Exit the program when EOF is reached
        """
        print("")  # Print a new line before exiting
        return True

    def help_EOF(self):
        """
        Print help message for EOF
        """
        print("EOF command to exit the program")

    def emptyline(self):
        """
        Do nothing on empty line
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
