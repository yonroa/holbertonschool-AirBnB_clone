#!/usr/bin/python3
"""Contains the `BaseModel` class which is
the base for all other classes
"""


import uuid


class BaseModel:
    """Class that defines all common attributes/methods 
    for other classes
    """

    def __init__(self, id=uuid.uuid4()):
        self.id = str(id)
