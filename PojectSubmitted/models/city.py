#!/usr/bin/python3

"""Module defining the City Class (Model)
and it inherits from the BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class deifning the City Model"""

    # Attributes
    name: str = ""
    state_id: str = ""
