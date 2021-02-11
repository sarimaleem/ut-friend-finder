from flask_jwt_extended import create_access_token, get_jwt_identity
from functools import wraps
from .models import User

def create_token(user):
    return create_access_token(identity=user.id)

def get_user(f):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return user

