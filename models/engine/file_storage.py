#!/usr/bin/python3
"""
Class FireStorage
"""
from models.base_model import BaseModel
import json
import os


class FileStorage(BaseModel):
    """
    Serializes instances to a JSON file and deserializes JSON file
    """

    def __init__(self, __file_path, __objects)
        self.__file_path = os.path.join()
        self.__objects = {}

    def all(self):
        return  self.__objects

    def new(self, obj):
        self.__objects = self.__name__.id

    def save(self):
        """
        Method: Serializes __objects to the JSON file (path: __file_path)
        """
        #comment: [objs_dict] Dictionary contains all dict ot the objects
        objs_dict = self.__objects.copy()

        #comment: Serializable objects and save in json file
        for key, obj in self.__objects.items():
            objs_dict[key] = obj.to_dict()
        with open(self.__file_path, mode="W") as file_json:
            file_json.write(json.dumps(__objects))


    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, mode="r") as file_jason:
                for key, values in json.load(file_json).items():
                    class_name = values["__class__"]
                    self.new(class_dict[class_name](**values))
        except Exception:

        """
        if os.path.exist(self.__file_path):
            json.loads(__objects)

        else:
            continue
        """
