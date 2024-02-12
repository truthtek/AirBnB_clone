import json
from models.base_model import BaseModel

class FileStorage:
    """Class to manage serialization and deserialization of instances to JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(json_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects (only if the JSON file exists)."""
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as file:
                json_dict = json.load(file)
            for key, value in json_dict.items():
                cls_name, obj_id = key.split('.')
                cls = BaseModel.__subclasses__()[0]
                if cls_name in globals():
                    cls = globals()[cls_name]
                obj = cls(**value)
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
