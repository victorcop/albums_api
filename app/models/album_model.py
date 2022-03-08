from app import db


class Album(db.Model):
    __tablename__ = "albums"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.Text(), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def serialize(self):
        return dict(id=self.id, name=self.name, description=self.description)
