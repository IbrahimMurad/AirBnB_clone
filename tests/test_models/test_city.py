
"""
This module uses unittest to test City class
"""

import unittest
import uuid
import os
import json
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    To run all the possible tests of City class
    using unittest
    """

    def setUp(self):
        """ starts a new connection """

        setattr(storage, "_FileStorage__objects", {})
        pass

    def tearDown(self):
        """ Removes all the connections (restoring the initial City)"""

        if os.path.exists('file.json'):
            os.remove('file.json')
        pass

    def test_City_type(self):
        """ What is a City """

        City_type = "<class 'models.city.City'>"
        self.assertEqual(str(City), City_type)

    def test_City_as_subclass(self):
        """ test to see if City is a subclass of BaseModel """

        self.assertTrue(issubclass(City, BaseModel))

    def test_instance_type(self):
        """ Is an instance a City """

        myCity = City()
        self.assertIsInstance(myCity, City)

    def test_City_attr(self):
        """ checks if City has its attributes """

        my_City = City()
        self.assertTrue(hasattr(my_City, "id"))
        self.assertTrue(hasattr(my_City, "created_at"))
        self.assertTrue(hasattr(my_City, "updated_at"))
        self.assertTrue(hasattr(my_City, "name"))
        self.assertTrue(hasattr(my_City, "state_id"))

    def test_City_extra_attr(self):
        """ checks if City has the added attributes """

        my_City = City()
        my_City.number = 129
        self.assertTrue(hasattr(my_City, "number"))

    def test_instance_attr_type(self):
        """ checks the types of the puplic instance attributes """

        myCity = City()
        self.assertEqual(str(type(myCity.id)), "<class 'str'>")
        self.assertEqual(str(type(myCity.name)), "<class 'str'>")
        self.assertEqual(str(type(myCity.state_id)), "<class 'str'>")
        datetime_type = "<class 'datetime.datetime'>"
        self.assertEqual(str(type(myCity.created_at)), datetime_type)
        self.assertEqual(str(type(myCity.updated_at)), datetime_type)

    def test_init_0_args(self):
        """ passing zero arguments (no self) """

        with self.assertRaises(TypeError) as excpt:
            City.__init__()
        excpt_msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_init_1_arg(self):
        """ ensures that args do nothing """

        my_City = City(15)
        my_City_json = my_City.to_dict()
        my_new_model = City(**my_City_json)
        self.assertEqual(my_City.id, my_new_model.id)
        self.assertEqual(my_City.created_at, my_new_model.created_at)
        self.assertEqual(my_City.updated_at, my_new_model.updated_at)

    def test_random_id(self):
        """ tests if id generated is a uuid """

        my_City = City()
        my_new_model = City()
        self.assertNotEqual(my_City.id, my_new_model.id)
        uuid_regex = r'^[\da-f]{8}(-[\da-f]{4}){3}-[\da-f]{12}$'
        self.assertRegex(my_City.id, uuid_regex)
        id_to_uuid_type = str(type(uuid.UUID(my_City.id)))
        self.assertEqual(id_to_uuid_type, "<class 'uuid.UUID'>")

    def test_cmplt_kwargs(self):
        """ passing a complete dictionary """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'created_at': '2017-09-28T21:05:54.119427',
            'updated_at': '2017-09-28T21:05:54.119572',
            'name': 'NY',
            'state_id': 'WC'
        }
        my_id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        my_created_at = datetime.fromisoformat('2017-09-28T21:05:54.119427')
        my_updated_at = datetime.fromisoformat('2017-09-28T21:05:54.119572')
        my_name = 'NY'
        my_state = 'WC'
        my_City = City(**my_dict)
        self.assertEqual(my_City.id, my_id)
        self.assertEqual(my_City.created_at, my_created_at)
        self.assertEqual(my_City.updated_at, my_updated_at)
        self.assertEqual(my_City.name, my_name)
        self.assertEqual(my_City.state_id, my_state)

    def test_no_id_kwargs(self):
        """ passing kwargs without id attribute """

        my_dict = {
            'created_at': '2017-09-28T21:05:54.119427',
            'updated_at': '2017-09-28T21:05:54.119572'
        }
        my_created_at = datetime.fromisoformat('2017-09-28T21:05:54.119427')
        my_updated_at = datetime.fromisoformat('2017-09-28T21:05:54.119572')
        my_City = City(**my_dict)
        self.assertNotEqual(my_City.id, "")
        uuid_regex = r'^[\da-f]{8}(-[\da-f]{4}){3}-[\da-f]{12}$'
        self.assertRegex(my_City.id, uuid_regex)
        self.assertEqual(my_City.created_at, my_created_at)
        self.assertEqual(my_City.updated_at, my_updated_at)

    def test_no_updated_kwargs(self):
        """ passing kwargs without updated_at attribute """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'created_at': '2017-09-28T21:05:54.119427'
        }
        my_id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        my_created_at = datetime.fromisoformat('2017-09-28T21:05:54.119427')
        my_City = City(**my_dict)
        my_updated_at = datetime.isoformat(my_City.updated_at)
        isoformat_regex = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}$'
        self.assertRegex(my_updated_at, isoformat_regex)
        self.assertEqual(my_City.id, my_id)
        self.assertEqual(my_City.created_at, my_created_at)

    def test_no_created_kwargs(self):
        """ passing kwargs without created_at attribute """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'updated_at': '2017-09-28T21:05:54.119427'
        }
        my_id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        my_updated_at = datetime.fromisoformat('2017-09-28T21:05:54.119427')
        my_City = City(**my_dict)
        my_created_at = datetime.isoformat(my_City.created_at)
        isoformat_regex = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}$'
        self.assertRegex(my_created_at, isoformat_regex)
        self.assertEqual(my_City.id, my_id)
        self.assertEqual(my_City.updated_at, my_updated_at)

    def test_manual_kwargs(self):
        """ manually passing kwargs """

        my_id = '17'
        my_cr = '2017-09-28T21:05:54.119427'
        my_up = '2017-09-28T21:05:54.119499'
        my_City = City(id=my_id, updated_at=my_up, created_at=my_cr)
        c = datetime(2017, 9, 28, 21, 5, 54, 119427)
        u = datetime(2017, 9, 28, 21, 5, 54, 119499)
        self.assertEqual(my_City.id, '17')
        self.assertEqual(my_City.created_at, c)
        self.assertEqual(my_City.updated_at, u)

    def test_updated_gt_created(self):
        """ tests if updated_at is greater than created_at """

        my_City = City()
        self.assertTrue(my_City.updated_at >= my_City.created_at)

    def test_not_isoformat(self):
        """ passing kwargs with wrong isoformat of datetime """

        my_dict = {
            'created_at': '2017/09/28S21-05-54:119427',
            'updated_at': '2017-09-28T21:05:54.119572'
        }
        with self.assertRaises(ValueError) as excpt:
            my_City = City(**my_dict)
        excpt_msg = "Invalid isoformat string: '2017/09/28S21-05-54:119427'"
        self.assertEqual(str(excpt.exception), excpt_msg)
        my_dict = {
            'created_at': '2017-09-28T21:05:54.119572',
            'updated_at': 'today'
        }
        with self.assertRaises(ValueError) as excpt:
            my_City = City(**my_dict)
        excpt_msg = "Invalid isoformat string: 'today'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_str_00(self):
        """ tests __str__ method """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'created_at': '2017-09-28T21:05:54.119427',
            'updated_at': '2017-09-28T21:05:54.119572',
            'name': 'NY',
            'state_id': 'WC'
        }
        my_City = City(**my_dict)
        my_str = "[City] (b6a6e15c-c67d-4312-9a75-9d084935e579) "
        my_str += "{'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', "
        my_str += "'created_at': "
        my_str += "datetime.datetime(2017, 9, 28, 21, 5, 54, 119427), "
        my_str += "'updated_at': "
        my_str += "datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), "
        my_str += "'name': 'NY', 'state_id': 'WC'}"
        self.assertEqual(my_City.__str__(), my_str)
        my_City = City()
        my_str = "[City] (" + my_City.id + ") "
        my_str += str(my_City.__dict__)
        self.assertEqual(my_City.__str__(), my_str)

    def test_str_01(self):
        """ tests __str__ method after adding more attributes """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'created_at': '2017-09-28T21:05:54.119427',
            'updated_at': '2017-09-28T21:05:54.119572',
            'name': 'NY',
            'state_id': 'WC'
        }
        my_City = City(**my_dict)
        my_City.add1 = 'Betty'
        my_City.add2 = 125
        my_str = "[City] (b6a6e15c-c67d-4312-9a75-9d084935e579) "
        my_str += "{'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', "
        my_str += "'created_at': "
        my_str += "datetime.datetime(2017, 9, 28, 21, 5, 54, 119427), "
        my_str += "'updated_at': "
        my_str += "datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), "
        my_str += "'name': 'NY', 'state_id': 'WC', "
        my_str += "'add1': 'Betty', "
        my_str += "'add2': 125}"
        self.assertEqual(my_City.__str__(), my_str)
        my_City = City()
        my_str = "[City] (" + my_City.id + ") "
        my_str += str(my_City.__dict__)
        self.assertEqual(my_City.__str__(), my_str)

    def test_save00(self):
        """ test to ensure that updated_at is really updated """

        my_City = City()
        last_updated = my_City.updated_at
        my_City.save()
        self.assertGreater(my_City.updated_at, last_updated)

    def test_save01(self):
        """ see if file.json exists after the call """

        my_City = City()
        my_City.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_save02(self):
        """ see if file.json contains the write output """

        my_City = City()
        my_id = "City." + my_City.id
        my_City.save()
        my_dict = {}
        my_dict[my_id] = my_City.to_dict()
        my_json = json.dumps(my_dict)
        with open('file.json', 'r', encoding='utf-8') as f:
            text_in_file = f.read()
        self.maxDiff = None
        self.assertEqual(text_in_file, my_json)

    def test_todect00(self):
        """ tests the output of a normal call """

        my_City = City()
        my_dict = {
            'id': my_City.id,
            'created_at': datetime.isoformat(my_City.created_at),
            'updated_at': datetime.isoformat(my_City.updated_at),
            '__class__': 'City',
            'name': '',
            'state_id': ''
        }
        self.assertEqual(my_City.to_dict(), my_dict)

    def test_todect01(self):
        """ tests the output after adding more attributes """

        my_City = City()
        my_City.name = 'Betty'
        my_City.number = 145
        my_dict = {
            'id': my_City.id,
            'created_at': datetime.isoformat(my_City.created_at),
            'updated_at': datetime.isoformat(my_City.updated_at),
            '__class__': 'City',
            'name': 'Betty',
            'state_id': '',
            'number': 145
        }
        self.assertEqual(my_City.to_dict(), my_dict)

    def test_todect02(self):
        """ exporting a dict and use it to init a new City """

        my_City = City(id='15')
        my_City_dict = my_City.to_dict()
        new_model = City(**my_City_dict)
        self.assertEqual(my_City.id, new_model.id)
        self.assertEqual(my_City.updated_at, new_model.updated_at)
        self.assertEqual(my_City.created_at, new_model.created_at)

    def test_todect_with_args(self):
        """ passing one argument to to_dict (with self) """

        my_City = City()
        with self.assertRaises(TypeError) as excpt:
            my_City.to_dict(15)
        excpt_msg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_save_with_args(self):
        """ passing 1 argument to save (with self) """

        my_City = City()
        with self.assertRaises(TypeError) as excpt:
            my_City.save(15)
        excpt_msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(excpt.exception), excpt_msg)


if __name__ == '__main__':
    unittest.main()
