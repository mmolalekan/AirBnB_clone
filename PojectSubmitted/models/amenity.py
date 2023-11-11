#!/usr/bin/python3

"""Module defining the Amenity Class (Model) and it inherits from BaseModel.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class defining The Amenity Model"""

    # Attributes
    name: str = ""
