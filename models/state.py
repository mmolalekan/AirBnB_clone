#!/usr/bin/python3

"""Module defining the State Class (Model)
and it inherits from the BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """Class defining the State Model"""

    # Attributes
    name: str = ""
