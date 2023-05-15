#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
import os
from models.review import Review
from models.base_model import BaseModel
from models import storage


class TestReview(unittest.TestCase):
    """Test Cases for the Review class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()

    def resetStorage(self):
        """Resets FileStorage data."""
        storage.reset()

    def test_instantiation(self):
        """Tests instantiation of Review class."""
        r = Review()
        self.assertIsInstance(r, Review)
        self.assertIsInstance(r, BaseModel)

    def test_attributes(self):
        """Tests the attributes of Review class."""
        attributes = storage.attributes()["Review"]
        r = Review()
        for k, v in attributes.items():
            self.assertTrue(hasattr(r, k))
            self.assertEqual(type(getattr(r, k, None)), v)


if __name__ == "__main__":
    unittest.main()
