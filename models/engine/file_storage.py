#!/usr/bin/env python3
'''File Storage file'''

import json
import os
from importlib import import_module

class FileStorage():
    """File storage module"""
    
    """Class for storing and retrieving data
    Class Methods:
        all: Returns the object (dictionary object)
        new: updates the object id
        save: Converts Python objects into JSON strings
        reload: Converts JSON strings inton Python objects

    Class Attributs:
        __file_path (str): The name of the file, objects are saved to
        __objects (dict): A dictionary of instantiated objects
        class_dict (dict): A dictionary of all the classes
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Initializes a FileStorage instance"""
        self.model_classes = {
                'BaseModel': import_module('models.base_model').BaseModel,
                'User': import_module('models.user').User,
                'State': import_module('models.state').State,
                'City': import_module('models.city').City,
                'Amenity': import_module('models.amenity').Amenity,
                'Place': import_module('models.place').Place,
                'Review': import_module('models.review').Review
            }

    def all(self, cls=None):
        """returns all objects or ojects of a specified class"""
        if cls is None:
            return self.__objects
        else:
            filtered_dict = {}
            for key, value in self.__objects.items():
                if type(value) is cls:
                    filtered_dict[key] = value
            return filtered_dict

    def new(self, obj):
        """Adds a new object to storage dictionary"""
        self.__objects.update( 
                {obj.to_dict()['__class__'] + '.' + obj.id: obj}
        )

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
        def is_valid_class(class_name):
            """Check if the class name is valid."""
            # Check if the class name exists in the global namespace
            return class_name in globals() and isinstance(globals()[class_name], type)

        file = FileStorage.__file_path

        try:
            if os.path.isfile(file):
                with open(file, 'r', encoding="utf-8") as f:
                    content = f.read()
                    formatted_content = json.loads(content)

                    for value in formatted_content.values():
                        class_name = value.get("__class__")
                        if class_name and is_valid_class(class_name):
                            self.new(obj)
                        else:
                            # Log or handle invalid class names
                            pass
        except FileNotFoundError as e:
            print(f"Error loading data from file: {e}")

    def update(self, key, attr, value):
        """updates an instance"""
        if key in FileStorage.__objects:
            instance = FileStorage.__objects[key]
            setattr(instance, attr, value)
            instance.save()
        else:
            print("** no instance found **")
            
    def delete(self, obj=None):
        """Deletes an object from __objects"""
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del FileStorage.__objects[key]

