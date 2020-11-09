rom flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

migrate = Migrate() # if we need to change the database this saves lives
db = SQLAlchemy() # for the database
bcrypt = Bcrypt() # for the passwords
jwt = JWTManager() # for the jwt webtokens and logging in stuff
