
"""
This module uses unittest to test Place class
"""

import unittest
import uuid
import os
import json
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    To run all the possible tests of Place class
    using unittest
    """

    def setUp(self):
        """ starts a new connection """

        setattr(storage, "_FileStorage__objects", {})
        pass

    def tearDown(self):
        """ Removes all the connections (restoring the initial Place)"""

        if os.path.exists('file.json'):
            os.remove('file.json')
        pass

    def test_Place_type(self):
        """ What is a Place """

        Place_type = "<class 'models.place.Place'>"
        self.assertEqual(str(Place), Place_type)

    def test_Place_as_subclass(self):
        """ test to see if Place is a subclass of BaseModel """

        self.assertTrue(issubclass(Place, BaseModel))

    def test_instance_type(self):
        """ Is an instance a Place """

        myPlace = Place()
        self.assertIsInstance(myPlace, Place)

    def test_Place_attr(self):
        """ checks if Place has its attributes """

        my_Place = Place()
        self.assertTrue(hasattr(my_Place, "id"))
        self.assertTrue(hasattr(my_Place, "created_at"))
        self.assertTrue(hasattr(my_Place, "updated_at"))
        self.assertTrue(hasattr(my_Place, "name"))
        self.assertTrue(hasattr(my_Place, "description"))
        self.assertTrue(hasattr(my_Place, "city_id"))
        self.assertTrue(hasattr(my_Place, "user_id"))
        self.assertTrue(hasattr(my_Place, "number_rooms"))
        self.assertTrue(hasattr(my_Place, "number_bathrooms"))
        self.assertTrue(hasattr(my_Place, "max_guest"))
        self.assertTrue(hasattr(my_Place, "price_by_night"))
        self.assertTrue(hasattr(my_Place, "latitude"))
        self.assertTrue(hasattr(my_Place, "longitude"))
        self.assertTrue(hasattr(my_Place, "amenity_ids"))

    def test_Place_extra_attr(self):
        """ checks if Place has the added attributes """

        my_Place = Place()
        my_Place.number = 129
        self.assertTrue(hasattr(my_Place, "number"))

    def test_instance_attr_type(self):
        """ checks the types of the puplic instance attributes """

        myPlace = Place()
        self.assertEqual(str(type(myPlace.id)), "<class 'str'>")
        self.assertEqual(str(type(myPlace.name)), "<class 'str'>")
        self.assertEqual(str(type(myPlace.city_id)), "<class 'str'>")
        self.assertEqual(str(type(myPlace.user_id)), "<class 'str'>")
        self.assertEqual(str(type(myPlace.description)), "<class 'str'>")
        self.assertEqual(str(type(myPlace.number_rooms)), "<class 'int'>")
        self.assertEqual(str(type(myPlace.number_bathrooms)), "<class 'int'>")
        self.assertEqual(str(type(myPlace.max_guest)), "<class 'int'>")
        self.assertEqual(str(type(myPlace.price_by_night)), "<class 'int'>")
        self.assertEqual(str(type(myPlace.latitude)), "<class 'float'>")
        self.assertEqual(str(type(myPlace.longitude)), "<class 'float'>")
        self.assertEqual(str(type(myPlace.amenity_ids)), "<class 'list'>")
        datetime_type = "<class 'datetime.datetime'>"
        self.assertEqual(str(type(myPlace.created_at)), datetime_type)
        self.assertEqual(str(type(myPlace.updated_at)), datetime_type)

    def test_init_0_args(self):
        """ passing zero arguments (no self) """

        with self.assertRaises(TypeError) as excpt:
            Place.__init__()
        excpt_msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_init_1_arg(self):
        """ ensures that args do nothing """

        my_Place = Place(15)
        my_Place_json = my_Place.to_dict()
        my_new_model = Place(**my_Place_json)
        self.assertEqual(my_Place.id, my_new_model.id)
        self.assertEqual(my_Place.created_at, my_new_model.created_at)
        self.assertEqual(my_Place.updated_at, my_new_model.updated_at)

    def test_random_id(self):
        """ tests if id generated is a uuid """

        my_Place = Place()
        my_new_model = Place()
        self.assertNotEqual(my_Place.id, my_new_model.id)
        uuid_regex = r'^[\da-f]{8}(-[\da-f]{4}){3}-[\da-f]{12}$'
        self.assertRegex(my_Place.id, uuid_regex)
        id_to_uuid_type = str(type(uuid.UUID(my_Place.id)))
        self.assertEqual(id_to_uuid_type, "<class 'uuid.UUID'>")

    def test_cmplt_kwargs(self):
        """ passing a complete dictionary """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'created_at': '2017-09-28T21:05:54.119427',
            'updated_at': '2017-09-28T21:05:54.119572',
            'name': 'NY',
            'city_id': 'WC',
            'user_id': 'Ahmed',
            'description': 'Fancy',
            'number_rooms': 15,
            'number_bathrooms': 20,
            'max_guest': 20,
            'price_by_night': 50,
            'latitude': 152.156,
            'longitude': 98.005,
            'amenity_ids': []
        }
        my_id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        my_created_at = datetime.fromisoformat('2017-09-28T21:05:54.119427')
        my_updated_at = datetime.fromisoformat('2017-09-28T21:05:54.119572')
        my_name = 'NY'
        my_city = 'WC'
        my_user = 'Ahmed'
        my_description = 'Fancy'
        my_number_rooms = 15
        my_number_bathrooms = 20
        my_max_guest = 20
        my_price_by_night = 50
        my_latitude = 152.156
        my_longitude = 98.005
        my_amenitys = []
        my_Place = Place(**my_dict)
        self.assertEqual(my_Place.id, my_id)
        self.assertEqual(my_Place.created_at, my_created_at)
        self.assertEqual(my_Place.updated_at, my_updated_at)
        self.assertEqual(my_Place.name, my_name)
        self.assertEqual(my_Place.city_id, my_city)
        self.assertEqual(my_Place.user_id, my_user)
        self.assertEqual(my_Place.description, my_description)
        self.assertEqual(my_Place.number_rooms, my_number_rooms)
        self.assertEqual(my_Place.number_bathrooms, my_number_bathrooms)
        self.assertEqual(my_Place.max_guest, my_max_guest)
        self.assertEqual(my_Place.price_by_night, my_price_by_night)
        self.assertEqual(my_Place.latitude, my_latitude)
        self.assertEqual(my_Place.longitude, my_longitude)
        self.assertEqual(my_Place.amenity_ids, my_amenitys)

    def test_no_id_kwargs(self):
        """ passing kwargs without id attribute """

        my_dict = {
            'created_at': '2017-09-28T21:05:54.119427',
            'updated_at': '2017-09-28T21:05:54.119572'
        }
        my_created_at = datetime.fromisoformat('2017-09-28T21:05:54.119427')
        my_updated_at = datetime.fromisoformat('2017-09-28T21:05:54.119572')
        my_Place = Place(**my_dict)
        self.assertNotEqual(my_Place.id, "")
        uuid_regex = r'^[\da-f]{8}(-[\da-f]{4}){3}-[\da-f]{12}$'
        self.assertRegex(my_Place.id, uuid_regex)
        self.assertEqual(my_Place.created_at, my_created_at)
        self.assertEqual(my_Place.updated_at, my_updated_at)

    def test_no_updated_kwargs(self):
        """ passing kwargs without updated_at attribute """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'created_at': '2017-09-28T21:05:54.119427'
        }
        my_id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        my_created_at = datetime.fromisoformat('2017-09-28T21:05:54.119427')
        my_Place = Place(**my_dict)
        my_updated_at = datetime.isoformat(my_Place.updated_at)
        isoformat_regex = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}$'
        self.assertRegex(my_updated_at, isoformat_regex)
        self.assertEqual(my_Place.id, my_id)
        self.assertEqual(my_Place.created_at, my_created_at)

    def test_no_created_kwargs(self):
        """ passing kwargs without created_at attribute """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'updated_at': '2017-09-28T21:05:54.119427'
        }
        my_id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        my_updated_at = datetime.fromisoformat('2017-09-28T21:05:54.119427')
        my_Place = Place(**my_dict)
        my_created_at = datetime.isoformat(my_Place.created_at)
        isoformat_regex = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}$'
        self.assertRegex(my_created_at, isoformat_regex)
        self.assertEqual(my_Place.id, my_id)
        self.assertEqual(my_Place.updated_at, my_updated_at)

    def test_manual_kwargs(self):
        """ manually passing kwargs """

        my_id = '17'
        my_cr = '2017-09-28T21:05:54.119427'
        my_up = '2017-09-28T21:05:54.119499'
        my_Place = Place(id=my_id, updated_at=my_up, created_at=my_cr)
        c = datetime(2017, 9, 28, 21, 5, 54, 119427)
        u = datetime(2017, 9, 28, 21, 5, 54, 119499)
        self.assertEqual(my_Place.id, '17')
        self.assertEqual(my_Place.created_at, c)
        self.assertEqual(my_Place.updated_at, u)

    def test_updated_gt_created(self):
        """ tests if updated_at is greater than created_at """

        my_Place = Place()
        self.assertTrue(my_Place.updated_at >= my_Place.created_at)

    def test_not_isoformat(self):
        """ passing kwargs with wrong isoformat of datetime """

        my_dict = {
            'created_at': '2017/09/28S21-05-54:119427',
            'updated_at': '2017-09-28T21:05:54.119572'
        }
        with self.assertRaises(ValueError) as excpt:
            my_Place = Place(**my_dict)
        excpt_msg = "Invalid isoformat string: '2017/09/28S21-05-54:119427'"
        self.assertEqual(str(excpt.exception), excpt_msg)
        my_dict = {
            'created_at': '2017-09-28T21:05:54.119572',
            'updated_at': 'today'
        }
        with self.assertRaises(ValueError) as excpt:
            my_Place = Place(**my_dict)
        excpt_msg = "Invalid isoformat string: 'today'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_str_00(self):
        """ tests __str__ method """

        self.maxDiff = None
        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'created_at': '2017-09-28T21:05:54.119427',
            'updated_at': '2017-09-28T21:05:54.119572',
            'name': 'NY',
            'city_id': 'WC',
            'user_id': 'Ahmed',
            'description': 'Fancy',
            'number_rooms': 15,
            'number_bathrooms': 20,
            'max_guest': 20,
            'price_by_night': 50,
            'latitude': 152.156,
            'longitude': 98.005,
            'amenity_ids': []
        }
        my_Place = Place(**my_dict)
        my_str = "[Place] (b6a6e15c-c67d-4312-9a75-9d084935e579) \
{'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', \
'created_at': \
datetime.datetime(2017, 9, 28, 21, 5, 54, 119427), \
'updated_at': \
datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), \
'name': 'NY', 'city_id': 'WC', 'user_id': 'Ahmed', \
'description': 'Fancy', \
'number_rooms': 15, \
'number_bathrooms': 20, \
'max_guest': 20, \
'price_by_night': 50, \
'latitude': 152.156, \
'longitude': 98.005, \
'amenity_ids': []}"
        self.assertEqual(my_Place.__str__(), my_str)
        my_Place = Place()
        my_str = "[Place] (" + my_Place.id + ") "
        my_str += str(my_Place.__dict__)
        self.assertEqual(my_Place.__str__(), my_str)

    def test_str_01(self):
        """ tests __str__ method after adding more attributes """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'created_at': '2017-09-28T21:05:54.119427',
            'updated_at': '2017-09-28T21:05:54.119572',
            'name': 'NY',
            'city_id': 'WC',
            'user_id': 'Ahmed',
            'description': 'Fancy',
            'number_rooms': 15,
            'number_bathrooms': 20,
            'max_guest': 20,
            'price_by_night': 50,
            'latitude': 152.156,
            'longitude': 98.005,
            'amenity_ids': []
        }
        my_Place = Place(**my_dict)
        my_Place.add1 = 'Betty'
        my_Place.add2 = 125
        my_str = "[Place] (b6a6e15c-c67d-4312-9a75-9d084935e579) \
{'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', \
'created_at': \
datetime.datetime(2017, 9, 28, 21, 5, 54, 119427), \
'updated_at': \
datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), \
'name': 'NY', 'city_id': 'WC', 'user_id': 'Ahmed', \
'description': 'Fancy', \
'number_rooms': 15, \
'number_bathrooms': 20, \
'max_guest': 20, \
'price_by_night': 50, \
'latitude': 152.156, \
'longitude': 98.005, \
'amenity_ids': [], \
'add1': 'Betty', \
'add2': 125}"
        self.assertEqual(my_Place.__str__(), my_str)
        my_Place = Place()
        my_str = "[Place] (" + my_Place.id + ") "
        my_str += str(my_Place.__dict__)
        self.assertEqual(my_Place.__str__(), my_str)

    def test_save00(self):
        """ test to ensure that updated_at is really updated """

        my_Place = Place()
        last_updated = my_Place.updated_at
        my_Place.save()
        self.assertGreater(my_Place.updated_at, last_updated)

    def test_save01(self):
        """ see if file.json exists after the call """

        my_Place = Place()
        my_Place.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_save02(self):
        """ see if file.json contains the write output """

        my_Place = Place()
        my_id = "Place." + my_Place.id
        my_Place.save()
        my_dict = {}
        my_dict[my_id] = my_Place.to_dict()
        my_json = json.dumps(my_dict)
        with open('file.json', 'r', encoding='utf-8') as f:
            name_in_file = f.read()
        self.maxDiff = None
        self.assertEqual(name_in_file, my_json)

    def test_todect00(self):
        """ tests the output of a normal call """

        my_Place = Place()
        my_dict = {
            'id': my_Place.id,
            'created_at': datetime.isoformat(my_Place.created_at),
            'updated_at': datetime.isoformat(my_Place.updated_at),
            '__class__': 'Place',
            'name': '',
            'city_id': '',
            'user_id': '',
            'description': '',
            'number_rooms': 0,
            'number_bathrooms': 0,
            'max_guest': 0,
            'price_by_night': 0,
            'latitude': 0.0,
            'longitude': 0.0,
            'amenity_ids': []
        }
        self.assertEqual(my_Place.to_dict(), my_dict)

    def test_todect01(self):
        """ tests the output after adding more attributes """

        my_Place = Place()
        my_Place.name = 'Betty'
        my_Place.number = 145
        my_dict = {
            'id': my_Place.id,
            'created_at': datetime.isoformat(my_Place.created_at),
            'updated_at': datetime.isoformat(my_Place.updated_at),
            '__class__': 'Place',
            'name': 'Betty',
            'city_id': '',
            'user_id': '',
            'description': '',
            'number_rooms': 0,
            'number_bathrooms': 0,
            'max_guest': 0,
            'price_by_night': 0,
            'latitude': 0.0,
            'longitude': 0.0,
            'amenity_ids': [],
            'number': 145
        }
        self.assertEqual(my_Place.to_dict(), my_dict)

    def test_todect02(self):
        """ exporting a dict and use it to init a new Place """

        my_Place = Place(id='15')
        my_Place_dict = my_Place.to_dict()
        new_model = Place(**my_Place_dict)
        self.assertEqual(my_Place.id, new_model.id)
        self.assertEqual(my_Place.updated_at, new_model.updated_at)
        self.assertEqual(my_Place.created_at, new_model.created_at)

    def test_todect_with_args(self):
        """ passing one argument to to_dict (with self) """

        my_Place = Place()
        with self.assertRaises(TypeError) as excpt:
            my_Place.to_dict(15)
        excpt_msg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_save_with_args(self):
        """ passing 1 argument to save (with self) """

        my_Place = Place()
        with self.assertRaises(TypeError) as excpt:
            my_Place.save(15)
        excpt_msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(excpt.exception), excpt_msg)


if __name__ == '__main__':
    unittest.main()
