#!/usr/bin/python3
"""BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """defines BaseModel for the projct """
    def __init__(self, *args, **kwargs):
        """function define *args **kwargs"""
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, j in kwargs.items():
                if k == "updated_at" or k == "created_at":
                    self.__dict__[k] = datetime.strptime(j, tform)
                else:
                    self.__dict__[k] = j
        else:
            models.storage.new(self)

    def save(self):
        """save updated_at with current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """print the representaion of BaseModel"""
        clname = self.__class__.__name__
        return "[{}], ({}), {}".format(clname, self.id, self.__dict__)
