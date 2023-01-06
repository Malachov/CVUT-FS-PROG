#for database models
#-----------------------------------------------------------

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#note database
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    
    print_name = db.Column(db.String(10000))
    url = db.Column(db.String(10000))
    amount = db.Column(db.Integer)
    address = db.Column(db.String(10000))

    comment = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#user database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')