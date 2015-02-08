from flask.ext.restful import Resource,abort
from database import db
from resources.auth import dec_authenticated, dec_administrator, is_administrator
from sql.user import UserSql

class User(Resource):

    @dec_authenticated
    def get(self,user_name):
        try:
            user = UserSql.query.filter_by(username=user_name).first()
            if user == None:
                return {"message": "There is no User with that username!"},404
        except Exception, e:
            return {"message": "Internal Server Error!: " + str(e),"status": 500},500
        if is_administrator():
            return {
            "user_name" : user.username,
            "user_mail" : user.mail,
            "user_password_hash" : user.password_hash,
            "user_status" : user.status,
            "user_roll" : user.roll,
            "user_registration_date" : str(user.registration_date),
            "user_last_password_change_date" : str(user.last_password_change_date),
            "user_last_login_date" : str(user.last_login_date)
            }
        return {
            "user_name" : user.username,
            "user_status" : user.status,
            "user_roll" : user.roll}

    @dec_administrator
    def delete(self,user_name):
        try:
            user = UserSql.query.filter_by(username=user_name).first()
            if user == None:
                abort(404)
            db.session.delete(user)
            db.session.commit()
        except Exception, e:
            return {"message": "Internal Server Error!: " + str(e),"status": 500},500
        return {"message" : "successfully deleted the User!","user_name" : user_name, "status": 200}, 200