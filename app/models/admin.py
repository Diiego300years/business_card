from app import db, bcrypt
from app.models.user_base import UserBase
from flask_login import UserMixin


class Admin(db.Model, UserBase, UserMixin):
    __tablename__ = 'admin'

    def __repr__(self):
        return f'Admin(name={self.name}), email={self.email}'
