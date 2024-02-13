import unittest
from unittest.mock import MagicMock, patch
from io import StringIO
import os
import sys
from console import HBNBCommand

class ConsoleTestCase(unittest.TestCase):

    def setUp(self):
        self.cmd = HBNBCommand()

    def tearDown(self):
        del self.cmd

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_cmd(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("help")
            self.assertTrue("Documented commands (type help <topic>):" in f.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_cmd(self, mock_stdout):
        with self.assertRaises(SystemExit):
            self.cmd.onecmd("quit")

    def test_empty_cmd(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("\n")
            self.assertEqual("", f.getvalue().strip())

    def test_create_cmd(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue().strip()) == 36)

    def test_show_cmd(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.cmd.onecmd(f"show BaseModel {obj_id}")
            self.assertTrue(obj_id in f.getvalue())

    def test_destroy_cmd(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.cmd.onecmd(f"destroy BaseModel {obj_id}")
            self.cmd.onecmd(f"show BaseModel {obj_id}")
            self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_all_cmd(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("create BaseModel")
            self.cmd.onecmd("create BaseModel")
            self.cmd.onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertTrue("BaseModel" in output)
            self.assertTrue(len(output.split('\n')) == 2)

    def test_update_cmd(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.cmd.onecmd(f"update BaseModel {obj_id} name 'test'")
            self.cmd.onecmd(f"show BaseModel {obj_id}")
            self.assertTrue("'name': 'test'" in f.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_count_cmd(self, mock_stdout):
        self.cmd.onecmd("create BaseModel")
        self.cmd.onecmd("create BaseModel")
        self.cmd.onecmd("create BaseModel")
        self.cmd.onecmd("count BaseModel")
        self.assertEqual("3", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_class_all_method(self, mock_stdout):
        self.cmd.onecmd("create BaseModel")
        self.cmd.onecmd("create BaseModel")
        self.cmd.onecmd("create BaseModel")
        self.cmd.onecmd("BaseModel.all()")
        self.assertTrue("BaseModel" in mock_stdout.getvalue().strip())

    def test_invalid_class_all_method(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("BaseModel.all()")
            self.assertEqual("** class doesn't exist **", mock_stdout.getvalue().strip())

    def test_invalid_class_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("show MyModel")
            self.assertEqual("** class doesn't exist **", mock_stdout.getvalue().strip())

    def test_invalid_class_destroy(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("destroy MyModel")
