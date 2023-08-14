#!/usr/bin/python3

"""Module defining the Review Class (Model)
and it inherits from the BaseModel.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class defining the Review Model"""

    # Attributes
    place_id: str = ""
    user_id: str = ""
    text: str = ""
