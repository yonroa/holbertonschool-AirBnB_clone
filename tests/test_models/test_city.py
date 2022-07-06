#!/usr/bin/python3
"""
"""


import unittest
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
import os


class TestCity(unittest.TestCase):
    """
    """

    def setUp(self):
        """
        """
        pass

    def reset_Storage(self):
        """
        """
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """
        """
        self.reset_Storage()
        pass

    def test_instance(self):
        """
        """
        city = City()
        self.assertEqual(str(type(city)), "<class 'models.city.City'>")
        self.assertIsInstance(city, City)
        self.assertTrue(issubclass(type(city), BaseModel))

    def test_attr(self):
        """
        """
        attr = {'state_id': str, 'name': str}
        city = City()
        for k, v in attr.items():
            self.assertTrue(hasattr(city, k))
            self.assertEqual(type(getattr(city, k, None)), v)


if __name__ == "__main__":
    unittest.main()
