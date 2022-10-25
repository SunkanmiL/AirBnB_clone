#!/usr/bin/python3
"""Defines a class ``BaseModel``"""
import uuid


class BaseModel:
    """A Base class that defines all methods/attributes for it Subclass

    ...

    Attributes
    ----------
    id (str): 


    Methods
    -------
    __init__(self,)

    """

    def __init__(self, ):
        """Initializes an instance

        Args:

        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime()
        self.updated_at = datetime.datetime()

    def save(self):
        """Updates self.updated_at with the current datetime"""
        self.updated_at = datetime.datetime()

    def __str__(self):
        """Returns the string representation of an instance"""
        return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))
