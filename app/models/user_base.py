from datetime import datetime
from app import db
import uuid
from sqlalchemy.dialects.postgresql import UUID


class UserBase:
    __abstract__ = True
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(64), nullable=False, index=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    added_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)