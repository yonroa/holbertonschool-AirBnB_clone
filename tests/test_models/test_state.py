#!/usr/bin/python3
"""
This is the test module for the state class.
"""


import unittest
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage
import os


class TestState(unittest.TestCase):
    """ Test state class methods """

    def setUp(self):
        """ Test setUp method """
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
        state = State()
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")
        self.assertIsInstance(state, State)
        self.assertTrue(issubclass(type(state), BaseModel))

    def test_attr(self):
        """ Test instance attributes attr """
        attr = {'name': str}
        state = State()
        for k, v in attr.items():
            self.assertTrue(hasattr(state, k))
            self.assertEqual(type(getattr(state, k, None)), v)


if __name__ == "__main__":
    unittest.main()
