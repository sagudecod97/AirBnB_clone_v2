#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from os import environ


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    glb_storage = environ.get('HBNB_TYPE_STORAGE')
    if glb_storage != 'db':
        @property
        def cities(self):
            """ Return all cities related with the state """
            all_cities = models.storage.all("City")
            own_city = []
            for value in all_cities.values():
                if self.id == value.state_id:
                    own_city.append(value)
            return own_city
    places = relationship("Place", backref="cities", cascade="all, delete")
