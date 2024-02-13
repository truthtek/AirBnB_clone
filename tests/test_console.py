import unittest
from unittest.mock import patch, MagicMock
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
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            self.assertTrue("Documented commands (type help <topic>):" in f.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_emptyline_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual("", f.getvalue().strip())

    def test_create_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue().strip()) == 36)

    def test_show_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"show BaseModel {obj_id}")
            self.assertTrue(obj_id in f.getvalue())

    def test_destroy_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"destroy BaseModel {obj_id}")
            self.console.onecmd(f"show BaseModel {obj_id}")
            self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_all_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertTrue("BaseModel" in output)
            self.assertTrue(len(output.split('\n')) == 2)

    def test_update_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"update BaseModel {obj_id} name 'test'")
            self.console.onecmd(f"show BaseModel {obj_id}")
            self.assertTrue("'name': 'test'" in f.getvalue())

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
        self.assertTrue("BaseModel" in mock_stdout.getvalue().strip())

    def test_class_all_method_non_existing_class(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("BaseModel.all()")
            self.assertEqual("** class doesn't exist **", mock_stdout.getvalue().strip())

    def test_non_existing_class_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("show MyModel")
            self.assertEqual("** class doesn't exist **", mock_stdout.getvalue().strip())

    def test_non_existing_class_destroy(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("destroy MyModel")
            self.assertEqual("** class doesn't exist **", mock_stdout.getvalue().strip())

    def test_non_existing_class_update(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("update MyModel")
            self.assertEqual("** class doesn't exist **", mock_stdout.getvalue().strip())

    def test_non_existing_class_count(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("count MyModel")
            self.assertEqual("** class doesn't exist **", mock_stdout.getvalue().strip())

    def test_non_existing_class_all(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("MyModel.all()")
            self.assertEqual("** class doesn't exist **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_non_existing_instance_show(self, mock_stdout):
        self.console.onecmd("create BaseModel")
        self.console.onecmd("show BaseModel 12345")
        self.assertEqual("** no instance found **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_non_existing_instance_destroy(self, mock_stdout):
        self.console.onecmd("create BaseModel")
        self.console.onecmd("destroy BaseModel 12345")
        self.assertEqual("** no instance found **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_non_existing_instance_update(self, mock_stdout):
        self.console.onecmd("create BaseModel")
        self.console.onecmd("update BaseModel 12345")
        self.assertEqual("** no instance found **", mock_stdout.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
