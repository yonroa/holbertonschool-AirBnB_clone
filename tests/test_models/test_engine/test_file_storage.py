#!/usr/bin/python3
"""
This module is used to test the FileStorage class
"""


import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os


class TestStorage(unittest.TestCase):
    """
    """

    def setUp(self):
        """
        """
        self.object_test = BaseModel()

    def reset_Storage(self):
        """
        """
        FileStorage.__objects = {}
        if os.path.exists(FileStorage.__file_path):
            os.remove(FileStorage.__file_path)

    def tearDown(self):
        """
        """
        self.reset_Storage()
        pass

    def test_instantiation(self):
        """
        """
        self.assertEqual(type(storage).__name__, FileStorage)

    def test_attributes(self):
        """
        """
        self.reset_Storage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def check_all(self, class_name):
        """
        """
        self.reset_Storage()
        obj = eval(class_name)()
        storage.new(obj)
        key = f"{type(obj).__name__}.{obj.id}"
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], obj)

    def test_all_base_model(self):
        """Tests all() method for BaseModel."""
        self.check_all("BaseModel")

    def test_all_user(self):
        """Tests all() method for User."""
        self.check_all("User")

    def test_all_state(self):
        """Tests all() method for State."""
        self.check_all("State")

    def test_all_city(self):
        """Tests all() method for City."""
        self.check_all("City")

    def test_all_amenity(self):
        """Tests all() method for Amenity."""
        self.check_all("Amenity")

    def test_all_place(self):
        """Tests all() method for Place."""
        self.check_all("Place")

    def test_all_review(self):
        """Tests all() method for Review."""
        self.check_all("Review")

    def check_all_multiple(self, class_name):
        """
        """
        self.resetStorage()

        objs = [eval(class_name)() for i in range(1000)]
        [storage.new(o) for o in objs]
        self.assertEqual(len(objs), len(storage.all()))
        for o in objs:
            key = "{}.{}".format(type(o).__name__, o.id)
            self.assertTrue(key in storage.all())
            self.assertEqual(storage.all()[key], o)

    def test_all_multiple_base_model(self):
        """Tests all() method with many objects."""
        self.check_all_multiple("BaseModel")

    def test_all_multiple_user(self):
        """Tests all_multiple() method for User."""
        self.check_all_multiple("User")

    def test_all_multiple_state(self):
        """Tests all_multiple() method for State."""
        self.check_all_multiple("State")

    def test_all_multiple_city(self):
        """Tests all_multiple() method for City."""
        self.check_all_multiple("City")

    def test_all_multiple_amenity(self):
        """Tests all_multiple() method for Amenity."""
        self.check_all_multiple("Amenity")

    def test_all_multiple_place(self):
        """Tests all_multiple() method for Place."""
        self.check_all_multiple("Place")

    def test_all_multiple_review(self):
        """Tests all_multiple() method for Review."""
        self.check_all_multiple("Review")

    def check_new(self, class_name):
        """
        """
        self.resetStorage()
        o = eval(class_name)()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        self.assertTrue(key in FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[key], o)

    def test_new_base_model(self):
        """Tests new() method for BaseModel."""
        self.check_new("BaseModel")

    def test_new_user(self):
        """Tests new() method for User."""
        self.check_new("User")

    def test_new_state(self):
        """Tests new() method for State."""
        self.check_new("State")

    def test_new_city(self):
        """Tests new() method for City."""
        self.check_new("City")

    def test_new_amenity(self):
        """Tests new() method for Amenity."""
        self.check_new("Amenity")

    def test_new_place(self):
        """Tests new() method for Place."""
        self.check_new("Place")

    def test_new_review(self):
        """Tests new() method for Review."""
        self.check_new("Review")

    def check_save(self, line):
        """
        """
        self.reset_Storage()
        obj = eval(line)()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))
        dict_n = {key: obj.to_dict()}
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(dict_n)))
            f.seek(0)
            self.assertEqual(json.load(f), dict_n)

    def test_save_base_model(self):
        """Tests save() method for BaseModel."""
        self.check_save("BaseModel")

    def test_save_user(self):
        """Tests save() method for User."""
        self.check_save("User")

    def test_save_state(self):
        """Tests save() method for State."""
        self.check_save("State")

    def test_save_city(self):
        """Tests save() method for City."""
        self.check_save("City")

    def test_save_amenity(self):
        """Tests save() method for Amenity."""
        self.check_save("Amenity")

    def test_save_place(self):
        """Tests save() method for Place."""
        self.check_save("Place")

    def test_save_review(self):
        """Tests save() method for Review."""
        self.check_save("Review")

    def check_reload(self, line):
        """
        """
        self.reset_Storage()
        self.assertEqual(FileStorage._FileStorage__objects, {})
        new_obje = eval(line)()
        storage.new(new_obje)
        key = "{}.{}".format(type(new_obje).__name__, new_obje.id)
        storage.save()
        storage.reload()
        self.assertEqual(new_obje.to_dict(), storage.all()[key].to_dict())

    def test_reload_base_model(self):
        """Tests reload() method for BaseModel."""
        self.check_reload("BaseModel")

    def test_reload_user(self):
        """Tests reload() method for User."""
        self.check_reload("User")

    def test_reload_state(self):
        """Tests reload() method for State."""
        self.check_reload("State")

    def test_reload_city(self):
        """Tests reload() method for City."""
        self.check_reload("City")

    def test_reload_amenity(self):
        """Tests reload() method for Amenity."""
        self.check_reload("Amenity")

    def test_reload_place(self):
        """Tests reload() method for Place."""
        self.check_reload("Place")

    def test_reload_review(self):
        """Tests reload() method for Review."""
        self.check_reload("Review")


if __name__ == "__main__":
    unittest.main()
