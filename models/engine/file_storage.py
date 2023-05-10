#!/usr/bin/env python3
"""
Module containing storage class
that enables persistence while serializing
or deserializing using Json
"""
import json
from base_model import BaseModel


class FileStorage(BaseModel):
    """
    file storage class
    """

    def __init__(self, file_path="", objects={}):
        """
        Initialization of the file storage class
        Args:
            file_path: private attribute
            objects: private dictionary object
        """
        self.__file_path = file_path
        self.__objects = objects

    def all(self):
        """returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with
        key <obj cls name>.id
        """
        super().__init__(id)
