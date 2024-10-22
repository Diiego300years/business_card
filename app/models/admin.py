from app import db
from app.models.user_base import UserBase
from flask_login import UserMixin


class Admin(db.Model, UserBase, UserMixin):
    __tablename__ = 'admin'
