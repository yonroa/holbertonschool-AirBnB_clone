#!/usr/bin/python3
"""FileStorage
This module contains the FileStorage class
which controls object storage
"""

import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


class FileStorage:
    """This class serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (__file_path)"""
        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            data = {key: v.to_dict() for key, v in self.__objects.items()}
            json.dump(data, file)

    def reload(self):
        """Desearlizes the JSON file to '__objects':
        checks existence of the JSON file, reads data and instantiates every
        dictionary representation according the ['__class__'] name"""
        file = FileStorage.__file_path
        if path.exists(file):
            with open(file, 'r', encoding='utf-8') as jfile:
                FileStorage.__objects = json.load(jfile)
                for key, val in FileStorage.__objects.items():
                    c = FileStorage.__objects[key]['__class__']
                    try:
                        FileStorage.__objects[key] = self.__classes[c](**val)
                    except Exception:
                        pass
