#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    glb_storage = environ.get('HBNB_TYPE_STORAGE')
    if glb_storage != 'db':
        @property
        def cities(self):
            """Return all cities related with the state"""
            all_cities = storage.all(City)
            own_city = []
            for value in all_cities.values():
                if self.id == value.state_id:
                    own_city.append(value)
            return own_city
    else:
        cities = relationship('City', back_populates='state')
