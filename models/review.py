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

    def __init__(self, *args, **kwargs):
        """
        Initializes place_id, user_id and text attributes
        and the attributes inhereted from BaseModel
        """

        if len(kwargs) == 0:
            self.place_id = ""
            self.user_id = ""
            self.text = ""
            super().__init__()
        else:
            super().__init__(**kwargs)
            if 'place_id' not in kwargs.keys():
                self.place_id = ""
            if 'user_id' not in kwargs.keys():
                self.user_id = ""
            if 'text' not in kwargs.keys():
                self.text = ""
