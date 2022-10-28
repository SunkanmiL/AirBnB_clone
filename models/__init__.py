#!/usr/bin/python3
"""Initializes the project package
-----

Variables
---------
    storage (FileStorage): instance of ``FileStorage``
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
