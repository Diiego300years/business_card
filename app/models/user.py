from datetime import datetime
from app import db
from app.models.user_base import UserBase
from flask_login import UserMixin


class User(db.Model, UserBase, UserMixin):
    __tablename__ = 'user'
    concat_number = db.Column(db.Integer, nullable=False, default=0)
    message = db.Column(db.Text, nullable=False, default='')
    message_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    commentator = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return (f'User(concat_number={self.concat_number},'
                f'repo_link={self.repo_link},'
                f'message_time={self.message_time},'
                f'commentator={self.commentator})')
