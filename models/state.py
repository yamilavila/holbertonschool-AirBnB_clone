#!/usr/bin/python3
""" Object that creates a state inherited form
    Base Model."""
from models.base_model import BaseModel


class State(BaseModel):
    """ State for the User"""
    name = ""
