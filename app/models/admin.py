from app import db


class Role(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.SmallInteger, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True, unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return 'Role: %r' % self.name