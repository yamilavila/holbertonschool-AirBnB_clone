#!usr/bin/python3
""" unittest for FileStorage"""
import models
import json
from time import sleep
from models import storage
from models.engine.file_storage import FileStorage
from datetime import datetime
import unittest
from models.base_model import BaseModel
import os

class TestFileStorage(unittest.TestCase):
    """unittest for FileStorage """

    def test_file_path(self):
        """ Testing file_path attribure"""
        test_obj = BaseModel()
        test_obj.id = "1"
        test_obj.save()
        try:
            os.remove("file.json")
        except:
            pass

    def test_objs(self):
        """ testing all the objects"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_all(self):
        """ testing all method """
        eval_obj = storage.all()
        self.assertEqual(dict, type(eval_obj))

    def test_docstring(self):
        """test"""
        self.assertIsNotNone(FileStorage.save.__doc__)

    def test_new(self):
        """ test new method"""
        test_obj = BaseModel()
        test_objx = FileStorage()
        test_objx.new(test_obj)
        self.assertNotEqual(test_objx.all(),0)

    def test_realod(self):
        """ test realod method"""
        test_obj = BaseModel()
        models.storage.new(test_obj)
        models.storage.save()
        models.storage.reload()
        dictionary = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + test_obj.id, dictionary)

    def test_save(self):
        """ test save method """
        my_mode = BaseModel()
        creat = test_objx.update_at
        sleep(2)
        my_mode.save()
        update = test_objx.update_at
        self.assertLess(creat, update)

    def test_save(self):
        test_objx = BaseModel()
        test_objy = FileStorage()
        models.storage.new(test_objx)
        models.storage.save()
        file_str = ""
        with open("file.json", 'r+') as j_file:
            file_str = j_file.read()
            self.assertIn("BaseModel", file_str)

if __name__ == '__main__':
    unittest.main()

