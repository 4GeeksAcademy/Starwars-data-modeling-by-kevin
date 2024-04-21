import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    is_active = Column(Boolean(), unique=False, nullable=False)
    fav_planet = relationship('Favorite_planet', back_populates = 'user')
    fav_character = relationship('Favorite_character', back_populates='user')


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(120), unique=True, nullable=False)
    population = Column(String(80), unique=False, nullable=False)
    gravity = Column(String(80), unique=False, nullable=False)
    fav_planet = relationship('Favorite_planet', back_populates='planet')


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(120), unique=True, nullable=False)
    age = Column(String(80), unique=False, nullable=False)
    weight = Column(String(80), unique=False, nullable=False)
    fav_character = relationship('Favorite_character', back_populates='character')

class Favorite_planet(Base):
    __tablename__ = 'favorite_planet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user = relationship('User', back_populates='fav_planet')
    planet = relationship('Planet', back_populates='fav_planet')

class Favorite_character(Base):
    __tablename__ = 'favorite_character'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    user = relationship('User', back_populates='fav_character')
    character = relationship('Planet', back_populates='fav_character')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
