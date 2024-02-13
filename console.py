#!/usr/bin/python3
"""Console module for command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Override emptyline method to do nothing"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program by EOF"""
        print("")
        return True

    def help_quit(self):
        """Help for quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help for EOF command"""
        print("Exit the program by EOF")

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        args = arg.split()
        if not args:
            print([str(value) for value in storage.all().values()])
            return
        try:
            cls = eval(args[0])
            print([str(value) for key, value in storage.all().items() if args[0] in key])
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            setattr(storage.all()[key], args[2], args[3])
            storage.all()[key].save()
        except NameError:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
