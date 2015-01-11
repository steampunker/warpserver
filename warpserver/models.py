from database import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), nullable=False, unique=True)
    mail = db.Column(db.String(250), nullable=False, unique=True)
    password_hash = db.Column(db.String(500), nullable=False)
    status = db.Column(db.Integer, default=0)
    roll = db.Column(db.Integer, default=0)

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


class Message(db.Model):
    __tablename__ = "message"
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    recipient_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    date = db.Column(db.DateTime)
    title = db.Column(db.String(32))
    content = db.Column(db.Text)

    sender = db.relationship("User", foreign_keys=[sender_id])
    recipient = db.relationship("User", foreign_keys=[recipient_id])

    def __repr__(self):
        return "<Message(id='%s', sender_id='%s',recipient_id='%s',)>" % (
            self.id,
            self.sender_id,
            self.recipient_id
        )
    
    def __init__(self, sender, recipient, title, content):
        self.sender = sender
        self.recipient = recipient
        self.title = title
        self.content = content
