
"""
This module uses unittest to test Review class
"""

import unittest
import uuid
import os
import json
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    To run all the possible tests of Review class
    using unittest
    """

    def setUp(self):
        """ starts a new connection """

        setattr(storage, "_FileStorage__objects", {})
        pass

    def tearDown(self):
        """ Removes all the connections (restoring the initial Review)"""

        if os.path.exists('file.json'):
            os.remove('file.json')
        pass

    def test_Review_type(self):
        """ What is a Review """

        Review_type = "<class 'models.review.Review'>"
        self.assertEqual(str(Review), Review_type)

    def test_Review_as_subclass(self):
        """ test to see if Review is a subclass of BaseModel """

        self.assertTrue(issubclass(Review, BaseModel))

    def test_instance_type(self):
        """ Is an instance a Review """

        myReview = Review()
        self.assertIsInstance(myReview, Review)

    def test_Review_attr(self):
        """ checks if Review has its attributes """

        my_Review = Review()
        self.assertTrue(hasattr(my_Review, "id"))
        self.assertTrue(hasattr(my_Review, "created_at"))
        self.assertTrue(hasattr(my_Review, "updated_at"))
        self.assertTrue(hasattr(my_Review, "text"))
        self.assertTrue(hasattr(my_Review, "place_id"))
        self.assertTrue(hasattr(my_Review, "user_id"))

    def test_Review_extra_attr(self):
        """ checks if Review has the added attributes """

        my_Review = Review()
        my_Review.number = 129
        self.assertTrue(hasattr(my_Review, "number"))

    def test_instance_attr_type(self):
        """ checks the types of the puplic instance attributes """

        myReview = Review()
        self.assertEqual(str(type(myReview.id)), "<class 'str'>")
        self.assertEqual(str(type(myReview.text)), "<class 'str'>")
        self.assertEqual(str(type(myReview.place_id)), "<class 'str'>")
        self.assertEqual(str(type(myReview.user_id)), "<class 'str'>")
        datetime_type = "<class 'datetime.datetime'>"
        self.assertEqual(str(type(myReview.created_at)), datetime_type)
        self.assertEqual(str(type(myReview.updated_at)), datetime_type)

    def test_init_0_args(self):
        """ passing zero arguments (no self) """

        with self.assertRaises(TypeError) as excpt:
            Review.__init__()
        excpt_msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_init_1_arg(self):
        """ ensures that args do nothing """

        my_Review = Review(15)
        my_Review_json = my_Review.to_dict()
        my_new_model = Review(**my_Review_json)
        self.assertEqual(my_Review.id, my_new_model.id)
        self.assertEqual(my_Review.created_at, my_new_model.created_at)
        self.assertEqual(my_Review.updated_at, my_new_model.updated_at)

    def test_random_id(self):
        """ tests if id generated is a uuid """

        my_Review = Review()
        my_new_model = Review()
        self.assertNotEqual(my_Review.id, my_new_model.id)
        uuid_regex = r'^[\da-f]{8}(-[\da-f]{4}){3}-[\da-f]{12}$'
        self.assertRegex(my_Review.id, uuid_regex)
        id_to_uuid_type = str(type(uuid.UUID(my_Review.id)))
        self.assertEqual(id_to_uuid_type, "<class 'uuid.UUID'>")

    def test_cmplt_kwargs(self):
        """ passing a complete dictionary """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'created_at': '2017-09-28T21:05:54.119427',
            'updated_at': '2017-09-28T21:05:54.119572',
            'text': 'NY',
            'place_id': 'WC',
            'user_id': 'Ahmed'
        }
        my_id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        my_created_at = datetime.fromisoformat('2017-09-28T21:05:54.119427')
        my_updated_at = datetime.fromisoformat('2017-09-28T21:05:54.119572')
        my_text = 'NY'
        my_place = 'WC'
        my_user = 'Ahmed'
        my_Review = Review(**my_dict)
        self.assertEqual(my_Review.id, my_id)
        self.assertEqual(my_Review.created_at, my_created_at)
        self.assertEqual(my_Review.updated_at, my_updated_at)
        self.assertEqual(my_Review.text, my_text)
        self.assertEqual(my_Review.place_id, my_place)
        self.assertEqual(my_Review.user_id, my_user)

    def test_no_id_kwargs(self):
        """ passing kwargs without id attribute """

        my_dict = {
            'created_at': '2017-09-28T21:05:54.119427',
            'updated_at': '2017-09-28T21:05:54.119572'
        }
        my_created_at = datetime.fromisoformat('2017-09-28T21:05:54.119427')
        my_updated_at = datetime.fromisoformat('2017-09-28T21:05:54.119572')
        my_Review = Review(**my_dict)
        self.assertNotEqual(my_Review.id, "")
        uuid_regex = r'^[\da-f]{8}(-[\da-f]{4}){3}-[\da-f]{12}$'
        self.assertRegex(my_Review.id, uuid_regex)
        self.assertEqual(my_Review.created_at, my_created_at)
        self.assertEqual(my_Review.updated_at, my_updated_at)

    def test_no_updated_kwargs(self):
        """ passing kwargs without updated_at attribute """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'created_at': '2017-09-28T21:05:54.119427'
        }
        my_id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        my_created_at = datetime.fromisoformat('2017-09-28T21:05:54.119427')
        my_Review = Review(**my_dict)
        my_updated_at = datetime.isoformat(my_Review.updated_at)
        isoformat_regex = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}$'
        self.assertRegex(my_updated_at, isoformat_regex)
        self.assertEqual(my_Review.id, my_id)
        self.assertEqual(my_Review.created_at, my_created_at)

    def test_no_created_kwargs(self):
        """ passing kwargs without created_at attribute """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'updated_at': '2017-09-28T21:05:54.119427'
        }
        my_id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        my_updated_at = datetime.fromisoformat('2017-09-28T21:05:54.119427')
        my_Review = Review(**my_dict)
        my_created_at = datetime.isoformat(my_Review.created_at)
        isoformat_regex = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}$'
        self.assertRegex(my_created_at, isoformat_regex)
        self.assertEqual(my_Review.id, my_id)
        self.assertEqual(my_Review.updated_at, my_updated_at)

    def test_manual_kwargs(self):
        """ manually passing kwargs """

        my_id = '17'
        my_cr = '2017-09-28T21:05:54.119427'
        my_up = '2017-09-28T21:05:54.119499'
        my_Review = Review(id=my_id, updated_at=my_up, created_at=my_cr)
        c = datetime(2017, 9, 28, 21, 5, 54, 119427)
        u = datetime(2017, 9, 28, 21, 5, 54, 119499)
        self.assertEqual(my_Review.id, '17')
        self.assertEqual(my_Review.created_at, c)
        self.assertEqual(my_Review.updated_at, u)

    def test_updated_gt_created(self):
        """ tests if updated_at is greater than created_at """

        my_Review = Review()
        self.assertTrue(my_Review.updated_at >= my_Review.created_at)

    def test_not_isoformat(self):
        """ passing kwargs with wrong isoformat of datetime """

        my_dict = {
            'created_at': '2017/09/28S21-05-54:119427',
            'updated_at': '2017-09-28T21:05:54.119572'
        }
        with self.assertRaises(ValueError) as excpt:
            my_Review = Review(**my_dict)
        excpt_msg = "Invalid isoformat string: '2017/09/28S21-05-54:119427'"
        self.assertEqual(str(excpt.exception), excpt_msg)
        my_dict = {
            'created_at': '2017-09-28T21:05:54.119572',
            'updated_at': 'today'
        }
        with self.assertRaises(ValueError) as excpt:
            my_Review = Review(**my_dict)
        excpt_msg = "Invalid isoformat string: 'today'"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_str_00(self):
        """ tests __str__ method """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'created_at': '2017-09-28T21:05:54.119427',
            'updated_at': '2017-09-28T21:05:54.119572',
            'text': 'NY',
            'place_id': 'WC',
            'user_id': 'Mohammed'
        }
        my_Review = Review(**my_dict)
        my_str = "[Review] (b6a6e15c-c67d-4312-9a75-9d084935e579) "
        my_str += "{'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', "
        my_str += "'created_at': "
        my_str += "datetime.datetime(2017, 9, 28, 21, 5, 54, 119427), "
        my_str += "'updated_at': "
        my_str += "datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), "
        my_str += "'text': 'NY', 'place_id': 'WC', 'user_id': 'Mohammed'}"
        self.assertEqual(my_Review.__str__(), my_str)
        my_Review = Review()
        my_str = "[Review] (" + my_Review.id + ") "
        my_str += str(my_Review.__dict__)
        self.assertEqual(my_Review.__str__(), my_str)

    def test_str_01(self):
        """ tests __str__ method after adding more attributes """

        my_dict = {
            'id': "b6a6e15c-c67d-4312-9a75-9d084935e579",
            'created_at': '2017-09-28T21:05:54.119427',
            'updated_at': '2017-09-28T21:05:54.119572',
            'text': 'NY',
            'place_id': 'WC',
            'user_id': 'Ibrahim'
        }
        my_Review = Review(**my_dict)
        my_Review.add1 = 'Betty'
        my_Review.add2 = 125
        my_str = "[Review] (b6a6e15c-c67d-4312-9a75-9d084935e579) "
        my_str += "{'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', "
        my_str += "'created_at': "
        my_str += "datetime.datetime(2017, 9, 28, 21, 5, 54, 119427), "
        my_str += "'updated_at': "
        my_str += "datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), "
        my_str += "'text': 'NY', 'place_id': 'WC', 'user_id': 'Ibrahim', "
        my_str += "'add1': 'Betty', "
        my_str += "'add2': 125}"
        self.assertEqual(my_Review.__str__(), my_str)
        my_Review = Review()
        my_str = "[Review] (" + my_Review.id + ") "
        my_str += str(my_Review.__dict__)
        self.assertEqual(my_Review.__str__(), my_str)

    def test_save00(self):
        """ test to ensure that updated_at is really updated """

        my_Review = Review()
        last_updated = my_Review.updated_at
        my_Review.save()
        self.assertGreater(my_Review.updated_at, last_updated)

    def test_save01(self):
        """ see if file.json exists after the call """

        my_Review = Review()
        my_Review.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_save02(self):
        """ see if file.json contains the write output """

        my_Review = Review()
        my_id = "Review." + my_Review.id
        my_Review.save()
        my_dict = {}
        my_dict[my_id] = my_Review.to_dict()
        my_json = json.dumps(my_dict)
        with open('file.json', 'r', encoding='utf-8') as f:
            text_in_file = f.read()
        self.maxDiff = None
        self.assertEqual(text_in_file, my_json)

    def test_todect00(self):
        """ tests the output of a normal call """

        my_Review = Review()
        my_dict = {
            'id': my_Review.id,
            'created_at': datetime.isoformat(my_Review.created_at),
            'updated_at': datetime.isoformat(my_Review.updated_at),
            '__class__': 'Review',
            'text': '',
            'place_id': '',
            'user_id': ''
        }
        self.assertEqual(my_Review.to_dict(), my_dict)

    def test_todect01(self):
        """ tests the output after adding more attributes """

        my_Review = Review()
        my_Review.text = 'Betty'
        my_Review.number = 145
        my_dict = {
            'id': my_Review.id,
            'created_at': datetime.isoformat(my_Review.created_at),
            'updated_at': datetime.isoformat(my_Review.updated_at),
            '__class__': 'Review',
            'text': 'Betty',
            'place_id': '',
            'user_id': '',
            'number': 145
        }
        self.assertEqual(my_Review.to_dict(), my_dict)

    def test_todect02(self):
        """ exporting a dict and use it to init a new Review """

        my_Review = Review(id='15')
        my_Review_dict = my_Review.to_dict()
        new_model = Review(**my_Review_dict)
        self.assertEqual(my_Review.id, new_model.id)
        self.assertEqual(my_Review.updated_at, new_model.updated_at)
        self.assertEqual(my_Review.created_at, new_model.created_at)

    def test_todect_with_args(self):
        """ passing one argument to to_dict (with self) """

        my_Review = Review()
        with self.assertRaises(TypeError) as excpt:
            my_Review.to_dict(15)
        excpt_msg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(excpt.exception), excpt_msg)

    def test_save_with_args(self):
        """ passing 1 argument to save (with self) """

        my_Review = Review()
        with self.assertRaises(TypeError) as excpt:
            my_Review.save(15)
        excpt_msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(excpt.exception), excpt_msg)


if __name__ == '__main__':
    unittest.main()
