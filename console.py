import cmd
import re
from shlex import split


class MyPythonAssistant(cmd.Cmd):
    intro = "Welcome to MyPythonAssistant! Type help or ? to list commands.\n"
    prompt = "(python) "

    def emptyline(self):
        pass

    def default(self, arg):
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arg_list = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_list[1])
            if match is not None:
                command = [arg_list[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    call = "{} {}".format(arg_list[0], command[1])
                    return arg_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Exit MyPythonAssistant"""
        return True

    def do_EOF(self, arg):
        """Exit MyPythonAssistant"""
        print("")
        return True

    def do_create(self, arg):
        """Create a new object"""
        arg_list = split(arg)
        if len(arg_list) == 0:
            print("** class name missing **")
        else:
            print("Creating a new {} object...".format(arg_list[0]))
            # Perform object creation logic here

    def do_show(self, arg):
        """Show details of an object"""
        arg_list = split(arg)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            print("Showing details of {} with id: {}".format(arg_list[0], arg_list[1]))
            # Perform object show logic here

    def do_destroy(self, arg):
        """Destroy an object"""
        arg_list = split(arg)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            print("Destroying {} with id: {}".format(arg_list[0], arg_list[1]))
            # Perform object destroy logic here

    def do_all(self, arg):
        """List all objects"""
        arg_list = split(arg)
        if len(arg_list) > 0:
            print("Listing all {} objects...".format(arg_list[0]))
            # Perform filtered object list logic here
        else:
            print("Listing all objects...")
            # Perform complete object list logic here

    def do_count(self, arg):
        """Count the number of objects"""
        arg_list = split(arg)
        count = 0
        if len(arg_list) > 0:
            print("Counting {} objects...".format(arg_list[0]))
            # Perform filtered object count logic here
        else:
            print("Counting all objects...")
            # Perform complete object count logic here


if __name__ == '__main__':
    MyPythonAssistant().cmdloop()
