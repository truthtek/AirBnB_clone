import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand  # Assuming this import is necessary

class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        del self.console

    def assertConsoleOutputContains(self, command, expected_output):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd(command)
            console_output = mock_stdout.getvalue().strip()
            self.assertIn(expected_output, console_output)

    def test_help_command(self):
        self.assertConsoleOutputContains("help", "Documented commands (type help <topic>):")

    def test_quit_command(self):
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_emptyline_command(self):
        self.assertConsoleOutputContains("\n", "")

    def test_create_command(self):
        self.assertConsoleOutputContains("create BaseModel", "")

    def test_show_command(self):
        self.assertConsoleOutputContains("create BaseModel", "")
        obj_id = self.console._last_id
        self.assertConsoleOutputContains(f"show BaseModel {obj_id}", obj_id)

    def test_destroy_command(self):
        self.assertConsoleOutputContains("create BaseModel", "")
        obj_id = self.console._last_id
        self.assertConsoleOutputContains(f"destroy BaseModel {obj_id}", "")
        self.assertConsoleOutputContains(f"show BaseModel {obj_id}", "** no instance found **")

    def test_all_command(self):
        self.assertConsoleOutputContains("create BaseModel", "")
        self.assertConsoleOutputContains("create BaseModel", "")
        self.assertConsoleOutputContains("all BaseModel", "BaseModel")

    def test_update_command(self):
        self.assertConsoleOutputContains("create BaseModel", "")
        obj_id = self.console._last_id
        self.assertConsoleOutputContains(f"update BaseModel {obj_id} name 'test'", "")
        self.assertConsoleOutputContains(f"show BaseModel {obj_id}", "'name': 'test'")

    def test_count_command(self):
        self.assertConsoleOutputContains("create BaseModel", "")
        self.assertConsoleOutputContains("create BaseModel", "")
        self.assertConsoleOutputContains("create BaseModel", "")
        self.assertConsoleOutputContains("count BaseModel", "3")

    def test_non_existing_class_show(self):
        self.assertConsoleOutputContains("show MyModel", "** class doesn't exist **")

    def test_non_existing_class_destroy(self):
        self.assertConsoleOutputContains("destroy MyModel", "** class doesn't exist **")

    def test_non_existing_class_update(self):
        self.assertConsoleOutputContains("update MyModel", "** class doesn't exist **")

    def test_non_existing_class_count(self):
        self.assertConsoleOutputContains("count MyModel", "** class doesn't exist **")

    def test_non_existing_instance_show(self):
        self.assertConsoleOutputContains("create BaseModel", "")
        self.assertConsoleOutputContains("show BaseModel 12345", "** no instance found **")

    def test_non_existing_instance_destroy(self):
        self.assertConsoleOutputContains("create BaseModel", "")
        self.assertConsoleOutputContains("destroy BaseModel 12345", "** no instance found **")

    def test_non_existing_instance_update(self):
        self.assertConsoleOutputContains("create BaseModel", "")
        self.assertConsoleOutputContains("update BaseModel 12345", "** no instance found **")

if __name__ == '__main__':
    unittest.main()
