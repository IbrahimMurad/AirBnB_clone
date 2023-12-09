import unittest
import uuid
import os
import json
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime
from models.base_model import BaseModel

"""
This module uses unittest to test FileStorage class
"""


class TestBaseModel(unittest.TestCase):
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

        my_model1 = BaseModel()
        my_model2 = BaseModel()
        my_model3 = BaseModel()
        my_objects = getattr(storage, '_FileStorage__objects')
        self.assertEqual(len(my_objects), 3)

    def test_all(self):
        """ test a normal call to all method """

        my_model1 = BaseModel()
        my_model2 = BaseModel()
        my_model3 = BaseModel()
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


if __name__ == '__main__':
    unittest.main()
