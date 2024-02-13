class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""

    prompt = "(hbnb) "

    # Existing methods...

    def do_all(self, arg):
        """Print all string representation of all instances."""
        try:
            cls_name = arg
            cls = eval(cls_name)
            all_objs = cls.all()
            objs_list = [str(obj) for obj in all_objs.values()]
            print(objs_list)
        except NameError:
            print("** class doesn't exist **")
