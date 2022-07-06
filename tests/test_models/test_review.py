#!/usr/bin/python3
""" unitets of amenity"""
from datetime import datetime
import unittest
from models import Review
from unittest.case import _AssertRaisesContext
from test_base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """ test Place class """

    def setUp(self):
        """ create two base models"""
        self.X_user = Review()
        self.Y_user = Review()

    def test_Init(self):
        """ Check if Init works"""
        self.assertIsInstance(self.X_user, Review)
        self.assertIsInstance(self.Y_user, Review)

