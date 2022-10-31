#!/usr/bin/python3
"""Unittest module for the class `City`
Unittest classes:
    TestCity_instantiation
    TestCity_
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity_instantiation(unittest.TestCase):
    """Tests the instanciation of the City class"""

    def test_has_stateId_attr(self):
        m1 = State()
        self.assertTrue('state_id' in dir(m1))

    def test_subclass_of_BaseClass(self):
        self.assertTrue(issubclass(City, BaseModel) is True)

    def test_creates_instance_of_BaseClass(self):
        self.assertTrue(isinstance(City(), BaseModel) is True)

    def test_diff_objects(self):
        c1 = City()
        c2 = City()
        self.assertTrue(c1 is not c2)

    def test_has_id(self):
        self.assertTrue(hasattr(City(), 'id') is True)

    def test_initializes_three_attr(self):
        self.assertEqual(len(City().__dict__), 3)

    def test_initializes_similar_attr(self):
        kwargs = {'name': 'Betty', 'age': 30}
        c1 = City(**kwargs)
        b1 = BaseModel(**kwargs)
        self.assertEqual(len(c1.__dict__), len(b1.__dict__))
