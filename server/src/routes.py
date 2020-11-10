"""
This is the module where we create all of our routes
"""
from flask import Blueprint, url_for, request, jsonify
from src.auth import get_user, create_token
from src.ext import bcrypt, db
from src.models import User
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint("main", __name__)

# simply to check if the site is running
@bp.route("/")
def index():
    return "hi ther uwuw"

@bp.route("/user/get", methods=["GET"])
@jwt_required
def get_user_by_id():
    user = get_user()
    return jsonify({"The json" : "oooh ye"})

@bp.route("/user/update", methods=["PUT"])
def update_profile():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    recieved_json = request.json()
    return jsonify({"The json" : "oooh ye", "what you gave me" : recieved_json})

@bp.route("/login", methods=["POST"])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        token = create_token(user)
        return jsonify({"token" : token})

    return jsonify({ "status": "Error", "msg": "Wrong username or password" })

@bp.route("/register")
def register():
    pass

@bp.route("/search")
def search():
    form = request.form

@bp.route("/user", methods=["DELETE"])
@jwt_required
def delete_user():
    user = get_user
    db.session.delete(user)

