#!/usr/bin/python3
"""
"""


import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
import os


class TestUser(unittest.TestCase):
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
        user = User()
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")
        self.assertIsInstance(user, User)
        self.assertTrue(issubclass(type(user), BaseModel))

    def test_attr(self):
        """
        """
        attr = {'email': str, 'password': str,
                'first_name': str, 'last_name': str}
        user = User()
        for k, v in attr.items():
            self.assertTrue(hasattr(user, k))
            self.assertEqual(type(getattr(user, k, None)), v)


if __name__ == "__main__":
    unittest.main()
