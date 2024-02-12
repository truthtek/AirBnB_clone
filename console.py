import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""
    
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it to the JSON file."""
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(arg)
            new_instance = cls()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show string representation of an instance based on class name and id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            cls_name = args[0]
            id = args[1]
            cls = eval(cls_name)
            all_objs = storage.all()
            key = "{}.{}".format(cls_name, id)
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            cls_name = args[0]
            id = args[1]
            cls = eval(cls_name)
            all_objs = storage.all()
            key = "{}.{}".format(cls_name, id)
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all string representation of all instances."""
        try:
            cls_name = arg
            cls = eval(cls_name)
            all_objs = storage.all()
            objs_list = [str(obj) for key, obj in all_objs.items() if key.startswith(cls_name)]
            print(objs_list)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on the class name and id by adding or updating attribute."""
        if not arg:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            cls_name = args[0]
            id = args[1]
            attr = args[2]
            value = args[3]
            cls = eval(cls_name)
            all_objs = storage.all()
            key = "{}.{}".format(cls_name, id)
            if key in all_objs:
                obj = all_objs[key]
                setattr(obj, attr, value)
                storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
