#!/usr/bin/python3
"""
Amenity.py testing file
"""
from models.amenity import Amenity
import unittest


class TestUser(unittest.TestCase):
    """Testing Amenity and the functions
    """
    def testInit(self):
        """
        """
        self.new_amenity = Amenity()
        self.assertIsIntance(self.new_amenity, Amenity)

    def testID(self):
        """
        """
        self.new_id_1 = Amenity()
        self.new_id_2 = Amenity()
        self.assertNotEqual(self.new_id_1.id, self.new_id_2.id)

    def testSave(self):
        """
        """
        self.save
