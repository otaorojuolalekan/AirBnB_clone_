#!/usr/bin/env python3
"""
This module contains and defines all
common attributes/methods for other classes.
"""
import uuid
from datetime import datetime as dt

class BaseModel():
    """
    BaseModel Class
    """
    def __init__(self, *args, **kwargs):
        """Initialization for the Base class"""
        # Deserialization: updating init method to use **kwargs
        if kwargs:
            # remove the __class__ attribute
            del kwargs["__class__"]
            # run through kwargs items
            for k, v in kwargs.items():
                if k in ("created_at", "updated_at"):
                    # convert datetime string to datetime object using strptime
                    setattr(self, k,
                            dt.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, k, v)
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = dt.now()
            storage.new(self)

    def __str__(self):
        """string representation of Base class Instance"""
        clsname = self.__class__.__name__
        args = [clsname, self.id, self.__dict__]
        return "[{}] ({}) {}".format(*args)

    def save(self):
        """This method updates the updated_at attribute"""
        from models import storage
        self.updated_at = dt.now()
        storage.save()

    def to_dict(self):
        """Dictionary representation of Base instance"""
        base_dicko = self.__dict__.copy()
        base_dicko["__class__"] = self.__class__.__name__
        # base_dicko['created_at'] = self.created_at.isoformat()
        # base_dicko['updated_at'] = self.updated_at.isoformat()
        # run through each item in base dicko, if date time

        # later in life, try using getattr and setattr for this...

        for k, v in base_dicko.items():
            if isinstance(v, dt):
                base_dicko[k] = v.isoformat()
            # else:
            #     base_dicko[k] = v
        return base_dicko


# if __name__ == "__main__":
#     bins1 = BaseModel()
#     print(bins1)
#     bins2 = BaseModel()
#     print(bins2)
