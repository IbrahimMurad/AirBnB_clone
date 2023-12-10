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

    def __init__(self, *args, **kwargs):
        """
        Initializes state_id and name attributes
        and the attributes inhereted from BaseModel
        """

        if len(kwargs) == 0:
            self.state_id = ""
            self.name = ""
            super().__init__()
        else:
            super().__init__(**kwargs)
            if 'name' not in kwargs.keys():
                self.name = ""
            if 'state_id' not in kwargs.keys():
                self.state_id = ""
