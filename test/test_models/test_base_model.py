#!/usr/bin/python3
"""
Test model for BaseModel class
"""
from models.base_model import BaseModel
import unittest
from models import storage
import pycodestyle


class TestBaseModelClass(unittest.TestCase):
    """
    unittest for BaseModel
    """
    def setUp(self):
        self.new_instance_1 = BaseModel()
        self.new_instance_2 = BaseModel()

    def testInit(self):
        self.assertIsInstance(self.new_instance_1, BaseModel)
        self.assertIsInstance(self.new_instance_2, BaseModel)

    def testCreate(self):
        self.before_save = self.new_instance_1.update_at
        self.new_instance_1.save()
        self.after_save = self.new_instance_1.update_at

    def testUpdate(self):
        self.before_update = self.new_instance_2.created_at
        self.new_instance_2.save()
        self.after_update = self.new_instance_2.created_at
        self.assertEqual(str(self.before_update), str(self.after_update))

    def testDict(self):
        self.dictionary = dict(self.new_instance_1.__dict__)
        self.dictionary['__class__'] = "BaseModel"
        self.dictionary['created_at'] =\
            self.dictionary['created_at'].isoformat()
        self.dictionary['updated_at'] =\
            self.dictionary['updated_at'] =\
        self.assertDictEqual(self.dictionary, self.new_instance_1.to_dict())


class CodeStyleTest(unittest.TestCase):
    """
    Pycodestyle test
    """

    def testPycodestyle(self):
    """
    Test cases for pycodestyle
    """
    code_style = pycodestyle.StyleGuide(quiet=True)
    result = code_style.check_files(["models/base_model.py"])
    self.assertEqual(result.total_errors, 0, "BaseModel pycodestyle error")


if __name__ == '__main__':
    unittest.main()
