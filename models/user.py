#!/usr/bin/python3
""" File contains the user class """
from models.base_model import BaseModel


class User(BaseModel):
    """ creates a user basic info """
    def __init__(self):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
