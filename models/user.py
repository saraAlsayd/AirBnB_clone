#!/usr/bin/python3
"""user class that inherits from basemodel"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class attributes"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
