#!/usr/bin/env python3
'''File Storage file'''

import json
import os
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class FileStorage():
    """File storage module"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all object"""
        return FileStorage.__objects

    def new(self, obj):
        """sets a new object"""
        FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """saves a new obj"""
        objects = FileStorage.__objects
        file = FileStorage.__file_path
        content = {}

        for key, value in objects.items():
            content[key] = value.to_dict()

        with open(file, 'w', encoding="utf-8") as f:
            f.write(json.dumps(content))

    def reload(self):
        """reloads from a json file"""

        file = FileStorage.__file_path

        try:
            if os.path.isfile(file):
                with open(file, 'r', encoding="utf-8") as f:
                    content = f.read()
                    formattedContent = json.loads(content)

                    for value in formattedContent.values():
                        class_name = value["__class__"]
                        self.new(eval(class_name)(**value))

        except FileNotFoundError:
            pass

    def update(self, key, attr, value):
        """updates an instance"""
        if key in FileStorage.__objects:
            instance = FileStorage.__objects[key]
            setattr(instance, attr, value)
            instance.save()
        else:
            print("** no instance found **")

    def delete(self, key):
        """deletes an instance"""
        if key in FileStorage.__objects:
            del FileStorage.__objects[key]
            self.save()
        else:
            print("** no instance found **")

    def delete(self, obj=None):

