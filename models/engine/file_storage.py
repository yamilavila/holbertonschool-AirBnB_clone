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
        return  self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = ob

    def save(self):
        """
        Method: Serializes __objects to the JSON file (path: __file_path)
        """
        #comment: [objs_dict] Dictionary contains all dict ot the objects
        objs_dict = {}

        #comment: Serializable objects and save in json file
        for key, obj in self.__objects.items():
            objs_dict[key] = obj.to_dict()
        with open(self.__file_path, mode="w") as file_json:
            file_json.write(json.dumps(objs_dict))


    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, mode="r") as file_json:
                for key, values in json.load(file_json).items():
                    class_name = values["__class__"]
                    self.new(class_dict[class_name](**values))
        except FileNotFoundError:
            pass
