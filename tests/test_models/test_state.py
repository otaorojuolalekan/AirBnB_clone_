import unittest
import os

from models import storage
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        self.reset_storage()

    def reset_storage(self):
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertIsInstance(state, State)

    def test_attributes(self):
        attributes = storage.attributes()["State"]
        state = State()
        for k, v in attributes.items():
            self.assertTrue(hasattr(state, k))
            self.assertEqual(type(getattr(state, k, None)), v)

if __name__ == "__main__":
    unittest.main()
