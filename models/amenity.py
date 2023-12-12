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

    name = ""
