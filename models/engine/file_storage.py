#!/usr/bin/python3
"""Defines a class ``FileStorage``"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


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
        for key, value in FileStorage.__objects:
            my_dict[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(my_dict, f)

    def reload(self):
        """deserializes the JSON file to @__objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                my_dict = json.load(f)
        except FileNotFoundError:
            return
        
        for key, value in my_dict.items():
            match value['__class__']:
                case 'Amenity':
                    FileStorage.__object[key] = Amenity(**value)
                case 'BaseModel':
                    FileStorage.__object[key] = BaseModel(**value)
                case 'City':
                    FileStorage.__object[key] = City(**value)
                case 'Review':
                    FileStorage.__object[key] = Review(**value)
                case 'Place':
                    FileStorage.__object[key] = Place(**value)
                case 'State':
                    FileStorage.__object[key] = State(**value)
                case 'User':
                    FileStorage.__object[key] = User(**value)
