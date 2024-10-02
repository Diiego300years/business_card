from datetime import datetime
from app import db
import uuid
from sqlalchemy.dialects.postgresql import UUID

# this table is for potential clients
class User(db.Model):
    __tablename__ = 'user'
    #id = db.Column(db.SmallInteger, primary_key=True)

    #new feature:
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(64), nullable=False, index=True)
    email = db.Column(db.String(120), nullable=False, unique=True)

    # For now below False
    concat_number = db.Column(db.Integer, unique=False, nullable=False, default=0)
    message = db.Column(db.Text, nullable=False, default='')
    added_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_admin = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f'User(name={self.name}, email={self.email}, concat_number={self.concat_number}, message={self.message})'
