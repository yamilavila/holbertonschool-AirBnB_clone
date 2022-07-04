#!/usr/bin/python3
""" File contains the user class """
from models.base_model import BaseModel


class User(BaseModel):
    """ creates a user basic info """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
