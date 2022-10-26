#!/usr/bin/python3
"""Defines a class ``User``"""
from models.base_model import BaseModel


class User(BaseModel):
    """Inherits from `BaseModel`

    Public Class Attributes
    -----------------------
        email (str): User's email
        password (str): user's password
        first_name (str): user's first name
        last_name (str): user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
