#!/usr/bin/python3
"""
This is the test module for the review class.
"""


import unittest
from models.base_model import BaseModel
from models.review import Review
from models.engine.file_storage import FileStorage
import os


class TestReview(unittest.TestCase):
    """Test the instance attributes of the Review class. """

    def setUp(self):
        """ Test setUp method"""
        pass

    def reset_Storage(self):
        """ Test reset_Storage """
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """ Test tearDown method """
        self.reset_Storage()
        pass

    def test_instance(self):
        """ Test instance of BaseModel """
        review = Review()
        self.assertEqual(str(type(review)), "<class 'models.review.Review'>")
        self.assertIsInstance(review, Review)
        self.assertTrue(issubclass(type(review), BaseModel))

    def test_attr(self):
        """ Test instance attributes attr """
        attr = {'place_id': str, 'user_id': str, 'text': str}
        review = Review()
        for k, v in attr.items():
            self.assertTrue(hasattr(review, k))
            self.assertEqual(type(getattr(review, k, None)), v)


if __name__ == "__main__":
    unittest.main()
