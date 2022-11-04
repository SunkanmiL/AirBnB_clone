#!/usr/bin/python3
"""Defines a class ``FileStorage``"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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
        return (FileStorage.__objects)

    def new(self, obj):
        """sets in @__objects the @obj with key <obj class_name>.id

        Args:
            obj (object): An instance of a class
        """
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes @__objects to the JSON file (path: __file_path)"""
        my_dict = dict()
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(my_dict, f)

    def reload(self):
        """deserializes the JSON file to @__objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                my_dict = json.load(f)
                for key, value in my_dict.items():
                    if (value['__class__'] == 'Amenity'):
                        FileStorage.__objects[key] = Amenity(**value)
                    elif (value['__class__'] == 'BaseModel'):
                        FileStorage.__objects[key] = BaseModel(**value)
                    elif (value['__class__'] == 'City'):
                        FileStorage.__objects[key] = City(**value)
                    elif (value['__class__'] == 'Review'):
                        FileStorage.__objects[key] = Review(**value)
                    elif (value['__class__'] == 'Place'):
                        FileStorage.__objects[key] = Place(**value)
                    elif (value['__class__'] == 'State'):
                        FileStorage.__objects[key] = State(**value)
                    elif (value['__class__'] == 'User'):
                        FileStorage.__objects[key] = User(**value)
        except FileNotFoundError:
            return
