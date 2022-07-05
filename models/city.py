#!/usr/bin/python3
"""This module contains the class `City`"""


from models.base_model import BaseModel


class City(BaseModel):
    """This class is inherited from BaseModel
    and is used to create Cities
    """
    state_id = ""
    name = ""
