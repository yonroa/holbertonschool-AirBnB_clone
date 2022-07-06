#!/usr/bin/python3
"""
"""


import unittest
from models.base_model import BaseModel
from models.place import Place
from models.engine.file_storage import FileStorage
import os


class TestPlace(unittest.TestCase):
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
        place = Place()
        self.assertEqual(str(type(place)), "<class 'models.place.Place'>")
        self.assertIsInstance(place, Place)
        self.assertTrue(issubclass(type(place), BaseModel))

    def test_attr(self):
        """
        """
        attr = {'city_id': str, 'user_id': str, 'name': str,
                'description': str, 'number_rooms': int,
                'number_bathrooms': int, 'max_guest': int,
                'price_by_night': int, 'latitude': float,
                'longitude': float, 'amenity_ids': list}
        place = Place()
        for k, v in attr.items():
            self.assertTrue(hasattr(place, k))
            self.assertEqual(type(getattr(place, k, None)), v)


if __name__ == "__main__":
    unittest.main()
