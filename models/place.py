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

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
