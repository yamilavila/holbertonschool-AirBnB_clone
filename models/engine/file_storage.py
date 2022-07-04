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
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

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
        ''' Method Deserializes '''
        temp_dic = {}
        try:
            with open(self.__file_path, 'r') as j_file:
                temp_dic = json.loads(j_file.read())
                for key, val in temp_dic.items():
                    self.__objects[key] = eval(value["__class__"])(**value)
        except IOError:
            pass


