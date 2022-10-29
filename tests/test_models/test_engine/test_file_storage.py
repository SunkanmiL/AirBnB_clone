#!/usr/bin/python3
"""Defines unittest for ``file_storage.py``

Unittest classes:
    TestFileStorage_all - line
    TestFileStorage_new - line
    TestFileStorage_save - line
    TestFileStorage_reload - line
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os

storage = FileStorage()


class TestFileStorage_all(unittest.TestCase):
    """Tests the all(...) method of FileStorage class"""

    def setUp(self):
        kwargs = {'name': 'Betty', 'age': 25}
        self.b1 = BaseModel(**kwargs)

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        storage.__objects = dict()

    def test_return_empt(self):
        ret = storage.all()
        self.assertTrue(ret == {})

    def test_no_arg(self):
        storage.new(self.b1)
        my_dict = storage.all()

    def test_returns_correct_data(self):
        storage.new(self.b1)
        my_dict = storage.all()
        key = obj.__class__.__name__ + '.' + obj.id
        self.assertTrue(key in my_dict)

    def test_returns_correct_data_2(self):
        storage.new(self.b1)
        my_dict = storage.all()
        key = obj.__class__.__name__ + '.' + obj.id
        self.assertEqual(my_dict[key]['name'], 'Betty')


class TestBaseModel_new(unittest.TestCase):
    """unittest class for testing the new(...) method of FileStorage"""

    def setUp(self):
        kwargs = {'name': 'Betty', 'age': 25}
        self.b1 = BaseModel(**kwargs)

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        storage.__objects = dict()

    def test_no_arg(self):
        with self.assertRaise(TypeError):
            storage.new()

    def test_one_arg(self):
        storage.new(self.b1)
        key = obj.__class__.__name__ + '.' + obj.id
        self.assertTrue(key in storage.all())

    def test_None_arg(self):
        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_NaN_arg(self):
        with self.assertRaises(AttributeError):
            storage.new(float('Nan'))

    def test_stores_correct(self):
        storage.new(self.b1)
        my_dict = storage.all()
        key = obj.__class__.__name__ + '.' + obj.id
        self.assertEqual(my_dict[key]['name'], 'Betty')


class TestBaseModel_save(unittest.TestCase):
    """unittest class to test for the save(...) method of FileStorage class"""

    def test_no_arg(self):
        storage.new(self.b1)
        storage.save()
        os.exists(storage.
