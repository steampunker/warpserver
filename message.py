from flask import Blueprint, session
from database import db
from models import Message
from auth import authenticated

message = Blueprint("message", __name__)

@message.record
def record(state):
    db = state.app.config.get("message.db")

@message.route("/list", methods=["GET"])
@authenticated
def list_messages():
    # Return all the Massages Sender, Title and Date for the Logged in User here!
    return "DUMMY",200

@message.route("/get/<int:message_id>", methods=["GET"])
@authenticated
def get_message(message_id):
    # Return the Message with the given ID, if the recipient is the logged in User!
    return "DUMMY",200

@message.route("/send", methods=["GET","POST"])
@authenticated
def send_message():
    # Send a Message to someon!
    return "DUMMY",200