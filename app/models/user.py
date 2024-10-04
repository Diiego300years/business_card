from datetime import datetime
from app import db
from app.models.user_base import UserBase

class User(db.Model, UserBase):
    __tablename__ = 'user'
    concat_number = db.Column(db.Integer, nullable=False, default=0)
    message = db.Column(db.Text, nullable=False, default='')
    message_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


    def __repr__(self):
        return f'User(name={self.name}, email={self.email}, message={self.message})'