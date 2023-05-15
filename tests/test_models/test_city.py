import unittest
import os

from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

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
        self.city = City()

    def tearDown(self):
        """Tears down method-level fixtures."""
        storage.delete_all()

    def test_instantiation(self):
        """Tests instantiation of City class."""
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """Tests the attributes of City class."""
        attributes = storage.attributes()["City"]
        for k, v in attributes.items():
            self.assertTrue(hasattr(self.city, k))
            self.assertEqual(type(getattr(self.city, k, None)), v)


if __name__ == "__main__":
    unittest.main()
