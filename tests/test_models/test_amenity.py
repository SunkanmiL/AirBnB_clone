#!/usr/bin/python3
"""Unittest module for the class `City`
Unittest classes:
    TestCity_instantiation
    TestCity_
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity_instantiation(unittest.TestCase):
    """Tests the instanciation of the City class"""

    def test_has_name_attr(self):
        m1 = Amenity()
        self.assertTrue('name' in dir(m1))

    def test_is_subclass_of_BaseClass(self):
        self.assertTrue(issubclass(Amenity, BaseModel) is True)

    def test_creates_instance_of_BaseClass(self):
        self.assertTrue(isinstance(Amenity(), BaseModel) is True)

    def test_diff_objects(self):
        m1 = Amenity()
        m2 = Amenity()
        self.assertTrue(m1 is not m2)

    def test_has_id(self):
        self.assertTrue(hasattr(Amenity(), 'id') is True)

    def test_initializes_three_attr(self):
        self.assertEqual(len(Amenity().__dict__), 3)

    def test_initializes_similar_attr(self):
        kwargs = {'name': 'Betty', 'age': 30}
        m1 = Amenity(**kwargs)
        b1 = BaseModel(**kwargs)
        self.assertEqual(len(m1.__dict__), len(b1.__dict__))
