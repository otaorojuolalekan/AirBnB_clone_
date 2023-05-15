#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
import os
from models.user import User
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test Cases for the User class."""

    @classmethod
    def setUpClass(cls):
        """Sets up test class."""
        storage.reload()

    def tearDown(self):
        """Tears down test methods."""
        storage.delete_all()

    def test_instantiation(self):
        """Tests instantiation of User class."""
        b = User()
        self.assertIsInstance(b, User)
        self.assertIsInstance(b, BaseModel)
        self.assertEqual(type(b).__name__, "User")

    def test_attributes(self):
        """Tests the attributes of User class."""
        attributes = ["email", "password", "first_name", "last_name"]
        o = User()
        for attr in attributes:
            self.assertTrue(hasattr(o, attr))
            self.assertEqual(getattr(o, attr, None), None)


if __name__ == "__main__":
    unittest.main()
