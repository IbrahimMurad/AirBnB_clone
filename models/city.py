#!/usr/bin/python3
"""
This module defines City class to store a city informations

Classes :
    City : inherits from BaseModel
    to store more information related to a city
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    a class to store city informations

    Args:
        name (string): the name of the city
        state.id (string): stores State.id
    """

    state_id = ""
    name = ""
