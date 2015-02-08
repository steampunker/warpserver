from database import db

class UserSql(db.Model):
    import datetime
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), nullable=False, unique=True)
    mail = db.Column(db.String(250), nullable=False, unique=True)
    password_hash = db.Column(db.String(500), nullable=False)
    status = db.Column(db.Integer, default=0, nullable=False)
    roll = db.Column(db.Integer, default=0, nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.datetime.utcnow(), nullable=False)
    last_password_change_date = db.Column(db.DateTime,default=None)
    last_login_date = db.Column(db.DateTime,default=None)

    def __repr__(self):
        return "<User(id='%s', username='%s', mail='%s', password_hash='%s...', status='%s', roll='%s')>" % (  # NOQA
            self.id,
            self.username,
            self.mail,
            self.password_hash[0:5],
            self.status,
            self.roll
        )

    def __init__(self, username, mail, password_hash, status=0, roll=0):
        self.username = username
        self.mail = mail
        self.password_hash = password_hash
        self.status = status
        self.roll = roll