import unittest
from unittest.mock import MagicMock, patch
from io import StringIO
import os
import sys
from console import HBNBCommand

class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        del self.console

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_command(self, mock_stdout):
        self.console.onecmd("help")
        self.assertIn("Documented commands (type help <topic>):", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_emptyline_command(self):
        self.console.onecmd("\n")
        self.assertEqual("", mock_stdout.getvalue().strip())

    def test_create_command(self):
        self.console.onecmd("create BaseModel")
        self.assertEqual(36, len(mock_stdout.getvalue().strip()))

    def test_show_command(self):
        self.console.onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()
        self.console.onecmd(f"show BaseModel {obj_id}")
        self.assertIn(obj_id, mock_stdout.getvalue())

    def test_destroy_command(self):
        self.console.onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()
        self.console.onecmd(f"destroy BaseModel {obj_id}")
        self.console.onecmd(f"show BaseModel {obj_id}")
        self.assertEqual("** no instance found **", mock_stdout.getvalue().strip())

    def test_all_command(self):
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create BaseModel")
        self.console.onecmd("all BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertIn("BaseModel", output)
        self.assertEqual(2, len(output.split('\n')))

    def test_update_command(self):
        self.console.onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()
        self.console.onecmd(f"update BaseModel {obj_id} name 'test'")
        self.console.onecmd(f"show BaseModel {obj_id}")
        self.assertIn("'name': 'test'", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_count_command(self, mock_stdout):
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create BaseModel")
        self.console.onecmd("count BaseModel")
        self.assertEqual("3", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_class_all_method(self, mock_stdout):
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create BaseModel")
        self.console.onecmd("BaseModel.all()")
        self.assertIn("BaseModel", mock_stdout.getvalue().strip())

    def test_class_all_method_non_existing_class(self):
        self.console.onecmd("BaseModel.all()")
        self.assertEqual("** class doesn't exist **", mock_stdout.getvalue().strip())

    def test_non_existing_class_show(self):
        self.console.onecmd("show MyModel")
        self.assertEqual("** class doesn't exist **", mock_stdout.getvalue().strip())

    def test_non_existing_class_destroy(self):
        self.console.onecmd("destroy MyModel")
        self.assertEqual("** class doesn't exist **", mock_stdout.getvalue().strip())
