from flask.ext.restful import Resource, reqparse
from database import db
from passlib.hash import pbkdf2_sha256
from sql.user import UserSql

class Users(Resource):

    def post(self):
        """Registration"""
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, help="The Username of a User is its unique Identifier and is Part of the Login Credentials.")
        parser.add_argument("password", type=str, help="The Password is needed to authenticate the User.")
        parser.add_argument("mail", type=str, help="The Mailaddress is needed for i.e. Password recovery, you should provide a valid mailaddress to use this Feature!")
        args = parser.parse_args()
        try:
            db.session.add(
                UserSql(
                    username=args["username"],
                    mail=args["mail"],
                    password_hash=pbkdf2_sha256.encrypt(args["password"],rounds=1337,salt_size=32)
                    )
                )
            db.session.commit()
            return {"status" : "Created User"}
        except Exception,e:
            return {
                "message": "Internal Server Error!: " + str(e),
                "status": 500},500