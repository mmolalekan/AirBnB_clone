#!/usr/bin/python3
"""Module Documentation"""
import json
import os


class FileStorage:
    """Class Documentation"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Function Documentation"""
        return type(self).__objects

    def new(self, obj):
        """Function Documentation"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """Function Documentation"""
        dct = {}
        for k, v in FileStorage.__objects.items():
            dct[k] = v.to_dict()
        with open(type(self).__file_path, 'w', encoding="utf-8") as file:
            json.dump(dct, file)
    
    def reload(self):
        """Function Documentation"""
        from models.base_model import BaseModel
        if os.path.exists(FileStorage.__file_path):
            with open(type(self).__file_path, 'r', encoding="utf-8") as file:
                objs = json.load(file)
                for k, v in objs.items():
                    obj_instance = BaseModel(**v)
                    objs[k] = obj_instance
                FileStorage.__objects = objs
        else:
            return
        
# class FileStorage:
#     """Class Documentation"""
#     __file_path = 'file.json'
#     __objects = {}
#
#     def all(self):
#         """Function Documentation"""
#         return type(self).__objects
#
#     def new(self, obj):
#         """Function Documentation"""
#         key = "{}.{}".format(type(obj).__name__, obj.id)
#         type(self).__objects[key] = obj
#
#     def save(self):
#         """Function Documentation"""
#         with open(type(self).__file_path, 'w', encoding='utf-8') as file:
#             d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
#             json.dump(d, file)
#
#     def classes(self):
#         """Returns a dictionary of valid classes and their references"""
#         from models.base_model import BaseModel
#         # from models.user import User
#         # from models.state import State
#         # from models.city import City
#         # from models.amenity import Amenity
#         # from models.place import Place
#         # from models.review import Review
#
#         classes = {"BaseModel": BaseModel,
#                    # "User": User,
#                    # "State": State,
#                    # "City": City,
#                    # "Amenity": Amenity,
#                    # "Place": Place,
#                    # "Review": Review
#                    }
#         return classes
#
#     def reload(self):
#         """Function Documentation"""
#         if os.path.exists(self.__file_path):
#             with open(type(self).__file_path, 'r', encoding='utf-8') as file:
#                 obj_dict = json.load(file)
#                 from models.base_model import BaseModel
#                 for key, value in obj_dict.items():
#                     class_name = value['__class__']
#                     obj_class = self.classes()[class_name]
#                     obj_instance = obj_class(**value)
#                     obj_dict[key] = obj_instance
#                 FileStorage.__objects = obj_dict
#         else:
#             return
