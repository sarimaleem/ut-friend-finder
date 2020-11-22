from src.models import User
from marshmallow import fields, Schema
from src.ext import ma

class UserSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = User
        load_instance = True

class LoginSchema(Schema):

    username = fields.String()
    password = fields.String()
