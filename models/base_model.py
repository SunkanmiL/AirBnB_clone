#!/usr/bin/python3
"""Defines a class ``BaseModel``"""
import uuid
import re
import models
from datetime import datetime


class BaseModel:
    """A Base class that defines all methods/attributes for it Subclass

    ...

    Attributes
    ----------
        id (str): The `id` of each instance, automatically allocated using
                  the ``uuid`` module.
        created_at (str): the isoformat representation of when the object was
                          created.
        updated_at (str): the isoformat representation of when the object was
                          last updated.


    Methods
    -------
        __init__(self, *args, **kwargs): Initializes an instance
        save(self): Updates self.updated_at with the current datetime
        to_dict(self): Returns a dictionary containing all keys/values
                       of __dict__ of the instance
        __str__(self): Returns the string representation of an instance
    """

    def __init__(self, *args, **kwargs):
        """Initializes an instance

        Args:
            args (tuple):
            kwargs (dict): a dict of key/word arguments passed, where each
                           key represents attribute name, with it value
                           representing the value of the attribute name
        """

        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    """
                    dt_values = re.split('[-T:.]', value)
                    dt_values = [int(i) for i in dt_values]
                    dt_values = tuple(dt_values)
                    value = datetime(*dt_values)
                    """
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)

    def save(self):
        """Updates self.updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        my_dict = dict()
        for key, value in self.__dict__.items():
            my_dict[key] = value
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()

        return (my_dict)

    def __str__(self):
        """Returns the string representation of an instance"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))
