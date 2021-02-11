from src.models import User
from src.ext import ma
from marshmallow import fields, Schema

class UserSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = User
        load_instance = True

class LoginSchema(Schema):

    username = fields.String()
    password = fields.String()
