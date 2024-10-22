from app import db
import uuid
from sqlalchemy.dialects.postgresql import UUID


class MyProjects(db.Model):
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
