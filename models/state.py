#!/usr/bin/python3

"""
This module defines State class to store a state informations

Classes :
    State : inherits from BaseModel
    to store more information related to a state
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    a class to store state informations

    Args:
        name (string): the name of the state
    """

    name = ""
