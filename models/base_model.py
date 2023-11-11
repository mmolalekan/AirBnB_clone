#!/usr/bin/python3
"""Module Documentation"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Class Documentation"""
    def __init__(self, *args, **kwargs):
        """Function Documentation"""
        if kwargs is not None and kwargs != {}:
            for k, v in kwargs.items():
                if k == "created_at":
                    setattr(self, k, datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f'))
                elif k == "updated_at":
                    setattr(self, k, datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f'))
                elif k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Function Documentation"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Function Documentation"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Function Documentation"""
        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        dct["created_at"] = dct["created_at"].strftime('%Y-%m-%dT%H:%M:%S.%f')
        dct["updated_at"] = dct["updated_at"].strftime('%Y-%m-%dT%H:%M:%S.%f')
        return dct
