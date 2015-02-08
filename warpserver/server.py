###############
# Workaround to prevent *.pyc Files from cluttering all over the Source Directorys
# https://stackoverflow.com/questions/154443/how-to-avoid-pyc-files?answertab=votes#tab-top
#
import sys
sys.dont_write_bytecode = True


import os
from flask import Flask
from flask.ext import restful
from resources.user import User
from resources.users import Users
from resources.auth import Authentication
from database import db

app = Flask(__name__)
app.secret_key = os.urandom(32)

# Flask Configuration
host = "0.0.0.0"
port = 1337


# Restful Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db.init_app(app)

# Restful Configuration
api = restful.Api(app)
api.add_resource(Users, "/users")
api.add_resource(User, "/user/<string:user_name>")
api.add_resource(Authentication, "/auth")


###############
# All these Routes are Basicly Debugging Stuff,
# which is currently needed to test the API's functionality,
# due to the Lack of a Client ^^
#
@app.route("/")
def index():
    return """<h1>Test Forms</h1>
    <p><a href="/forms/user_registration">user_registration</a></p>
    <p><a href="/forms/user_authentication">user_authentication</a></p>
    """

@app.route("/forms/user_registration")
def regform_test():
    return """<h1>REGISTER TESTFORM!!!</h1><form action="/users" method="post">
                <p>username <input name="username" type="text" size="30"></p>
                <p>mail <input name="mail" type="text" size="30"></p>
                <p>password <input name="password" type="text" size="30"></p>
                <input type="submit" value=" post "></form>
            """, 200

@app.route("/forms/user_authentication")
def loginform_test():
    return """<h1>LOGIN TESTFORM!!!</h1><form action="/auth" method="post">
                  <p>username <input name="username" type="text" size="30"></p>
                  <p>password <input name="password" type="text" size="30"></p>
                  <input type="submit" value=" post "></form>
        """, 200

###############
# This is a temporary Solution for Argumentparsing!
# I plan to implement all the Argument Parsing with "argparse"
# https://docs.python.org/2.7/library/argparse.html
#
def print_help():
    print(""" That Command is not implemented! use:
initdb - Initials the Database Tables
dropdb - Drops all the Database Tables
run - Runs the Server via the Werkzeug WSGI Server""")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "initdb":
            with app.app_context():
                db.create_all()
        elif sys.argv[1] == "dropdb":
            with app.app_context():
                db.drop_all()
        elif sys.argv[1] == "run":
            app.run(debug=True,host=host,port=port)
        else:
            print_help()
    else:
        print_help()
