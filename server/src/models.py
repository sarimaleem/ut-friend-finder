"""
This module holds in all of the sweeet sweet database models/tables
"""
from src.ext import db
from sqlalchemy import Column, Integer, String, Text

class User(db.Model):

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(256), nullable=False)

    # These are all defaulted to being nullable
    email = Column(String)
    school_email = Column(String)
    major = Column(String)
    bio = Column(String)
    image_link = Column(String)
    classification = Column(String)
    birthdate = Column(String)
    gender = Column(String)

    # How do we store this one?? we'll do sting for now, but we need to talk about this one
    location = Column(String)

