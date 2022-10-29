#!/usr/bin/python3
"""Defines a class ``FileStorage``"""
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to
    instance

    Private class Attributes
    ------------------------
        __file_path (str): path to the JSON file
        __objects (dict): stores all objects

    Public Instance Methods
    -----------------------
        all(self): returns the dictionary @__objects
        new(self, obj): sets in @__objects the @obj with key
                        <obj class-name>.id
        save(self): serializes @__objects to the JSON file (path: @__file_path)
        reload(self): deserializes the JSON file to @__objects.
    """

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """Returns the dictionary @__objects"""
        return (self.__objects)

    def new(self, obj):
        """sets in @__objects the @obj with key <obj class_name>.id

        Args:
            obj (object): An instance of a class
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes @__objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes the JSON file to @__objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
