#!/usr/bin/python3
"""
Module for FileStorage class
"""
import json
from os.path import exists


class FileStorage:
    """
    FileStorage class for serializing instances to a JSON file and deserializing JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        json_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(json_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        if exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                json_dict = json.load(file)
                for key, value in json_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_dict = value.copy()
                    obj_dict['__class__'] = class_name
                    self.__objects[key] = eval(class_name)(**obj_dict)
