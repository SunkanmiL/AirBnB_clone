#!/usr/bin/python3
"""Defines a class ``Amenity``"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Creates an `Amenity` instance, a subclass of `BaseModel`

    Public Class Attributes
    -----------------------
        name (str): Name of Amenity
    """
    name = ""
