#!/usr/bin/python3
"""This module contains the class `User`"""


from models.base_model import BaseModel
import models


class User(BaseModel):
    """This class is inherited from BaseModel
    and is used to create users
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
