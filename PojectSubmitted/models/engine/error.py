#!/usr/bin/python3

"""
Module defining the user errors used in File Storage
"""


class ModelNotFoundError(Exception):
    """This Exception is Raised indicating an unknown module"""
    def __init__(self, arg="BaseModel"):
        super().__init__(f"Model with name {arg} is not registered!")


class InstanceNotFoundError(Exception):
    """This Exceptio is Raised indicating an unknown id"""

    def __init__(self, obj_id="", mod="BaseModel"):
        super().__init__(
                f"Instance of {mod} with id {obj_id} does not exist!")
