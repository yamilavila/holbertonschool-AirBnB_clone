#!/usr/bin/python3
""" unittest module for User """
from models import User
from datetime import datetime
import unittest
from test_base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Class User test"""

    def setUp(self):
        """ create 2 base models """
        self.X_user = User()
        self.Y_user = User()

    def test_str_v_str(self):
        """ test __str__ """
        self.assertIsInstance(self.X_user.__str__(), str)

    def test_str_info(self):
        """ check info of __str__"""
        self.assertIsInstance(self.X_user, User)
        self.assertIsInstance(self.Y_user, BaseModel)

    def test_id(self):
        """ Test if each object has it own id"""
        self.assertNotEqual(self.X_user.id,
                            self.Y_user.id)

    def test_Init(self):
        """ check if init works """
        self.assertIsInstance(self.X_user, User)
        self.assertIsInstance(self.Y_user, BaseModel)

    def test_id_str(self):
        """ test if id is string """
        self.assertIsInstance(self.X_user.id, str)

    def test_if_dict_has_key(self):
        """ ckeck if to_dict works """
        self.assertIn("created_at", self.X_user.to_dict())

    def test_to_dict(self):
        """check if to_dict works"""
        self.assertIsInstance(self.X_user.to_dict(), dict)

    def test_date(self):
        """ test if date works """
        self.assertIsInstance(self.X_user.created_at, datetime)
        self.assertIsInstance(self.Y_user.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
