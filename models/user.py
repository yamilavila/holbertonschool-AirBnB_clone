#!/usr/bin/python3
""" File contains the user class """
from models.base_model import BaseModel


class User(BaseModel):
    """class User """

    last_name = ""
    email = ""
    password = ""
    first_name = ""
