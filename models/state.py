#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
    __tablename__ = "states"

    @property
    def cities(self):
        """retrieve all citites objects"""
        clist = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                clist.append(city)
        return clist
