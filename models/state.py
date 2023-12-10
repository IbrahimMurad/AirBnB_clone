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
