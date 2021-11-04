import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class User(Base):
    __tablename__ = 'user'
    id =  Column(Integer, primary_key=True)
    user_name = Column(String(30),nullable=False)
    password = Column(String(30),nullable=False)
    

class Planets(Base):
    __tablename__ = 'planets'
    id =  Column(Integer, primary_key=True)
    planet_name = Column(String(30),nullable=False)

    
class Characters(Base):
    __tablename__ = 'characters'
    id =  Column(Integer, primary_key=True)
    character_name = Column(String(30),nullable=False)

class Fav_Planets(Base):
    __tablename__ = 'fav_planets'
    id =  Column(Integer, primary_key=True)
    user_id = Column(String(30), ForeignKey('user.id'))
    planets_id = Column(String(30), ForeignKey('planets.id'))

class Fav_Characters(Base):
    __tablename__ = 'fav_characters'
    id =  Column(Integer, primary_key=True)
    user_id = Column(String(30), ForeignKey('user.id'))
    charac_id = Column(String(30), ForeignKey('characters.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e