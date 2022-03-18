import uuid

from app import db


class Album(db.Model):
    __tablename__ = "albums"

    id = db.Column(db.Integer(), primary_key=True)
    uuid = db.Column(db.String(36), unique=True, default=str(uuid.uuid4()))
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text(), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def serialize(self):
        return dict(uuid=self.uuid, name=self.name, description=self.description)
