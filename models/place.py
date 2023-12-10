#!/usr/bin/python3
"""
This module defines Place class to store the informations
related to a place

Classes :
    Place : inherits from BaseModel
    to store the information related to a palce
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    a class to store a place informations

    Args:
        city_id (string): stores City.id
        user_id (string): stores User.id
        name (string): stores the name of the place
        description (string): a description of the place
        number_rooms (integer): the number of the rooms
        number_bathrooms (integer): the number of the bathrooms
        max_guest (integer): the capacity of the place
        price_by_night (integer): price per night
        latitude (float): latitude (location)
        longitude (float): longitude (location)
        amenity_ids (list of string): a list to store Amenity.id's
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes all the attributes including
        the attributes inhereted from BaseModel
        """

        if len(kwargs) == 0:
            self.city_id = ""
            self.user_id = ""
            self.name = ""
            self.description = ""
            self.number_rooms = 0
            self.number_bathrooms = 0
            self.max_guest = 0
            self.price_by_night = 0
            self.latitude = 0.0
            self.longitude = 0.0
            self.amenity_ids = []
            super().__init__()
        else:
            super().__init__(**kwargs)
            if 'city_id' not in kwargs.keys():
                self.city_id = ""
            if 'user_id' not in kwargs.keys():
                self.user_id = ""
            if 'name' not in kwargs.keys():
                self.name = ""
            if 'description' not in kwargs.keys():
                self.description = ""
            if 'number_rooms' not in kwargs.keys():
                self.number_rooms = 0
            if 'number_bathrooms' not in kwargs.keys():
                self.number_bathrooms = 0
            if 'max_guest' not in kwargs.keys():
                self.max_guest = 0
            if 'price_by_night' not in kwargs.keys():
                self.price_by_night = 0
            if 'latitude' not in kwargs.keys():
                self.latitude = 0.0
            if 'longitude' not in kwargs.keys():
                self.longitude = 0.0
            if 'amenity_ids' not in kwargs.keys():
                self.amenity_ids = []
