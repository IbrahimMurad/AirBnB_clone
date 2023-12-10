#!/usr/bin/python3
"""
This module uses unittest to test Amenity class
"""

import unittest
import uuid
import os
import json
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    To run all the possible tests of Amenity class
    using unittest
    """

    def setUp(self):
        """ starts a new connection """

        setattr(storage, "_FileStorage__objects", {})
        pass

    def tearDown(self):
        """ Removes all the connections (restoring the initial Amenity)"""

        if os.path.exists('file.json'):
            os.remove('file.json')
        pass

    def test_Amenity_type(self):
        """ What is a Amenity """

        Amenity_type = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(Amenity), Amenity_type)

    def test_Amenity_as_subclass(self):
        """ test to see if Amenity is a subclass of BaseModel """

        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_instance_type(self):
        """ Is an instance a Amenity """

        myAmenity = Amenity()
        self.assertIsInstance(myAmenity, Amenity)

    def test_Amenity_attr(self):
        """ checks if Amenity has its attributes """

        my_Amenity = Amenity()
        self.assertTrue(hasattr(my_Amenity, "id"))
        self.assertTrue(hasattr(my_Amenity, "created_at"))
        self.assertTrue(hasattr(my_Amenity, "updated_at"))
        self.assertTrue(hasattr(my_Amenity, "name"))

    def test_Amenity_extra_attr(self):
        """ checks if Amenity has the added attributes """

        my_Amenity = Amenity()
        my_Amenity.number = 129
        self.assertTrue(hasattr(my_Amenity, "number"))

    def test_instance_attr_type(self):
        """ checks the types of the puplic instance attributes """

        myAmenity = Amenity()
        self.assertEqual(str(type(myAmenity.id)), "<class 'str'>")
        self.assertEqual(str(type(myAmenity.name)), "<class 'str'>")
        datetime_type = "<class 'datetime.datetime'>"
        self.assertEqual(str(type(myAmenity.created_at)), datetime_type)
        self.assertEqual(str(type(myAmenity.updated_at)), datetime_type)

    def test_init_0_args(self):
        """ passing zero arguments (no self) """

        with self.assertRaises(TypeError) as excpt:
            Amenity.__init__()
        excpt_msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_init_1_arg(self):
        """ ensures that args do nothing """

        my_Amenity = Amenity(15)
        my_Amenity_json = my_Amenity.to_dict()
        my_new_model = Amenity(**my_Amenity_json)
        self.assertEqual(my_Amenity.id, my_new_model.id)
        self.assertEqual(my_Amenity.created_at, my_new_model.created_at)
        self.assertEqual(my_Amenity.updated_at, my_new_model.updated_at)

    def test_random_id(self):
        """ tests if id generated is a uuid """

        my_Amenity = Amenity()
        my_new_model = Amenity()
        self.assertNotEqual(my_Amenity.id, my_new_model.id)
        uuid_regex = r'^[\da-f]{8}(-[\da-f]{4}){3}-[\da-f]{12}$'
        self.assertRegex(my_Amenity.id, uuid_regex)
        id_to_uuid_type = str(type(uuid.UUID(my_Amenity.id)))
        self.assertEqual(id_to_uuid_type, "<class 'uuid.UUID'>")

    def test_cmplt_kwargs(self):
        """ passing a complete dictionary """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'created_at': '2017-09-28T21:05:54.119427',
            'updated_at': '2017-09-28T21:05:54.119572',
            'name': 'NY'
        }
        my_id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        my_created_at = datetime.fromisoformat('2017-09-28T21:05:54.119427')
        my_updated_at = datetime.fromisoformat('2017-09-28T21:05:54.119572')
        my_name = 'NY'
        my_Amenity = Amenity(**my_dict)
        self.assertEqual(my_Amenity.id, my_id)
        self.assertEqual(my_Amenity.created_at, my_created_at)
        self.assertEqual(my_Amenity.updated_at, my_updated_at)
        self.assertEqual(my_Amenity.name, my_name)

    def test_no_id_kwargs(self):
        """ passing kwargs without id attribute """

        my_dict = {
            'created_at': '2017-09-28T21:05:54.119427',
            'updated_at': '2017-09-28T21:05:54.119572'
        }
        my_created_at = datetime.fromisoformat('2017-09-28T21:05:54.119427')
        my_updated_at = datetime.fromisoformat('2017-09-28T21:05:54.119572')
        my_Amenity = Amenity(**my_dict)
        self.assertNotEqual(my_Amenity.id, "")
        uuid_regex = r'^[\da-f]{8}(-[\da-f]{4}){3}-[\da-f]{12}$'
        self.assertRegex(my_Amenity.id, uuid_regex)
        self.assertEqual(my_Amenity.created_at, my_created_at)
        self.assertEqual(my_Amenity.updated_at, my_updated_at)

    def test_no_updated_kwargs(self):
        """ passing kwargs without updated_at attribute """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'created_at': '2017-09-28T21:05:54.119427'
        }
        my_id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        my_created_at = datetime.fromisoformat('2017-09-28T21:05:54.119427')
        my_Amenity = Amenity(**my_dict)
        my_updated_at = datetime.isoformat(my_Amenity.updated_at)
        isoformat_regex = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}$'
        self.assertRegex(my_updated_at, isoformat_regex)
        self.assertEqual(my_Amenity.id, my_id)
        self.assertEqual(my_Amenity.created_at, my_created_at)

    def test_no_created_kwargs(self):
        """ passing kwargs without created_at attribute """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'updated_at': '2017-09-28T21:05:54.119427'
        }
        my_id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        my_updated_at = datetime.fromisoformat('2017-09-28T21:05:54.119427')
        my_Amenity = Amenity(**my_dict)
        my_created_at = datetime.isoformat(my_Amenity.created_at)
        isoformat_regex = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}$'
        self.assertRegex(my_created_at, isoformat_regex)
        self.assertEqual(my_Amenity.id, my_id)
        self.assertEqual(my_Amenity.updated_at, my_updated_at)

    def test_manual_kwargs(self):
        """ manually passing kwargs """

        my_id = '17'
        my_cr = '2017-09-28T21:05:54.119427'
        my_up = '2017-09-28T21:05:54.119499'
        my_Amenity = Amenity(id=my_id, updated_at=my_up, created_at=my_cr)
        c = datetime(2017, 9, 28, 21, 5, 54, 119427)
        u = datetime(2017, 9, 28, 21, 5, 54, 119499)
        self.assertEqual(my_Amenity.id, '17')
        self.assertEqual(my_Amenity.created_at, c)
        self.assertEqual(my_Amenity.updated_at, u)

    def test_updated_gt_created(self):
        """ tests if updated_at is greater than created_at """

        my_Amenity = Amenity()
        self.assertTrue(my_Amenity.updated_at >= my_Amenity.created_at)

    def test_not_isoformat(self):
        """ passing kwargs with wrong isoformat of datetime """

        my_dict = {
            'created_at': '2017/09/28S21-05-54:119427',
            'updated_at': '2017-09-28T21:05:54.119572'
        }
        with self.assertRaises(ValueError) as excpt:
            my_Amenity = Amenity(**my_dict)
        excpt_msg = "Invalid isoformat string: '2017/09/28S21-05-54:119427'"
        self.assertEqual(str(excpt.exception), excpt_msg)
        my_dict = {
            'created_at': '2017-09-28T21:05:54.119572',
            'updated_at': 'today'
        }
        with self.assertRaises(ValueError) as excpt:
            my_Amenity = Amenity(**my_dict)
        excpt_msg = "Invalid isoformat string: 'today'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_str_00(self):
        """ tests __str__ method """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'created_at': '2017-09-28T21:05:54.119427',
            'updated_at': '2017-09-28T21:05:54.119572',
            'name': 'Ibrahim'
        }
        my_Amenity = Amenity(**my_dict)
        my_str = "[Amenity] (b6a6e15c-c67d-4312-9a75-9d084935e579) "
        my_str += "{'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', "
        my_str += "'created_at': "
        my_str += "datetime.datetime(2017, 9, 28, 21, 5, 54, 119427), "
        my_str += "'updated_at': "
        my_str += "datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), "
        my_str += "'name': 'Ibrahim'}"
        self.assertEqual(my_Amenity.__str__(), my_str)
        my_Amenity = Amenity()
        my_str = "[Amenity] (" + my_Amenity.id + ") "
        my_str += str(my_Amenity.__dict__)
        self.assertEqual(my_Amenity.__str__(), my_str)

    def test_str_01(self):
        """ tests __str__ method after adding more attributes """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'created_at': '2017-09-28T21:05:54.119427',
            'updated_at': '2017-09-28T21:05:54.119572',
            'name': 'Ibrahim'
        }
        my_Amenity = Amenity(**my_dict)
        my_Amenity.add1 = 'Betty'
        my_Amenity.add2 = 125
        my_str = "[Amenity] (b6a6e15c-c67d-4312-9a75-9d084935e579) "
        my_str += "{'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', "
        my_str += "'created_at': "
        my_str += "datetime.datetime(2017, 9, 28, 21, 5, 54, 119427), "
        my_str += "'updated_at': "
        my_str += "datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), "
        my_str += "'name': 'Ibrahim', "
        my_str += "'add1': 'Betty', "
        my_str += "'add2': 125}"
        self.assertEqual(my_Amenity.__str__(), my_str)
        my_Amenity = Amenity()
        my_str = "[Amenity] (" + my_Amenity.id + ") "
        my_str += str(my_Amenity.__dict__)
        self.assertEqual(my_Amenity.__str__(), my_str)

    def test_save00(self):
        """ test to ensure that updated_at is really updated """

        my_Amenity = Amenity()
        last_updated = my_Amenity.updated_at
        my_Amenity.save()
        self.assertGreater(my_Amenity.updated_at, last_updated)

    def test_save01(self):
        """ see if file.json exists after the call """

        my_Amenity = Amenity()
        my_Amenity.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_save02(self):
        """ see if file.json contains the write output """

        my_Amenity = Amenity()
        my_id = "Amenity." + my_Amenity.id
        my_Amenity.save()
        my_dict = {}
        my_dict[my_id] = my_Amenity.to_dict()
        my_json = json.dumps(my_dict)
        with open('file.json', 'r', encoding='utf-8') as f:
            text_in_file = f.read()
        self.maxDiff = None
        self.assertEqual(text_in_file, my_json)

    def test_todect00(self):
        """ tests the output of a normal call """

        my_Amenity = Amenity()
        my_dict = {
            'id': my_Amenity.id,
            'created_at': datetime.isoformat(my_Amenity.created_at),
            'updated_at': datetime.isoformat(my_Amenity.updated_at),
            '__class__': 'Amenity',
            'name': ''
        }
        self.assertEqual(my_Amenity.to_dict(), my_dict)

    def test_todect01(self):
        """ tests the output after adding more attributes """

        my_Amenity = Amenity()
        my_Amenity.name = 'Betty'
        my_Amenity.number = 145
        my_dict = {
            'id': my_Amenity.id,
            'created_at': datetime.isoformat(my_Amenity.created_at),
            'updated_at': datetime.isoformat(my_Amenity.updated_at),
            '__class__': 'Amenity',
            'name': 'Betty',
            'number': 145
        }
        self.assertEqual(my_Amenity.to_dict(), my_dict)

    def test_todect02(self):
        """ exporting a dict and use it to init a new Amenity """

        my_Amenity = Amenity(id='15')
        my_Amenity_dict = my_Amenity.to_dict()
        new_model = Amenity(**my_Amenity_dict)
        self.assertEqual(my_Amenity.id, new_model.id)
        self.assertEqual(my_Amenity.updated_at, new_model.updated_at)
        self.assertEqual(my_Amenity.created_at, new_model.created_at)

    def test_todect_with_args(self):
        """ passing one argument to to_dict (with self) """

        my_Amenity = Amenity()
        with self.assertRaises(TypeError) as excpt:
            my_Amenity.to_dict(15)
        excpt_msg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_save_with_args(self):
        """ passing 1 argument to save (with self) """

        my_Amenity = Amenity()
        with self.assertRaises(TypeError) as excpt:
            my_Amenity.save(15)
        excpt_msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(excpt.exception), excpt_msg)


if __name__ == '__main__':
    unittest.main()
