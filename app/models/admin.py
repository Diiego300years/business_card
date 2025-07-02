from app.extensions import db
from app.models.user_base import UserBase
from flask_login import UserMixin
import uuid
from sqlalchemy.dialects.postgresql import UUID
import datetime


class Admin(db.Model, UserBase, UserMixin):
    __tablename__ = 'admin'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(64), nullable=False, index=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    added_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    confirmed = db.Column(db.Boolean, default=False, nullable=False)
    is_account_active = db.Column(db.Boolean, default=True, nullable=False)
