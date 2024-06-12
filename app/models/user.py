from datetime import datetime
from app import db


class Prospect(db.Model):
    __tablename__ = 'potentialClient'
    id = db.Column(db.SmallInteger, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    concat_number = db.Column(db.Integer, uniqe=True, default=0)
    added_at = db.Column(db.DateTime, default=datetime.utcnow)
    message = db.Column(db.Text, nullable=False, default='')


    def __repr__(self):
        return f'Prospect(name={self.name}, email={self.email}, concat_number={self.concat_number}, message={self.message})'

class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Admin(username={self.username}), email={self.email}'