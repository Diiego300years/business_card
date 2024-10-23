import datetime
from app import db


class HomeEditor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hidden_title = db.Column(db.String(64), nullable=False, index=True, default='')
    title = db.Column(db.String(64), nullable=False, default='')
    description = db.Column(db.Text, nullable=False, default='')
    added_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    photos = db.Column(db.String(255), nullable=False, default="default.jpg")




    def __repr__(self):
        return (f'HomeEditor(title={self.title},'
                f'description={self.description},'
                f'added_at={self.added_at},'
                f'photos={self.photos})')

