#!/usr/bin/python3
"""
Test the user class and its methods.
"""


import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
import os


class TestUser(unittest.TestCase):
    """
    Test the user class and its methods.
    """

    def setUp(self):
        """
        Test setUp method
        """
        pass

    def reset_Storage(self):
        """ test reset_Storage """
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """ Test tearDown method """
        self.reset_Storage()
        pass

    def test_instance(self):
        """Test instance of BaseModel"""
        user = User()
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")
        self.assertIsInstance(user, User)
        self.assertTrue(issubclass(type(user), BaseModel))

    def test_attr(self):
        """ Test instance attributes attr """
        attr = {'email': str, 'password': str,
                'first_name': str, 'last_name': str}
        user = User()
        for k, v in attr.items():
            self.assertTrue(hasattr(user, k))
            self.assertEqual(type(getattr(user, k, None)), v)


if __name__ == "__main__":
    unittest.main()
