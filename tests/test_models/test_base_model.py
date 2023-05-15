#!/usr/bin/env python3
"""
This is the unit test module
for base model
"""
import unittest
from uuid import uuid4
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Unit Test Class for Base Model
    """

    def test_class_initiation(self):
        """Test if instance created successfully"""
        chk = BaseModel()
        self.assertTrue(isinstance(chk, BaseModel))

    def test_has_id_attr(self):
        """
        checks if model has id attr
        """
        checker = BaseModel()
        self.assertTrue(hasattr(checker, "id"))

    def test_has_created_at_attr(self):
        """
        test if isinstance has attr created_at
        """
        chk = BaseModel()
        self.assertTrue(hasattr(chk, "created_at"))

    def test_has_updated_at_attr(self):
        """
        test if isisntance has attr updated_at
        """
        chk = BaseModel()
        self.assertTrue(hasattr(chk, "updated_at"))

    def test_has_extra_attr(self):
        """
        test if isisntance has extra added attributes
        And if the values of the attributes are appropriate
        """
        chk = BaseModel()
        extattr = {"name": "my_first_ model", "my_number": 89}
        for k, v in extattr.items():
            setattr(chk, k, v)
            self.assertTrue(hasattr(chk, k))
            self.assertEqual(getattr(chk, k), v)

    def test_to_dict_returns_dict(self):
        chk = BaseModel()
        chk1 = chk.to_dict()
        self.assertIsInstance(chk1, dict)

    def test_id_type(self):
        """
        test if id is of type string
        """
        chk = BaseModel()
        chk_id = chk.id
        self.assertIsInstance(chk_id, str)

    def test_print_instance(self):
        """
        test if print instance Output is formatted right
        """
        chk = BaseModel()
        clsname = self.__class__.__name__
        args = [clsname, self.id, self.__dict__]
        expRes = print("[{}] ({}) {}".format(*args))
        # self.assertTrue(isinstance(print(chk), str))
        self.assertEqual(print(chk), expRes)

    def test_contains_class_(self):
        """
        confirm that to_dict contains __class__
        """
        chk = BaseModel()
        self.assertTrue("__class__" in chk.to_dict())

    def test_unique_ids(self):
        """Test uuid returns unique values"""
        chk1 = BaseModel()
        chk2 = BaseModel()
        chk3 = BaseModel()
        self.assertNotEqual(chk1.id, chk2.id)
        self.assertNotEqual(chk2.id, chk3.id)

    def test_created_at_type(self):
        """test created at type is datetime"""
        chk = BaseModel()
        self.assertIsInstance(chk.created_at, datetime)

    def test_updated_at_type(self):
        """test updated at type is datetime"""
        chk = BaseModel()
        self.assertIsInstance(chk.created_at, datetime)

    def test_created_updated_at_eq(self):
        """
        Test to see that created_at and updated_at
        are equal at instance initiation
        """
        chk = BaseModel()
        self.assertEqual(chk.created_at, chk.updated_at)

    def test_to_dict_output(self):
        """
        test output of to_dict
        """
        chk = BaseModel()
        chk.id = 123456
        chk.name = "My_Model"
        dtnow = datetime.now()
        chk.created_at = chk.updated_at = dtnow
        chk_dictresult = {
            'id': 123456,
            'created_at': dtnow.isoformat(),
            'name': "My_Model",
            'updated_at': dtnow.isoformat(),
            '__class__': "BaseModel"
        }
        self.assertDictEqual(chk_dictresult, chk.to_dict())


if __name__ == "__main__":
    unittest.main()
