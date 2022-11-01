#!/usr/bin/python3
"""Defines unittest for base_model.py

Unittest classes:
    TestBaseModel_instantiation - line 16
    TestBaseModel_save - line 68
    TestBaseModel_to_dict - line 100
"""
import unittest
import re
import os
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """unittest class for testing `BaseModel` object instantiation"""

    def test_no_arg(self):
        b1 = BaseModel()
        self.assertEqual(len(b1.__dict__), 3)

    def test_has_diff_id(self):
        b1 = BaseMode()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_none_arg(self):
        b1 = BaseModel(None)
        self.assertNotEqual(b1.id, None)

    def test_unique_id(self):
        self.assertEqual(BaseModel(id=33).id, 33)

    def test_unique_created_at(self):
        created = "2022-10-26T21:34:09.045778"
        self.assertEqual(BaseModel(created_at=created).created_at, created)

    def test_unique_updated_at(self):
        updated = "2022-10-26T21:34:09.045778"
        self.assertEqual(BaseModel(updated_at=updated).updated_at, updated)

    def test_created_at_isoformat(self):
        kwargs = {'created_at': '2022-10-26T21:34:09.045778'}
        base = BaseModel(**kwargs)
        len_split = len(re.split("[:-T.]", base.created_at))
        self.assertEqual(len_split, 7)

    def test_updated_at_isoformat(self):
        kwargs = {'updated_at': '2022-10-26T21:34:09.046778'}
        base = BaseModel(**kwargs)
        len_split = len(re.split("[:-T.]", base.updated_at))
        self.assertEqual(len_split, 7)

    def test_assign_args(self):
        args = ('age', 'name')
        self.assertEqual(len(Basemodel(*args).__dict__), 3)

    def test_assign_kwargs_attrCount(self):
        kwargs = {name = "Betty", age = 14}
        self.assertEqual(len(BaseModel(**kwargs).__dict__), 5)

    def test_assign_kwargs(self):
        kwargs = {name = "Betty", age = 14}
        self.assertIn('name', BaseModel(**kwargs).__dict__)


class TestBaseModel_save(unittest.TestCase):
    """unittest class for testing the save method"""

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_one_arg(self):
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.save(3)

    def test_None_arg(self):
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.save(None)

    def test_updated_at_diff(self):
        base = BaseModel()
        before_save = base.updated_at
        base.save()
        after_save = base.updated_at
        self.assertNotEqual(before_save, after_save)

    def test_saved_to_file(self):
        base = BaseModel()
        base.save()
        self.assertTrue(os.path.exists("file.json") is True)


class TestBaseModel_to_dict(unittest.TestCase):
    """unittest class to test the `to_dict(...)` method"""

    def setUp(self):
        self.base = BaseModel()

    def test_no_arg(self):
        self.assertEqual(len(self.base.to_dict()), 4)

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            self.base.to_dict(3)

    def test_None_arg(self):
        with self.assertRaises(TypeError):
            self.base.to_dict(None)

    def test_stores_complete_attrLen(self):
        kwargs = {None: 3, 'Age': 25}
        base = BaseModel(**kwargs)
        my_dict = base.to_dict()
        self.assertEqual(len(my_dict), 6)

    def test_stores_complete_attr(self):
        kwargs = {'Name': 'Betty', 'Age': 25}
        base = BaseModel(**kwargs)
        my_dict = base.to_dict()
        self.assertTrue('Age' in my_dict)

    def test_stores_correct_class(self):
        kwargs = {'Name': 'Betty', 'Age': 25, '__class__': 'int'}
        base = BaseModel(**kwargs)
        my_dict = base.to_dict()
        self.assertTrue(my_dict['__class__'] == base.__class__.__name__)

    def test_store_correct_date(self):
        kwargs = {'Name': 'Betty', 'Age': 25, 'created_at': '20-10-20M
                  20-10-20.23456'}
        base = BaseModel(**kwargs)
        my_dict = base.to_dict()
        self.assertTrue(my_dict['created_at'] != '20-10-20M
                        20-10-20.23456')


if __name__ == "__main__":
    unittest.main()
