#!/usr/bin/python3
"""
This module defines User class to store a user informations

Classes :
    User : inherits from BaseModel
    to store more information related to a user
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    a class to store user informations

    Args:
        first_name (string): the first name of the user
        last_name (string): the last name of the user
        email (string): the email of the user
        password (string): the passowrd of the user
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes all the attributes,
        the local and the inherited from BaseModel
        """

        if len(kwargs) == 0:
            self.first_name = ""
            self.last_name = ""
            self.email = ""
            self.password = ""
            super().__init__()
        else:
            super().__init__(**kwargs)
            if 'first_name' not in kwargs.keys():
                self.first_name = ""
            if 'last_name' not in kwargs.keys():
                self.last_name = ""
            if 'email' not in kwargs.keys():
                self.email = ""
            if 'password' not in kwargs.keys():
                self.password = ""
