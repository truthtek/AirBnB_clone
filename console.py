#!/usr/bin/python3
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[args[0]]()
        print(new_instance.id)
        new_instance.save()

    def do_show(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    # other do_* methods

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
