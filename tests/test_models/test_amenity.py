import unittest
import os

from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    @classmethod
    def setUpClass(cls):
        """Sets up class-level fixtures."""
        cls.file_path = FileStorage._FileStorage__file_path

    @classmethod
    def tearDownClass(cls):
        """Tears down class-level fixtures."""
        os.remove(cls.file_path)

    def setUp(self):
        """Sets up method-level fixtures."""
        self.amenity = Amenity()

    def tearDown(self):
        """Tears down method-level fixtures."""
        storage.delete_all()

    def test_instantiation(self):
        """Tests instantiation of Amenity class."""
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        """Tests the attributes of Amenity class."""
        attributes = storage.attributes()["Amenity"]
        for k, v in attributes.items():
            self.assertTrue(hasattr(self.amenity, k))
            self.assertEqual(type(getattr(self.amenity, k, None)), v)


if __name__ == "__main__":
    unittest.main()
