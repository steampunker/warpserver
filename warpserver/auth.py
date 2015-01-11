from flask import Blueprint, url_for, request, session, escape
from functools import wraps
from passlib.hash import pbkdf2_sha256
from database import db
from models import User

auth = Blueprint("auth", __name__)


@auth.record
def record(state):
    db = state.app.config.get("auth.db")  # NOQA


@auth.route("/login", methods=["GET", "POST"])
def login_user():
    if request.method == "POST":
        temp_user = User.query.filter_by(
            username=request.form["username"]
        ).first()
        
        if temp_user is not None:
            if pbkdf2_sha256.verify(
                request.form["password"],
                temp_user.password_hash
            ):
                session["username"] = request.form["username"]
                return "SUCCESSFULLY LOGGED IN!", 200
        return "ACCESS DENIED!", 401
    if request.method == "GET":
        return """<h1>LOGIN TESTFORM!!!</h1><form action="%s" method="post">
                  <p>username</p>
                  <input name="username" type="text" size="30">
                  <p>password</p>
                  <input name="password" type="text" size="30">
                  <input type="submit" value=" Absenden ">
               """ % url_for('auth.login_user'), 200

               
@auth.route("/whoami", methods=["GET"])
def whoami():
    if "username" in session:
        return "%s" % escape(session["username"]), 200
    else:
        return "you are not logged in!", 401


@auth.route("/logout")
def logout_user():
    if "username" not in session:
        return "Already logged out!"
    else:
        session.pop("username", None)
        return "Logout successfully!", 200


@auth.route("/register", methods=["GET", "POST"])
def register_user():
    if request.method == "POST":
        if User.query.filter_by(
            username=request.form["username"]
        ).first() is not None:
            return "user with that username already exists!", 409
        
        if User.query.filter_by(mail=request.form["mail"]).first() is not None:
            return "user with that mail already exists!", 409
        else:
            db.session.add(
                User(
                    username=request.form["username"],
                    mail=request.form["mail"],
                    password_hash=pbkdf2_sha256.encrypt(
                        request.form["password"], rounds=200, salt_size=16)
                )
            )
            db.session.commit()
            return "SUCCESSFULLY REGISTERD!", 200
    if request.method == "GET":
        return """<h1>REGISTER TESTFORM!!!</h1><form action="%s" method="post">
                  <p>username
                  <input name="username" type="text" size="30"></p>
                  <p>mail
                  <input name="mail" type="text" size="30"></p>
                  <p>password
                  <input name="password" type="text" size="30"></p>
                  <input type="submit" value=" Absenden ">
        """ % url_for('auth.register_user'), 200


def authenticated(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "username" not in session:
            return "you need to login first!", 401
        return f(*args, **kwargs)
    return decorated_function
