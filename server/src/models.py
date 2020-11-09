"""
This module holds in all of the sweeet sweet database models/tables
"""
from src.ext import db
from sqlalchemy import Column, Integer

class User(db.model):

    id = Column(Integer, primary_key=True)
