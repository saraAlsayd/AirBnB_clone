#!/usr/bin/python3
"""serializes instances to a JSON file and
deserializes JSON file to instances"""
import json
import os.path


class FileStorage():
    """Private class attributes"""
    __file_path = "file.json"
    __objects = {}
    classes = {'BaseModel': BaseModel, 'User': User,
        'State': State, 'City': City, 'Amenity': Amenity, 'Place': Place, 'Review': Review}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with
        key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file """
        obj_dict = {}
        for instance in self.__objects:
            obj_dict[instance] = self.__objects[instance].to_dict()
        with open(self.__file_path, mode='w', encoding="utf-8") as f:
            f.write(json.dumps(obj_dict))
        
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, mode='r', encoding="utf-8") as f:
                obj_dict = json.loads(f.read())
                for key in obj_dict:
                    cls = self.classes[key.split('.')[0]]
                    self.__objects[key] = cls(**(obj_dict[key]))
        except FileNotFoundError:
            pass
