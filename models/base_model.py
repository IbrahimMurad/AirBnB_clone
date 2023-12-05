from uuid import uuid4
from datetime import datetime

"""
Module : base_model.py

This module defines BaseModel class that defines all common
attributes/methods for other classes in AirBnB clone project.

Classes :
    BaseModel : A class that defines id, created_at and updated_at attributes
    and save() and to_dict() methods
"""


class BaseModel:
    """
    defines all common attributes/methods for other classes
    in AirBnB clone project.

    Attributes:
        id (str): a unique identifier string assigned to each instance.
        created_at (datetime): the time at which the instance increated.
        updated_at (datetime) : the time at which the instance is edited.

    Methods:
        save(): updates updated_at attribute to the current datetime.
        to_dict(): creates a dictionary containing all keys/values
        of the instance.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize BaseModel attributes, id, created_at and updated_at
        """

        if not len(kwargs) == 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    pass
                elif key == 'created_at':
                    self.created_at = datetime.fromisoformat(value)
                elif key == 'updated_at':
                    self.updated_at = datetime.fromisoformat(value)
                else:
                    setattr(self, key, value)
        if 'id' not in kwargs.keys():
            self.id = uuid4()
        if 'created_at' not in kwargs.keys():
            self.created_at = datetime.now()
        if 'updated_at' not in kwargs.keys():
            self.updated_at = datetime.now()

    def __str__(self):
        """
        formats data of the instance in a string

        Returns:
            string : in the format [<class name>] (<self.id>) <self.__dict__>
        """

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        updates updated_at attribute to the current time

        Returns:
            None
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Stores all the date of the instance in a dictionary, where:
        a key __class__ is added to this dictionary with the class name
        created_at and updated_at must be converted to
        string object in ISO format

        Returns :
            a dictionary representation of the class
        """

        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
