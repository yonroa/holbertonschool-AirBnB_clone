#!/usr/bin/python3
"""This module contains the class `Review`"""


from models.base_model import BaseModel


class Review(BaseModel):
    """This class is inherited from BaseModel
    and is used to create Reviews
    """
    place_id = ""
    user_id = ""
    text = ""
