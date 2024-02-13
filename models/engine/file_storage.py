#!/usr/bin/python3
"""
Module for FileStorage class
"""
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""
    
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Initialize FileStorage instance."""
        self.reload()

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        serializable = {}
        for key, value in FileStorage.__objects.items():
            serializable[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(serializable, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as file:
                deserialized = json.load(file)
                for key, value in deserialized.items():
                    cls_name, obj_id = key.split('.')
                    cls = {"BaseModel": BaseModel, "User": User}[cls_name]
                    self.new(cls(**value))
        except FileNotFoundError:
            pass


