#!/usr/bin/python3
""" This module defines Amenity class to store an amenity informations

Classes :
    Amenity : inherits from BaseModel
    to store amenity informations
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    a class to store amenity informations

    Args:
        name (string): the name of the amenity
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes name attribute
        and the attributes inhereted from BaseModel
        """

        if len(kwargs) == 0:
            self.name = ""
            super().__init__()
        else:
            super().__init__(**kwargs)
            if 'name' not in kwargs.keys():
                self.name = ""
