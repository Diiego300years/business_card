# from datetime import datetime
# from app import db
#
#
# class Admin(db.Model):
#     __tablename__ = 'admin'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), nullable=False, index=True)
#     phone_number = db.Column(db.Integer, unique=True, default=0)
#     password_hash = db.Column(db.String(255), nullable=False)
#     email = db.Column(db.String(120), nullable=False, unique=True)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#
#     def __repr__(self):
#         return f'Admin(username={self.username}), email={self.email}'
