#!/usr/bin/python3
"""
This is the amenity test module.
"""


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import os


class TestAmenity(unittest.TestCase):
    """
    Test the amenity class
    """

    def setUp(self):
        """
        Test Set instance attributes
        """
        pass

    def reset_Storage(self):
        """
        Test reset_Storage
        """
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """
        Test tearDown method
        """
        self.reset_Storage()
        pass

    def test_instance(self):
        """
        Test instance of BaseModel
        """
        amenity = Amenity()
        self.assertEqual(str(type(amenity)),
                         "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(issubclass(type(amenity), BaseModel))

    def test_attr(self):
        """
        Test instance attributes attr 
        """
        attr = {'name': str}
        amenity = Amenity()
        for k, v in attr.items():
            self.assertTrue(hasattr(amenity, k))
            self.assertEqual(type(getattr(amenity, k, None)), v)


if __name__ == "__main__":
    unittest.main()
