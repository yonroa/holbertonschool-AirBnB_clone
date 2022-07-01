#!/usr/bin/python3
"""Contains the `BaseModel` class which is
the base for all other classes
"""


import uuid
import datetime


class BaseModel:
    """Class that defines all common attributes/methods
    for other classes
    """

    def __init__(self, id=uuid.uuid4()):
        """Initialites a base model"""
        self.id = str(id)
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns a nice print of the base model"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Saves the date of the update of the class"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a new dict of the class"""
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
