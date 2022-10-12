#!/usr/bin/python3


import json
import os
from models.base_model import BaseModel

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        FileStorage.__objects[obj.id] = obj

    def save(self):
        objs = {}
        for id in FileStorage.__objects:
            objs[id] = FileStorage.__objects[id].to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(objs))

    def reload(self):
        FileStorage.__objects = {}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                file_content = f.read()
                data = json.loads(file_content) if file_content is not None else []
                for key, value in data.items():
                    FileStorage.__objects[key] = BaseModel(value)
