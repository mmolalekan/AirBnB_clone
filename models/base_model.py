#!/usr/bin/python3
"""
This module Defines the BaseModel class that
serves as the base class for all the models.
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Class defining Base class for all the classes"""

    def __init__(self, *args, **kwargs):
        """Instantiation: it either decodes
        an encoded class or initialises a new"""

        # initialization
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
            return

        # Decoding
        for key, val in kwargs.items():
            if key == '__class__':
                continue
            self.__dict__[key] = val
        if 'created_at' in kwargs:
            self.created_at = datetime.strptime(
                    kwargs['created_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')
        if 'updated_at' in kwargs:
            self.updated_at = datetime.strptime(
                    kwargs['updated_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """Defines magic method str representation of self"""
        fmt = "[{}] ({}) {}"
        return fmt.format(
                type(self).__name__,
                self.id,
                self.__dict__)

    def save(self):
        """Overwrite and updates latest update"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Converts an object(self) as a dictionary representation"""
        tmp = {**self.__dict__}
        tmp['__class__'] = type(self).__name__
        tmp['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        tmp['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return temp

    @classmethod
    def all(cls):
        """current instances of cls"""
        return models.storage.find_all(cls.__name__)

    @classmethod
    def count(cls):
        """Return the number of all current instances of cls"""
        return len(models.storage.find_all(cls.__name__))

    @classmethod
    def create(cls, *args, **kwargs):
        """Creates and returns an Instance"""
        new = cls(*args, **kwargs)
        return new.id

    @classmethod
    def show(cls, instance_id):
        """Retrieve an instance"""
        return models.storage.find_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def destroy(cls, instance_id):
        """Destroys an instance"""
        return models.storage.delete_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def update(cls, instance_id, *args):
        """Instance Update"""
        if not len(args):
            print("** attribute name missing **")
            return
        if len(args) == 1 and isinstance(args[0], dict):
            args = args[0].items()
        else:
            args = [args[:2]]
        for arg in args:
            models.storage.update_one(
                cls.__name__,
                instance_id,
                *arg
            )
