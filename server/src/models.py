"""
This module holds in all of the sweeet sweet database models/tables
"""
from src.ext import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DATETIME

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
    birthdate = Column(DATETIME)
    school = Column(String) # Switch to enum
    gender = Column(String) # Switch to enum??

    # How do we store this one?? we'll do sting for now, but we need to talk about this one
    location = Column(String)

    @property
    def age(self):
        return (datetime.now() - self.birthdate).days // 365

