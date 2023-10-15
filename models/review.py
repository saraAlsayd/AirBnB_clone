#!/usr/bin/python3
"""Defines Review class that inherits from basemodel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class attributes"""

    place_id = ""
    user_id = ""
    text = ""
