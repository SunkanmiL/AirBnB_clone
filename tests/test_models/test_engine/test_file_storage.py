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

    def test_return_empt(self):
        ret = storage.all()
        self.assertTrue(ret == {})

    def test_no_arg(self):
        storage.new(self.b1)
        my_dict = storage.all()

    def test_returns_correct_data(self):
        
