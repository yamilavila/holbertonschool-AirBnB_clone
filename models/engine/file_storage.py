#!/usr/bin/python3
from models.base_model import BaseModel
import json
import os


class FileStorage(BaseModel):
    def __init__(self, __file_path, __objects)
        self.__file_path = os.path.join()
        self.__objects = 

    def all(self):
        return __objects

    def new(self, obj):
        self.__objects = self.__name__.id

    def save(self):
        json.dumps(__objects)


    def realod(self):
        if os.path.exist(self.__file_path):
            json.loads(__objects)
        else:
            continue




