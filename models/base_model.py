#!/usr/bin/python3
import datetime
from uuid import uuid4
import uuid


class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def __str__(self):
        print(f"[{type(self)}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        return self.__dict__
