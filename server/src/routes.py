"""
This is the module where we create all of our routes
"""
from flask import Blueprint, url_for, request, jsonify
from src.auth import get_user, create_token
from src.schemas import UserSchema, LoginSchema
from src.ext import bcrypt, db
from src.models import User
from flask_jwt_extended import jwt_required, get_jwt_identity
import functools
from marshmallow import ValidationError

bp = Blueprint("main", __name__)

# Utility wrapper method that returns json for the error when a ValidationError is raised
def validate_schema(f):

    @functools.wraps(f)
    def decorator(*a, **kw):
        try: 
            return f(*a, **kw)
        except ValidationError as err:
            resp = jsonify({"status" :"Error", "msg": err.messages})
            resp.status_code = 400
            return resp
    return decorator

# simply to check if the site is running
@bp.route("/")
def index():
    return "hi ther uwuw"

# A very simple example of how to use all these crazy extensions together
@bp.route("/user/update", methods=["PUT"])
@jwt_required
@validate_schema
def update_profile():
    # Because we have the jwt_required tag we are able to get the user using get_user
    user = get_user()
    # This validate_schema tag allows for if the request json is invalid it throws an error
    user_form = UserSchema().load(request.json)
    if user.username == user_form.username:
        # add the user_form to the database, this will update the user
        db.session.add(user_form)
        db.session.commit()
        # return status code 200
        return 200
    # If it reaches this point then it failed somewhere. Lets tell them that
    return jsonify({"status": "Error", "msg": "Usernames do not match"})

@bp.route("/user/get", methods=["GET"])
@jwt_required
def get_user_by_id():
    user = get_user()
    return jsonify({"The json" : "oooh ye"})


@bp.route("/login", methods=["POST"])
@validate_schema
def login():
    login_form = LoginSchema.load(request.json)
    user = User.query.filter_by(username=login_form.username).first()
    if user and bcrypt.check_password_hash(user.password, login_form.password):
        token = create_token(user)
        return jsonify({"token" : token, "status": "Success"})

    return jsonify({ "status": "Error", "msg": "Wrong username or password" })

@bp.route("/register", methods=["POST"])
@validate_schema
def register():
    user_form = UserSchema().load(request.json)

    if User.query.filter_by(username=user_form.username).first():
        return jsonify({"status" : "Error", "msg" : "Username already exists"})

    user_form.password = bcrypt.generate_password_hash(user_form.password).decode('utf-8')

    db.session.add(user_form)
    db.session.commit()
    
    return jsonify({ "status" : "Success" })

@bp.route("/search")
def search():
    form = request.form

@bp.route("/user", methods=["DELETE"])
@jwt_required
def delete_user():
    # DELETE's the user from the database
    user = get_user()
    db.session.delete(user)

