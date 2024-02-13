#!/usr/bin/python3
"""Console module for command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.engine.file_storage import FileStorage


    class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "
    file = None

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print its id."""
        if not arg:
            print("** class name missing **")
            return
        cls_name = arg.split()[0]
        if cls_name not in {"BaseModel", "User"}:
            print("** class doesn't exist **")
            return
        new_instance = BaseModel() if cls_name == "BaseModel" else User()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show string representation of an instance based on class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in {"BaseModel", "User"}:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(args[0], obj_id)
        objs = FileStorage().all()
        if key not in objs:
            print("** no instance found **")
            return
        print(objs[key])

    def do_destroy(self, arg):
        """Delete an instance based on class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in {"BaseModel", "User"}:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(args[0], obj_id)
        objs = FileStorage().all()
        if key not in objs:
            print("** no instance found **")
            return
        del objs[key]
        FileStorage().save()

    def do_all(self, arg):
        """Print string representation of all instances, based or not on class name."""
        args = arg.split()
        objs = FileStorage().all()
        if not arg:
            print([str(obj) for obj in objs.values()])
            return
        if args[0] not in {"BaseModel", "User"}:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in objs.items() if args[0] in key])

    def do_update(self, arg):
        """Update an instance based on class name and id by adding or updating attribute."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in {"BaseModel", "User"}:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(args[0], obj_id)
        objs = FileStorage().all()
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        value = args[3]
        try:
            value = eval(value)
        except (NameError, SyntaxError):
            pass
        setattr(objs[key], attribute_name, value)
        objs[key].save()

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program."""
        print("")
        return True

    def emptyline(self):
        """Called when an empty line is entered."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
