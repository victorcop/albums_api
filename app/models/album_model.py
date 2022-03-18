from app import db


class Album(db.Model):
    __tablename__ = "albums"

    id = db.Column(db.Integer(), primary_key=True)
    uuid = db.Column(db.String(36), unique=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text(), nullable=False)

    def __init__(self, uuid, name, description):
        self.name = name
        self.description = description
        self.uuid = uuid
