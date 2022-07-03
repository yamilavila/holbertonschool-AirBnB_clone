#!usr/bin/python3
""" Have specific information of the User place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Places inherit form BaseModel """
    city_id = ""
    user_id = ""
    name = ""
    descritpion = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
