from datetime import datetime
from app import db


# this table is for potential clients
class Prospect(db.Model):
    __tablename__ = 'potentialClient'
    id = db.Column(db.SmallInteger, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    concat_number = db.Column(db.Integer, unique=True, default=0)
    message = db.Column(db.Text, nullable=False, default='')
    added_at = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return f'Prospect(name={self.name}, email={self.email}, concat_number={self.concat_number}, message={self.message})'
