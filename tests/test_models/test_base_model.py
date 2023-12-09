import unittest
import uuid
import os
import json
from models import storage
from datetime import datetime
from models.base_model import BaseModel

"""
This module uses unittest to test BaseModel class
"""


class TestBaseModel(unittest.TestCase):
    """
    To run all the possible tests of BaseModel class
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

    def test_BaseModel_type(self):
        """ What is a BaseModel """

        basemodel_type = "<class 'models.base_model.BaseModel'>"
        self.assertEqual(str(BaseModel), basemodel_type)

    def test_instance_type(self):
        """ Is an instance a BaseModel """

        myBaseModel = BaseModel()
        self.assertIsInstance(myBaseModel, BaseModel)

    def test_instance_attr_type(self):
        """ checks the types of the puplic instance attributes """

        myBaseModel = BaseModel()
        self.assertEqual(str(type(myBaseModel.id)), "<class 'str'>")
        datetime_type = "<class 'datetime.datetime'>"
        self.assertEqual(str(type(myBaseModel.created_at)), datetime_type)
        self.assertEqual(str(type(myBaseModel.updated_at)), datetime_type)

    def test_init_0_args(self):
        """ passing zero arguments (no self) """

        with self.assertRaises(TypeError) as excpt:
            BaseModel.__init__()
        excpt_msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_init_1_arg(self):
        """ ensures that args do nothing """

        my_model = BaseModel(15)
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)

    def test_random_id(self):
        """ tests if id generated is a uuid """

        my_model = BaseModel()
        my_new_model = BaseModel()
        self.assertNotEqual(my_model.id, my_new_model.id)
        uuid_regex = r'^[\da-f]{8}(-[\da-f]{4}){3}-[\da-f]{12}$'
        self.assertRegex(my_model.id, uuid_regex)
        id_to_uuid_type = str(type(uuid.UUID(my_model.id)))
        self.assertEqual(id_to_uuid_type, "<class 'uuid.UUID'>")

    def test_cmplt_kwargs(self):
        """ passing a complete dictionary """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'created_at': '2017-09-28T21:05:54.119427',
            'updated_at': '2017-09-28T21:05:54.119572'
        }
        my_id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        my_created_at = datetime.fromisoformat('2017-09-28T21:05:54.119427')
        my_updated_at = datetime.fromisoformat('2017-09-28T21:05:54.119572')
        my_model = BaseModel(**my_dict)
        self.assertEqual(my_model.id, my_id)
        self.assertEqual(my_model.created_at, my_created_at)
        self.assertEqual(my_model.updated_at, my_updated_at)

    def test_no_id_kwargs(self):
        """ passing kwargs without id attribute """

        my_dict = {
            'created_at': '2017-09-28T21:05:54.119427',
            'updated_at': '2017-09-28T21:05:54.119572'
        }
        my_created_at = datetime.fromisoformat('2017-09-28T21:05:54.119427')
        my_updated_at = datetime.fromisoformat('2017-09-28T21:05:54.119572')
        my_model = BaseModel(**my_dict)
        self.assertNotEqual(my_model.id, "")
        uuid_regex = r'^[\da-f]{8}(-[\da-f]{4}){3}-[\da-f]{12}$'
        self.assertRegex(my_model.id, uuid_regex)
        self.assertEqual(my_model.created_at, my_created_at)
        self.assertEqual(my_model.updated_at, my_updated_at)

    def test_no_updated_kwargs(self):
        """ passing kwargs without updated_at attribute """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'created_at': '2017-09-28T21:05:54.119427'
        }
        my_id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        my_created_at = datetime.fromisoformat('2017-09-28T21:05:54.119427')
        my_model = BaseModel(**my_dict)
        my_updated_at = datetime.isoformat(my_model.updated_at)
        isoformat_regex = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}$'
        self.assertRegex(my_updated_at, isoformat_regex)
        self.assertEqual(my_model.id, my_id)
        self.assertEqual(my_model.created_at, my_created_at)

    def test_no_created_kwargs(self):
        """ passing kwargs without created_at attribute """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'updated_at': '2017-09-28T21:05:54.119427'
        }
        my_id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        my_updated_at = datetime.fromisoformat('2017-09-28T21:05:54.119427')
        my_model = BaseModel(**my_dict)
        my_created_at = datetime.isoformat(my_model.created_at)
        isoformat_regex = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}$'
        self.assertRegex(my_created_at, isoformat_regex)
        self.assertEqual(my_model.id, my_id)
        self.assertEqual(my_model.updated_at, my_updated_at)

    def test_manual_kwargs(self):
        """ manually passing kwargs """

        my_id = '17'
        my_cr = '2017-09-28T21:05:54.119427'
        my_up = '2017-09-28T21:05:54.119499'
        my_model = BaseModel(id=my_id, updated_at=my_up, created_at=my_cr)
        c = datetime(2017, 9,28, 21, 5, 54, 119427)
        u = datetime(2017, 9,28, 21, 5, 54, 119499)
        self.assertEqual(my_model.id, '17')
        self.assertEqual(my_model.created_at, c)
        self.assertEqual(my_model.updated_at, u)

    def test_updated_gt_created(self):
        """ tests if updated_at is greater than created_at """

        my_model = BaseModel()
        self.assertTrue(my_model.updated_at >= my_model.created_at)

    def test_not_isoformat(self):
        """ passing kwargs with wrong isoformat of datetime """

        my_dict = {
            'created_at': '2017/09/28S21-05-54:119427',
            'updated_at': '2017-09-28T21:05:54.119572'
        }
        with self.assertRaises(ValueError) as excpt:
            my_model = BaseModel(**my_dict)
        excpt_msg = "Invalid isoformat string: '2017/09/28S21-05-54:119427'"
        self.assertEqual(str(excpt.exception), excpt_msg)
        my_dict = {
            'created_at': '2017-09-28T21:05:54.119572',
            'updated_at': 'today'
        }
        with self.assertRaises(ValueError) as excpt:
            my_model = BaseModel(**my_dict)
        excpt_msg = "Invalid isoformat string: 'today'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_str_00(self):
        """ tests __str__ method """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'created_at': '2017-09-28T21:05:54.119427',
            'updated_at': '2017-09-28T21:05:54.119572'
        }
        my_model = BaseModel(**my_dict)
        my_str = "[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) "
        my_str += "{'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', "
        my_str += "'created_at': "
        my_str += "datetime.datetime(2017, 9, 28, 21, 5, 54, 119427), "
        my_str += "'updated_at': "
        my_str += "datetime.datetime(2017, 9, 28, 21, 5, 54, 119572)}"
        self.assertEqual(my_model.__str__(), my_str)
        my_model = BaseModel()
        my_str = "[BaseModel] (" + my_model.id + ") "
        my_str += str(my_model.__dict__)
        self.assertEqual(my_model.__str__(), my_str)

    def test_str_01(self):
        """ tests __str__ method after adding more attributes """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'created_at': '2017-09-28T21:05:54.119427',
            'updated_at': '2017-09-28T21:05:54.119572',
        }
        my_model = BaseModel(**my_dict)
        my_model.name = 'Betty'
        my_model.number = 125
        my_str = "[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) "
        my_str += "{'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', "
        my_str += "'created_at': "
        my_str += "datetime.datetime(2017, 9, 28, 21, 5, 54, 119427), "
        my_str += "'updated_at': "
        my_str += "datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), "
        my_str += "'name': 'Betty', "
        my_str += "'number': 125}"
        self.assertEqual(my_model.__str__(), my_str)
        my_model = BaseModel()
        my_str = "[BaseModel] (" + my_model.id + ") "
        my_str += str(my_model.__dict__)
        self.assertEqual(my_model.__str__(), my_str)

    def test_save00(self):
        """ test to ensure that updated_at is really updated """

        my_model = BaseModel()
        last_updated = my_model.updated_at
        my_model.save()
        self.assertGreater(my_model.updated_at, last_updated)

    def test_save01(self):
        """ see if file.json exists after the call """

        my_model = BaseModel()
        my_model.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_save02(self):
        """ see if file.json contains the write output """

        my_model = BaseModel()
        my_id = "BaseModel." + my_model.id
        my_model.save()
        my_dict = {}
        my_dict[my_id] = my_model.to_dict()
        my_json = json.dumps(my_dict)
        with open('file.json', 'r', encoding='utf-8') as f:
            text_in_file = f.read()
        self.maxDiff = None
        self.assertEqual(text_in_file, my_json)

    def test_todect00(self):
        """ tests the output of a normal call """

        my_model = BaseModel()
        my_dict = {
            'id': my_model.id,
            'created_at': datetime.isoformat(my_model.created_at),
            'updated_at': datetime.isoformat(my_model.updated_at),
            '__class__': 'BaseModel'
        }
        self.assertEqual(my_model.to_dict(), my_dict)

    def test_todect01(self):
        """ tests the output after adding more attributes """

        my_model = BaseModel()
        my_model.name = 'Betty'
        my_model.number = 145
        my_dict = {
            'id': my_model.id,
            'created_at': datetime.isoformat(my_model.created_at),
            'updated_at': datetime.isoformat(my_model.updated_at),
            '__class__': 'BaseModel',
            'name': 'Betty',
            'number': 145
        }
        self.assertEqual(my_model.to_dict(), my_dict)

    def test_todect02(self):
        """ exporting a dict and use it to init a new BaseModel """

        my_model = BaseModel(id='15')
        my_model_dict = my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        self.assertEqual(my_model.id, new_model.id)
        self.assertEqual(my_model.updated_at, new_model.updated_at)
        self.assertEqual(my_model.created_at, new_model.created_at)


if __name__ == '__main__':
    unittest.main()
