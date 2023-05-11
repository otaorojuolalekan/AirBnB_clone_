#!/usr/bin/env python3
"""
This is the unit test module
for base model
    TEST CASES:
    test if isinstance of BaseModel✅
    test if isisntance has attr id✅
    test if isisntance has attr created_at✅
    test if isisntance has attr updated_at✅
    test output of to_dict
    test if isisntance has extra added attributes✅
    test if created at is in isoformat
    test if to_dict returns a dictionary
    test if magic string Output is formatted right
    test if string representation of instance is correct
    test if ids generated from uuid is unique
    test if type of id is string
    test if datecreated is isinstance of datetime
    test if dateupdated is instance of datetime
    datecreated must be initially equal to updated_at
    confirm that to_dict contains __class__
    to_dict returns type dictionary
"""
import os.path
import unittest
from uuid import uuid4

import models
from models.base_model import BaseModel

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
        test if isisntance has attr created_at
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
        test if isisntance has attr name
        """
        chk = BaseModel()
        chk.name = "new_base_model"
        self.assertTrue(hasattr(chk, "name"))

    def test_to_dict_returns_dict(self):
        chk = BaseModel()
        chk1 = chk.to_dict()
        self.assertTrue(isinstance(chk1, dict))
        
if __name__ == "__main__":
    unittest.main()