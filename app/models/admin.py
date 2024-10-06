from app import db, bcrypt
from app.models.user_base import UserBase
import uuid
from sqlalchemy.dialects.postgresql import UUID
from flask_login import UserMixin


class Admin(db.Model, UserBase):
    __tablename__ = 'admin'
    password_hash = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'Admin(username={self.username}), email={self.email}'

    @property
    def password(self):
        raise AttributeError('Password is write-only')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
