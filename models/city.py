#!/usr/bin/python3
"""Defines the class ``City``"""
from models.base_model import BaseModel


class City(BaseModel):
    """Creates a `City` instance, which is a subclass of `BaseModel`

    Public Class Attributes
    -----------------------
        state_id (str): state.id value
        name (str): Name of City
    """
    state_id = ""
    name = ""
