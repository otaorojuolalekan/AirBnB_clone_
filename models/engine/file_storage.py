#!/usr/bin/env python3
"""
Module containing storage class
that enables persistence while serializing
or deserializing using Json
"""
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """
    file storage class
    """
    __file_path = "basemodelfile.json"
    __objects = {}

    def all(self):
        """returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with
        key <obj cls name>.id
        """
        args = [obj.__class__.__name__, obj.id]
        key = "{}.{}".format(*args)
        self.__objects[key] = obj

    def save(self):
        """
         serializes __objects to the JSON file (path: __file_path)
        """
        jsondict = {}
        for k, v in self.__objects.items():
            jsondict[k] = v.to_dict()

        with open(self.__file_path, 'w', encoding="UTF-8") as fp:
            json.dump(jsondict, fp)

    def reload(self):
        """
        Deserializes the JSON file to __objects
            Only IF it exists!
                if it doesn't exist, do nothing
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, encoding="utf-8") as jsfile:
                json_dict  = json.load(jsfile)

            for obj_key, base_obj in json_dict.items():
                clsname, obj_id = obj_key.split('.')
                self.new(eval(base_obj["__class__"])(**base_obj))

    def classes(self):
        """Contains dictionary of classes to be used in Filestorage instance"""
        from models.base_model import BaseModel
        classdict = {"BaseModel": BaseModel}
        return classdict
