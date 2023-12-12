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

    first_name = ""
    last_name = ""
    email = ""
    password = ""
