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


class TestFileStorage_all(unittest.TestCase):
    """Tests the all(...) method of FileStorage class"""

    def setUp(self):
        kwargs = {'name': 'Betty', 'age': 25}
        self.b1 = BaseModel(**kwargs)
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        delattr(self, 'storage')

    def test_return_empt(self):
        ret = self.storage.all()
        self.assertTrue(ret == {})

    def test_no_arg(self):
        storage.new(self.b1)
        my_dict = self.storage.all()

    def test_returns_correct_data(self):
        self.storage.new(self.b1)
        my_dict = self.storage.all()
        key = obj.__class__.__name__ + '.' + obj.id
        self.assertTrue(key in my_dict)

    def test_returns_correct_data_2(self):
        self.storage.new(self.b1)
        my_dict = self.storage.all()
        key = obj.__class__.__name__ + '.' + obj.id
        self.assertEqual(my_dict[key]['name'], 'Betty')


class TestBaseModel_new(unittest.TestCase):
    """unittest class for testing the new(...) method of FileStorage"""

    def setUp(self):
        kwargs = {'name': 'Betty', 'age': 25}
        self.b1 = BaseModel(**kwargs)
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        delattr(self, 'storage')

    def test_no_arg(self):
        with self.assertRaise(TypeError):
            storage.new()

    def test_one_arg(self):
        self.storage.new(self.b1)
        key = obj.__class__.__name__ + '.' + obj.id
        self.assertTrue(key in storage.all())

    def test_None_arg(self):
        with self.assertRaises(AttributeError):
            self.storage.new(None)

    def test_NaN_arg(self):
        with self.assertRaises(AttributeError):
            self.storage.new(float('Nan'))

    def test_stores_correct(self):
        self.storage.new(self.b1)
        my_dict = self.storage.all()
        key = obj.__class__.__name__ + '.' + obj.id
        self.assertEqual(my_dict[key]['name'], 'Betty')


class TestBaseModel_save(unittest.TestCase):
    """unittest class to test for the save(...) method of FileStorage class"""

    def setUp(self):
        self.file = '_' + type(storage).__name__ + '__file_path'
        self.storage = FileStorage()
        self.b1 = BaseModel('name': 'Betty', 'age': 25)
        self.b2 = BaseModel('name': 'John', 'age': 23)

    def tearDown(self):
        delattr(self, 'storage')
        try:
            os.remove(self.file)
        except IOError:
            pass

    def test_no_arg(self):
        self.storage.new(self.b1)
        self.storage.save()
        file_exists = os.path.exists(getattr(storage, self.file))
        self.assertTrue(file_exists, True)

    def test_one_arg(self):
        self.storage.new(self.b1)
        with self.assertRaises(TypeError):
            self.storage.save("name")

    def test_saves_empty(self):
        self.storage.save()
        self.storage.reload()
        my_dict = self.storage.all()
        self.assertEqual(my_dict, {})

    def test_looses_unsaved_data_1(self):
        self.storage.new(self.b1)
        self.storage.save()

        self.storage.new(b2)

        self.storage.reload()
        my_dict = self.storage.all()

        self.assertEqual(len(my_dict), 1)

    def test_looses_unsaved_data_2(self):
        self.storage.new(self.b1)
        self.storage.save()

        self.storage.new(self.b2)
        my_dict_1 = self.storage.all()

        self.storage.reload()
        my_dict_2 = self.storage.all()

        self.assertNotEqual(my_dict_1, my_dict_2)


if __name__ == "__main__":
    unittest.main()
