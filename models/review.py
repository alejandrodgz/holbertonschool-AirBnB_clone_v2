#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String, Integer, ForeignKey, Float


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
