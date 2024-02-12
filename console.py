import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl + D)"""
        print()
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("Exit the program with EOF (Ctrl + D)")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
