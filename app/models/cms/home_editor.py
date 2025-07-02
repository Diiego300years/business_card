import datetime
from app.extensions import db
import uuid
from sqlalchemy.dialects.postgresql import UUID


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


class ProjectsEditor(db.Model):
    __tablename__ = 'my_project'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False, default='')
    repo_link = db.Column(db.String(255), nullable=False)
    page_link = db.Column(db.String(255), nullable=False)
    graphics = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return (f'User(project_name={self.project_name},'
                f'description={self.description},'
                f'repo_link={self.repo_link},'
                f'page_link={self.page_link},'
                f'graphics={self.graphics})')
