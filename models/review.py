#!/usr/bin/python3
"""python interpreter"""


from models.base_model import BaseModel

class Review(BaseModel):
    """class that inherits from bm"""
    place_id = ""
    user_id = ""
    text = ""
