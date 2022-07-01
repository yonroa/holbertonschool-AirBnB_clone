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

    def __init__(self, *args, **kwargs):
        """Initialites a base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
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
