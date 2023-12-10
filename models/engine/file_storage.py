#!/usr/bin/python3
"""
Module : models.engine.file_storage.py

This module works as a storage system (saves and loads)
to all the objects created before

Classes :
    FileStorage : a class that serializes instances to a JSON file
    and deserializes JSON file to instances.
"""

import json


class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances.

    Attributes :
        __file_path : stores json file in which all the objects are stored
        __objects : a dictionary containing all the created objects
    """

    def all_classes(self):
        """
        returns a dictionary of all object types of AirBnB project
        """

        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.state import State
        my_classes = {
            'BaseModel': BaseModel,
            'User': User,
            'City': City,
            'Amenity': Amenity,
            'Review': Review,
            'Place': Place,
            'State': State
            }
        return my_classes

    def __init__(self):
        """
        Initialize __file_path and __objects attributes
        """

        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        returns __objects attribute
        """
        return self.__objects

    def new(self, obj):
        """
        add a new object to the __objects dictionary,
        where the key is in the format <class name>.id

        Args:
            obj (any): the object to be added to __objects
        """

        obj_key = obj.__class__.__name__ + "." + obj.__dict__['id']
        self.__objects[obj_key] = obj

    def save(self):
        """
        serializing all the objects in __objects
        (saves all the current objects stored in __objects into a json file)
        """

        obj_to_json = {}
        for key, value in self.__objects.items():
            obj_dict = value.to_dict()
            obj_to_json[key] = obj_dict
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_to_json, f)

    def reload(self):
        """
        deserializing all the objects from the json file
        (loads all the current objects stored in the json file
        to __objects)
        """

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json_to_dict = json.load(f)
            for key, value in json_to_dict.items():
                obj_type = self.all_classes()[value['__class__']]
                self.__objects[key] = obj_type(**value)
        except FileNotFoundError:
            pass
