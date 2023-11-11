#!/usr/bin/python3

"""Module defining the UserModel class
It inherits from the BaseModel.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class defining the User Model"""

    # Attributes
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
