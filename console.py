import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse_arguments(arg):
    """Parse command arguments."""
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """HolbertonBnB command interpreter."""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for invalid commands."""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Create a new instance of a class."""
        argl = parse_arguments(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            instance = eval(argl[0])()
            print(instance.id)
            storage.save()

    def do_show(self, arg):
        """Show instance information."""
        argl = parse_arguments(arg)
        obj_dict = storage.all()
        if len(argl) < 2:
            print("** class name missing **" if len(argl) == 0 else "** instance id missing **")
        elif argl[0] not in self.__classes:
            print("** class doesn't exist **")
        elif f"{argl[0]}.{argl[1]}" not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict[f"{argl[0]}.{argl[1]}"])

    def do_destroy(self, arg):
        """Delete an instance."""
        argl = parse_arguments(arg)
        obj_dict = storage.all()
        if len(argl) < 2:
            print("** class name missing **" if len(argl) == 0 else "** instance id missing **")
        elif argl[0] not in self.__classes:
            print("** class doesn't exist **")
        elif f"{argl[0]}.{argl[1]}" not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict[f"{argl[0]}.{argl[1]}"]
            storage.save()

    def do_all(self, arg):
        """Show all instances."""
        argl = parse_arguments(arg)
        obj_list = []
        for obj in storage.all().values():
            if not argl or obj.__class__.__name__ == argl[0]:
                obj_list.append(str(obj))
        print(obj_list)

    def do_count(self, arg):
        """Count instances."""
        argl = parse_arguments(arg)
        count = sum(1 for obj in storage.all().values() if obj.__class__.__name__ == argl[0])
        print(count)

    def do_update(self, arg):
        """Update an instance."""
        argl = parse_arguments(arg)
        obj_dict = storage.all()

        if len(argl) < 2:
            print("** class name missing **" if len(argl) == 0 else "** instance id missing **")
            return
        if argl[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if f"{argl[0]}.{argl[1]}" not in obj_dict:
            print("** no instance found **")
            return

        instance = obj_dict[f"{argl[0]}.{argl[1]}"]
        if len(argl) < 3:
            print("** attribute name missing **")
            return
        if len(argl) < 4:
            print("** value missing **")
            return

        attribute_name = argl[2]
        attribute_value = argl[3]
        setattr(instance, attribute_name, attribute_value)
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
