#!/usr/bin/python3
"""
This module uses unittest to test FileStorage class
"""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """
    To run all the possible tests of FileStorage class
    using unittest
    """

    def setUp(self):
        """ starts a new connection """

        setattr(storage, "_FileStorage__objects", {})
        pass

    def tearDown(self):
        """ Removes all the connections (restoring the initial state)"""

        if os.path.exists('file.json'):
            os.remove('file.json')
        pass

    def test_FileStorage_type(self):
        """ What is a FileStorage """

        filestorage_type = "<class 'models.engine.file_storage.FileStorage'>"
        self.assertEqual(str(FileStorage), filestorage_type)

    def test_FileStorage_attr(self):
        """ checks if FileStorage has its attributes """

        my_storage = FileStorage()
        self.assertTrue(hasattr(my_storage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(my_storage, "_FileStorage__objects"))

    def test_instance_type(self):
        """ Is an instance a FileStorage """

        my_storage = FileStorage()
        self.assertIsInstance(my_storage, FileStorage)

    def test_instance_attr_type(self):
        """ checks the types of the attributes """

        my_storage = FileStorage()
        my_file = getattr(my_storage, '_FileStorage__file_path')
        my_objects = getattr(my_storage, '_FileStorage__objects')
        self.assertEqual(str(type(my_file)), "<class 'str'>")
        self.assertEqual(str(type(my_objects)), "<class 'dict'>")

    def test_init_0_args(self):
        """ passing zero arguments (no self) """

        with self.assertRaises(TypeError) as excpt:
            FileStorage.__init__()
        excpt_msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_init_self_arg(self):
        """ check the initialized values of the attributes """

        my_storage = FileStorage()
        self.assertEqual(my_storage._FileStorage__file_path, 'file.json')
        self.assertEqual(my_storage._FileStorage__objects, {})

    def test_init_2_arg(self):
        """ check the initialized values of the attributes
        when passing extra args """

        with self.assertRaises(TypeError) as excpt:
            my_storage = FileStorage('junk')
        excpt_msg = "__init__() takes 1 positional argument but 2 were given"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_objects_after_basemodel(self):
        """ checks if a basemodel object is added to objects """

        my_model = BaseModel()
        key = 'BaseModel.' + my_model.id
        my_objects = getattr(storage, '_FileStorage__objects')
        self.assertEqual(my_objects[key], my_model)

    def test_objects_len_after_1_obj(self):
        """ Creating an object, then
        ckecks if the length of objects is really 1 """

        my_model = BaseModel()
        my_objects = getattr(storage, '_FileStorage__objects')
        self.assertEqual(len(my_objects), 1)

    def test_objects_len_after_3_obj(self):
        """ Creating an object, then
        ckecks if the length of objects is really 1 """

        my_model = BaseModel()
        my_user = User()
        my_city = City()
        my_objects = getattr(storage, '_FileStorage__objects')
        self.assertEqual(len(my_objects), 3)

    def test_all(self):
        """ test a normal call to all method """

        my_model = BaseModel()
        my_user = User()
        my_city = City()
        my_objects = getattr(storage, '_FileStorage__objects')
        self.assertEqual(my_objects, storage.all())

    def test_all_without_self(self):
        """ calling call without self argument """

        with self.assertRaises(TypeError) as excpt:
            FileStorage.all()
        excpt_msg = "all() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_all_with_args(self):
        """ calling call with some args """

        with self.assertRaises(TypeError) as excpt:
            storage.all('junk')
        excpt_msg = "all() takes 1 positional argument but 2 were given"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_save00(self):
        """ a normal call to save method with no objects """

        storage.save()
        with open('file.json', 'r', encoding='utf-8') as f:
            text_in_file = f.read()
        self.assertEqual(text_in_file, '{}')

    def test_save01(self):
        """ a normal call to save method with one object """

        my_model = BaseModel()
        storage.save()
        with open('file.json', 'r', encoding='utf-8') as f:
            text_in_file = f.read()
        my_text = '{"BaseModel.'
        my_text += my_model.id
        my_text += '": '
        my_text += json.dumps(my_model.to_dict())
        my_text += '}'
        self.assertEqual(text_in_file, my_text)
        self.maxDiff = None

    def test_save02(self):
        """ a normal call to save method with 3 objects """

        my_model = BaseModel()
        storage.save()
        my_user = User()
        my_review = Review()
        storage.save()
        with open('file.json', 'r', encoding='utf-8') as f:
            text_in_file = f.read()
        my_text = '{'
        my_text += '"BaseModel.'
        my_text += my_model.id
        my_text += '": '
        my_text += json.dumps(my_model.to_dict())
        my_text += ', '
        my_text += '"User.'
        my_text += my_user.id
        my_text += '": '
        my_text += json.dumps(my_user.to_dict())
        my_text += ', '
        my_text += '"Review.'
        my_text += my_review.id
        my_text += '": '
        my_text += json.dumps(my_review.to_dict())
        my_text += '}'
        self.assertEqual(text_in_file, my_text)
        self.maxDiff = None

    def test_save_without_self(self):
        """ calling save without self argument """

        with self.assertRaises(TypeError) as excpt:
            FileStorage.save()
        excpt_msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_save_with_args(self):
        """ calling save with some args """

        with self.assertRaises(TypeError) as excpt:
            storage.save('junk')
        excpt_msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_reload_without_self(self):
        """ calling reload without self argument """

        with self.assertRaises(TypeError) as excpt:
            FileStorage.reload()
        excpt_msg = "reload() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_reload_with_args(self):
        """ calling reload with some args """

        with self.assertRaises(TypeError) as excpt:
            storage.reload('junk')
        excpt_msg = "reload() takes 1 positional argument but 2 were given"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_reload_with_no_file(self):
        """ test the reload method when file.json doesn't exixt """

        storage.reload()
        my_objects = getattr(storage, '_FileStorage__objects')
        self.assertEqual(my_objects, {})

    def test_reload_no_obj_in_file(self):
        """ test the reload method when file.json has no objects """

        storage.save()
        storage.reload()
        my_objects = getattr(storage, '_FileStorage__objects')
        self.assertEqual(my_objects, {})

    def test_new_without_self(self):
        """ calling save without self argument """

        with self.assertRaises(TypeError) as excpt:
            FileStorage.new()
        excpt_msg = "new() missing 2 required positional arguments:"
        excpt_msg += " 'self' and 'obj'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_new_with_args(self):
        """ calling save with some args """

        my_model = BaseModel()
        with self.assertRaises(TypeError) as excpt:
            storage.new(my_model, 'junk')
        excpt_msg = "new() takes 2 positional arguments but 3 were given"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_new_noramlly(self):
        """ run new with noraml args """

        my_base = BaseModel()
        setattr(storage, '_FileStorage__objects', {})
        storage.new(my_base)
        my_objects = getattr(storage, '_FileStorage__objects')
        my_key = "BaseModel." + my_base.id
        self.assertEqual(my_objects[my_key], my_base)


if __name__ == '__main__':
    unittest.main()
