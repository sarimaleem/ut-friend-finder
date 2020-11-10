"""
This module holds in all of the sweeet sweet database models/tables
"""
from src.ext import db
from sqlalchemy import Column, Integer, String, Text

class User(db.Model):

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    password = Column(String(256))
