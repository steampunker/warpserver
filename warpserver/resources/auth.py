from flask import session
from flask.ext.restful import Resource, reqparse, abort
from sql.user import UserSql
from passlib.hash import pbkdf2_sha256
from functools import wraps

###################
# You can use these in other resources, to make simple "if" Authentication Checks.
#
def is_authenticated():
    if "username" in session:
        return True
    return False

def is_administrator():
    if "username" in session and "administrator" in session:
        return True
    return False

###############
# Decorators used by other resources, to check if a Client is authenticated!
#
def dec_authenticated(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if "username" not in session:
            abort(401)
        return function(*args, **kwargs)
    return decorated_function

def dec_administrator(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if "username" not in session or "administrator" not in session:
            abort(403)
        return function(*args, **kwargs)
    return decorated_function

###############
# The RESTful Resource for Authentication
#
class Authentication(Resource):
    def post(self):
        """Login"""
        # Argument Parsing
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, help="The Username of a User is its unique Identifier and is Part of the Login Credentials.")
        parser.add_argument("password", type=str, help="The Password is needed to authenticate the User.")
        args = parser.parse_args()
        # select the User ith the given username from the Database
        user = UserSql.query.filter_by(username=args["username"]).first()
        if user == None:
            abort(404)
        # Authentication (if the session variable "username" is set, the User is authenticated!)
        if pbkdf2_sha256.verify(args["password"],user.password_hash):
            session["username"] = user.username
        # Check if the User is an administrator, and add the session Variable
            if user.roll >= 3:
                session["administrator"] = True
            return {"authenticated" : True,"username": session["username"]}
        # If all of the above failed, you just could not authenticate :(
        abort(403)
        
    def get(self):
        """Authentication Status"""
        if "username" in session:
            return {"authenticated" : True,"username": session["username"]}
        return {"authenticated" : False},401

    def delete(self):
        """Logout"""
        if "username" in session:
            session.pop("username", None)
        if "administrator" in session:
            session.pop("administrator",None)
        return {"authenticated" : False}