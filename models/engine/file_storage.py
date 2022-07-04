#!/usr/bin/python3
"""
Class FireStorage
"""
from models.base_model import BaseModel
import json
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
    Serializes instances to a JSON file and deserializes JSON file
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = ob

    def save(self):
        """
        Method: Serializes __objects to the JSON file (path: __file_path)
        """
        # comment: [objs_dict] Dictionary contains all dict of the objects
        new_dict = {}

        # comment: Serializable objects and save in json file
        with open(self.__file_path, mode="w") as file_json:
            for key, val in self.__objects.items(file_json):
                new_dict[key] = val.to_dict()
            json.dump(new_dict, file_json, default=str)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        temp_dict = {}
        try:
            with open(self.__file_path, mode="r") as file_json:
                temp_dict = json.loads(file_json.read())
                for key, values in temp_dict.items():
                    self.__objects[key] = eval(val["__class__"])(**val)
        except FileNotFoundError:
            pass
