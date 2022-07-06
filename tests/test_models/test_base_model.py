#!/usr/bin/python3
"""
Test model for BaseModel class
"""
from test_base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import unittest
from models.base_model import BaseModel
from unittest.case import _AssertRaisesContext


class TestBaseModel(unittest.TestCase):
    """ Class test Base Model """

    def setUp(self):
        """ create base models """
        self.x_base_model = BaseModel()
        self.y_base_model = BaseModel()

    def test_str_v_str(self):
        """ compare two stirng """
        self.assertIsInstance(self.x_base_model.__str__(), str)

    def test_str_info(self):
        """ check the info of the string"""
        self.assertIn("[BaseModel]", self.y_base_model.__str__())

    def test_Init(self):
        """ check if init is working """
        self.assertIsInstance(self.x_base_model, BaseModel)
        self.assertIsInstance(self.y_base_model, BaseModel)

    def test_id(self):
        """ check if all the insatnce hast it own id """
        self.assertNotEqual(self.x_base_model.id,
                            self.y_base_model.id)

    def test_kwarg(self):
        objdict = self.x_base_model.to_dict()
        self.kwarginstance = BaseModel(**objdict)
        self.assertIsInstance(self.kwarginstance, BaseModel)


if __name__ == "__main__":
    unittest.main()
