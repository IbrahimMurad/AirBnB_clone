#!/usr/bin/python3
"""
This module defines Review class to store
a review of a user to a place

Classes :
    Review : inherits from BaseModel
    to store the review of a user to a place
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    stores the review of a user to a place

    Args:
        place_id (string): stores Place.id
        user_id (string): stores User_id
        text (string): stores the review
    """

    place_id = ""
    user_id = ""
    text = ""
