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
from models.user import User


class FileStorage():
    """
    Serializes instances to a JSON file and deserializes JSON file
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return all objects of the dictionary """
        return self.__objects

    def new(self, obj):
        """ create a new object in the dictionary  """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """
        Method: Serializes __objects to the JSON file (path: __file_path)
        """
        # comment: [objs_dict] Dictionary contains all dict ot the objects
        objs_dict = {}

        # comment: Serializable objects and save in json file
        with open(self.__file_path, 'w') as j_file:
            for k, v in self.__objects.items():
                objs_dict[k] = v.to_dict()
            json.dump(objs_dict, j_file, default=str)

    def reload(self):
        ''' Method Deserializes '''
        temp_dic = {}
        try:
            with open(self.__file_path, 'r') as file_json:
                temp_dic = json.loads(file_json.read())
                for key, value in temp_dic.items():
                    self.__objects[key] = eval(value["__class__"])(**value)
        except IOError:
            pass
