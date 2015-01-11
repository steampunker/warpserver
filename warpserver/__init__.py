#!/usr/bin/env python
from flask import Flask
from database import db
from auth import auth
from message import message
import sys
import os

app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(message, url_prefix='/message')
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)
app.config["albianwarp_version_number"] = "0.0.0.1a"
app.config["albianwarp_version_name"] = "Much Alpha, verry Bug!"
host = "0.0.0.0"
app.secret_key = os.urandom(32)


@app.route("/")
def index():
    return "Hello World!", 200

if __name__ == "__main__":
    if sys.argv[1] == "initdb":
        with app.app_context():
            db.create_all()
    elif sys.argv[1] == "dropdb":
        with app.app_context():
            db.drop_all()
    elif sys.argv[1] == "run":
        app.run(host=host, port=80)
    else:
        print(
            """That Argument/Command is not implemented! use:
initdb - Initials the Database Tables
dropdb - Drops all the Database Tables
run - Runs the Server via the Werkzeug WSGI Server"""
        )
