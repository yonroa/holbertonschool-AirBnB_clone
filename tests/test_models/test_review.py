#!/usr/bin/python3
"""
"""


import unittest
from models.base_model import BaseModel
from models.review import Review
from models.engine.file_storage import FileStorage
import os


class TestReview(unittest.TestCase):
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
        review = Review()
        self.assertEqual(str(type(review)), "<class 'models.review.Review'>")
        self.assertIsInstance(review, Review)
        self.assertTrue(issubclass(type(review), BaseModel))

    def test_attr(self):
        """
        """
        attr = {'place_id': str, 'user_id': str, 'text': str}
        review = Review()
        for k, v in attr.items():
            self.assertTrue(hasattr(review, k))
            self.assertEqual(type(getattr(review, k, None)), v)


if __name__ == "__main__":
    unittest.main()
