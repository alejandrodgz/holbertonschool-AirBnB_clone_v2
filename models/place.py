#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import models


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        place_amenity = Table(
            'place_amenity',
            Base.metadata,
            Column(
                'place_id',
                String(60),
                ForeignKey(
                    'places.id',
                    onupdate='CASCADE',
                    ondelete='CASCADE'),
                primary_key=True,
                nullable=False),
            Column(
                'amenity_id',
                String(60),
                ForeignKey(
                    'amenities.id',
                    onupdate='CASCADE',
                    ondelete='CASCADE'),
                primary_key=True,
                nullable=False))

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship(
            "Review",
            backref='place',
            cascade='all, delete, delete-orphan')
        amenities = relationship(
            "Amenity",
            backref='place_amenities',
            secondary=place_amenity,
            viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        '''initializes places'''
        super().__init__(*args, **kwargs)

    if os.getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def reviews(self):
            dict_result = {}
            '''getter'''
            dict1 = models.storage.all('Review')
            for key, value in dict1.items():
                if value.place_id == self.id:
                    dict_result[key] = value
            return dict_result
            
    @property
    def amenities(self):
        """getter attribute returns the list of Amenity instances"""
        from models.amenity import Amenity
        amenity_list = []
        all_amenities = models.storage.all(Amenity)
        for amenity in all_amenities.values():
            if amenity.place_id == self.id:
                amenity_list.append(amenity)
        return amenity_list